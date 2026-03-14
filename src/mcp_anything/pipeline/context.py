"""Shared pipeline context."""

from pathlib import Path

from rich.console import Console

from mcp_anything.config import CLIOptions
from mcp_anything.models.manifest import GenerationManifest


class PipelineContext:
    """Shared state passed through all pipeline phases."""

    def __init__(self, options: CLIOptions, manifest: GenerationManifest, console: Console) -> None:
        self.options = options
        self.manifest = manifest
        self.console = console

    @property
    def codebase_path(self) -> Path:
        return self.options.codebase_path.resolve()

    @property
    def output_dir(self) -> Path:
        return Path(self.manifest.output_dir)

    @property
    def manifest_path(self) -> Path:
        return self.output_dir / "mcp-anything-manifest.json"

    def save_manifest(self) -> None:
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.manifest.save(self.manifest_path)
