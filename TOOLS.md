# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

### 飞书通知代理问题
Python requests 被代理（127.0.0.1:7897）拦截，发送飞书通知时需禁用代理：
```python
requests.post(url, json=payload, proxies={'http': None, 'https': None})
```

### 通达信监控
- 监控进程：PID 23220（2026-04-14重启）
- 窗口HWND：**动态变化**（2026-04-14记录：133538→133982→133632）
- 启动命令：`C:\tdx_monitor\start.bat`
- Python路径：`C:\Users\李桥\AppData\Local\Programs\Python\Python312\python.exe`
- 飞书Webhook：`https://open.feishu.cn/open-apis/bot/v2/hook/7a1c74c1-eff2-4439-8030-9cb5a3e9e823`（从config.json读取）
- **核心教训**：每次截图前必须用`find_runze.py`重新查询HWND，绝不能hardcode
- **窗口标题编码问题**：GetWindowTextW返回UTF-16LE乱码，应用GetWindowTextA+GBK解码或直接用子窗口HWND=330078（图表区）

Add whatever helps you do your job. This is your cheat sheet.
