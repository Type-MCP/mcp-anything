"""bool_param_type tools for click."""

import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register bool_param_type tools with the server."""

    @server.tool()
    async def bool_param_type_convert(
        value: str,
        param: str,
        ctx: str,
    ) -> str:
        """Convert"""
        # Call function via CLI backend: src/click/types.py::convert
        return await backend.run_function_as_cli(
            "src/click/types.py",
            "convert",
            value=value,
            param=param,
            ctx=ctx,
        )

    @server.tool()
    async def bool_param_type_str_to_bool(
        value: str,
    ) -> str:
        """Convert a string to a boolean value."""
        # Call function via CLI backend: src/click/types.py::str_to_bool
        return await backend.run_function_as_cli(
            "src/click/types.py",
            "str_to_bool",
            value=value,
        )

