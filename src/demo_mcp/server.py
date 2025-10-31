# src/demo_mcp/server.py

from mcp.server import Server
from mcp.types import Tool
from typing import Any, Dict, List, AsyncGenerator

# 工具函数
async def say_hello(name: str) -> AsyncGenerator[Dict[str, Any], None]:
    message = f"Hello, {name}! 🌟 This is your MCP server speaking."
    yield {
        "type": "update",
        "output": [
            {"type": "text", "text": message}
        ]
    }

async def get_weather(location: str) -> AsyncGenerator[Dict[str, Any], None]:
    result_text = f"Weather in {location}: ☀️ Sunny and 25°C"
    yield {
        "type": "update",
        "output": [
            {"type": "text", "text": result_text}
        ]
    }

# ✅ 正确：使用 inputSchema，且格式为完整的 JSON Schema
tools: List[Tool] = [
    Tool(
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
        fn=say_hello
    ),
    Tool(
        name="get_weather",
        description="Get the weather for a location",
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
        fn=get_weather
    )
]

# 创建服务器
server = Server(
    name="demo-mcp-server",
    version="0.1.0",
    tools=tools
)
