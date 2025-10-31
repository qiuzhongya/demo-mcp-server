
from .server import server
import asyncio
import uvicorn
from mcp.server.serve import serve

def main():
    print("🚀 Starting demo-mcp-server...")
    print("📦 MCP Server Name: demo-mcp-server")
    print("🔧 Available Tools:")
    print("  • say_hello(name: str)")
    print("  • get_weather(location: str)")
    print("🌐 Running on http://127.0.0.1:8080")
    print("💡 Use Ctrl+C to stop.")

    # 启动 MCP 服务器（通过 Uvicorn）
    try:
        asyncio.run(serve(server, host="127.0.0.1", port=8080))
    except KeyboardInterrupt:
        print("\n👋 MCP server stopped. Goodbye!")
