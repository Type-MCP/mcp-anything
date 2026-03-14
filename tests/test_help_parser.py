"""Tests for CLI --help output parsing."""

from mcp_anything.analysis.help_parser import (
    _extract_options,
    _extract_subcommands,
    parse_help_text,
)


class TestExtractSubcommands:
    def test_basic_commands_section(self):
        help_text = """Usage: mytool [OPTIONS] COMMAND

Commands:
  init        Initialize a new project
  build       Build the project
  test        Run test suite
  deploy      Deploy to production

Options:
  --help      Show this message and exit
"""
        commands = _extract_subcommands(help_text)
        names = [c[0] for c in commands]
        assert "init" in names
        assert "build" in names
        assert "test" in names
        assert "deploy" in names

    def test_no_commands_section(self):
        help_text = """Usage: simple-tool [OPTIONS] FILE

Options:
  -o, --output FILE    Output path
  --verbose            Enable verbose
"""
        commands = _extract_subcommands(help_text)
        assert commands == []

    def test_go_style_help(self):
        help_text = """Usage:
  kubectl [command]

Available Commands:
  apply       Apply a configuration
  create      Create a resource
  delete      Delete resources
  get         Display resources

Flags:
  -h, --help   help for kubectl
"""
        commands = _extract_subcommands(help_text)
        names = [c[0] for c in commands]
        assert "apply" in names
        assert "get" in names
        assert len(commands) == 4


class TestExtractOptions:
    def test_long_and_short_flags(self):
        help_text = """
Options:
  -o, --output FILE    Output file path
  -v, --verbose        Enable verbose mode
  --timeout INT        Request timeout (default: 30)
"""
        options = _extract_options(help_text)
        names = [o.name for o in options]
        assert "output" in names
        assert "verbose" in names
        assert "timeout" in names

    def test_option_types(self):
        help_text = """
Options:
  --count INT          Number of items
  --ratio FLOAT        Ratio value
  --path PATH          File path
  -v, --verbose        Be verbose
"""
        options = _extract_options(help_text)
        by_name = {o.name: o for o in options}
        assert by_name["count"].type == "integer"
        assert by_name["ratio"].type == "float"
        assert by_name["path"].type == "string"
        assert by_name["verbose"].type == "boolean"

    def test_default_values(self):
        help_text = """
Options:
  --timeout INT        Timeout in seconds (default: 30)
  --format TEXT        Output format (default: json)
"""
        options = _extract_options(help_text)
        by_name = {o.name: o for o in options}
        assert by_name["timeout"].default == "30"
        assert by_name["format"].default == "json"


class TestParseHelpText:
    def test_full_help_to_capabilities(self):
        help_text = """Usage: myapp [OPTIONS] COMMAND

A sample application.

Commands:
  serve       Start the server
  migrate     Run database migrations
  seed        Seed the database

Options:
  --help      Show help
"""
        caps = parse_help_text(help_text, "myapp")
        names = [c.name for c in caps]
        assert "serve" in names
        assert "migrate" in names
        assert "seed" in names
        for cap in caps:
            assert cap.category == "cli_command"
            assert cap.ipc_type is not None

    def test_empty_help(self):
        caps = parse_help_text("", "myapp")
        assert caps == []

    def test_dashes_become_underscores(self):
        help_text = """
Commands:
  run-tests    Run the test suite
  check-deps   Check dependencies
"""
        caps = parse_help_text(help_text, "myapp")
        names = [c.name for c in caps]
        assert "run_tests" in names
        assert "check_deps" in names
