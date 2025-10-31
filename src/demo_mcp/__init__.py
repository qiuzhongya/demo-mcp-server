# src/demo_mcp/__init__.py

from .server import main as _main
import asyncio

def main():
    """Entry point for `demo-mcp-server` command"""
    print("🚀 Starting demo-mcp-server (stdio mode)...")
    print("📦 MCP Server Name: demo-mcp-server")
    print("🔧 Tools: say_hello, get_weather")
    print("💡 This server communicates via stdin/stdout (stdio)")
    print("💡 Use Ctrl+C to stop.")
    try:
        asyncio.run(_main())
    except KeyboardInterrupt:
        print("\n👋 MCP server stopped. Goodbye!")
