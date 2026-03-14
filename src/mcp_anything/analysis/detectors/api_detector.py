"""Detect Python API/bindings patterns."""

import re
from pathlib import Path

from mcp_anything.models.analysis import FileInfo, IPCMechanism, IPCType, Language

from .base import Detector

API_PATTERNS = [
    (r"from\s+\w+\s+import\s+\w+", "Python module import", 0.3),
    (r"class\s+\w+.*:\s*\n\s+\"\"\"", "documented class", 0.4),
    (r"def\s+\w+\s*\(.*\)\s*->\s*\w+", "type-annotated function", 0.5),
    (r"__all__\s*=\s*\[", "__all__ export list", 0.6),
    (r"ctypes\.", "ctypes FFI", 0.8),
    (r"cffi\.", "cffi FFI", 0.8),
    (r"pybind11", "pybind11 binding", 0.9),
    (r"PYBIND11_MODULE", "pybind11 module def", 0.95),
    (r"cython", "Cython binding", 0.8),
    (r"\.pyx$", "Cython source", 0.8),
    (r"SWIG", "SWIG binding", 0.85),
    (r"boost::python", "Boost.Python binding", 0.9),
    (r"PyModule_Create", "CPython module", 0.9),
    (r"PyMethodDef", "CPython method table", 0.9),
]


class APIDetector(Detector):
    @property
    def name(self) -> str:
        return "Python API Detector"

    def detect(self, root: Path, files: list[FileInfo]) -> list[IPCMechanism]:
        evidence: list[str] = []
        max_confidence = 0.0
        has_binding = False

        for fi in files:
            content = self._read_file(root, fi)
            if not content:
                continue

            for pattern, desc, conf in API_PATTERNS:
                if re.search(pattern, content):
                    evidence.append(f"{fi.path}: {desc}")
                    max_confidence = max(max_confidence, conf)
                    if conf >= 0.8:
                        has_binding = True

        if not evidence:
            return []

        # Only report Python API if there's strong evidence of bindings
        # or a significant number of typed API surfaces
        if not has_binding and len(evidence) < 5:
            return []

        return [
            IPCMechanism(
                ipc_type=IPCType.PYTHON_API,
                confidence=min(max_confidence, 1.0),
                evidence=evidence,
            )
        ]
