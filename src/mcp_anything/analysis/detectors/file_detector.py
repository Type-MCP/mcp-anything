"""Detect file-based I/O patterns."""

import re
from pathlib import Path

from mcp_anything.models.analysis import FileInfo, IPCMechanism, IPCType

from .base import Detector

FILE_PATTERNS = [
    (r"open\s*\(.*['\"]w['\"]", "file write", 0.5),
    (r"open\s*\(.*['\"]r['\"]", "file read", 0.4),
    (r"json\.(load|dump)\s*\(", "JSON file I/O", 0.6),
    (r"yaml\.(safe_load|dump)\s*\(", "YAML file I/O", 0.6),
    (r"toml\.(load|dump)", "TOML file I/O", 0.6),
    (r"xml\.etree|lxml\.", "XML processing", 0.6),
    (r"csv\.(reader|writer|DictReader|DictWriter)", "CSV I/O", 0.6),
    (r"sqlite3\.", "SQLite database", 0.7),
    (r"pathlib\.Path.*\.(read_text|write_text|read_bytes|write_bytes)", "pathlib I/O", 0.5),
    (r"shutil\.(copy|move|rmtree)", "file operations", 0.5),
    (r"tempfile\.", "temp file usage", 0.4),
    (r"watchdog\.", "file watching", 0.7),
    (r"inotify", "inotify watching", 0.7),
]


class FileDetector(Detector):
    @property
    def name(self) -> str:
        return "File I/O Detector"

    def detect(self, root: Path, files: list[FileInfo]) -> list[IPCMechanism]:
        evidence: list[str] = []
        max_confidence = 0.0

        for fi in files:
            content = self._read_file(root, fi)
            if not content:
                continue

            for pattern, desc, conf in FILE_PATTERNS:
                if re.search(pattern, content):
                    evidence.append(f"{fi.path}: {desc}")
                    max_confidence = max(max_confidence, conf)

        if not evidence:
            return []

        # File I/O alone is weak evidence — require multiple signals
        if len(evidence) < 3:
            return []

        return [
            IPCMechanism(
                ipc_type=IPCType.FILE,
                confidence=min(max_confidence, 1.0),
                evidence=evidence,
            )
        ]
