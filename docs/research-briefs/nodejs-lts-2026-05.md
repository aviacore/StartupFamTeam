# Research brief: Node.js LTS baseline

Date: 2026-05-17

## Short answer

Use **Node.js v24 LTS (Krypton)** for new StartupFamTeam JavaScript/TypeScript projects. The current Node.js download page lists **Node.js v24.15.0 LTS**, while v26 is still Current and v22 is already in Maintenance LTS.

## Facts and sources

- The official Node.js download page currently offers **Node.js v24.15.0 LTS** as the default LTS download. Source: <https://nodejs.org/en/download>
- The official Node.js releases page says production applications should use **Active LTS** or **Maintenance LTS** releases. Source: <https://nodejs.org/en/about/previous-releases>
- The official releases table lists:
  - **v24 Krypton**: LTS, first released 2025-05-06, last updated 2026-04-15.
  - **v22 Jod**: LTS, first released 2024-04-24, last updated 2026-05-13.
  - **v26**: Current, first released 2026-05-05.
  Source: <https://nodejs.org/en/about/previous-releases>
- The official Node.js release schedule lists:
  - **v24**: LTS started 2025-10-28, Maintenance starts 2026-10-20, End-of-Life 2028-04-30.
  - **v22**: Maintenance started 2025-10-21, End-of-Life 2027-04-30.
  - **v26**: LTS starts 2026-10-28, End-of-Life 2029-04-30.
  Source: <https://raw.githubusercontent.com/nodejs/Release/main/schedule.json>

## Implications

- **New MVPs**: choose Node.js 24 because it is the current LTS line and has the longest active support window among currently LTS-ready releases.
- **Existing Node.js 22 projects**: staying on v22 is acceptable short-term, but it is already Maintenance LTS, so plan an upgrade path to v24.
- **Node.js 26**: avoid for production defaults today because it is Current, not LTS, until 2026-10-28.
- **Node.js 20 and older**: avoid for new work; Node.js 20 reached End-of-Life on 2026-04-30 according to the release schedule.

## Recommendation

Set the team default to **Node.js 24 LTS** in project docs, local tool version files, Docker images, and CI. For hackathon/MVP deployments, confirm the target host supports Node.js 24 before locking it; if not, Node.js 22 Maintenance LTS is the fallback.

## Unknowns / caveats

- Hosting providers can lag behind the Node.js release schedule. Check the selected platform's runtime support before deployment.
- This brief uses public official Node.js sources checked on 2026-05-17; re-check before major production launches.
