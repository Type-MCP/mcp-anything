# MCP-Anything

## What this project does
Auto-generates MCP servers from any scriptable application's source code.
Analyzes codebases to find IPC mechanisms, designs tool/resource schemas, and generates
fully functional pip-installable MCP server packages.

## Development
- Install: `pip install -e ".[dev,llm]"`
- Run tests: `pytest tests/ -v`
- Run CLI: `mcp-anything --help`

## Architecture
- 6-phase pipeline: ANALYZE → DESIGN → IMPLEMENT → TEST → DOCUMENT → PACKAGE
- Static detectors + optional LLM analysis (Claude API)
- Jinja2 templates for code generation
- Generated servers use `mcp` SDK's FastMCP
- Pipeline state saved as JSON manifest for resume support
