"""Detect Micronaut patterns in Java source files."""

import re
from pathlib import Path

from mcp_anything.models.analysis import FileInfo, IPCMechanism, IPCType, Language

from .base import Detector

MICRONAUT_PATTERNS = [
    # Micronaut imports
    (r"import\s+io\.micronaut", "Micronaut import", 0.95),
    # Controller annotations
    (r"@Controller\s*\(", "Micronaut controller", 0.9),
    # HTTP method annotations (Micronaut uses @Get, @Post, etc.)
    (r"@Get\b", "Micronaut GET", 0.85),
    (r"@Post\b", "Micronaut POST", 0.85),
    (r"@Put\b", "Micronaut PUT", 0.85),
    (r"@Delete\b", "Micronaut DELETE", 0.85),
    (r"@Patch\b", "Micronaut PATCH", 0.85),
    # Parameter annotations
    (r"@QueryValue\b", "Micronaut query param", 0.8),
    (r"@PathVariable\b", "Micronaut path variable", 0.8),
    (r"@Body\b", "Micronaut request body", 0.8),
]


class MicronautDetector(Detector):
    @property
    def name(self) -> str:
        return "Micronaut Detector"

    def detect(self, root: Path, files: list[FileInfo]) -> list[IPCMechanism]:
        evidence: list[str] = []
        max_confidence = 0.0
        port = "8080"
        has_micronaut_import = False

        for fi in files:
            if fi.language not in (Language.JAVA, Language.KOTLIN, Language.OTHER):
                continue
            content = self._read_file(root, fi)
            if not content:
                continue

            for pattern, desc, conf in MICRONAUT_PATTERNS:
                if re.search(pattern, content):
                    evidence.append(f"{fi.path}: {desc}")
                    max_confidence = max(max_confidence, conf)
                    if "Micronaut import" in desc:
                        has_micronaut_import = True

        # Check Micronaut config files
        for config_name in ("application.yml", "application.yaml"):
            config_path = root / "src" / "main" / "resources" / config_name
            if config_path.exists():
                try:
                    config_content = config_path.read_text(errors="replace")
                    if "micronaut" in config_content:
                        evidence.append(f"src/main/resources/{config_name}: Micronaut config")
                        max_confidence = max(max_confidence, 0.85)
                    port_match = re.search(
                        r"(?:micronaut\.server\.port|port)\s*:\s*(\d+)", config_content
                    )
                    if port_match:
                        port = port_match.group(1)
                except OSError:
                    pass

        # Check build files for Micronaut dependency
        for build_file in ("build.gradle", "build.gradle.kts", "pom.xml"):
            build_path = root / build_file
            if build_path.exists():
                try:
                    build_content = build_path.read_text(errors="replace")
                    if "io.micronaut" in build_content:
                        evidence.append(f"{build_file}: Micronaut dependency")
                        has_micronaut_import = True
                        max_confidence = max(max_confidence, 0.9)
                except OSError:
                    pass

        if not evidence:
            return []

        # Need Micronaut import to distinguish from Spring's @Controller
        has_endpoints = any(
            "Micronaut GET" in e or "Micronaut POST" in e or "Micronaut PUT" in e
            or "Micronaut DELETE" in e or "Micronaut PATCH" in e
            or "Micronaut controller" in e
            for e in evidence
        )
        if not has_micronaut_import:
            return []
        if not has_endpoints:
            return []

        return [
            IPCMechanism(
                ipc_type=IPCType.PROTOCOL,
                confidence=min(max_confidence, 1.0),
                evidence=evidence,
                details={"protocol": "http", "port": port, "framework": "micronaut"},
            )
        ]
