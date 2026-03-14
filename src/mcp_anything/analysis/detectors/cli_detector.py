"""Detect CLI/command-line interface patterns."""

import re
from pathlib import Path

from mcp_anything.models.analysis import FileInfo, IPCMechanism, IPCType, Language

from .base import Detector

CLI_PATTERNS = [
    (r"import\s+argparse", "argparse import", 0.8),
    (r"from\s+argparse\s+import", "argparse import", 0.8),
    (r"ArgumentParser\s*\(", "ArgumentParser usage", 0.9),
    (r"add_argument\s*\(", "add_argument call", 0.7),
    (r"import\s+click", "click import", 0.85),
    (r"@click\.(command|group|option|argument)", "click decorator", 0.9),
    (r"import\s+typer", "typer import", 0.85),
    (r"from\s+typer\s+import", "typer import", 0.85),
    (r"import\s+fire", "python-fire import", 0.8),
    (r"getopt\s*\(", "getopt usage", 0.7),
    (r"sys\.argv", "sys.argv access", 0.5),
    (r"subprocess\.(run|call|Popen|check_output)", "subprocess usage", 0.6),
    (r"os\.system\s*\(", "os.system call", 0.5),
    # C/C++ patterns
    (r"int\s+main\s*\(\s*int\s+argc", "C main with argc/argv", 0.8),
    (r"getopt_long\s*\(", "getopt_long usage", 0.8),
    # Go patterns
    (r"flag\.Parse\(\)", "Go flag.Parse", 0.8),
    (r"\"github\.com/spf13/cobra\"", "Go cobra import", 0.9),
]


class CLIDetector(Detector):
    @property
    def name(self) -> str:
        return "CLI Detector"

    def detect(self, root: Path, files: list[FileInfo]) -> list[IPCMechanism]:
        evidence: list[str] = []
        max_confidence = 0.0

        for fi in files:
            if fi.language in (Language.OTHER,):
                continue
            content = self._read_file(root, fi)
            if not content:
                continue

            for pattern, desc, conf in CLI_PATTERNS:
                if re.search(pattern, content):
                    evidence.append(f"{fi.path}: {desc}")
                    max_confidence = max(max_confidence, conf)

        if not evidence:
            return []

        return [
            IPCMechanism(
                ipc_type=IPCType.CLI,
                confidence=min(max_confidence, 1.0),
                evidence=evidence,
            )
        ]
