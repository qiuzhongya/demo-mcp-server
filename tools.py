# 模拟 d2c_task.py
from enum import Enum

class TaskStatus(Enum):
    Creating = "Creating"
    Running = "Running"
    Successed = "Successed"
    Failed = "Failed"
    CreateFail = "CreateFail"

def create_task(figma_url: str, figma_token: str, app_name: str) -> dict:
    return {
        "task_id": "task_123",
        "msg": f"Task created for {figma_url}",
    }

def query_task(task_id: str) -> dict:
    return {
        "status": TaskStatus.Successed,
        "output_code": "/* Sample Kotlin Code */\n@Composable\nfun MyApp() {\n    Text(\"Hello World\")\n}",
        "output_url": "https://example.com/project.zip",
    }