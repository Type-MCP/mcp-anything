"""Phase 4: TEST — generate and run test files for the MCP server."""

import subprocess
import sys
from pathlib import Path

from mcp_anything.codegen.emitter import Emitter
from mcp_anything.pipeline.context import PipelineContext
from mcp_anything.pipeline.phase import Phase


class TestPhase(Phase):
    @property
    def name(self) -> str:
        return "test"

    def validate_preconditions(self, ctx: PipelineContext) -> list[str]:
        if not ctx.manifest.design:
            return ["Design phase must complete before test generation"]
        return []

    async def execute(self, ctx: PipelineContext) -> None:
        design = ctx.manifest.design
        assert design is not None

        output_dir = Path(ctx.manifest.output_dir)
        emitter = Emitter(design, output_dir)

        ctx.console.print("    Generating test files...")
        generated = emitter.emit_tests()

        ctx.manifest.generated_files.extend(generated)
        ctx.console.print(f"    Generated {len(generated)} test files")

        # Run the generated tests
        test_dir = output_dir / "tests"
        if test_dir.exists():
            self._run_tests(ctx, output_dir)

    def _run_tests(self, ctx: PipelineContext, output_dir: Path) -> None:
        """Run pytest on the generated test suite."""
        ctx.console.print("    Running generated tests...")
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pytest", str(output_dir / "tests"), "-v", "--tb=short"],
                capture_output=True,
                text=True,
                timeout=120,
                cwd=str(output_dir),
            )
            # Show output
            if result.stdout:
                for line in result.stdout.strip().splitlines()[-10:]:
                    ctx.console.print(f"      {line}")

            if result.returncode == 0:
                ctx.console.print("    [green]All generated tests passed[/green]")
            else:
                ctx.console.print("    [yellow]Some generated tests failed[/yellow]")
                if result.stderr:
                    for line in result.stderr.strip().splitlines()[-5:]:
                        ctx.console.print(f"      [dim]{line}[/dim]")
        except subprocess.TimeoutExpired:
            ctx.console.print("    [yellow]Test run timed out (120s)[/yellow]")
        except FileNotFoundError:
            ctx.console.print("    [yellow]pytest not available, skipping test execution[/yellow]")
