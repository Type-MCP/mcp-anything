"""cbcie tools for yt-dlp."""

import inspect
import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register cbcie tools with the server."""

    @server.tool()
    async def cbcie_suitable(
        url: str,
    ) -> str:
        """Suitable"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("cbcie_suitable")

