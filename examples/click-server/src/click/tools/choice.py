"""choice tools for click."""

import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register choice tools with the server."""

    @server.tool()
    async def choice_convert(
        value: str,
        param: str,
        ctx: str,
    ) -> str:
        """For a given value from the parser, normalize it and find its"""
        # Call function via CLI backend: src/click/types.py::convert
        return await backend.run_function_as_cli(
            "src/click/types.py",
            "convert",
            value=value,
            param=param,
            ctx=ctx,
        )

    @server.tool()
    async def choice_get_invalid_choice_message(
        value: str,
        ctx: str,
    ) -> str:
        """Get the error message when the given choice is invalid."""
        # Call function via CLI backend: src/click/types.py::get_invalid_choice_message
        return await backend.run_function_as_cli(
            "src/click/types.py",
            "get_invalid_choice_message",
            value=value,
            ctx=ctx,
        )

    @server.tool()
    async def choice_get_metavar(
        param: str,
        ctx: str,
    ) -> str:
        """Get metavar"""
        # Call function via CLI backend: src/click/types.py::get_metavar
        return await backend.run_function_as_cli(
            "src/click/types.py",
            "get_metavar",
            param=param,
            ctx=ctx,
        )

    @server.tool()
    async def choice_get_missing_message(
        param: str,
        ctx: str,
    ) -> str:
        """Message shown when no choice is passed."""
        # Call function via CLI backend: src/click/types.py::get_missing_message
        return await backend.run_function_as_cli(
            "src/click/types.py",
            "get_missing_message",
            param=param,
            ctx=ctx,
        )

    @server.tool()
    async def choice_normalize_choice(
        choice: str,
        ctx: str,
    ) -> str:
        """Normalize a choice value, used to map a passed string to a choice."""
        # Call function via CLI backend: src/click/types.py::normalize_choice
        return await backend.run_function_as_cli(
            "src/click/types.py",
            "normalize_choice",
            choice=choice,
            ctx=ctx,
        )

    @server.tool()
    async def choice_shell_complete(
        ctx: str,
        param: str,
        incomplete: str,
    ) -> str:
        """Complete choices that start with the incomplete value."""
        # Call function via CLI backend: src/click/types.py::shell_complete
        return await backend.run_function_as_cli(
            "src/click/types.py",
            "shell_complete",
            ctx=ctx,
            param=param,
            incomplete=incomplete,
        )

    @server.tool()
    async def choice_to_info_dict(
    ) -> str:
        """To info dict"""
        # Call function via CLI backend: src/click/types.py::to_info_dict
        return await backend.run_function_as_cli(
            "src/click/types.py",
            "to_info_dict",
        )

