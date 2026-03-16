"""f4m_fd tools for yt-dlp."""

import inspect
import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register f4m_fd tools with the server."""

    @server.tool()
    async def f4m_fd_real_download(
        filename: str,
        info_dict: str,
    ) -> str:
        """Real download"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("f4m_fd_real_download")

