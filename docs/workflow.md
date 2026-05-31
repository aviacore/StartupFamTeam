# CraftStack Pipeline Workflow

## Flow Diagram

```
User (Dashboard)           Server (pythonw)           Assistant (OpenCode)
     │                          │                           │
     │  POST /api/task          │                           │
     │─────────────────────────>│                           │
     │                          │ writes task.txt           │
     │                          │ state.json: "waiting"     │
     │                          │ SSE push to monitor       │
     │                          │                           │
     │  "Go" / "Start"                                   │
     │─────────────────────────────────────────────────────>│
     │                          │                           │
     │                          │                    reads task.txt
     │                          │                    state.json: "running"
     │                          │<── PUT /api/log ─────────┤
     │                          │ SSE push                  │
     │  Monitor shows progress  │                           │
     │                          │                    executes task
     │                          │<── PUT /api/log ─────────┤
     │                          │                    produces files
     │                          │                    state.json: "done"
     │                          │<── PUT /api/log ─────────┤
     │                          │ SSE push                  │
     │  Dashboard polls         │                           │
     │  /api/state → "done"    │                           │
     │  Task moves to "Done"   │                           │
```

## File Paths

- Task file: `project/.craftstack/task.txt`
- State file: `project/.craftstack/state.json`
- Agent log: `project/.craftstack/agents.txt`

## State Machine

`idle` → `waiting` → `running` → `done`

| State | Meaning |
|---|---|
| idle | No task, server just started |
| waiting | Task submitted via dashboard, not yet picked up |
| running | Assistant is executing |
| done | Task complete |

## Dashboard ↔ Server Sync

- Dashboard polls `/api/state` every 3 seconds
- When server status = "running" → move matching task to "Progress"
- When server status = "done" → move matching task to "Done"
- Task matching: substring match between server task text and kanban task description

## Monitor ↔ Server Sync

- Monitor uses EventSource('/events') for SSE
- Server pushes state.json on every write
- Fallback: auto-reload every 5s if SSE fails or opened from file://
