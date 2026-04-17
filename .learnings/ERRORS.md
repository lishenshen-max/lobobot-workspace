# Errors

Command failures and integration errors.

---
## [ERR-20260413-001] feishu_delivery_failed

**Logged**: 2026-04-13T00:40:00+08:00
**Priority**: medium
**Status**: resolved
**Area**: infra

### Summary
Cron job 飞书通知失败，连续4次错误

### Error
```
Delivering to Feishu requires target <chatId|user:openId|chat:chatId>
```

### Context
- Cron Job: Stock Monitor - Trading Hours (连续4次失败)
- Cron Job: Weekly Security Scan (1次失败)
- delivery mode 设置为 announce 但缺少 target

### Resolution
- 将 delivery.mode 改为 "none"
- isolated session 不再尝试发送飞书通知
- 任务结果直接输出到控制台

### Metadata
- Related Files: task_state/*.json
- Reproducible: yes

---
