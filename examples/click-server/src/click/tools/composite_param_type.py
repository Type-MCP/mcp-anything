"""composite_param_type tools for click."""

import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register composite_param_type tools with the server."""

    @server.tool()
    async def composite_param_type_arity(
    ) -> str:
        """Arity"""
        # Call function via CLI backend: src/click/types.py::arity
        return await backend.run_function_as_cli(
            "src/click/types.py",
            "arity",
        )

