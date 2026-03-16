"""general tools for click."""

import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register general tools with the server."""

    @server.tool()
    async def augment_usage_errors(
        ctx: str,
        param: str | None = None,
    ) -> str:
        """Context manager that attaches extra information to exceptions."""
        # Call function via CLI backend: src/click/core.py::augment_usage_errors
        return await backend.run_function_as_cli(
            "src/click/core.py",
            "augment_usage_errors",
            ctx=ctx,
            param=param,
        )

    @server.tool()
    async def batch(
        iterable: str,
        batch_size: int,
    ) -> str:
        """Batch"""
        # Call function via CLI backend: src/click/core.py::batch
        return await backend.run_function_as_cli(
            "src/click/core.py",
            "batch",
            iterable=iterable,
            batch_size=batch_size,
        )

    @server.tool()
    async def clear(
    ) -> str:
        """Clears the terminal screen.  This will have the effect of clearing"""
        # Call function via CLI backend: src/click/termui.py::clear
        return await backend.run_function_as_cli(
            "src/click/termui.py",
            "clear",
        )

    @server.tool()
    async def command(
        name: str,
    ) -> str:
        """Command"""
        # Call function via CLI backend: src/click/decorators.py::command
        return await backend.run_function_as_cli(
            "src/click/decorators.py",
            "command",
            name=name,
        )

    @server.tool()
    async def confirm(
        text: str,
        default: bool | None = False,
        abort: bool | None = False,
        prompt_suffix: str | None = ": ",
        show_default: bool | None = True,
        err: bool | None = False,
    ) -> str:
        """Prompts for confirmation (yes/no question)."""
        # Call function via CLI backend: src/click/termui.py::confirm
        return await backend.run_function_as_cli(
            "src/click/termui.py",
            "confirm",
            text=text,
            default=default,
            abort=abort,
            prompt_suffix=prompt_suffix,
            show_default=show_default,
            err=err,
        )

    @server.tool()
    async def confirmation_option(
    ) -> str:
        """Add a ``--yes`` option which shows a prompt before continuing if"""
        # Call function via CLI backend: src/click/decorators.py::confirmation_option
        return await backend.run_function_as_cli(
            "src/click/decorators.py",
            "confirmation_option",
        )

