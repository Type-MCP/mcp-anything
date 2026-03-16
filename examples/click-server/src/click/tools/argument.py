"""argument tools for click."""

import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register argument tools with the server."""

    @server.tool()
    async def argument_add_to_parser(
        parser: str,
        ctx: str,
    ) -> str:
        """Add to parser"""
        # Call function via CLI backend: src/click/core.py::add_to_parser
        return await backend.run_function_as_cli(
            "src/click/core.py",
            "add_to_parser",
            parser=parser,
            ctx=ctx,
        )

    @server.tool()
    async def argument_get_error_hint(
        ctx: str,
    ) -> str:
        """Get error hint"""
        # Call function via CLI backend: src/click/core.py::get_error_hint
        return await backend.run_function_as_cli(
            "src/click/core.py",
            "get_error_hint",
            ctx=ctx,
        )

    @server.tool()
    async def argument_get_usage_pieces(
        ctx: str,
    ) -> str:
        """Get usage pieces"""
        # Call function via CLI backend: src/click/core.py::get_usage_pieces
        return await backend.run_function_as_cli(
            "src/click/core.py",
            "get_usage_pieces",
            ctx=ctx,
        )

    @server.tool()
    async def argument_human_readable_name(
    ) -> str:
        """Human readable name"""
        # Call function via CLI backend: src/click/core.py::human_readable_name
        return await backend.run_function_as_cli(
            "src/click/core.py",
            "human_readable_name",
        )

    @server.tool()
    async def argument_make_metavar(
        ctx: str,
    ) -> str:
        """Make metavar"""
        # Call function via CLI backend: src/click/core.py::make_metavar
        return await backend.run_function_as_cli(
            "src/click/core.py",
            "make_metavar",
            ctx=ctx,
        )

