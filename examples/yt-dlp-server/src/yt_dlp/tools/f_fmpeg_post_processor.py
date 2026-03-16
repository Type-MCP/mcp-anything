"""f_fmpeg_post_processor tools for yt-dlp."""

import inspect
import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register f_fmpeg_post_processor tools with the server."""

    @server.tool()
    async def f_fmpeg_post_processor_available(
    ) -> str:
        """Available"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("f_fmpeg_post_processor_available")

    @server.tool()
    async def f_fmpeg_post_processor_basename(
    ) -> str:
        """Basename"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("f_fmpeg_post_processor_basename")

    @server.tool()
    async def f_fmpeg_post_processor_check_version(
    ) -> str:
        """Check version"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("f_fmpeg_post_processor_check_version")

    @server.tool()
    async def f_fmpeg_post_processor_concat_files(
        in_files: str,
        out_file: str,
        concat_opts: str | None = None,
    ) -> str:
        """Use concat demuxer to concatenate multiple files having identical streams."""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("f_fmpeg_post_processor_concat_files")

    @server.tool()
    async def f_fmpeg_post_processor_executable(
    ) -> str:
        """Executable"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("f_fmpeg_post_processor_executable")

    @server.tool()
    async def f_fmpeg_post_processor_force_keyframes(
        filename: str,
        timestamps: str,
    ) -> str:
        """Force keyframes"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("f_fmpeg_post_processor_force_keyframes")

    @server.tool()
    async def f_fmpeg_post_processor_get_audio_codec(
        path: str,
    ) -> str:
        """Get audio codec"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("f_fmpeg_post_processor_get_audio_codec")

    @server.tool()
    async def f_fmpeg_post_processor_get_metadata_object(
        path: str,
        opts: str | None = "[]",
    ) -> str:
        """Get metadata object"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("f_fmpeg_post_processor_get_metadata_object")

    @server.tool()
    async def f_fmpeg_post_processor_get_stream_number(
        path: str,
        keys: str,
        value: str,
    ) -> str:
        """Get stream number"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("f_fmpeg_post_processor_get_stream_number")

    @server.tool()
    async def f_fmpeg_post_processor_get_versions(
        downloader: str | None = None,
    ) -> str:
        """Get versions"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("f_fmpeg_post_processor_get_versions")

    @server.tool()
    async def f_fmpeg_post_processor_get_versions_and_features(
        downloader: str | None = None,
    ) -> str:
        """Get versions and features"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("f_fmpeg_post_processor_get_versions_and_features")

    @server.tool()
    async def f_fmpeg_post_processor_probe_available(
    ) -> str:
        """Probe available"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("f_fmpeg_post_processor_probe_available")

    @server.tool()
    async def f_fmpeg_post_processor_probe_basename(
    ) -> str:
        """Probe basename"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("f_fmpeg_post_processor_probe_basename")

    @server.tool()
    async def f_fmpeg_post_processor_probe_executable(
    ) -> str:
        """Probe executable"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("f_fmpeg_post_processor_probe_executable")

    @server.tool()
    async def f_fmpeg_post_processor_run_ffmpeg(
        path: str,
        out_path: str,
        opts: str,
    ) -> str:
        """Run ffmpeg"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("f_fmpeg_post_processor_run_ffmpeg")

    @server.tool()
    async def f_fmpeg_post_processor_run_ffmpeg_multiple_files(
        input_paths: str,
        out_path: str,
        opts: str,
    ) -> str:
        """Run ffmpeg multiple files"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("f_fmpeg_post_processor_run_ffmpeg_multiple_files")

    @server.tool()
    async def f_fmpeg_post_processor_stream_copy_opts(
        copy: str | None = "True",
        ext: str | None = None,
    ) -> str:
        """Stream copy opts"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("f_fmpeg_post_processor_stream_copy_opts")

