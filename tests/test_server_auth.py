"""Tests for MCP server bearer token authentication (--server-auth flag)."""

import ast
import json

import pytest
from rich.console import Console

from mcp_anything.config import CLIOptions
from mcp_anything.models.manifest import GenerationManifest
from mcp_anything.pipeline.engine import PipelineEngine


async def _run_pipeline(
    codebase_path,
    output_dir,
    *,
    transport: str = "http",
    server_auth: bool = False,
):
    options = CLIOptions(
        codebase_path=codebase_path,
        output_dir=output_dir,
        no_llm=True,
        no_install=True,
        transport=transport,
        server_auth=server_auth,
    )
    console = Console(quiet=True)
    engine = PipelineEngine(options, console)
    await engine.run()
    manifest_path = output_dir / "mcp-anything-manifest.json"
    return GenerationManifest.load(manifest_path)


class TestServerAuthModel:
    def test_default_disabled(self):
        from mcp_anything.models.design import ServerDesign
        d = ServerDesign(server_name="test")
        assert d.enable_server_auth is False
        assert d.server_auth_env_var == "MCP_SERVER_TOKEN"

    def test_enable_server_auth(self):
        from mcp_anything.models.design import ServerDesign
        d = ServerDesign(server_name="test", enable_server_auth=True)
        assert d.enable_server_auth is True

    def test_custom_env_var(self):
        from mcp_anything.models.design import ServerDesign
        d = ServerDesign(server_name="test", enable_server_auth=True, server_auth_env_var="MY_TOKEN")
        assert d.server_auth_env_var == "MY_TOKEN"


class TestServerAuthGeneration:
    @pytest.mark.asyncio
    async def test_server_auth_enabled_in_manifest(self, fake_flask_app, tmp_path):
        manifest = await _run_pipeline(fake_flask_app, tmp_path / "out", server_auth=True)
        assert manifest.design is not None
        assert manifest.design.enable_server_auth is True

    @pytest.mark.asyncio
    async def test_server_auth_disabled_by_default(self, fake_flask_app, tmp_path):
        manifest = await _run_pipeline(fake_flask_app, tmp_path / "out")
        assert manifest.design is not None
        assert manifest.design.enable_server_auth is False

    @pytest.mark.asyncio
    async def test_server_py_contains_oauth_provider(self, fake_flask_app, tmp_path):
        output_dir = tmp_path / "out"
        manifest = await _run_pipeline(fake_flask_app, output_dir, server_auth=True)

        package_name = f"mcp_{manifest.design.server_name.replace('-', '_')}"
        server_py = output_dir / "src" / package_name / "server.py"
        assert server_py.exists()

        source = server_py.read_text()
        assert "oauth_provider" in source
        assert "auth_server_provider" in source
        assert "AuthSettings" in source
        assert "login_routes" in source

    @pytest.mark.asyncio
    async def test_auth_provider_py_generated(self, fake_flask_app, tmp_path):
        output_dir = tmp_path / "out"
        manifest = await _run_pipeline(fake_flask_app, output_dir, server_auth=True)

        package_name = f"mcp_{manifest.design.server_name.replace('-', '_')}"
        auth_py = output_dir / "src" / package_name / "_auth_provider.py"
        assert auth_py.exists(), "_auth_provider.py not generated"

        source = auth_py.read_text()
        assert "SimpleOAuthProvider" in source
        assert "verify_token" in source or "load_access_token" in source
        assert "MCP_SERVER_TOKEN" in source
        assert "/_mcp_auth/login" in source

    @pytest.mark.asyncio
    async def test_server_py_without_auth_has_no_oauth(self, fake_flask_app, tmp_path):
        output_dir = tmp_path / "out"
        manifest = await _run_pipeline(fake_flask_app, output_dir, server_auth=False)

        package_name = f"mcp_{manifest.design.server_name.replace('-', '_')}"
        server_py = output_dir / "src" / package_name / "server.py"
        source = server_py.read_text()

        assert "oauth_provider" not in source
        assert "auth_server_provider" not in source

        auth_py = output_dir / "src" / package_name / "_auth_provider.py"
        assert not auth_py.exists(), "_auth_provider.py should not exist without --server-auth"

    @pytest.mark.asyncio
    async def test_server_py_is_valid_python(self, fake_flask_app, tmp_path):
        output_dir = tmp_path / "out"
        manifest = await _run_pipeline(fake_flask_app, output_dir, server_auth=True)

        package_name = f"mcp_{manifest.design.server_name.replace('-', '_')}"
        server_py = output_dir / "src" / package_name / "server.py"
        source = server_py.read_text()

        # Must parse without error
        ast.parse(source)

    @pytest.mark.asyncio
    async def test_generated_readme_mentions_auth_setup(self, fake_flask_app, tmp_path):
        output_dir = tmp_path / "out"
        await _run_pipeline(fake_flask_app, output_dir, server_auth=True)

        readme = (output_dir / "README.md").read_text()
        assert "MCP server authentication" in readme
        assert "MCP_SERVER_TOKEN" in readme
        assert "MCP_SERVER_URL" in readme

    @pytest.mark.asyncio
    async def test_mcp_json_has_only_url_when_auth_enabled(self, fake_flask_app, tmp_path):
        """mcp.json should only contain the URL — MCP_SERVER_TOKEN is server-side only."""
        output_dir = tmp_path / "out"
        await _run_pipeline(fake_flask_app, output_dir, server_auth=True)

        mcp_config = json.loads((output_dir / "mcp.json").read_text())
        server_entry = next(iter(mcp_config["mcpServers"].values()))

        assert "url" in server_entry
        # Token is NOT in mcp.json — it's set as a server env var, not exposed to clients
        assert "env" not in server_entry

    @pytest.mark.asyncio
    async def test_mcp_json_url_only_when_auth_disabled(self, fake_flask_app, tmp_path):
        output_dir = tmp_path / "out"
        await _run_pipeline(fake_flask_app, output_dir, server_auth=False)

        mcp_config = json.loads((output_dir / "mcp.json").read_text())
        server_entry = next(iter(mcp_config["mcpServers"].values()))

        assert "url" in server_entry
        assert "env" not in server_entry

    @pytest.mark.asyncio
    async def test_server_auth_only_for_http_transport(self, fake_flask_app, tmp_path):
        """server_auth=True on stdio transport should not enable server auth."""
        # server_auth is ignored for stdio — only meaningful with HTTP
        options = CLIOptions(
            codebase_path=fake_flask_app,
            output_dir=tmp_path / "out",
            no_llm=True,
            no_install=True,
            transport="stdio",
            server_auth=True,
        )
        console = Console(quiet=True)
        engine = PipelineEngine(options, console)
        await engine.run()
        manifest = GenerationManifest.load(tmp_path / "out" / "mcp-anything-manifest.json")
        # stdio transport → server auth must be disabled regardless
        assert manifest.design.enable_server_auth is False
