"""curl_cffirh tools for yt-dlp."""

import inspect
import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register curl_cffirh tools with the server."""

    @server.tool()
    async def curl_cffirh_send(
        request: str,
    ) -> str:
        """Send"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("curl_cffirh_send")

