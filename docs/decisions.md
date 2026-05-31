# CraftStack Architecture Decisions

All significant decisions with rationale.

---

## AD-1: Replace Paperclip with CraftStack

**Decision:** Build a custom lightweight workbench instead of using Paperclip.

**Context:** Paperclip requires running heavy agents locally. On i5-10400 / Core m7-6Y75 with 16 GB RAM and no GPU, Paperclip agents consume too much memory and context.

**Consequence:** Zero external orchestration dependencies. Everything is files + Python stdlib.

---

## AD-2: Remove Ollama

**Decision:** Do not use Ollama for local models.

**Context:** Tested Phi-3.5 (1.5B) — too weak for code generation. Llama 3.1 8B doesn't fit hardware constraints. Any useful local model requires GPU.

**Consequence:** All generation via cloud API (DeepSeek V4 Flash primary).

---

## AD-3: DeepSeek V4 Flash as Primary Provider

**Decision:** Use DeepSeek V4 Flash as the default model provider.

**Context:** Free, strong coding capabilities, no geo-blocking for Russia. Other free providers (Gemini 2.0 Flash, OpenRouter, GitHub Models, Mistral) as fallback.

**Consequence:** One provider per session — no multi-provider routing until needed.

---

## AD-4: Port 8765

**Decision:** Use port 8765 instead of 8080.

**Context:** Hikvision iVMS-4200 surveillance software occupies port 8080, returning JSON error `{"code":"1-11","msg":"Invalid url."}`.

**Consequence:** Must remember non-standard port. start.bat uses 8765.

---

## AD-5: Files Instead of Database

**Decision:** Store all state as JSON/text files.

**Context:** Zero dependencies, portable across machines, inspectable with any editor.

**Consequence:** State files: `project/.craftstack/state.json`, `task.txt`, `agents.txt`.

---

## AD-6: SSE for Live Updates

**Decision:** Server-Sent Events for monitor live updates.

**Context:** Simpler than WebSocket (no custom protocol), works with Python stdlib `http.server`. Unidirectional (server → client) is sufficient.

**Consequence:** Monitor.html uses EventSource('/events'). Auto-reconnects on error.

---

## AD-7: pythonw.exe on Windows

**Decision:** Run server with pythonw.exe (no console window).

**Context:** python.exe with console causes UnicodeEncodeError when printing UTF-8 (emoji) to cp1251 console. pythonw.exe has no console at all.

**Consequence:** start.bat kills old pythonw.exe processes, launches new one with full path via %LOCALAPPDATA%.

---

## AD-8: CEO = User, Not an Agent

**Decision:** User (CEO) sets tasks, Assistant (OpenCode) executes.

**Context:** The CEO makes decisions; agents execute technical work. No agent represents the CEO.

**Consequence:** 8 agent modes, not 9.

---

## AD-9: No Copy-Paste Workflow (Server-Integrated)

**Decision:** Dashboard submits tasks to server via HTTP; Assistant picks up from task.txt.

**Context:** Initially tasks were copied to clipboard and pasted here. Server integration eliminates manual step.

**Consequence:** User submits in dashboard → server writes task.txt → user types «старт» → Assistant reads and executes.

---

## AD-10: Session Memory in docs/ Files

**Decision:** Save all project knowledge in docs/ files (not GitHub, not external storage).

**Context:** Chat history lost on terminal close. Files persist across reboots and sessions.

**Consequence:** docs/ contains decisions, architecture, daily notes. CONTEXT.md at root for quick reference.
