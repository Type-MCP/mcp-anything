"""Test configuration for click MCP server."""

import pytest


@pytest.fixture
def server():
    """Create a test server instance."""
    from click.server import server
    return server
