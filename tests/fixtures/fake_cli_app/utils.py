"""Utility functions for the fake CLI app."""

import csv
import json
from pathlib import Path


def read_json(path: str) -> dict:
    """Read a JSON file."""
    with open(path, "r") as f:
        return json.load(f)


def write_csv(path: str, data: list[dict]) -> None:
    """Write data to CSV."""
    if not data:
        return
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
