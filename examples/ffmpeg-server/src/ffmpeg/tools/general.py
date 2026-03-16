"""general tools for ffmpeg."""

import inspect
import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register general tools with the server."""

    @server.tool()
    async def run_ffmpeg(
        args: str,
    ) -> str:
        """Run ffmpeg with the given command-line arguments"""
        # Run CLI subcommand: 
        cmd_args: list[str] = []
        if args:
            cmd_args.extend(args.split())
        return await backend.run_subcommand("", cmd_args)

