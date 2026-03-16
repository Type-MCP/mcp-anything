"""general tools for httpstat."""

import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register general tools with the server."""

    @server.tool()
    async def run_httpstat(
        args: str,
    ) -> str:
        """Run httpstat with the given command-line arguments"""
        # Run CLI subcommand: 
        cmd_args: list[str] = []
        if args:
            cmd_args.extend(args.split())
        return await backend.run_subcommand("", cmd_args)

    @server.tool()
    async def print_help(
    ) -> str:
        """Print help"""
        # Call function via CLI backend: httpstat.py::print_help
        return await backend.run_function_as_cli(
            "httpstat.py",
            "print_help",
        )

