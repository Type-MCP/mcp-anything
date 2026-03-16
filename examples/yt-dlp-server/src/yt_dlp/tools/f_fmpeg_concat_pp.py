"""f_fmpeg_concat_pp tools for yt-dlp."""

import inspect
import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register f_fmpeg_concat_pp tools with the server."""

    @server.tool()
    async def f_fmpeg_concat_pp_concat_files(
        in_files: str,
        out_file: str,
    ) -> str:
        """Concat files"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("f_fmpeg_concat_pp_concat_files")

