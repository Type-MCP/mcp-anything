"""f_fmpeg_thumbnails_convertor_pp tools for yt-dlp."""

import inspect
import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register f_fmpeg_thumbnails_convertor_pp tools with the server."""

    @server.tool()
    async def f_fmpeg_thumbnails_convertor_pp_convert_thumbnail(
        thumbnail_filename: str,
        target_ext: str,
    ) -> str:
        """Convert thumbnail"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("f_fmpeg_thumbnails_convertor_pp_convert_thumbnail")

    @server.tool()
    async def f_fmpeg_thumbnails_convertor_pp_fixup_webp(
        info: str,
        idx: str | None = None,
    ) -> str:
        """Fixup webp"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("f_fmpeg_thumbnails_convertor_pp_fixup_webp")

    @server.tool()
    async def f_fmpeg_thumbnails_convertor_pp_is_webp(
        path: str,
    ) -> str:
        """Is webp"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("f_fmpeg_thumbnails_convertor_pp_is_webp")

