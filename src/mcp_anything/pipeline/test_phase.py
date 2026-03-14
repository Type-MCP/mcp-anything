"""Phase 4: TEST — generate test files for the MCP server."""

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
