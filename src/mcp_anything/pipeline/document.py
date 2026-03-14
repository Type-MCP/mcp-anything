"""Phase 5: DOCUMENT — generate README and documentation."""

from pathlib import Path

from mcp_anything.codegen.emitter import Emitter
from mcp_anything.pipeline.context import PipelineContext
from mcp_anything.pipeline.phase import Phase


class DocumentPhase(Phase):
    @property
    def name(self) -> str:
        return "document"

    def validate_preconditions(self, ctx: PipelineContext) -> list[str]:
        if not ctx.manifest.design:
            return ["Design phase must complete before documentation"]
        return []

    async def execute(self, ctx: PipelineContext) -> None:
        design = ctx.manifest.design
        assert design is not None

        output_dir = Path(ctx.manifest.output_dir)
        emitter = Emitter(design, output_dir)

        ctx.console.print("    Generating documentation...")
        generated = emitter.emit_docs()

        ctx.manifest.generated_files.extend(generated)
        ctx.console.print(f"    Generated {len(generated)} doc files")
