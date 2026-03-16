"""curl_cffi_response_adapter tools for yt-dlp."""

import inspect
import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register curl_cffi_response_adapter tools with the server."""

    @server.tool()
    async def curl_cffi_response_adapter_read(
        amt: str | None = None,
    ) -> str:
        """Read"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("curl_cffi_response_adapter_read")

