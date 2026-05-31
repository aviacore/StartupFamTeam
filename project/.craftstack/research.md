## Our project facts (GROUND TRUTH — base all comparisons on this)
## AGENTS.md (project overview)
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


---

## CONTEXT.md (full context)
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


---

## server.py (header)
"""
CraftStack Server v0.7 — with Agent Router + multi-provider + model tiers
Zero-dependency: stdlib only.
Usage: pythonw server.py [port]
"""

import os, sys, json, time, mimetypes, threading, urllib.request, urllib.error, re
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, TimeoutError
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

PIPELINE_TIMEOUT = 600  # max total pipeline seconds
AI_TIMEOUT = 30         # second

---

## Project structure
  .gitkeep
  ai-hub.html
  arch.md
  card.html
  craftstack.html
  output.html
  output.md
  plan.md
  Plan_05.md
  Plan_07.md
.craftstack/
  agents.json
  config.example.json
  config.json
analyst/
  analyst-20260526-231145.md
  analyst-20260527-115004.md
  analyst-20260527-123645.md
ceo/
  ceo-20260526-231145.md

---



[No results found]

---



## GitHub search results for: paperclip

- [paperclip](https://github.com/paperclipai/paperclip) — The open-source app everyone uses to manage agents at work (⭐68430, TypeScript)
- [paperclip](https://github.com/thoughtbot/paperclip) — Easy file attachment management for ActiveRecord (⭐9017, Ruby)
- [hermes-paperclip-adapter](https://github.com/NousResearch/hermes-paperclip-adapter) — Paperclip adapter for Hermes Agent — run Hermes as a managed employee in a Paperclip company (⭐1446, TypeScript)
