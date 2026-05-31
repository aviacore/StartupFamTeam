# CraftStack Components

## File Map

```
CraftStack/
├── CONTEXT.md                       # Project overview (this)
├── dashboard.html                   # Three-column kanban UI
│   ├── Left column: Agents          # 8 agent toggles (CEO, PM, etc.)
│   ├── Center: Kanban               # Idea → Progress → Done
│   │   ├── Task input + submit      # Creates task, POST to server
│   │   ├── Column counters          # Task counts per column
│   │   └── Task cards              # Title, agent, description, delete
│   ├── Right: Providers             # Free/paid model cards
│   │   ├── Free: DeepSeek, Gemini, OpenRouter, GitHub, Mistral
│   │   └── Paid: OpenAI, Anthropic, Google Pro (collapsible)
│   ├── Floating Assistant chat      # Bottom-right bubble
│   └── Background animation         # Particle canvas
│
├── monitor.html                     # SSE-powered live monitor
│   ├── Connection badge             # [live] / [offline]
│   ├── Agent + Task display         # Current agent and task text
│   ├── Progress pips                # Agent status (done/running/waiting)
│   └── Log                          # Timestamped action log
│
├── server.py                        # HTTP server (v0.4)
│   ├── ThreadingHTTPServer           # Concurrent SSE + API
│   ├── GET /events                  # SSE endpoint
│   ├── GET /api/state               # JSON state
│   ├── GET /api/task                # Current task text
│   ├── POST /api/task               # Submit new task
│   ├── POST /api/log                # Add log entry
│   ├── POST /api/start              # Mark pipeline started
│   └── Static file serving          # dashboard.html, project/, etc.
│
├── start.bat                        # Launcher
│   ├── Kill pythonw.exe             # Old server cleanup
│   ├── Kill python.exe              # Safety cleanup
│   └── Start pythonw server.py     # Silent background server
│
├── .opencode/
│   └── modes/*.json                 # 8 agent mode definitions
│       ├── ceo.json                 # Strategic decisions
│       ├── pm.json                  # Task management
│       ├── cto.json                 # Architecture / tech lead
│       ├── developer.json           # Code implementation
│       ├── designer.json            # UI/UX design
│       ├── marketer.json            # Landing pages, copy
│       ├── qa.json                  # Testing
│       └── analyst.json            # Research, analysis
│
├── project/
│   ├── .craftstack/                 # Server runtime files
│   │   ├── state.json              # Current pipeline state
│   │   ├── task.txt                # Active task text
│   │   └── agents.txt              # Selected agents
│   ├── src/
│   │   ├── index.html              # 15-puzzle game (original)
│   │   └── sortpuzzle.html         # SortPuzzle (alternative design)
│   ├── landing/
│   │   ├── index.html              # Landing page
│   │   └── craftstack.html         # Earlier landing page
│   ├── card.html                   # CraftStack business card (deployed)
│   ├── plan.md                     # Pipeline test artifact
│   ├── tasks.md                    # Pipeline test artifact
│   ├── arch.md                     # Pipeline test artifact
│   └── qa-report.md               # Pipeline test artifact
│
├── docs/
│   ├── decisions.md                # Architecture Decision Log
│   ├── workflow.md                 # Pipeline flow diagram
│   ├── components.md               # File map (this file)
│   └── session-2026-05-25.md       # Today's session notes
│
├── dashboard-v1.html               # Historical backup
├── dashboard-v2.html               # Historical backup
├── dashboard-v3.html               # Historical backup
└── archive/14-puzzle/              # Earlier puzzle experiment
```

## Ports

| Service | Port |
|---|---|
| CraftStack Server | 8765 |
| Hikvision iVMS-4200 | 8080 (conflict) |
| Future services | avoid 8080 |

## Dependencies

| Component | Dependencies |
|---|---|
| server.py | Python 3 stdlib only |
| dashboard.html | Browser only |
| monitor.html | Browser only |
| start.bat | Windows only (Batch) |
| OpenCode | npm global package |
