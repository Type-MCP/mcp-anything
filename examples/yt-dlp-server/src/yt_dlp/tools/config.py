"""config tools for yt-dlp."""

import inspect
import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register config tools with the server."""

    @server.tool()
    async def config_all_args(
    ) -> str:
        """All args"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("config_all_args")

    @server.tool()
    async def config_append_config(
        label: str | None = None,
    ) -> str:
        """Append config"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("config_append_config")

    @server.tool()
    async def config_init(
        args: str | None = None,
        filename: str | None = None,
    ) -> str:
        """Init"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("config_init")

    @server.tool()
    async def config_read_file(
        filename: str,
        default: str | None = "[]",
    ) -> str:
        """Read file"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("config_read_file")

