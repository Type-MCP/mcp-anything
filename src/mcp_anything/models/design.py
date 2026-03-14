"""Models for the design phase output."""

from typing import Optional

from pydantic import BaseModel, Field

from mcp_anything.models.analysis import IPCType, ParameterSpec


class ToolImpl(BaseModel):
    """How to actually call the underlying application for this tool."""

    strategy: str = "stub"  # "cli_subcommand", "cli_function", "python_call", "stub"
    # For cli_subcommand: the subcommand name to pass to the app binary
    cli_subcommand: str = ""
    # For cli_function: the source file + function that wraps into a CLI call
    cli_entry: str = ""
    # For python_call: module path and function to import and call directly
    python_module: str = ""
    python_function: str = ""
    python_import_path: str = ""
    # Mapping of tool param names to CLI argument forms
    # e.g. {"input_path": {"position": 0}, "format": {"flag": "--format"}}
    arg_mapping: dict[str, dict] = Field(default_factory=dict)


class ToolSpec(BaseModel):
    """Specification for a single MCP tool."""

    name: str
    description: str
    parameters: list[ParameterSpec] = Field(default_factory=list)
    return_type: str = "string"
    module: str = ""
    ipc_type: Optional[IPCType] = None
    implementation_hint: str = ""
    impl: ToolImpl = Field(default_factory=ToolImpl)


class ResourceSpec(BaseModel):
    """Specification for a single MCP resource."""

    uri: str
    name: str
    description: str
    mime_type: str = "application/json"


class BackendConfig(BaseModel):
    """Configuration for the communication backend."""

    backend_type: IPCType
    host: str = "localhost"
    port: int = 0
    socket_path: str = ""
    command: str = ""
    command_args: list[str] = Field(default_factory=list)
    env_vars: dict[str, str] = Field(default_factory=dict)
    codebase_path: str = ""  # absolute path to the target app


class ServerDesign(BaseModel):
    """Complete design for the generated MCP server."""

    server_name: str
    server_description: str = ""
    tools: list[ToolSpec] = Field(default_factory=list)
    resources: list[ResourceSpec] = Field(default_factory=list)
    tool_modules: dict[str, list[str]] = Field(default_factory=dict)
    backend: Optional[BackendConfig] = None
    dependencies: list[str] = Field(default_factory=lambda: ["mcp>=1.0"])
    python_requires: str = ">=3.10"
    target_install_hint: str = ""  # pip install instruction for the target app
