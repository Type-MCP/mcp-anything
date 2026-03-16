"""bash_complete tools for click."""

import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register bash_complete tools with the server."""

    @server.tool()
    async def bash_complete_format_completion(
        item: str,
    ) -> str:
        """Format completion"""
        # Call function via CLI backend: src/click/shell_completion.py::format_completion
        return await backend.run_function_as_cli(
            "src/click/shell_completion.py",
            "format_completion",
            item=item,
        )

