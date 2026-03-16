"""chrome_cookie_decryptor tools for yt-dlp."""

import inspect
import json

from mcp.server.fastmcp import FastMCP


def register_tools(server: FastMCP, backend) -> None:
    """Register chrome_cookie_decryptor tools with the server."""

    @server.tool()
    async def chrome_cookie_decryptor_decrypt(
        encrypted_value: str,
    ) -> str:
        """Decrypt"""
        # Stub — implementation not yet generated
        return await backend.run_subcommand("chrome_cookie_decryptor_decrypt")

