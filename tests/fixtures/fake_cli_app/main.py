"""A fake CLI application for testing mcp-anything analysis."""

import argparse
import json
import sys


def process_file(input_path: str, output_path: str, format: str = "json") -> str:
    """Process an input file and write results."""
    with open(input_path, "r") as f:
        data = f.read()

    result = {"processed": True, "length": len(data), "format": format}

    with open(output_path, "w") as f:
        json.dump(result, f)

    return json.dumps(result)


def get_status() -> str:
    """Return application status."""
    return json.dumps({"status": "running", "version": "1.0.0"})


def list_formats() -> list[str]:
    """List supported output formats."""
    return ["json", "csv", "xml"]


def main():
    parser = argparse.ArgumentParser(description="Fake CLI App for testing")
    subparsers = parser.add_subparsers(dest="command")

    proc = subparsers.add_parser("process", help="Process a file")
    proc.add_argument("input", help="Input file path")
    proc.add_argument("output", help="Output file path")
    proc.add_argument("--format", default="json", choices=["json", "csv", "xml"])

    subparsers.add_parser("status", help="Show status")
    subparsers.add_parser("formats", help="List formats")

    args = parser.parse_args()

    if args.command == "process":
        print(process_file(args.input, args.output, args.format))
    elif args.command == "status":
        print(get_status())
    elif args.command == "formats":
        print(json.dumps(list_formats()))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
