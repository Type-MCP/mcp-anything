"""Tests for IPC mechanism detectors."""

import pytest

from mcp_anything.analysis.detectors import ALL_DETECTORS
from mcp_anything.analysis.detectors.cli_detector import CLIDetector
from mcp_anything.analysis.detectors.file_detector import FileDetector
from mcp_anything.analysis.detectors.socket_detector import SocketDetector
from mcp_anything.analysis.scanner import scan_codebase
from mcp_anything.models.analysis import IPCType


class TestCLIDetector:
    def test_detects_argparse(self, fake_cli_app):
        files = scan_codebase(fake_cli_app)
        detector = CLIDetector()
        mechanisms = detector.detect(fake_cli_app, files)

        assert len(mechanisms) == 1
        assert mechanisms[0].ipc_type == IPCType.CLI
        assert mechanisms[0].confidence >= 0.7
        assert len(mechanisms[0].evidence) > 0

    def test_no_false_positive(self, tmp_path):
        # Create a file with no CLI patterns
        (tmp_path / "empty.py").write_text("x = 1\n")
        files = scan_codebase(tmp_path)
        detector = CLIDetector()
        mechanisms = detector.detect(tmp_path, files)
        assert mechanisms == []


class TestFileDetector:
    def test_detects_file_io(self, fake_cli_app):
        files = scan_codebase(fake_cli_app)
        detector = FileDetector()
        mechanisms = detector.detect(fake_cli_app, files)

        # fake_cli_app has json and csv I/O plus open() calls
        assert len(mechanisms) >= 1
        assert mechanisms[0].ipc_type == IPCType.FILE

    def test_requires_multiple_signals(self, tmp_path):
        # Single file open is not enough
        (tmp_path / "one.py").write_text('open("x", "r")\n')
        files = scan_codebase(tmp_path)
        detector = FileDetector()
        mechanisms = detector.detect(tmp_path, files)
        assert mechanisms == []


class TestSocketDetector:
    def test_no_sockets_in_cli_app(self, fake_cli_app):
        files = scan_codebase(fake_cli_app)
        detector = SocketDetector()
        mechanisms = detector.detect(fake_cli_app, files)
        assert mechanisms == []


class TestAllDetectors:
    def test_all_detectors_instantiate(self):
        for cls in ALL_DETECTORS:
            d = cls()
            assert d.name

    def test_run_all_on_fake_app(self, fake_cli_app):
        files = scan_codebase(fake_cli_app)
        all_mechanisms = []
        for cls in ALL_DETECTORS:
            mechanisms = cls().detect(fake_cli_app, files)
            all_mechanisms.extend(mechanisms)

        # Should find at least CLI
        types_found = {m.ipc_type for m in all_mechanisms}
        assert IPCType.CLI in types_found
