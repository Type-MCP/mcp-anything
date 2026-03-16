"""external_fd tools for yt-dlp."""

import inspect
import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register external_fd tools with the server."""

    @server.tool()
    async def external_fd_exe_name(
    ) -> str:
        """EXE NAME"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("external_fd_exe_name")

    @server.tool()
    async def external_fd_available(
        path: str | None = None,
    ) -> str:
        """Available"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("external_fd_available")

    @server.tool()
    async def external_fd_can_download(
        info_dict: str,
        path: str | None = None,
    ) -> str:
        """Can download"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("external_fd_can_download")

    @server.tool()
    async def external_fd_exe(
    ) -> str:
        """Exe"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("external_fd_exe")

    @server.tool()
    async def external_fd_get_basename(
    ) -> str:
        """Get basename"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("external_fd_get_basename")

    @server.tool()
    async def external_fd_real_download(
        filename: str,
        info_dict: str,
    ) -> str:
        """Real download"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("external_fd_real_download")

    @server.tool()
    async def external_fd_supports(
        info_dict: str,
    ) -> str:
        """Supports"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("external_fd_supports")

