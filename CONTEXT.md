# CraftStack

**Goal:** Lightweight AI agent workbench using OpenCode modes, direct API models, and a web dashboard for managing pipeline from idea to result.

**User:** CEO, startup founder. Russian speaker (informal «ты»).

---

## Core Idea

CraftStack replaces heavy orchestration tools (Paperclip, Ollama) with a simple file-based pipeline:
- User writes a task in the dashboard (or directly in chat)
- Assistant (OpenCode) executes using mode definitions
- Results stored as files in `project/`
- Monitor shows progress live via SSE

## Key Decisions

| Decision | Rationale |
|---|---|
| No Paperclip | Too heavy for local hardware, excessive context overhead |
| No Ollama | Too slow, models too weak for CPU-only hardware |
| DeepSeek V4 Flash primary | Free, strong coding; other free APIs as fallback |
| CEO = user, not an agent | User sets tasks, Assistant executes |
| Files instead of database | No dependencies, portable, simple |
| Port 8765 | Port 8080 occupied by Hikvision iVMS-4200 |
| SSE for live updates | Simpler than WebSocket, works with Python stdlib |
| pythonw.exe on Windows | No console window, no Unicode encoding issues |
| 8 agent modes | CEO, PM, CTO, Developer, Designer, Marketer, QA, Analyst |

## Hardware

| Machine | CPU | RAM | GPU |
|---|---|---|---|
| Desktop | i5-10400 | 16 GB | None |
| Laptop (HP EliteBook 1030 G1) | Core m7-6Y75 | 16 GB | None |
| Both run Windows, no WSL | | | |

## Pipeline

1. User submits task in dashboard → POST /api/task → server writes task.txt
2. User says «старт» in chat → Assistant reads task.txt, executes
3. Assistant updates state.json → SSE pushes to monitor
4. Dashboard polls /api/state → moves task to «Done» when status=«done»

## Files

- `dashboard.html` — 3-column kanban + provider cards + floating Assistant chat
- `monitor.html` — SSE live monitor with auto-refresh fallback
- `server.py` — Python HTTP server (ThreadingHTTPServer), REST API + SSE
- `start.bat` — kills old processes, launches server with pythonw.exe, opens browser
- `.opencode/modes/*.json` — 8 agent mode definitions
- `project/` — task artifacts (code, plans, reports)
- `docs/` — documentation and session notes
