"""Resources for github."""

import json

from mcp.server.fastmcp import FastMCP


def register_resources(server: FastMCP, backend) -> None:
    """Register resources with the server."""

    @server.resource("app://github/status")
    async def github_status() -> str:
        """Current status and version of github"""
        return json.dumps({
            "name": "github",
            "status": "running",
        }, indent=2)

    @server.resource("app://github/commands")
    async def github_commands() -> str:
        """Available commands and tools in github"""
        tools = server.list_tools()
        commands = []
        for tool in tools:
            commands.append({
                "name": tool.name,
                "description": tool.description or "",
            })
        return json.dumps({"commands": commands}, indent=2)

    @server.resource("app://github/config")
    async def github_config() -> str:
        """Current configuration of github"""
        return json.dumps({
            "note": "Configuration resource for github",
        }, indent=2)

    @server.resource("docs://github/tool-index")
    async def github_tool_index() -> str:
        """Complete index of all github tools with parameters and usage"""
        # Dynamic documentation resource
        tools = server.list_tools()
        doc_entries = []
        for tool in tools:
            entry = {"name": tool.name, "description": tool.description or ""}
            if hasattr(tool, "inputSchema") and tool.inputSchema:
                entry["parameters"] = tool.inputSchema.get("properties", {})
                entry["required"] = tool.inputSchema.get("required", [])
            doc_entries.append(entry)
        return json.dumps({
            "server": "github",
            "resource": "docs://github/tool-index",
            "tools": doc_entries,
        }, indent=2)

    @server.resource("docs://github/api")
    async def github_api_docs() -> str:
        """Documentation for github api capabilities"""
        # Dynamic documentation resource
        tools = server.list_tools()
        doc_entries = []
        for tool in tools:
            entry = {"name": tool.name, "description": tool.description or ""}
            if hasattr(tool, "inputSchema") and tool.inputSchema:
                entry["parameters"] = tool.inputSchema.get("properties", {})
                entry["required"] = tool.inputSchema.get("required", [])
            doc_entries.append(entry)
        return json.dumps({
            "server": "github",
            "resource": "docs://github/api",
            "tools": doc_entries,
        }, indent=2)

