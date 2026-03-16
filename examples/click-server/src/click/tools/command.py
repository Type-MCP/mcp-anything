"""command tools for click."""

import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register command tools with the server."""

    @server.tool()
    async def command_collect_usage_pieces(
        ctx: str,
    ) -> str:
        """Returns all the pieces that go into the usage line and returns"""
        # Call function via CLI backend: src/click/core.py::collect_usage_pieces
        return await backend.run_function_as_cli(
            "src/click/core.py",
            "collect_usage_pieces",
            ctx=ctx,
        )

    @server.tool()
    async def command_format_epilog(
        ctx: str,
        formatter: str,
    ) -> str:
        """Writes the epilog into the formatter if it exists."""
        # Call function via CLI backend: src/click/core.py::format_epilog
        return await backend.run_function_as_cli(
            "src/click/core.py",
            "format_epilog",
            ctx=ctx,
            formatter=formatter,
        )

    @server.tool()
    async def command_format_help(
        ctx: str,
        formatter: str,
    ) -> str:
        """Writes the help into the formatter if it exists."""
        # Call function via CLI backend: src/click/core.py::format_help
        return await backend.run_function_as_cli(
            "src/click/core.py",
            "format_help",
            ctx=ctx,
            formatter=formatter,
        )

    @server.tool()
    async def command_format_help_text(
        ctx: str,
        formatter: str,
    ) -> str:
        """Writes the help text to the formatter if it exists."""
        # Call function via CLI backend: src/click/core.py::format_help_text
        return await backend.run_function_as_cli(
            "src/click/core.py",
            "format_help_text",
            ctx=ctx,
            formatter=formatter,
        )

    @server.tool()
    async def command_format_options(
        ctx: str,
        formatter: str,
    ) -> str:
        """Writes all the options into the formatter if they exist."""
        # Call function via CLI backend: src/click/core.py::format_options
        return await backend.run_function_as_cli(
            "src/click/core.py",
            "format_options",
            ctx=ctx,
            formatter=formatter,
        )

    @server.tool()
    async def command_format_usage(
        ctx: str,
        formatter: str,
    ) -> str:
        """Writes the usage line into the formatter."""
        # Call function via CLI backend: src/click/core.py::format_usage
        return await backend.run_function_as_cli(
            "src/click/core.py",
            "format_usage",
            ctx=ctx,
            formatter=formatter,
        )

    @server.tool()
    async def command_get_help(
        ctx: str,
    ) -> str:
        """Formats the help into a string and returns it."""
        # Call function via CLI backend: src/click/core.py::get_help
        return await backend.run_function_as_cli(
            "src/click/core.py",
            "get_help",
            ctx=ctx,
        )

    @server.tool()
    async def command_get_help_option(
        ctx: str,
    ) -> str:
        """Returns the help option object."""
        # Call function via CLI backend: src/click/core.py::get_help_option
        return await backend.run_function_as_cli(
            "src/click/core.py",
            "get_help_option",
            ctx=ctx,
        )

    @server.tool()
    async def command_get_help_option_names(
        ctx: str,
    ) -> str:
        """Returns the names for the help option."""
        # Call function via CLI backend: src/click/core.py::get_help_option_names
        return await backend.run_function_as_cli(
            "src/click/core.py",
            "get_help_option_names",
            ctx=ctx,
        )

    @server.tool()
    async def command_get_params(
        ctx: str,
    ) -> str:
        """Get params"""
        # Call function via CLI backend: src/click/core.py::get_params
        return await backend.run_function_as_cli(
            "src/click/core.py",
            "get_params",
            ctx=ctx,
        )

    @server.tool()
    async def command_get_short_help_str(
        limit: int | None = 45,
    ) -> str:
        """Gets short help for the command or makes it by shortening the"""
        # Call function via CLI backend: src/click/core.py::get_short_help_str
        return await backend.run_function_as_cli(
            "src/click/core.py",
            "get_short_help_str",
            limit=limit,
        )

    @server.tool()
    async def command_get_usage(
        ctx: str,
    ) -> str:
        """Formats the usage line into a string and returns it."""
        # Call function via CLI backend: src/click/core.py::get_usage
        return await backend.run_function_as_cli(
            "src/click/core.py",
            "get_usage",
            ctx=ctx,
        )

    @server.tool()
    async def command_make_context(
        info_name: str,
        args: list,
        parent: str | None = None,
    ) -> str:
        """This function when given an info name and arguments will kick"""
        # Call function via CLI backend: src/click/core.py::make_context
        return await backend.run_function_as_cli(
            "src/click/core.py",
            "make_context",
            info_name=info_name,
            args=args,
            parent=parent,
        )

    @server.tool()
    async def command_make_parser(
        ctx: str,
    ) -> str:
        """Creates the underlying option parser for this command."""
        # Call function via CLI backend: src/click/core.py::make_parser
        return await backend.run_function_as_cli(
            "src/click/core.py",
            "make_parser",
            ctx=ctx,
        )

    @server.tool()
    async def command_shell_complete(
        ctx: str,
        incomplete: str,
    ) -> str:
        """Return a list of completions for the incomplete value. Looks"""
        # Call function via CLI backend: src/click/core.py::shell_complete
        return await backend.run_function_as_cli(
            "src/click/core.py",
            "shell_complete",
            ctx=ctx,
            incomplete=incomplete,
        )

    @server.tool()
    async def command_to_info_dict(
        ctx: str,
    ) -> str:
        """To info dict"""
        # Call function via CLI backend: src/click/core.py::to_info_dict
        return await backend.run_function_as_cli(
            "src/click/core.py",
            "to_info_dict",
            ctx=ctx,
        )

