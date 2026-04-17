import json
import os
import time
from datetime import datetime

TASK_STATE_DIR = r"C:\Users\李桥\.openclaw\workspace\task_state"

def save_task_state(task_id, status, **kwargs):
    """保存任务状态快照"""
    state = {
        "task_id": task_id,
        "status": status,
        "timestamp": datetime.now().isoformat(),
        **kwargs
    }
    filepath = os.path.join(TASK_STATE_DIR, f"{task_id}.json")
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

def load_task_state(task_id):
    """加载任务状态"""
    filepath = os.path.join(TASK_STATE_DIR, f"{task_id}.json")
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def recover_task(task_id):
    """恢复任务执行"""
    state = load_task_state(task_id)
    if state and state["status"] == "running":
        # 执行恢复命令（示例：重启监控）
        if "recovery_cmd" in state:
            os.system(state["recovery_cmd"])
            # 更新状态为已恢复
            save_task_state(
                task_id, 
                "recovered",
                recovered_at=datetime.now().isoformat()
            )
    return state