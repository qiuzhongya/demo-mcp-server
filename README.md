# demo-mcp-server

Minimal MCP (Model Context Protocol) Server Demo

Exposes two simple tools:
- `say_hello(name)`
- `get_weather(location)`

## Usage

```bash
uv run --python 3.13 --with "git+https://github.com/qiuzhongya/demo-mcp-server.git" demo-mcp-server
