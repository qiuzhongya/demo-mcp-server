# src/demo_mcp/server.py

from mcp.server import Server
from mcp.types import Tool
from typing import Any, Dict, List, AsyncGenerator

# 定义工具函数（使用生成器返回内容）
async def say_hello(name: str) -> AsyncGenerator[Dict[str, Any], None]:
    """
    A simple tool that returns a greeting.
    """
    message = f"Hello, {name}! 🌟 This is your MCP server speaking."
    yield {
        "type": "update",
        "output": [
            {
                "type": "text",
                "text": message
            }
        ]
    }

async def get_weather(location: str) -> AsyncGenerator[Dict[str, Any], None]:
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

# 手动创建 Tool 对象
tools: List[Tool] = [
    Tool(
        name="say_hello",
        description="Say hello to someone",
        parameters={
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
        parameters={
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

# 创建 Server 实例，并传入 tools 列表
server = Server(
    name="demo-mcp-server",
    version="0.1.0",
    tools=tools
)
