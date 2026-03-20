# v0.1.2 — Founder trial hardening

This release tightens the path from `mcp-anything generate ...` to a working MCP server for real production codebases, with a specific focus on HTTP onboarding and frameworks the upcoming founder trial depends on.

## Highlights

- **Direct OpenAPI file input** — `mcp-anything generate ./openapi.json` now works without wrapping the spec in a directory first
- **HTTP onboarding fixes** — generated docs now explain upstream `*_BASE_URL` and upstream auth environment variables
- **Safer `mcp.json` generation** — stdio configs now include required env placeholders for HTTP proxy tools, and the `mcp-anything serve` fallback preserves them if editable install fails
- **Better Express coverage** — added support for `routing-controllers` decorator-based apps and fixed HTTP body handling in generated tools
- **Stronger validation** — added regression coverage for codegen, integration, CLI, and new framework detection paths

## Real-repo validation

- `spring-guides/gs-rest-service`
- `spring-projects/spring-petclinic`
- `w3tecch/express-typescript-boilerplate`
- `eclipse-ee4j/jersey` (`examples/helloworld-webapp`)

These checks exercised real Spring, Express/TypeScript, and Jersey/JAX-RS repositories and validated the generated MCP packages and fallback configs end to end.

## Installation

```bash
pip install -U mcp-anything
```

See the [README](https://github.com/gabrielekarra/mcp-anything#readme) for the latest quickstart and deployment notes.

# v0.1.0 — First public release

MCP-Anything auto-generates fully functional MCP server packages from any codebase. Point it at source code — Python, Java, Go, Rust, Ruby, TypeScript — and get a pip-installable MCP server in minutes, no manual wrapping required.

## Key capabilities

- **15 static detectors** — CLI (argparse, Click, Typer), HTTP frameworks (FastAPI, Flask, Spring Boot, Express, Django, Rails, Gin, Actix, Axum), OpenAPI/Swagger, GraphQL, gRPC/Protobuf, WebSockets
- **6-phase pipeline** — Analyze, Design, Implement, Test, Document, Package — with JSON manifest for resume support
- **Multiple backend strategies** — CLI subprocess, HTTP proxy, Python call, stub — auto-selected based on what the codebase exposes
- **Full MCP protocol** — Tools, Resources, Prompts, AGENTS.md generation for agent discoverability
- **HTTP transport** — `--transport http` for remote deployment with OpenTelemetry tracing and Docker packaging
- **LLM-enhanced analysis** — Optional Claude API integration for better tool descriptions and grouping

## Installation

```bash
pip install mcp-anything
```

## Quick start

```bash
mcp-anything generate /path/to/any/app
```

See the [README](https://github.com/gabrielekarra/mcp-anything#readme) for full documentation, examples, and usage.

## What's next

- Desktop software showcase (Blender, GIMP, Audacity)
- Plugin system for custom detectors
