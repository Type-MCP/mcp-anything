"""f_fmpeg_extract_audio_pp tools for yt-dlp."""

import inspect
import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register f_fmpeg_extract_audio_pp tools with the server."""

    @server.tool()
    async def f_fmpeg_extract_audio_pp_run_ffmpeg(
        path: str,
        out_path: str,
        codec: str,
        more_opts: str,
    ) -> str:
        """Run ffmpeg"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("f_fmpeg_extract_audio_pp_run_ffmpeg")

