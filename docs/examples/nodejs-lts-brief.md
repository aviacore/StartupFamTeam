# Research Brief: Which Node.js version is LTS?

## Short answer
- As of 2026-05-17, the official Node.js releases page lists Node.js v24
  "Krypton" and Node.js v22 "Jod" as LTS.
- For a new production project, prefer the newest LTS line that your hosting,
  framework, and dependencies support; currently that is v24.
- Avoid starting new production work on Current releases v26 or v25 unless a
  specific dependency requires them.

## Context
- Requester: Fullstack / CTO
- Decision this supports: choosing a Node.js runtime for project setup and deployment.
- Scope: official Node.js release status.
- Date researched: 2026-05-17.

## Key facts
| Fact | Source | Confidence |
| --- | --- | --- |
| Node.js v24 "Krypton" is listed as LTS. | [Node.js releases](https://nodejs.org/en/about/previous-releases), accessed 2026-05-17 | High |
| Node.js v22 "Jod" is listed as LTS. | [Node.js releases](https://nodejs.org/en/about/previous-releases), accessed 2026-05-17 | High |
| Node.js v26 and v25 are listed as Current, not LTS. | [Node.js releases](https://nodejs.org/en/about/previous-releases), accessed 2026-05-17 | High |
| Node.js says production applications should only use Active LTS or Maintenance LTS releases. | [Node.js releases](https://nodejs.org/en/about/previous-releases), accessed 2026-05-17 | High |

## Options
| Version | Status | Notes |
| --- | --- | --- |
| Node.js v24 "Krypton" | LTS | Best default for new projects if the deployment target and dependencies support it. |
| Node.js v22 "Jod" | LTS | Conservative fallback when a host, dependency, or base image is not ready for v24. |
| Node.js v26 / v25 | Current | Useful for testing upcoming changes, but not the default for production. |

## Sources reviewed
- Node.js releases: https://nodejs.org/en/about/previous-releases - official
  release table and LTS guidance.
- nodejs/release schedule: https://github.com/nodejs/release#release-schedule -
  linked by the official Node.js releases page for detailed scheduling.

## Conclusions
- Use Node.js v24 LTS for new StartupFamTeam services unless the chosen host or
  dependency stack requires v22.
- If a starter template pins v22 LTS, that is still within the official LTS
  guidance; document the reason before staying on it.

## Data gaps
- This brief does not verify every hosting provider's currently supported Node
  runtime list. Check the selected host before deployment.

## Suggested follow-up
- Confirm the Node.js runtime supported by the chosen deployment platform and
  pin it in the project config or Docker image.
