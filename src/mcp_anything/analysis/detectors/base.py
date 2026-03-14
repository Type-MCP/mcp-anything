"""Base class for IPC mechanism detectors."""

from abc import ABC, abstractmethod
from pathlib import Path

from mcp_anything.models.analysis import FileInfo, IPCMechanism


class Detector(ABC):
    """Scans source files for a specific IPC pattern."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Human-readable detector name."""

    @abstractmethod
    def detect(self, root: Path, files: list[FileInfo]) -> list[IPCMechanism]:
        """Analyze files and return detected IPC mechanisms."""

    def _read_file(self, root: Path, file_info: FileInfo) -> str:
        """Safely read a source file."""
        try:
            return (root / file_info.path).read_text(errors="replace")
        except OSError:
            return ""
