# Contributing to MCP-Anything

Thanks for your interest in contributing to MCP-Anything! This guide will help you get set up and understand how the project is structured.

## Getting Started

### Prerequisites

- Python 3.10+
- Git

### Setup

```bash
git clone https://github.com/gabrielekarra/mcp-anything.git
cd mcp-anything
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev,llm]"
```

The `[dev]` extra installs pytest and test dependencies. The `[llm]` extra installs the Anthropic SDK for optional LLM-enhanced analysis.

### Running Tests

```bash
pytest tests/ -v
```

All tests should pass before submitting a PR. The test suite runs in under 1 second.

## Project Architecture

MCP-Anything follows a 6-phase pipeline architecture:

```
ANALYZE → DESIGN → IMPLEMENT → TEST → DOCUMENT → PACKAGE
```

### Directory Structure

```
src/mcp_anything/
├── cli.py                      # CLI entry point
├── analysis/                   # Phase 1: Codebase analysis
│   ├── scanner.py              # Filesystem walker and file classifier
│   ├── ast_analyzer.py         # Python AST parsing
│   ├── flask_fastapi_analyzer.py  # Flask/FastAPI route extraction
│   ├── java_analyzer.py        # Spring Boot endpoint extraction
│   ├── openapi_analyzer.py     # OpenAPI/Swagger spec parsing
│   ├── help_parser.py          # CLI --help output parsing
│   ├── llm_analyzer.py         # Optional Claude API analysis
│   └── detectors/              # IPC mechanism detectors
│       ├── base.py             # Abstract Detector base class
│       ├── cli_detector.py
│       ├── flask_fastapi_detector.py
│       ├── openapi_detector.py
│       ├── spring_detector.py
│       └── ...
├── models/                     # Pydantic data models
│   ├── analysis.py             # AnalysisResult, Capability, IPCMechanism
│   ├── design.py               # ToolSpec, ServerDesign, BackendConfig
│   └── manifest.py             # Pipeline state tracking
├── pipeline/                   # Pipeline phases
│   ├── engine.py               # PipelineEngine orchestrator
│   ├── context.py              # Shared pipeline context
│   ├── analyze.py              # Phase 1: ANALYZE
│   ├── design.py               # Phase 2: DESIGN
│   ├── implement.py            # Phase 3: IMPLEMENT
│   ├── test_phase.py           # Phase 4: TEST
│   ├── document.py             # Phase 5: DOCUMENT
│   └── package.py              # Phase 6: PACKAGE
└── codegen/                    # Code generation
    ├── emitter.py              # File writer with AST validation
    ├── renderer.py             # Jinja2 template engine
    └── templates/              # Jinja2 templates for generated code
```

### Key Concepts

**Detector** — Scans source files for patterns indicating a specific IPC mechanism (CLI, HTTP, socket, etc.). Returns `IPCMechanism` objects with confidence scores and evidence.

**Analyzer** — Deep extraction of capabilities from source code. The AST analyzer handles Python; the Java analyzer handles Spring Boot; the Flask/FastAPI analyzer handles Python web frameworks; the OpenAPI analyzer handles spec files.

**Capability** — A single feature/tool the target application exposes (e.g., an HTTP endpoint, a CLI subcommand, a Python function).

**ToolSpec** — A designed MCP tool with implementation strategy, parameters, and metadata. Created from Capabilities during the Design phase.

**ToolImpl** — How to actually invoke a tool at runtime. Strategies: `cli_subcommand`, `cli_function`, `python_call`, `http_call`, `stub`.

### Data Flow

```
Source Code
    ↓
Detectors → IPCMechanism (what IPC the app uses)
Analyzers → Capability[] (what the app can do)
    ↓
Design Phase → ToolSpec[] + ResourceSpec[] + BackendConfig
    ↓
Codegen → Generated MCP Server Package
```

## How to Contribute

### Adding a New Detector

Detectors identify IPC mechanisms via pattern matching. To add one:

1. Create `src/mcp_anything/analysis/detectors/my_detector.py`:

```python
from pathlib import Path
from mcp_anything.models.analysis import FileInfo, IPCMechanism, IPCType
from .base import Detector

MY_PATTERNS = [
    (r"pattern_regex", "Description of what matched", 0.9),
]

class MyDetector(Detector):
    @property
    def name(self) -> str:
        return "My Detector"

    def detect(self, root: Path, files: list[FileInfo]) -> list[IPCMechanism]:
        evidence = []
        max_confidence = 0.0

        for fi in files:
            content = self._read_file(root, fi)
            if not content:
                continue
            for pattern, desc, conf in MY_PATTERNS:
                if re.search(pattern, content):
                    evidence.append(f"{fi.path}: {desc}")
                    max_confidence = max(max_confidence, conf)

        if not evidence:
            return []

        return [IPCMechanism(
            ipc_type=IPCType.PROTOCOL,  # or CLI, SOCKET, etc.
            confidence=max_confidence,
            evidence=evidence,
            details={"key": "value"},
        )]
```

2. Register it in `detectors/__init__.py`:

```python
from .my_detector import MyDetector

ALL_DETECTORS = [
    ...,
    MyDetector,
]
```

3. Add tests in `tests/test_my_detector.py`.

### Adding a New Analyzer

Analyzers extract capabilities from source code. See `flask_fastapi_analyzer.py` or `java_analyzer.py` for examples.

Key steps:
1. Create the analyzer in `src/mcp_anything/analysis/`
2. Return `Capability` objects with `category="api"`, `ipc_type=IPCType.PROTOCOL`
3. Include HTTP method and path in the description: `"GET /users - List users"`
4. Wire it into `pipeline/analyze.py` in the `execute()` method
5. Add results to `_ast_fallback()` for merging

### Adding a New Backend Template

Backend templates define how generated servers communicate with target apps.

1. Create `src/mcp_anything/codegen/templates/backend_mytype.py.j2`
2. Update `emitter.py` to select your template based on IPC type
3. The template receives the `design` object (type `ServerDesign`)

### Writing Tests

- Place test files in `tests/`
- Use fixtures in `tests/fixtures/` for fake applications
- Register fixtures in `tests/conftest.py`
- Follow existing patterns — see `test_flask_fastapi.py` for a good example

Test structure:
```python
class TestMyDetector:
    def test_detects_pattern(self, fixture_dir):
        files = scan_codebase(fixture_dir)
        detector = MyDetector()
        mechs = detector.detect(fixture_dir, files)
        assert len(mechs) == 1
        assert mechs[0].ipc_type == IPCType.PROTOCOL

class TestMyAnalyzer:
    def test_extracts_endpoints(self, fixture_dir):
        fi = FileInfo(path="app.py", language=Language.PYTHON, ...)
        result = analyze_my_file(fixture_dir, fi)
        assert len(result.routes) == 5
```

### Testing Against Real Repos

After implementing a new analyzer, test it end-to-end:

```bash
# Clone a real project
git clone --depth 1 https://github.com/user/project.git /tmp/project

# Generate MCP server
mcp-anything generate /tmp/project --name my-project --no-llm

# Install and verify
pip install -e /tmp/mcp-my-project-server

# Test MCP protocol
echo '{"jsonrpc":"2.0","id":1,"method":"initialize",...}' | mcp-my-project
```

## Code Style

- No strict formatter enforced, but keep code consistent with existing style
- Use type annotations for function signatures
- Keep functions focused — extract helpers when logic gets complex
- Prefer simple regex over external parsing libraries where possible
- Skip adding docstrings/comments to code you didn't change

## Submitting Changes

1. Fork the repository
2. Create a feature branch: `git checkout -b my-feature`
3. Make your changes
4. Run the test suite: `pytest tests/ -v`
5. Commit with a descriptive message
6. Open a pull request against `main`

### PR Guidelines

- Keep PRs focused on a single feature or fix
- Include tests for new functionality
- Update `ROADMAP.md` if your change completes a planned item
- Test against at least one real-world project when adding framework support

## Questions?

Open an issue at https://github.com/gabrielekarra/mcp-anything/issues.
