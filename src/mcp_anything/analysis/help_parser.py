"""Parse CLI --help output to extract commands and options."""

import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Optional

from mcp_anything.models.analysis import Capability, IPCType, ParameterSpec


def parse_help_text(help_text: str, app_name: str) -> list[Capability]:
    """Parse --help output text into capabilities."""
    if not help_text.strip():
        return []

    capabilities = []

    # Try to detect subcommands section
    subcommands = _extract_subcommands(help_text)
    for name, desc in subcommands:
        capabilities.append(Capability(
            name=name.replace("-", "_"),
            description=desc or f"Run {name} command",
            category="cli_command",
            parameters=[ParameterSpec(
                name="args",
                type="string",
                description=f"Arguments for {name}",
                required=False,
            )],
            ipc_type=IPCType.CLI,
            source_file=app_name,
        ))

    return capabilities


def _extract_subcommands(help_text: str) -> list[tuple[str, str]]:
    """Extract subcommands from help text.

    Handles common patterns:
    - "Commands:" or "Available commands:" sections
    - Indented lines with "command_name    Description"
    """
    commands: list[tuple[str, str]] = []
    in_commands_section = False

    for line in help_text.split("\n"):
        stripped = line.strip()

        # Detect commands section headers
        if re.match(
            r"^(commands|available commands|subcommands|positional arguments)\s*:?\s*$",
            stripped,
            re.IGNORECASE,
        ):
            in_commands_section = True
            continue

        # End of section: new section header (not commands-related)
        if in_commands_section and stripped and re.match(r"^[A-Z].*:\s*$", stripped):
            if not re.match(
                r"^(commands|available commands|subcommands)\s*:?\s*$",
                stripped,
                re.IGNORECASE,
            ):
                in_commands_section = False
                continue

        if in_commands_section:
            # Parse "  command_name    Description text"
            match = re.match(r"^\s{2,}(\w[\w-]*)\s{2,}(.+)", line)
            if match:
                cmd_name = match.group(1)
                cmd_desc = match.group(2).strip()
                if not cmd_name.startswith("-"):
                    commands.append((cmd_name, cmd_desc))

    return commands


def _extract_options(help_text: str) -> list[ParameterSpec]:
    """Extract options/flags from help text."""
    options = []

    pattern = re.compile(
        r"^\s+"
        r"(?:(-\w),?\s+)?"          # short flag (optional)
        r"(--[\w-]+)"               # long flag (required)
        r"(?:\s+(\w+))?"            # value placeholder (optional)
        r"\s{2,}"                   # separator
        r"(.+?)$",                  # description
        re.MULTILINE,
    )

    for match in pattern.finditer(help_text):
        long_flag = match.group(2)
        value_type = match.group(3)
        description = match.group(4).strip()

        name = long_flag.lstrip("-").replace("-", "_")

        # Determine type
        param_type = "string"
        if value_type:
            type_map = {
                "INT": "integer", "FLOAT": "float", "NUM": "integer",
                "FILE": "string", "PATH": "string", "DIR": "string",
                "URL": "string", "TEXT": "string",
            }
            param_type = type_map.get(value_type.upper(), "string")
        else:
            param_type = "boolean"

        # Check for default values
        default = None
        default_match = re.search(r"\(default[:\s]+([^)]+)\)", description)
        if default_match:
            default = default_match.group(1).strip()

        options.append(ParameterSpec(
            name=name,
            type=param_type,
            description=description,
            required=False,
            default=default,
        ))

    return options


def run_help_command(codebase_path: Path) -> Optional[str]:
    """Try to run --help on a project in the codebase."""
    path = codebase_path.resolve()

    # Check for Go main.go or cmd/
    if (path / "main.go").exists() or (path / "cmd").is_dir():
        output = _try_command(["go", "run", ".", "--help"], cwd=path)
        if output:
            return output

    # Check for Cargo.toml (Rust)
    if (path / "Cargo.toml").exists():
        output = _try_command(["cargo", "run", "--", "--help"], cwd=path, timeout=30)
        if output:
            return output

    # Check for package.json (Node.js)
    pkg_json = path / "package.json"
    if pkg_json.exists():
        try:
            pkg = json.loads(pkg_json.read_text())
            if "bin" in pkg:
                bin_entries = pkg["bin"]
                if isinstance(bin_entries, str):
                    output = _try_command(["node", str(path / bin_entries), "--help"], cwd=path)
                    if output:
                        return output
                elif isinstance(bin_entries, dict):
                    for bin_path in bin_entries.values():
                        output = _try_command(["node", str(path / bin_path), "--help"], cwd=path)
                        if output:
                            return output
        except Exception:
            pass

    return None


def _try_command(cmd: list[str], cwd: Path, timeout: int = 15) -> Optional[str]:
    """Run a command and return stdout+stderr if it produces meaningful output."""
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=str(cwd),
        )
        output = result.stdout or result.stderr
        if output and len(output.strip()) > 20:
            return output.strip()
    except Exception:
        pass
    return None
