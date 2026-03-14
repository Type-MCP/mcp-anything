"""A WebSocket JSON-RPC server for device management."""

import asyncio
import json
import websockets

DEVICES = {}


async def handler(websocket):
    """Handle incoming WebSocket connections."""
    async for message in websocket:
        data = json.loads(message)
        method = data.get("method", "")
        params = data.get("params", {})
        request_id = data.get("id")

        result = dispatch(method, params)
        response = json.dumps({"jsonrpc": "2.0", "result": result, "id": request_id})
        await websocket.send(response)


def dispatch(method: str, params: dict) -> dict:
    """Route JSON-RPC methods to handler functions."""
    handlers = {
        "register_device": register_device,
        "get_device": get_device,
        "list_devices": list_devices,
    }
    fn = handlers.get(method)
    if fn:
        return fn(**params)
    return {"error": f"Unknown method: {method}"}


def register_device(device_id: str, name: str) -> dict:
    """Register a new IoT device with the server."""
    DEVICES[device_id] = {"id": device_id, "name": name, "status": "online"}
    return DEVICES[device_id]


def get_device(device_id: str) -> dict:
    """Get information about a registered device."""
    return DEVICES.get(device_id, {"error": "Device not found"})


def list_devices() -> list:
    """List all registered devices."""
    return list(DEVICES.values())


async def main():
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
