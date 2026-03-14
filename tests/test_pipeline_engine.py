"""Tests for the pipeline engine."""

import pytest
from rich.console import Console

from mcp_anything.config import CLIOptions
from mcp_anything.models.manifest import GenerationManifest
from mcp_anything.pipeline.context import PipelineContext
from mcp_anything.pipeline.engine import ALL_PHASES, PipelineEngine, _load_phases
from mcp_anything.pipeline.phase import Phase


class TestPipelineEngine:
    def test_all_phases_defined(self):
        assert ALL_PHASES == ["analyze", "design", "implement", "document", "package"]

    def test_load_all_phases(self):
        phases = _load_phases(ALL_PHASES)
        assert len(phases) == 5
        assert all(isinstance(p, Phase) for p in phases)
        assert [p.name for p in phases] == ALL_PHASES

    def test_load_subset(self):
        phases = _load_phases(["analyze", "design"])
        assert len(phases) == 2
        assert phases[0].name == "analyze"
        assert phases[1].name == "design"

    def test_load_unknown_phase(self):
        phases = _load_phases(["unknown"])
        assert len(phases) == 0


class TestPipelineContext:
    def test_context_properties(self, fake_cli_app, tmp_output):
        options = CLIOptions(codebase_path=fake_cli_app, output_dir=tmp_output)
        manifest = GenerationManifest(
            codebase_path=str(fake_cli_app),
            output_dir=str(tmp_output),
            server_name="test",
        )
        ctx = PipelineContext(options, manifest, Console())

        assert ctx.codebase_path == fake_cli_app.resolve()
        assert ctx.output_dir == tmp_output

    def test_save_manifest(self, fake_cli_app, tmp_output):
        options = CLIOptions(codebase_path=fake_cli_app, output_dir=tmp_output)
        manifest = GenerationManifest(
            codebase_path=str(fake_cli_app),
            output_dir=str(tmp_output),
            server_name="test",
        )
        ctx = PipelineContext(options, manifest, Console())
        ctx.save_manifest()

        assert ctx.manifest_path.exists()
        loaded = GenerationManifest.load(ctx.manifest_path)
        assert loaded.server_name == "test"


class TestManifest:
    def test_phase_tracking(self):
        m = GenerationManifest()
        assert not m.phase_completed("analyze")
        m.mark_phase_completed("analyze")
        assert m.phase_completed("analyze")
        # Idempotent
        m.mark_phase_completed("analyze")
        assert m.completed_phases.count("analyze") == 1

    def test_roundtrip(self, tmp_path):
        m = GenerationManifest(server_name="test", codebase_path="/foo")
        m.mark_phase_completed("analyze")
        path = tmp_path / "manifest.json"
        m.save(path)

        loaded = GenerationManifest.load(path)
        assert loaded.server_name == "test"
        assert loaded.phase_completed("analyze")
