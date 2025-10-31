# src/demo_mcp/__init__.py

from .server import server
import asyncio
from mcp.server.serve import serve

def main():
    print("🚀 Starting demo-mcp-server...")
    print("📦 MCP Server Name: demo-mcp-server")
    print("🌐 Running on http://127.0.0.1:8080")
    print("💡 Use Ctrl+C to stop.")

    try:
        asyncio.run(serve(server, host="127.0.0.1", port=8080))
    except KeyboardInterrupt:
        print("\n👋 MCP server stopped. Goodbye!")
