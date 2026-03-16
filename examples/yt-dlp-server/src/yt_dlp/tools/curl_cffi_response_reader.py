"""curl_cffi_response_reader tools for yt-dlp."""

import inspect
import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register curl_cffi_response_reader tools with the server."""

    @server.tool()
    async def curl_cffi_response_reader_close(
    ) -> str:
        """Close"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("curl_cffi_response_reader_close")

    @server.tool()
    async def curl_cffi_response_reader_read(
        size: str | None = None,
    ) -> str:
        """Read"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("curl_cffi_response_reader_read")

