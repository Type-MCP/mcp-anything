"""Phase 6: PACKAGE — generate pyproject.toml and verify structure."""

from pathlib import Path

from mcp_anything.codegen.emitter import Emitter
from mcp_anything.pipeline.context import PipelineContext
from mcp_anything.pipeline.phase import Phase


class PackagePhase(Phase):
    @property
    def name(self) -> str:
        return "package"

    def validate_preconditions(self, ctx: PipelineContext) -> list[str]:
        if not ctx.manifest.design:
            return ["Design phase must complete before packaging"]
        return []

    async def execute(self, ctx: PipelineContext) -> None:
        design = ctx.manifest.design
        assert design is not None

        output_dir = Path(ctx.manifest.output_dir)
        emitter = Emitter(design, output_dir)

        ctx.console.print("    Generating packaging files...")
        generated = emitter.emit_packaging()

        ctx.manifest.generated_files.extend(generated)

        # Verify structure
        errors = self._verify_structure(output_dir, design.server_name.replace("-", "_"))
        if errors:
            for err in errors:
                ctx.console.print(f"    [yellow]Warning:[/yellow] {err}")
        else:
            ctx.console.print("    Package structure verified")

        ctx.console.print(f"    Generated {len(generated)} packaging files")

    def _verify_structure(self, output_dir: Path, package_name: str) -> list[str]:
        """Verify the generated package has the expected structure."""
        errors: list[str] = []

        expected = [
            "pyproject.toml",
            f"src/{package_name}/__init__.py",
            f"src/{package_name}/server.py",
        ]

        for rel in expected:
            if not (output_dir / rel).exists():
                errors.append(f"Missing expected file: {rel}")

        return errors
