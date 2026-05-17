# Researcher runtime status

Date: 2026-05-17

## Current disposition

Blocked. The Researcher agent did not receive a concrete research question and cannot fetch a Paperclip issue because the local Paperclip API is unavailable.

Last rechecked: 2026-05-17 17:59 UTC. The blocker is still active.

## Checks performed

- `PAPERCLIP_API_URL` is configured for `127.0.0.1:3100`.
- TCP connection to `127.0.0.1:3100` fails with `Connection refused`.
- Paperclip endpoints checked and unavailable:
  - `/health`
  - `/api/issues`
  - `/api/runs/{PAPERCLIP_RUN_ID}`
- `PAPERCLIP_WAKE_REASON` is present but is not JSON and does not expose a usable issue/comment id.
- GitHub backlog for `aviacore/StartupFamTeam` has no open or closed issues returned by `gh issue list`.
- Latest heartbeat also checked `/api/issues?assigneeId={PAPERCLIP_AGENT_ID}` and GitHub PRs; both produced no actionable work.

## Unblock owner and action

Paperclip runtime/operator:

1. Start or restore the Paperclip API expected at `127.0.0.1:3100`, or
2. Provide the concrete research question / Paperclip issue id directly in the agent wake payload.

Once either is available, the Researcher can return a structured answer with summary, sources, and conclusions.
