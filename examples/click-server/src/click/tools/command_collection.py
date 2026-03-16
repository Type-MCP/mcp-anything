"""command_collection tools for click."""

import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register command_collection tools with the server."""

    @server.tool()
    async def command_collection_add_source(
        group: str,
    ) -> str:
        """Add a group as a source of commands."""
        # Call function via CLI backend: src/click/core.py::add_source
        return await backend.run_function_as_cli(
            "src/click/core.py",
            "add_source",
            group=group,
        )

    @server.tool()
    async def command_collection_get_command(
        ctx: str,
        cmd_name: str,
    ) -> str:
        """Get command"""
        # Call function via CLI backend: src/click/core.py::get_command
        return await backend.run_function_as_cli(
            "src/click/core.py",
            "get_command",
            ctx=ctx,
            cmd_name=cmd_name,
        )

    @server.tool()
    async def command_collection_list_commands(
        ctx: str,
    ) -> str:
        """List commands"""
        # Call function via CLI backend: src/click/core.py::list_commands
        return await backend.run_function_as_cli(
            "src/click/core.py",
            "list_commands",
            ctx=ctx,
        )

