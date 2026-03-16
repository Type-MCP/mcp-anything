"""creation tools for click."""

import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register creation tools with the server."""

    @server.tool()
    async def add_completion_class(
        name: str | None = None,
    ) -> str:
        """Register a :class:`ShellComplete` subclass under the given name."""
        # Call function via CLI backend: src/click/shell_completion.py::add_completion_class
        return await backend.run_function_as_cli(
            "src/click/shell_completion.py",
            "add_completion_class",
            name=name,
        )

