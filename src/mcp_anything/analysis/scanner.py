"""Filesystem walker and file classifier."""

import re
from pathlib import Path

from mcp_anything.models.analysis import FileInfo, Language

_NAME_MAIN_RE = re.compile(r'''if\s+__name__\s*==\s*['"]__main__['"]\s*:''')

EXTENSION_MAP: dict[str, Language] = {
    ".py": Language.PYTHON,
    ".c": Language.C,
    ".h": Language.C,
    ".cpp": Language.CPP,
    ".cxx": Language.CPP,
    ".cc": Language.CPP,
    ".hpp": Language.CPP,
    ".rs": Language.RUST,
    ".go": Language.GO,
    ".js": Language.JAVASCRIPT,
    ".mjs": Language.JAVASCRIPT,
    ".ts": Language.TYPESCRIPT,
    ".tsx": Language.TYPESCRIPT,
    ".lua": Language.LUA,
    ".sh": Language.SHELL,
    ".bash": Language.SHELL,
    ".zsh": Language.SHELL,
}

SKIP_DIRS = {
    ".git", ".hg", ".svn", "__pycache__", "node_modules", ".venv", "venv",
    ".tox", ".eggs", "dist", "build", ".mypy_cache", ".pytest_cache",
    "test", "tests", "testing", "test_data", "testdata", "fixtures",
    "examples", "example", "docs", "doc", "benchmarks", "bench",
}

SKIP_FILES = {
    "setup.py", "conftest.py", "noxfile.py", "fabfile.py",
    "tasks.py", "manage.py",
}

ENTRY_POINT_PATTERNS = {
    "__main__.py", "main.py", "cli.py", "app.py", "server.py",
    "main.c", "main.cpp", "main.go", "main.rs", "index.js", "index.ts",
}


def classify_language(path: Path) -> Language:
    return EXTENSION_MAP.get(path.suffix.lower(), Language.OTHER)


def is_entry_point(path: Path) -> bool:
    return path.name.lower() in ENTRY_POINT_PATTERNS


def scan_codebase(root: Path, max_files: int = 5000) -> list[FileInfo]:
    """Walk the codebase and return classified file metadata."""
    files: list[FileInfo] = []
    root = root.resolve()

    root_depth = len(root.parts)

    for item in sorted(root.rglob("*")):
        # Only check directory components *below* the scan root
        relative_parts = item.parts[root_depth:]
        if any(part in SKIP_DIRS for part in relative_parts):
            continue
        if not item.is_file():
            continue
        if item.name.lower() in SKIP_FILES:
            continue
        if item.name.startswith("test_") or item.name.endswith("_test.py"):
            continue

        lang = classify_language(item)
        if lang == Language.OTHER:
            continue

        try:
            content = item.read_text(errors="replace")
            line_count = content.count("\n") + 1
        except (OSError, UnicodeDecodeError):
            content = ""
            line_count = 0

        # Detect entry point by filename or by `if __name__ == '__main__':` guard
        entry = is_entry_point(item)
        if not entry and lang == Language.PYTHON and _NAME_MAIN_RE.search(content):
            entry = True

        rel_path = str(item.relative_to(root))
        files.append(
            FileInfo(
                path=rel_path,
                language=lang,
                size_bytes=item.stat().st_size,
                line_count=line_count,
                is_entry_point=entry,
            )
        )

        if len(files) >= max_files:
            break

    return files
