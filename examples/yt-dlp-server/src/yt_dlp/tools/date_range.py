"""date_range tools for yt-dlp."""

import inspect
import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register date_range tools with the server."""

    @server.tool()
    async def date_range_day(
        day: str,
    ) -> str:
        """Returns a range that only contains the given day"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("date_range_day")

