"""Detect JAX-RS and Quarkus patterns in Java source files."""

import re
from pathlib import Path

from mcp_anything.models.analysis import FileInfo, IPCMechanism, IPCType, Language

from .base import Detector

JAXRS_PATTERNS = [
    # JAX-RS imports (javax and jakarta namespaces)
    (r"import\s+javax\.ws\.rs", "JAX-RS import (javax)", 0.9),
    (r"import\s+jakarta\.ws\.rs", "JAX-RS import (jakarta)", 0.9),
    # JAX-RS annotations
    (r"@Path\s*\(", "JAX-RS path annotation", 0.9),
    (r"@GET\b", "JAX-RS GET", 0.85),
    (r"@POST\b", "JAX-RS POST", 0.85),
    (r"@PUT\b", "JAX-RS PUT", 0.85),
    (r"@DELETE\b", "JAX-RS DELETE", 0.85),
    (r"@PATCH\b", "JAX-RS PATCH", 0.85),
    (r"@Consumes\b", "JAX-RS Consumes", 0.7),
    (r"@Produces\b", "JAX-RS Produces", 0.7),
    (r"@QueryParam\b", "JAX-RS query param", 0.8),
    (r"@PathParam\b", "JAX-RS path param", 0.8),
    (r"@FormParam\b", "JAX-RS form param", 0.8),
    # Quarkus-specific
    (r"@ApplicationScoped\b", "Quarkus/CDI bean", 0.7),
    (r"import\s+io\.quarkus", "Quarkus import", 0.9),
    (r"quarkus\.http\.port", "Quarkus port config", 0.85),
]


class JaxRSDetector(Detector):
    @property
    def name(self) -> str:
        return "JAX-RS Detector"

    def detect(self, root: Path, files: list[FileInfo]) -> list[IPCMechanism]:
        evidence: list[str] = []
        max_confidence = 0.0
        port = "8080"
        has_quarkus = False
        has_jaxrs_import = False

        for fi in files:
            if fi.language not in (Language.JAVA, Language.KOTLIN, Language.OTHER):
                continue
            content = self._read_file(root, fi)
            if not content:
                continue

            for pattern, desc, conf in JAXRS_PATTERNS:
                if re.search(pattern, content):
                    evidence.append(f"{fi.path}: {desc}")
                    max_confidence = max(max_confidence, conf)
                    if "Quarkus" in desc:
                        has_quarkus = True
                    if "JAX-RS import" in desc:
                        has_jaxrs_import = True

            # Extract Quarkus port
            port_match = re.search(r"quarkus\.http\.port\s*=\s*(\d+)", content)
            if port_match:
                port = port_match.group(1)

        # Check Quarkus config files
        for config_name in ("application.properties", "application.yml", "application.yaml"):
            config_path = root / "src" / "main" / "resources" / config_name
            if config_path.exists():
                try:
                    config_content = config_path.read_text(errors="replace")
                    if "quarkus." in config_content:
                        evidence.append(f"src/main/resources/{config_name}: Quarkus config")
                        has_quarkus = True
                        max_confidence = max(max_confidence, 0.85)
                    port_match = re.search(
                        r"quarkus\.http\.port\s*[=:]\s*(\d+)", config_content
                    )
                    if port_match:
                        port = port_match.group(1)
                except OSError:
                    pass

        if not evidence:
            return []

        # Need JAX-RS imports or @Path to be confident
        has_path = any("path annotation" in e.lower() for e in evidence)
        has_endpoints = any(
            "JAX-RS GET" in e or "JAX-RS POST" in e or "JAX-RS PUT" in e
            or "JAX-RS DELETE" in e or "JAX-RS PATCH" in e
            for e in evidence
        )
        if not has_jaxrs_import and not has_path:
            return []
        if not has_endpoints and not has_path:
            return []

        framework = "quarkus" if has_quarkus else "jaxrs"

        return [
            IPCMechanism(
                ipc_type=IPCType.PROTOCOL,
                confidence=min(max_confidence, 1.0),
                evidence=evidence,
                details={"protocol": "http", "port": port, "framework": framework},
            )
        ]
