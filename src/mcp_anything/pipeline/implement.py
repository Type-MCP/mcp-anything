"""Phase 3: IMPLEMENT — generate MCP server source code."""

import ast
import subprocess
import sys
from pathlib import Path

from mcp_anything.codegen.emitter import Emitter
from mcp_anything.pipeline.context import PipelineContext
from mcp_anything.pipeline.phase import Phase


class ImplementPhase(Phase):
    @property
    def name(self) -> str:
        return "implement"

    def validate_preconditions(self, ctx: PipelineContext) -> list[str]:
        if not ctx.manifest.design:
            return ["Design phase must complete before implement"]
        return []

    async def execute(self, ctx: PipelineContext) -> None:
        design = ctx.manifest.design
        assert design is not None

        output_dir = Path(ctx.manifest.output_dir)
        emitter = Emitter(design, output_dir)

        ctx.console.print("    Generating server code...")
        generated = emitter.emit_all()

        # Validate all generated Python files compile
        ctx.console.print("    Validating generated Python...")
        errors = self._validate_python(output_dir, generated)
        if errors:
            for path, err in errors:
                ctx.console.print(f"    [red]Syntax error in {path}:[/red] {err}")
            raise RuntimeError(
                f"Generated {len(errors)} file(s) with syntax errors. "
                "This is a bug in mcp-anything's code generation."
            )

        ctx.manifest.generated_files.extend(generated)
        ctx.console.print(f"    Generated {len(generated)} files (all valid Python)")

        # Auto-install dependencies
        if not ctx.options.no_install:
            install_errors = self._install_dependencies(ctx, output_dir)
            if install_errors:
                for err in install_errors:
                    ctx.console.print(f"    [yellow]Install warning:[/yellow] {err}")

    def _validate_python(
        self, output_dir: Path, generated_files: list[str]
    ) -> list[tuple[str, str]]:
        """Parse all generated .py files and return (path, error) for failures."""
        errors: list[tuple[str, str]] = []
        for rel_path in generated_files:
            if not rel_path.endswith(".py"):
                continue
            full_path = output_dir / rel_path
            try:
                source = full_path.read_text()
                ast.parse(source)
            except SyntaxError as exc:
                errors.append((rel_path, f"line {exc.lineno}: {exc.msg}"))
        return errors

    def _install_dependencies(
        self, ctx: PipelineContext, output_dir: Path
    ) -> list[str]:
        """Install target project and generated server dependencies."""
        errors: list[str] = []

        # Install the target project if we have an install hint
        design = ctx.manifest.design
        if design and design.target_install_hint:
            hint = design.target_install_hint
            ctx.console.print(f"    Installing target: {hint}")
            try:
                # Parse the hint to get pip args
                if "install " in hint:
                    pip_args = hint.split("install ", 1)[1].split()
                else:
                    pip_args = [hint]
                result = subprocess.run(
                    [sys.executable, "-m", "pip", "install", "-q"] + pip_args,
                    capture_output=True, text=True, timeout=120,
                )
                if result.returncode != 0:
                    errors.append(f"Target install failed: {result.stderr.strip()[:200]}")
            except subprocess.TimeoutExpired:
                errors.append("Target install timed out")
            except Exception as e:
                errors.append(f"Target install error: {e}")

        # Install the generated server package
        ctx.console.print("    Installing generated server...")
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", "-q", "-e", str(output_dir)],
                capture_output=True, text=True, timeout=120,
            )
            if result.returncode != 0:
                errors.append(f"Server install failed: {result.stderr.strip()[:200]}")
        except subprocess.TimeoutExpired:
            errors.append("Server install timed out")
        except Exception as e:
            errors.append(f"Server install error: {e}")

        if not errors:
            ctx.console.print("    Dependencies installed successfully")

        return errors
