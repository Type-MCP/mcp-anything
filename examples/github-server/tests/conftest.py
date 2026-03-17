"""Test configuration for github MCP server."""

import pytest


@pytest.fixture
def server():
    """Create a test server instance."""
    from mcp_github.server import server
    return server
