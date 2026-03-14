"""IPC mechanism detectors."""

from mcp_anything.analysis.detectors.api_detector import APIDetector
from mcp_anything.analysis.detectors.base import Detector
from mcp_anything.analysis.detectors.cli_detector import CLIDetector
from mcp_anything.analysis.detectors.file_detector import FileDetector
from mcp_anything.analysis.detectors.protocol_detector import ProtocolDetector
from mcp_anything.analysis.detectors.socket_detector import SocketDetector

ALL_DETECTORS: list[type[Detector]] = [
    CLIDetector,
    SocketDetector,
    APIDetector,
    ProtocolDetector,
    FileDetector,
]

__all__ = [
    "Detector",
    "CLIDetector",
    "SocketDetector",
    "APIDetector",
    "ProtocolDetector",
    "FileDetector",
    "ALL_DETECTORS",
]
