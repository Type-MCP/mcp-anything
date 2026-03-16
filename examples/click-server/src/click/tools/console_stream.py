"""console_stream tools for click."""

import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register console_stream tools with the server."""

    @server.tool()
    async def console_stream_name(
    ) -> str:
        """Name"""
        # Call function via CLI backend: src/click/_winconsole.py::name
        return await backend.run_function_as_cli(
            "src/click/_winconsole.py",
            "name",
        )

    @server.tool()
    async def console_stream_write(
        x: str,
    ) -> str:
        """Write"""
        # Call function via CLI backend: src/click/_winconsole.py::write
        return await backend.run_function_as_cli(
            "src/click/_winconsole.py",
            "write",
            x=x,
        )

    @server.tool()
    async def console_stream_writelines(
        lines: str,
    ) -> str:
        """Writelines"""
        # Call function via CLI backend: src/click/_winconsole.py::writelines
        return await backend.run_function_as_cli(
            "src/click/_winconsole.py",
            "writelines",
            lines=lines,
        )

