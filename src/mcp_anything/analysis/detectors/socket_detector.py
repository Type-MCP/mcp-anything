"""Detect socket/IPC patterns."""

import re
from pathlib import Path

from mcp_anything.models.analysis import FileInfo, IPCMechanism, IPCType, Language

from .base import Detector

SOCKET_PATTERNS = [
    (r"socket\.socket\s*\(", "Python socket creation", 0.8),
    (r"\.bind\s*\(\s*\(.*,\s*\d+\s*\)\s*\)", "socket bind with port", 0.85),
    (r"\.listen\s*\(", "socket listen", 0.8),
    (r"\.accept\s*\(", "socket accept", 0.8),
    (r"xmlrpc\.(server|client)", "XML-RPC", 0.9),
    (r"SimpleXMLRPCServer", "XML-RPC server", 0.9),
    (r"socketserver\.", "socketserver module", 0.85),
    (r"zmq\.", "ZeroMQ usage", 0.9),
    (r"import\s+zmq", "ZeroMQ import", 0.85),
    # C patterns
    (r"#include\s+<sys/socket\.h>", "C socket header", 0.8),
    (r"AF_UNIX|AF_INET", "address family", 0.7),
    (r"SOCK_STREAM|SOCK_DGRAM", "socket type", 0.7),
]


class SocketDetector(Detector):
    @property
    def name(self) -> str:
        return "Socket Detector"

    def detect(self, root: Path, files: list[FileInfo]) -> list[IPCMechanism]:
        evidence: list[str] = []
        max_confidence = 0.0
        details: dict[str, str] = {}

        for fi in files:
            content = self._read_file(root, fi)
            if not content:
                continue

            for pattern, desc, conf in SOCKET_PATTERNS:
                if re.search(pattern, content):
                    evidence.append(f"{fi.path}: {desc}")
                    max_confidence = max(max_confidence, conf)

            # Try to extract port numbers
            port_matches = re.findall(r"\.bind\s*\(\s*\(['\"].*?['\"]\s*,\s*(\d+)\s*\)", content)
            if port_matches:
                details["port"] = port_matches[0]

        if not evidence:
            return []

        return [
            IPCMechanism(
                ipc_type=IPCType.SOCKET,
                confidence=min(max_confidence, 1.0),
                evidence=evidence,
                details=details,
            )
        ]
