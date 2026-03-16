"""cli_runner tools for click."""

import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register cli_runner tools with the server."""

    @server.tool()
    async def cli_runner_get_default_prog_name(
        cli: str,
    ) -> str:
        """Given a command object it will return the default program name"""
        # Call function via CLI backend: src/click/testing.py::get_default_prog_name
        return await backend.run_function_as_cli(
            "src/click/testing.py",
            "get_default_prog_name",
            cli=cli,
        )

    @server.tool()
    async def cli_runner_isolated_filesystem(
        temp_dir: str | None = None,
    ) -> str:
        """A context manager that creates a temporary directory and"""
        # Call function via CLI backend: src/click/testing.py::isolated_filesystem
        return await backend.run_function_as_cli(
            "src/click/testing.py",
            "isolated_filesystem",
            temp_dir=temp_dir,
        )

    @server.tool()
    async def cli_runner_make_env(
        overrides: str | None = None,
    ) -> str:
        """Returns the environment overrides for invoking a script."""
        # Call function via CLI backend: src/click/testing.py::make_env
        return await backend.run_function_as_cli(
            "src/click/testing.py",
            "make_env",
            overrides=overrides,
        )

