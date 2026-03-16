# httpstat MCP Server

MCP server for httpstat

## Available Tools

### run_httpstat

Run httpstat with the given command-line arguments

Parameters:
- `args` (string): Command-line arguments to pass to httpstat (e.g. a URL or flags)
### print_help

Print help


## Available Resources

- `app://httpstat/status` — Current status and version of httpstat
- `app://httpstat/commands` — Available commands and tools in httpstat
- `docs://httpstat/tool-index` — Complete index of all httpstat tools with parameters and usage

## Available Prompts

- `use_httpstat` — Guide for using httpstat tools effectively
- `debug_httpstat` — Diagnose issues with httpstat operations

## Usage

This server runs over stdio. Add it to your MCP client config:

```json
{
  "mcpServers": {
    "httpstat": {
      "command": "mcp-httpstat"
    }
  }
}
```
