# src/demo_mcp/server.py

from mcp.server import Server
from mcp.types import Tool, TextContent
from typing import List, AsyncGenerator
import asyncio

# 创建 MCP 服务器
server = Server("demo-mcp-server")

# ✅ 使用 @server.tool 注册工具（官方支持）
@server.tool("say_hello")
async def say_hello(name: str) -> List[TextContent]:
    """
    Say hello to someone.
    """
    return [TextContent(type="text", text=f"Hello, {name}! 🌟 This is your MCP server speaking.")]

@server.tool("get_weather")
async def get_weather(location: str) -> List[TextContent]:
    """
    Mock weather tool.
    """
    return [TextContent(type="text", text=f"Weather in {location}: ☀️ Sunny and 25°C")]

# 可选：启动日志
print("🔧 MCP Tools Registered:")
print("  • say_hello(name: str)")
print("  • get_weather(location: str)")
