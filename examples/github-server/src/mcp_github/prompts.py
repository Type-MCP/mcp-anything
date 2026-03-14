"""Server-delivered MCP prompts (skills) for github."""

from mcp.server.fastmcp import FastMCP


def register_prompts(server: FastMCP) -> None:
    """Register prompts with the server."""

    @server.prompt("use_github")
    async def use_github_prompt() -> str:
        """Guide for using github tools effectively"""
        return """You have access to the github MCP server with these tools:

- meta_root: GET / - GitHub API Root
- security_advisories_list_global_advisories: GET /advisories - List global security advisories
- security_advisories_get_global_advisory: GET /advisories/{ghsa_id} - Get a global security advisory
- apps_get_authenticated: GET /app - Get the authenticated app
- apps_create_from_manifest: POST /app-manifests/{code}/conversions - Create a GitHub App from a manifest
- apps_update_webhook_config_for_app: PATCH /app/hook/config - Update a webhook configuration for an app
- apps_get_webhook_config_for_app: GET /app/hook/config - Get a webhook configuration for an app
- apps_list_webhook_deliveries: GET /app/hook/deliveries - List deliveries for an app webhook
- apps_get_webhook_delivery: GET /app/hook/deliveries/{delivery_id} - Get a delivery for an app webhook
- apps_redeliver_webhook_delivery: POST /app/hook/deliveries/{delivery_id}/attempts - Redeliver a delivery for an app webhook
- get_app_installation_requests: GET /app/installation-requests - List installation requests for the authenticated app
- apps_list_installations: GET /app/installations - List installations for the authenticated app
- apps_delete_installation: DELETE /app/installations/{installation_id} - Delete an installation for the authenticated app
- apps_get_installation: GET /app/installations/{installation_id} - Get an installation for the authenticated app
- apps_create_installation_access_token: POST /app/installations/{installation_id}/access_tokens - Create an installation access token for an app
- apps_unsuspend_installation: DELETE /app/installations/{installation_id}/suspended - Unsuspend an app installation
- apps_suspend_installation: PUT /app/installations/{installation_id}/suspended - Suspend an app installation
- apps_delete_authorization: DELETE /applications/{client_id}/grant - Delete an app authorization
- apps_check_token: POST /applications/{client_id}/token - Check a token
- apps_reset_token: PATCH /applications/{client_id}/token - Reset a token

Use the appropriate tool based on the user's request. Always check required parameters before calling a tool."""

    @server.prompt("debug_github")
    async def debug_github_prompt(error_message: str) -> str:
        """Diagnose issues with github operations"""
        return """The user encountered an error while using github.

Error: {{error_message}}

Available tools: meta_root, security_advisories_list_global_advisories, security_advisories_get_global_advisory, apps_get_authenticated, apps_create_from_manifest, apps_update_webhook_config_for_app, apps_get_webhook_config_for_app, apps_list_webhook_deliveries, apps_get_webhook_delivery, apps_redeliver_webhook_delivery, get_app_installation_requests, apps_list_installations, apps_delete_installation, apps_get_installation, apps_create_installation_access_token

Diagnose the issue and suggest which tool to use to resolve it."""

