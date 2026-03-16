"""MCP server for click."""

import os

from mcp.server.fastmcp import FastMCP

server = FastMCP("click")

from click.backend import Backend

_backend = Backend()

# Import and register tool modules
from click.tools.creation import register_tools as register_creation_tools
register_creation_tools(server, _backend)
from click.tools.argument import register_tools as register_argument_tools
register_argument_tools(server, _backend)
from click.tools.general import register_tools as register_general_tools
register_general_tools(server, _backend)
from click.tools.bash_complete import register_tools as register_bash_complete_tools
register_bash_complete_tools(server, _backend)
from click.tools.bool_param_type import register_tools as register_bool_param_type_tools
register_bool_param_type_tools(server, _backend)
from click.tools.bytes_io_copy import register_tools as register_bytes_io_copy_tools
register_bytes_io_copy_tools(server, _backend)
from click.tools.choice import register_tools as register_choice_tools
register_choice_tools(server, _backend)
from click.tools.cli_runner import register_tools as register_cli_runner_tools
register_cli_runner_tools(server, _backend)
from click.tools.click_exception import register_tools as register_click_exception_tools
register_click_exception_tools(server, _backend)
from click.tools.command import register_tools as register_command_tools
register_command_tools(server, _backend)
from click.tools.command_collection import register_tools as register_command_collection_tools
register_command_collection_tools(server, _backend)
from click.tools.composite_param_type import register_tools as register_composite_param_type_tools
register_composite_param_type_tools(server, _backend)
from click.tools.console_stream import register_tools as register_console_stream_tools
register_console_stream_tools(server, _backend)

# Import and register resources
from click.resources import register_resources
register_resources(server, _backend)

# Import and register prompts
from click.prompts import register_prompts
register_prompts(server)



def main():
    """Run the MCP server."""
    transport = os.environ.get("MCP_TRANSPORT", "stdio")

    if transport == "http":
        host = os.environ.get("MCP_HOST", "0.0.0.0")
        port = int(os.environ.get("MCP_PORT", "8000"))
        server.run(transport="sse", host=host, port=port)
    else:
        server.run(transport="stdio")


if __name__ == "__main__":
    main()
