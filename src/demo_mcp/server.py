# src/demo_mcp/server.py

import asyncio
import mcp.server.stdio as stdio
import mcp.types as types
from mcp.server.lowlevel import NotificationOptions, Server
from mcp.server.models import InitializationOptions
from typing import Any, Dict

# 创建 MCP 服务器实例
server = Server("demo-mcp-server")

# ---------------- 工具列表 ----------------
@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="say_hello",
            description="Say hello to someone",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "The person's name"
                    }
                },
                "required": ["name"]
            },
        ),
        types.Tool(
            name="get_weather",
            description="Get the weather for a location (mock)",
            inputSchema={
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city or place"
                    }
                },
                "required": ["location"]
            },
        ),
    ]

# ---------------- 工具执行 ----------------
@server.call_tool()
async def handle_call_tool(name: str, arguments: Dict[str, Any]) -> list[types.TextContent]:
    if name == "say_hello":
        name_arg = arguments.get("name", "World")
        if not name_arg:
            return [types.TextContent(type="text", text="Missing required parameter: name")]
        await asyncio.sleep(900)
        return [types.TextContent(type="text", text=f"Hello, {name_arg}! 🌟 This is your MCP server speaking.")]

    elif name == "get_weather":
        location = arguments.get("location", "Unknown")
        if not location:
            return [types.TextContent(type="text", text="Missing required parameter: location")]
        return [types.TextContent(type="text", text=f"Weather in {location}: ☀️ Sunny and 26°C")]

    raise ValueError(f"Unknown tool: {name}")

# ---------------- 主入口 ----------------
async def main() -> None:
    async with stdio.stdio_server() as (reader, writer):
        await server.run(
            reader,
            writer,
            InitializationOptions(
                server_name="demo-mcp-server",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )
