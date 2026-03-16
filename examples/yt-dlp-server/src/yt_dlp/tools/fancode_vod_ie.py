"""fancode_vod_ie tools for yt-dlp."""

import inspect
import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register fancode_vod_ie tools with the server."""

    @server.tool()
    async def fancode_vod_ie_download_gql(
        variable: str,
        data: str,
        note: str,
        fatal: str | None = "False",
        headers: str | None = None,
    ) -> str:
        """Download gql"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("fancode_vod_ie_download_gql")

