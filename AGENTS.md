# CraftStack — AI Agent Workbench

**Goal:** Lightweight AI agent workbench using OpenCode modes, direct API models, and web dashboard for managing pipeline from idea to result.

**User:** CEO, startup founder. Russian speaker (informal «ты»). Boss sets tasks, Assistant executes.

## Key Decisions

- No Paperclip, No Ollama — too heavy/slow for CPU-only hardware
- DeepSeek V4 Flash primary (free, strong coding); other free APIs as fallback
- Files instead of database — no dependencies, portable, simple
- Port 8765 (8080 occupied by Hikvision)
- SSE for live updates (simpler than WebSocket, works with Python stdlib)
- pythonw.exe on Windows — no console window, no Unicode issues
- 8 agent modes: CEO, PM, CTO, Developer, Designer, Marketer, QA, Analyst

## Pipeline

1. User submits task in dashboard → POST /api/task → server writes task.txt
2. User says «старт» in chat → Assistant reads task.txt, executes
3. Assistant updates state.json → SSE pushes to monitor
4. Dashboard polls /api/state → moves task to «Done» when status=«done»

## Project Structure

```
.opencode/modes/      — 8 agent mode definitions (CEO, PM, CTO, etc.)
.opencode.jsonc       — OpenCode config
AGENTS.md             — this file (auto-loaded every session)
CONTEXT.md            — full project context
server.py             — Python HTTP server (ThreadingHTTPServer), REST API + SSE
dashboard.html        — 3-column kanban + provider cards + floating chat
monitor.html          — SSE live monitor with auto-refresh
start.bat             — kill old processes, launch server with pythonw.exe, open browser
project/              — task artifacts (code, plans, reports)
docs/                 — documentation and session notes
```

## Agent Modes

| Mode | Role | When to use |
|------|------|-------------|
| ceo | Strategy, business model, plan | Setting vision, high-level decisions |
| pm | Tasks, sprints, requirements | Breaking down work, specs |
| cto | Architecture, tech stack | System design decisions |
| developer | Writing code | Building features, fixing bugs |
| designer | UI/UX, visual design | Frontend, CSS, branding |
| marketer | Landing page, GTM | Marketing materials |
| qa | Testing, bug reports | Quality assurance |
| analyst | Data analysis, research | Market research, analytics |

## Hardware

Both Windows machines (no WSL), no GPU — Intel i5-10400 / Core m7-6Y75, 16 GB RAM each.

## Running the Project

```cmd
start.bat          # kills old, starts server, opens browser
http://127.0.0.1:8765/dashboard.html
http://127.0.0.1:8765/monitor.html
```

## Conventions

- Keep it simple, no heavy dependencies
- Russian language for communication, English for code/docs
- File-based storage (JSON/text), no DB
- When user says «старт», read task.txt and execute it
- Update state.json and project/ files as work progresses
