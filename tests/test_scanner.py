"""Tests for the filesystem scanner."""

from pathlib import Path

import pytest

from mcp_anything.analysis.scanner import classify_language, is_entry_point, scan_codebase
from mcp_anything.models.analysis import Language


class TestClassifyLanguage:
    def test_python(self):
        assert classify_language(Path("foo.py")) == Language.PYTHON

    def test_javascript(self):
        assert classify_language(Path("foo.js")) == Language.JAVASCRIPT

    def test_typescript(self):
        assert classify_language(Path("foo.ts")) == Language.TYPESCRIPT

    def test_c(self):
        assert classify_language(Path("foo.c")) == Language.C

    def test_rust(self):
        assert classify_language(Path("foo.rs")) == Language.RUST

    def test_unknown(self):
        assert classify_language(Path("foo.txt")) == Language.OTHER


class TestEntryPoint:
    def test_main_py(self):
        assert is_entry_point(Path("main.py")) is True

    def test_cli_py(self):
        assert is_entry_point(Path("cli.py")) is True

    def test_random_py(self):
        assert is_entry_point(Path("utils.py")) is False


class TestScanCodebase:
    def test_scan_fake_cli_app(self, fake_cli_app):
        files = scan_codebase(fake_cli_app)
        assert len(files) >= 2
        paths = [f.path for f in files]
        assert "main.py" in paths
        assert "utils.py" in paths

    def test_all_python(self, fake_cli_app):
        files = scan_codebase(fake_cli_app)
        assert all(f.language == Language.PYTHON for f in files)

    def test_entry_point_detected(self, fake_cli_app):
        files = scan_codebase(fake_cli_app)
        main_file = next(f for f in files if f.path == "main.py")
        assert main_file.is_entry_point is True

    def test_line_count(self, fake_cli_app):
        files = scan_codebase(fake_cli_app)
        for f in files:
            assert f.line_count > 0
            assert f.size_bytes > 0

    def test_scan_nonexistent(self, tmp_path):
        empty = tmp_path / "empty"
        empty.mkdir()
        files = scan_codebase(empty)
        assert files == []

    def test_detects_name_main_entry_point(self, tmp_path):
        """Scripts with if __name__ == '__main__': should be entry points."""
        script = tmp_path / "httpstat.py"
        script.write_text('import sys\n\ndef main():\n    pass\n\nif __name__ == \'__main__\':\n    main()\n')
        files = scan_codebase(tmp_path)
        assert len(files) == 1
        assert files[0].is_entry_point is True

    def test_no_name_main_not_entry_point(self, tmp_path):
        """Regular modules without __name__ guard are not entry points."""
        lib = tmp_path / "utils.py"
        lib.write_text('def helper():\n    return 42\n')
        files = scan_codebase(tmp_path)
        assert len(files) == 1
        assert files[0].is_entry_point is False
