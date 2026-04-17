import os
import sys
sys.path.append(r"C:\Users\李桥\.openclaw\workspace\task_state")

from recovery_utils import recover_task

# 会话启动时自动恢复任务
if __name__ == "__main__":
    # 恢复股票监控
    tdx_state = recover_task("tdx_monitor_20260410")
    if tdx_state:
        print(f"[恢复成功] 股票监控任务 {tdx_state['task_id']}")
    else:
        print("[无任务] 未找到可恢复的股票监控任务")