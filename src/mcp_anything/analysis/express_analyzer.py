"""Regex-based analyzer for Express.js route endpoints.

Extracts HTTP routes, path parameters, query parameters, and request
bodies from Express.js source files using regex patterns.
"""

import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from mcp_anything.models.analysis import Capability, FileInfo, IPCType, Language, ParameterSpec
from mcp_anything.analysis.route_utils import endpoint_to_tool_name, normalize_path, make_description


@dataclass
class ExpressEndpoint:
    """A route extracted from Express.js source."""

    http_method: str
    path: str
    function_name: str
    description: str
    parameters: list[ParameterSpec]
    source_file: str


@dataclass
class ExpressAnalysisResult:
    """Result of analyzing JS/TS files for Express routes."""

    routes: list[ExpressEndpoint] = field(default_factory=list)
    framework: str = "express"
    has_routers: bool = False


# Regex for route definitions: app.get('/path', handler) or router.post('/path', ...)
_ROUTE_RE = re.compile(
    r"(app|router|\w+Router|\w+)\."
    r"(get|post|put|delete|patch|all)\s*\(\s*"
    r"['\"]([^'\"]+)['\"]",
    re.IGNORECASE,
)

# Chained route pattern: router.route('/path').get(...).post(...)
_ROUTE_CHAIN_RE = re.compile(
    r"(\w+)\.route\s*\(\s*['\"]([^'\"]+)['\"]\s*\)"
)
_CHAIN_METHOD_RE = re.compile(
    r"\.(get|post|put|delete|patch)\s*\(",
    re.IGNORECASE,
)

# Regex for router mount: app.use('/prefix', router)
_ROUTER_USE_RE = re.compile(
    r"app\.use\s*\(\s*['\"]([^'\"]+)['\"]\s*,\s*(\w+)",
)

# Regex for require: const varName = require('./path')
_REQUIRE_RE = re.compile(
    r"(?:const|let|var)\s+(\w+)\s*=\s*require\s*\(\s*['\"]([^'\"]+)['\"]\s*\)",
)

# Regex for ES module import: import varName from './path'
_IMPORT_RE = re.compile(
    r"import\s+(\w+)\s+from\s+['\"]([^'\"]+)['\"]",
)

# Regex for handler function name in route: app.get('/path', handlerName)
_HANDLER_NAME_RE = re.compile(
    r"\.(get|post|put|delete|patch)\s*\(\s*"
    r"['\"][^'\"]+['\"]\s*,\s*"
    r"(?:[\w.]+,\s*)*"  # skip middleware
    r"(\w+)\s*\)",
)

# Regex for inline handler: app.get('/path', (req, res) => { or function(req, res) {
_INLINE_HANDLER_RE = re.compile(
    r"\.(get|post|put|delete|patch)\s*\(\s*"
    r"['\"]([^'\"]+)['\"]\s*,\s*"
    r"(?:[\w.]+,\s*)*"  # skip middleware
    r"(?:async\s+)?"
    r"(?:\(\s*(?:req|request)\s*,\s*(?:res|response)|function\s*\(\s*(?:req|request)\s*,\s*(?:res|response))",
)

# Extract params from handler body: req.params.id, req.query.limit, req.body.name
_REQ_PARAM_RE = re.compile(r"req\.params\.(\w+)")
_REQ_QUERY_RE = re.compile(r"req\.query\.(\w+)")
_REQ_BODY_RE = re.compile(r"req\.body\.(\w+)")

# Destructured params: const { id } = req.params
# Optional TS type annotation before `=`: const { id }: { id: string } = req.params
_TS_TYPE_ANNOTATION = r"(?:\s*:\s*\{[^}]*\})?"
_DESTRUCTURE_PARAMS_RE = re.compile(
    r"(?:const|let|var)\s*\{([^}]+)\}" + _TS_TYPE_ANNOTATION + r"\s*=\s*req\.params"
)
_DESTRUCTURE_QUERY_RE = re.compile(
    r"(?:const|let|var)\s*\{([^}]+)\}" + _TS_TYPE_ANNOTATION + r"\s*=\s*req\.query"
)
_DESTRUCTURE_BODY_RE = re.compile(
    r"(?:const|let|var)\s*\{([^}]+)\}" + _TS_TYPE_ANNOTATION + r"\s*=\s*req\.body"
)

# ── TypeScript type-hint patterns ────────────────────────────────────────────

# `as number` / `as string` / `as boolean` cast after req.params/query access
# e.g.  req.params.id as number   or   req.query.limit as number
_TS_CAST_RE = re.compile(
    r"req\.(?:params|query|body)\.(\w+)\s+as\s+(number|string|boolean|integer|float)",
)

# parseInt / Number / parseFloat applied to a req param
# e.g.  parseInt(req.params.id)   Number(req.query.page)
_TS_PARSEINT_RE = re.compile(
    r"parseInt\s*\(\s*req\.(?:params|query)\.(\w+)",
)
_TS_PARSEFLOAT_RE = re.compile(
    r"parseFloat\s*\(\s*req\.(?:params|query)\.(\w+)",
)
_TS_NUMBER_RE = re.compile(
    r"Number\s*\(\s*req\.(?:params|query)\.(\w+)",
)

# Typed destructuring: const { id, count }: { id: string; count: number } = req.params
# Captures the whole type block and the source (params/query/body)
_TS_TYPED_DESTRUCTURE_RE = re.compile(
    r"(?:const|let|var)\s*\{[^}]+\}\s*:\s*\{([^}]+)\}\s*=\s*req\.(params|query|body)",
)

# Within the type block: `name: type`  or  `name?: type`
_TS_FIELD_TYPE_RE = re.compile(r"(\w+)\??:\s*(number|string|boolean|integer|float)")

# Request<Params, ResBody, Body, Query> generic on handler signature:
# (req: Request<{ id: string }, any, { name: string }, { page?: number }>, res) => ...
_TS_REQUEST_GENERIC_RE = re.compile(
    r"req\s*:\s*Request\s*<\s*"
    r"\{([^}]*)\}"   # group 1: Params
    r"(?:\s*,\s*[^,>]+)?"  # skip ResBody
    r"(?:\s*,\s*\{([^}]*)\})?"  # group 3: Body (optional)
    r"(?:\s*,\s*\{([^}]*)\})?"  # group 4: Query (optional)
    r"\s*>",
    re.DOTALL,
)

_TS_TYPE_MAP = {
    "number": "integer",
    "integer": "integer",
    "float": "float",
    "string": "string",
    "boolean": "boolean",
}


def _resolve_ts_types(context: str) -> dict[str, str]:
    """Scan handler context for TypeScript type hints. Returns {param_name: mcp_type}."""
    hints: dict[str, str] = {}

    # `as number/string/boolean` casts
    for m in _TS_CAST_RE.finditer(context):
        hints[m.group(1)] = _TS_TYPE_MAP.get(m.group(2), "string")

    # parseInt / parseFloat / Number wrappers
    for m in _TS_PARSEINT_RE.finditer(context):
        hints[m.group(1)] = "integer"
    for m in _TS_PARSEFLOAT_RE.finditer(context):
        hints[m.group(1)] = "float"
    for m in _TS_NUMBER_RE.finditer(context):
        hints[m.group(1)] = "integer"

    # Typed destructuring blocks
    for m in _TS_TYPED_DESTRUCTURE_RE.finditer(context):
        type_block = m.group(1)
        for field_m in _TS_FIELD_TYPE_RE.finditer(type_block):
            hints[field_m.group(1)] = _TS_TYPE_MAP.get(field_m.group(2), "string")

    # Request<Params, _, Body, Query> generic
    req_m = _TS_REQUEST_GENERIC_RE.search(context)
    if req_m:
        for block in (req_m.group(1), req_m.group(2), req_m.group(3)):
            if block:
                for field_m in _TS_FIELD_TYPE_RE.finditer(block):
                    hints[field_m.group(1)] = _TS_TYPE_MAP.get(field_m.group(2), "string")

    return hints


def _extract_params_from_context(
    source: str, route_pos: int, is_typescript: bool = False
) -> list[ParameterSpec]:
    """Extract parameters by scanning the handler body after a route definition."""
    # Look at the next ~800 chars after the route for the handler body
    context = source[route_pos:route_pos + 800]
    params: list[ParameterSpec] = []
    seen: set[str] = set()

    # Pre-compute TypeScript type hints for this handler window
    ts_types: dict[str, str] = _resolve_ts_types(context) if is_typescript else {}

    def _type_of(name: str, default: str) -> str:
        return ts_types.get(name, default)

    # Path params from req.params.X or destructured
    for match in _REQ_PARAM_RE.finditer(context):
        name = match.group(1)
        if name not in seen:
            seen.add(name)
            params.append(ParameterSpec(name=name, type=_type_of(name, "string"), required=True))
    for match in _DESTRUCTURE_PARAMS_RE.finditer(context):
        for name in re.split(r"\s*,\s*", match.group(1).strip()):
            name = name.strip().split("=")[0].strip()  # strip default value
            if name and name not in seen:
                seen.add(name)
                params.append(ParameterSpec(name=name, type=_type_of(name, "string"), required=True))

    # Query params from req.query.X or destructured
    for match in _REQ_QUERY_RE.finditer(context):
        name = match.group(1)
        if name not in seen:
            seen.add(name)
            params.append(ParameterSpec(name=name, type=_type_of(name, "string"), required=False))
    for match in _DESTRUCTURE_QUERY_RE.finditer(context):
        for name in re.split(r"\s*,\s*", match.group(1).strip()):
            name = name.strip().split("=")[0].strip()  # strip default value
            if name and name not in seen:
                seen.add(name)
                params.append(ParameterSpec(name=name, type=_type_of(name, "string"), required=False))

    # Body params from req.body.X or destructured
    for match in _REQ_BODY_RE.finditer(context):
        name = match.group(1)
        if name not in seen:
            seen.add(name)
            params.append(ParameterSpec(name=name, type=_type_of(name, "string"), required=True))
    for match in _DESTRUCTURE_BODY_RE.finditer(context):
        for name in re.split(r"\s*,\s*", match.group(1).strip()):
            name = name.strip().split("=")[0].strip()  # strip default value
            if name and name not in seen:
                seen.add(name)
                params.append(ParameterSpec(name=name, type=_type_of(name, "string"), required=True))

    return params


def _extract_path_params(path: str) -> list[ParameterSpec]:
    """Extract path parameters from Express :param syntax."""
    params = []
    for match in re.finditer(r":(\w+)", path):
        params.append(ParameterSpec(name=match.group(1), type="string", required=True))
    return params


def build_router_mount_map(root: Path, files: list[FileInfo]) -> dict[str, str]:
    """Scan all JS/TS files to build a map of file path → mount prefix.

    Resolves cross-file router mounts by correlating require/import statements
    with app.use('/prefix', routerVar) calls.
    """
    # file_path → mount_prefix
    mount_map: dict[str, str] = {}

    for fi in files:
        if fi.language not in (Language.JAVASCRIPT, Language.TYPESCRIPT):
            continue
        try:
            source = (root / fi.path).read_text(errors="replace")
        except OSError:
            continue

        # Build var_name → resolved file path from require/import
        var_to_file: dict[str, str] = {}
        for pattern in (_REQUIRE_RE, _IMPORT_RE):
            for match in pattern.finditer(source):
                var_name = match.group(1)
                rel_path = match.group(2)
                if rel_path.startswith("."):
                    # Resolve relative to the file's directory
                    base_dir = (root / fi.path).parent
                    resolved = (base_dir / rel_path).resolve()
                    # Try common extensions
                    for ext in ("", ".js", ".ts", ".mjs"):
                        candidate = Path(str(resolved) + ext)
                        if candidate.exists():
                            resolved = candidate
                            break
                    try:
                        var_to_file[var_name] = str(resolved.relative_to(root))
                    except ValueError:
                        pass

        # Find app.use('/prefix', varName) and map to resolved file
        for match in _ROUTER_USE_RE.finditer(source):
            prefix = match.group(1).rstrip("/")
            var_name = match.group(2)
            if var_name in var_to_file:
                mount_map[var_to_file[var_name]] = prefix

    return mount_map


def analyze_express_file(
    root: Path, file_info: FileInfo,
    mount_map: dict[str, str] | None = None,
) -> Optional[ExpressAnalysisResult]:
    """Analyze a JS/TS file for Express.js route endpoints."""
    if file_info.language not in (Language.JAVASCRIPT, Language.TYPESCRIPT):
        return None

    try:
        source = (root / file_info.path).read_text(errors="replace")
    except OSError:
        return None

    # Must have express reference
    if not re.search(r"express|require\s*\(\s*['\"]express['\"]|from\s+['\"]express['\"]", source):
        # Could be a router file — check for Router()
        if "Router()" not in source and "router." not in source:
            return None

    result = ExpressAnalysisResult()
    is_typescript = file_info.language == Language.TYPESCRIPT

    if "Router()" in source:
        result.has_routers = True

    # Find router prefixes from local app.use() calls
    router_prefixes: dict[str, str] = {}
    for match in _ROUTER_USE_RE.finditer(source):
        prefix = match.group(1).rstrip("/")
        var_name = match.group(2)
        router_prefixes[var_name] = prefix

    # Cross-file mount prefix: if this file is mounted via app.use() in another file
    file_mount_prefix = ""
    if mount_map and file_info.path in mount_map:
        file_mount_prefix = mount_map[file_info.path]

    # Find chained routes: router.route('/path').get(...).post(...)
    for match in _ROUTE_CHAIN_RE.finditer(source):
        chain_router_var = match.group(1)
        chain_path = match.group(2)

        # Prepend router mount prefix if applicable (same-file)
        if chain_router_var in router_prefixes:
            chain_path = router_prefixes[chain_router_var] + chain_path
        elif file_mount_prefix:
            chain_path = file_mount_prefix + chain_path
        # Scan ahead for chained methods
        chain_text = source[match.end():match.end() + 1500]
        for method_match in _CHAIN_METHOD_RE.finditer(chain_text):
            http_method = method_match.group(1).upper()
            # Stop if we hit another .route( call
            preceding = chain_text[:method_match.start()]
            if ".route(" in preceding:
                break

            path_params = _extract_path_params(chain_path)
            body_params = _extract_params_from_context(source, match.end() + method_match.start(), is_typescript)

            seen_names = {p.name for p in path_params}
            all_params = list(path_params)
            for p in body_params:
                if p.name not in seen_names:
                    all_params.append(p)
                    seen_names.add(p.name)

            func_name = chain_path.strip("/").replace("/", "_").replace(":", "")
            func_name = re.sub(r"[^a-zA-Z0-9_]", "_", func_name) or "handler"

            normalized = normalize_path(chain_path)
            desc = make_description(func_name)

            endpoint = ExpressEndpoint(
                http_method=http_method,
                path=normalized,
                function_name=func_name,
                description=desc,
                parameters=all_params,
                source_file=file_info.path,
            )
            result.routes.append(endpoint)

    # Find all routes
    for match in _ROUTE_RE.finditer(source):
        router_var = match.group(1)
        http_method = match.group(2).upper()
        path = match.group(3)

        # Prepend router mount prefix if this route belongs to a mounted router
        if router_var in router_prefixes:
            path = router_prefixes[router_var] + path
        elif file_mount_prefix and router_var != "app":
            path = file_mount_prefix + path

        # Try to find handler name
        func_name = ""
        handler_match = _HANDLER_NAME_RE.search(source[match.start():match.start() + 300])
        if handler_match:
            func_name = handler_match.group(2)
        if not func_name:
            # Generate from path
            func_name = path.strip("/").replace("/", "_").replace(":", "")
            func_name = re.sub(r"[^a-zA-Z0-9_]", "_", func_name) or "handler"

        # Extract parameters from path and handler body
        path_params = _extract_path_params(path)
        body_params = _extract_params_from_context(source, match.start(), is_typescript)

        # For TypeScript: apply type hints to path params too (e.g. parseInt infers integer)
        if is_typescript:
            context = source[match.start():match.start() + 800]
            ts_types = _resolve_ts_types(context)
            for p in path_params:
                if p.name in ts_types:
                    p.type = ts_types[p.name]

        # Merge: path params first, then body params (avoiding duplicates)
        seen_names = {p.name for p in path_params}
        all_params = list(path_params)
        for p in body_params:
            if p.name not in seen_names:
                all_params.append(p)
                seen_names.add(p.name)

        normalized = normalize_path(path)
        desc = make_description(func_name)

        endpoint = ExpressEndpoint(
            http_method=http_method,
            path=normalized,
            function_name=func_name,
            description=desc,
            parameters=all_params,
            source_file=file_info.path,
        )
        result.routes.append(endpoint)

    return result if result.routes else None


def express_results_to_capabilities(
    results: dict[str, ExpressAnalysisResult],
) -> list[Capability]:
    """Convert Express analysis results into Capability objects."""
    capabilities: list[Capability] = []
    seen: set[str] = set()

    for file_path, result in results.items():
        for ep in result.routes:
            tool_name = endpoint_to_tool_name(ep.http_method, ep.path, ep.function_name)
            if tool_name in seen:
                continue
            seen.add(tool_name)

            desc = f"{ep.http_method} {ep.path} - {ep.description}"

            capabilities.append(Capability(
                name=tool_name,
                description=desc,
                category="api",
                parameters=ep.parameters,
                return_type="object",
                source_file=file_path,
                source_function=ep.function_name,
                ipc_type=IPCType.PROTOCOL,
            ))

    return capabilities
