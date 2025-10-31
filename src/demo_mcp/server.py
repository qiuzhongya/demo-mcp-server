# src/demo_mcp/server.py

from mcp.server import Server
from mcp.types import Tool, TextContent, ToolResult  # ✅ 全部从 types 导入

# 创建 MCP 服务器实例
server = Server("demo-mcp-server")

# 定义一个最简单的工具
@server.tool("say_hello")
async def say_hello(name: str) -> ToolResult:
    """
    A simple tool that returns a greeting.
    """
    message = f"Hello, {name}! 🌟 This is your MCP server speaking."
    return ToolResult(content=[TextContent(type="text", text=message)])

# 可选：添加第二个工具
@server.tool("get_weather")
async def get_weather(location: str) -> ToolResult:
    """
    Mock weather tool.
    """
    return ToolResult(
        content=[TextContent(type="text", text=f"Weather in {location}: ☀️ Sunny and 25°C")]
    )
