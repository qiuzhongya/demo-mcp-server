# demo_mcp/server.py
import asyncio
import os
from typing import Any, Dict

import mcp.server.stdio as stdio
import mcp.types as types
from mcp.server.lowlevel import NotificationOptions, Server
from mcp.server.models import InitializationOptions

# ---------- 引入业务函数 ----------
from demo_mcp.tools import create_task, query_task
from demo_mcp.tools import TaskStatus

server = Server("demo-mcp")

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="translate_figma",
            description="一键把 Figma 设计翻译成 Kotlin Compose 源码",
            inputSchema={
                "type": "object",
                "properties": {
                    "figma_url": {"type": "string", "description": "Figma URL"},
                    "figma_token": {"type": "string", "description": "Figma Token (optional)"},
                    "app_name": {"type": "string", "description": "App Name (optional)"},
                },
                "required": ["figma_url"],
            },
        ),
    ]

async def wait_for_code(task_id: str) -> str:
    started = asyncio.get_event_loop().time()
    while True:
        if asyncio.get_event_loop().time() - started > 10:
            raise RuntimeError(f"任务 {task_id} 等待超时")

        data = query_task(task_id)
        status = data["status"]
        code_str = data.get("output_code", "")
        zip_url = data.get("output_url", "")

        if status == TaskStatus.Successed:
            md_parts = [
                "任务执行成功！完整 Kotlin 源码如下：\n",
                f"```kotlin\n{code_str}\n```"
            ]
            if zip_url:
                md_parts.append(f"\n其他资源：{zip_url}")
            return "".join(md_parts)

        if status in (TaskStatus.Creating, TaskStatus.Running):
            await asyncio.sleep(1)
            continue

        if status == TaskStatus.CreateFail:
            raise RuntimeError("服务器忙")
        if status == TaskStatus.Failed:
            raise RuntimeError(f"任务失败：{zip_url or '无'}")

        raise RuntimeError(f"未知状态：{status}")

@server.call_tool()
async def handle_call_tool(name: str, arguments: Dict[str, Any]) -> list[types.TextContent]:
    if name == "translate_figma":
        try:
            figma_url = arguments["figma_url"]
            figma_token = arguments.get("figma_token") or os.getenv("FIGMA_TOKEN", "dummy")
            app_name = arguments.get("app_name") or os.getenv("APP_NAME", "demo_app")

            if not figma_url:
                return [types.TextContent(type="text", text="缺少 figma_url")]

            print(f"创建任务: {figma_url}")
            result = create_task(figma_url, figma_token, app_name)
            task_id = result["task_id"]

            markdown = await wait_for_code(task_id)
            return [types.TextContent(type="text", text=markdown)]

        except Exception as e:
            return [types.TextContent(type="text", text=f"错误：{e}")]

    raise ValueError(f"Unknown tool: {name}")

async def async_main():
    async with stdio.stdio_server() as (reader, writer):
        await server.run(
            reader,
            writer,
            InitializationOptions(
                server_name="demo-mcp",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )

# ✅ 供 scripts 调用
def main():
    asyncio.run(async_main())

if __name__ == "__main__":
    main()