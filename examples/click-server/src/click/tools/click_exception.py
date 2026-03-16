"""click_exception tools for click."""

import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register click_exception tools with the server."""

    @server.tool()
    async def click_exception_show(
        file: str | None = None,
    ) -> str:
        """Show"""
        # Call function via CLI backend: src/click/exceptions.py::show
        return await backend.run_function_as_cli(
            "src/click/exceptions.py",
            "show",
            file=file,
        )

