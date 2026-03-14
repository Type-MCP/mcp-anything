"""Abstract base class for pipeline phases."""

from abc import ABC, abstractmethod

from mcp_anything.pipeline.context import PipelineContext


class Phase(ABC):
    """A single phase in the generation pipeline."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Phase identifier (e.g. 'analyze', 'design')."""

    @abstractmethod
    async def execute(self, ctx: PipelineContext) -> None:
        """Run this phase, updating ctx.manifest in place."""

    def validate_preconditions(self, ctx: PipelineContext) -> list[str]:
        """Return list of error messages if preconditions aren't met. Empty = OK."""
        return []
