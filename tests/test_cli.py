"""Tests for the CLI interface."""

import pytest

from mcp_anything.cli import build_parser, parse_options


class TestCLIParser:
    def test_help(self, capsys):
        parser = build_parser()
        with pytest.raises(SystemExit) as exc_info:
            parser.parse_args(["--help"])
        assert exc_info.value.code == 0

    def test_version(self, capsys):
        parser = build_parser()
        with pytest.raises(SystemExit) as exc_info:
            parser.parse_args(["--version"])
        assert exc_info.value.code == 0

    def test_generate_subcommand(self):
        parser = build_parser()
        args = parser.parse_args(["generate", "/some/path", "--name", "myapp", "-v"])
        assert args.command == "generate"
        assert str(args.codebase_path) == "/some/path"
        assert args.name == "myapp"
        assert args.verbose is True

    def test_analyze_subcommand(self):
        parser = build_parser()
        args = parser.parse_args(["analyze", "/some/path", "--no-llm"])
        assert args.command == "analyze"
        assert args.no_llm is True

    def test_design_subcommand(self):
        parser = build_parser()
        args = parser.parse_args(["design", "/some/path"])
        assert args.command == "design"

    def test_status_subcommand(self):
        parser = build_parser()
        args = parser.parse_args(["status", "/some/output"])
        assert args.command == "status"

    def test_generate_with_backend(self):
        parser = build_parser()
        args = parser.parse_args(["generate", "/path", "--backend", "socket"])
        assert args.backend == "socket"

    def test_generate_with_phases(self):
        parser = build_parser()
        args = parser.parse_args(["generate", "/path", "--phases", "analyze,design"])
        options = parse_options(args)
        assert options.phases == ["analyze", "design"]

    def test_parse_options_defaults(self):
        parser = build_parser()
        args = parser.parse_args(["generate", "/some/path"])
        options = parse_options(args)
        assert options.codebase_path.parts[-1] == "path"
        assert options.name is None
        assert options.backend is None
        assert options.resume is False
        assert options.no_llm is False

    def test_resolved_name(self):
        parser = build_parser()
        args = parser.parse_args(["generate", "/some/my-app"])
        options = parse_options(args)
        assert options.resolved_name() == "my-app"

    def test_resolved_name_override(self):
        parser = build_parser()
        args = parser.parse_args(["generate", "/some/path", "--name", "custom"])
        options = parse_options(args)
        assert options.resolved_name() == "custom"
