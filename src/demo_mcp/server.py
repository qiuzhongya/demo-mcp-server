# src/demo_mcp/server.py

from mcp.server import Server
from mcp.types import Tool, TextContent  # 只保留存在的类型

# 创建 MCP 服务器实例
server = Server("demo-mcp-server")

# ✅ 正确示例：使用 yield 返回内容
@server.tool("say_hello")
async def say_hello(name: str):
    """
    A simple tool that returns a greeting.
    """
    message = f"Hello, {name}! 🌟 This is your MCP server speaking."
    # MCP 当前使用 yield 返回内容
    yield {
        "type": "update",
        "output": [
            {
                "type": "text",
                "text": message
            }
        ]
    }

# ✅ 第二个工具：模拟天气
@server.tool("get_weather")
async def get_weather(location: str):
    """
    Mock weather tool.
    """
    result_text = f"Weather in {location}: ☀️ Sunny and 25°C"
    yield {
        "type": "update",
        "output": [
            {
                "type": "text",
                "text": result_text
            }
        ]
    }
