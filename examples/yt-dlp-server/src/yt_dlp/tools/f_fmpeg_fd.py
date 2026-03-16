"""f_fmpeg_fd tools for yt-dlp."""

import inspect
import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register f_fmpeg_fd tools with the server."""

    @server.tool()
    async def f_fmpeg_fd_available(
        path: str | None = None,
    ) -> str:
        """Available"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("f_fmpeg_fd_available")

    @server.tool()
    async def f_fmpeg_fd_can_merge_formats(
        info_dict: str,
        params: str,
    ) -> str:
        """Can merge formats"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("f_fmpeg_fd_can_merge_formats")

    @server.tool()
    async def f_fmpeg_fd_on_process_started(
        proc: str,
        stdin: str,
    ) -> str:
        """Override this in subclasses"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("f_fmpeg_fd_on_process_started")

