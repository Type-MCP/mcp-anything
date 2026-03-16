"""fc2_live_fd tools for yt-dlp."""

import inspect
import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register fc2_live_fd tools with the server."""

    @server.tool()
    async def fc2_live_fd_real_download(
        filename: str,
        info_dict: str,
    ) -> str:
        """Real download"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("fc2_live_fd_real_download")

