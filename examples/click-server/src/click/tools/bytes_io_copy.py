"""bytes_io_copy tools for click."""

import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register bytes_io_copy tools with the server."""

    @server.tool()
    async def bytes_io_copy_write(
        b: str,
    ) -> str:
        """Write"""
        # Call function via CLI backend: src/click/testing.py::write
        return await backend.run_function_as_cli(
            "src/click/testing.py",
            "write",
            b=b,
        )

