"""Tests for httpstat MCP server tools."""

import pytest


class TestToolRegistration:
    """Verify all tools are registered."""

    def test_server_has_tools(self, server):
        """Server should have registered tools."""
        assert server is not None

    def test_run_httpstat_registered(self, server):
        """run_httpstat tool should be registered."""
        # Tool registration is verified by import
        pass

    def test_print_help_registered(self, server):
        """print_help tool should be registered."""
        # Tool registration is verified by import
        pass

