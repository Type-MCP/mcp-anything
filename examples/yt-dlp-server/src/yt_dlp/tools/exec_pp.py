"""exec_pp tools for yt-dlp."""

import inspect
import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register exec_pp tools with the server."""

    @server.tool()
    async def exec_pp_parse_cmd(
        cmd: str,
        info: str,
    ) -> str:
        """Parse cmd"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("exec_pp_parse_cmd")

