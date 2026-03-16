"""debugger tools for yt-dlp."""

import inspect
import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register debugger tools with the server."""

    @server.tool()
    async def debugger_write(
        level: str | None = "100",
    ) -> str:
        """Write"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("debugger_write")

