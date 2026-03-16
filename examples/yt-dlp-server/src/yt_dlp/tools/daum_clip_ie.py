"""daum_clip_ie tools for yt-dlp."""

import inspect
import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register daum_clip_ie tools with the server."""

    @server.tool()
    async def daum_clip_ie_suitable(
        url: str,
    ) -> str:
        """Suitable"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("daum_clip_ie_suitable")

