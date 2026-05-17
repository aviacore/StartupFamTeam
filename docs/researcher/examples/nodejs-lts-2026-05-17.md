# Example research answer: Node.js LTS version

Question: "What is the current Node.js LTS version?"

Date checked: 2026-05-17

## Short answer

Use **Node.js 24 LTS (Krypton)** for new production work. Node.js 26 exists, but it is a **Current** release as of this check and is scheduled to become LTS on 2026-10-28. Node.js 22 is still LTS, but it is already in Maintenance LTS.

## Key facts

- The official Node.js releases page lists **v24 Krypton** with status **LTS** and **v26** with status **Current**.
- The Node.js releases page says production applications should use **Active LTS** or **Maintenance LTS** releases.
- The official Node.js Release Working Group schedule says:
  - v24 entered LTS on 2025-10-28, moves to maintenance on 2026-10-20, and ends support on 2028-04-30.
  - v22 entered maintenance on 2025-10-21 and ends support on 2027-04-30.
  - v26 starts on 2026-05-05 and is scheduled for LTS on 2026-10-28.

## Comparison

| Version | Status on 2026-05-17 | Best fit |
| --- | --- | --- |
| Node.js 24 | LTS, codename Krypton | Default choice for new production apps |
| Node.js 22 | Maintenance LTS, codename Jod | Existing apps that have not migrated yet |
| Node.js 26 | Current | Experimentation, library compatibility checks, not default production baseline yet |

## Recommendation

Set the project baseline to **Node.js 24 LTS** unless a dependency explicitly requires Node.js 22 or Node.js 26. For package metadata, use a range such as:

```json
{
  "engines": {
    "node": ">=24 <27"
  }
}
```

For stricter reproducibility, pin the exact runtime in the deployment platform or version manager, then revisit before Node.js 24 enters Maintenance LTS in October 2026.

## Sources

- Node.js releases page: https://nodejs.org/en/about/previous-releases
- Node.js Release Working Group schedule: https://raw.githubusercontent.com/nodejs/Release/main/schedule.json
- Node.js Release Working Group repository: https://github.com/nodejs/Release#release-schedule

## Confidence / gaps

High confidence: the answer is based on official Node.js release pages and the official release schedule. Check again before making a long-lived infrastructure decision because release status and patch versions change over time.
