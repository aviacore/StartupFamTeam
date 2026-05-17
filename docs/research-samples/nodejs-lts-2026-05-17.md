# Research sample: current Node.js LTS

Date checked: 2026-05-17

## Question

What is the current Node.js LTS version line?

## Short answer

Use **Node.js 24.x (Krypton)** for new production work that needs the current
Active LTS line. As of this check, Node.js 24 is Active LTS and is scheduled to
move to Maintenance LTS on 2026-10-20, with end-of-life on 2028-04-30.

Node.js 22.x (Jod) is still supported, but it is already in Maintenance LTS and
is a better choice only when project dependencies or hosting environments have
not yet caught up with Node.js 24.

Do not treat Node.js 26.x as LTS yet. It is the Current release line and is
scheduled to enter LTS on 2026-10-28.

## Facts and sources

- The official Node.js releases page lists production applications as suitable
  for **Active LTS or Maintenance LTS** releases, and shows Node.js 24
  (Krypton) and Node.js 22 (Jod) as LTS lines:
  <https://nodejs.org/about/releases/>
- The Node.js Release Working Group schedule lists:
  - 24.x: **Active LTS**, codename Krypton, Maintenance start 2026-10-20,
    End-of-life 2028-04-30.
  - 22.x: **Maintenance LTS**, codename Jod, End-of-life 2027-04-30.
  - 26.x: **Current**, LTS start 2026-10-28.
  Source: <https://raw.githubusercontent.com/nodejs/Release/main/README.md>
- The Node.js 26.0.0 release post says Node.js 26 is **Current** and will enter
  LTS in October 2026:
  <https://nodejs.org/en/blog/release/v26.0.0>

## Implications for StartupFamTeam

- Default new backend/fullstack projects to Node.js 24.x unless a framework,
  package, or hosting provider requires Node.js 22.x.
- If using managed hosting, check the provider's Node.js runtime support before
  committing to Node.js 24 in deployment configuration.
- Track Node.js 26 for later evaluation, especially if Temporal API support
  matters, but avoid it for production defaults until it reaches LTS.

## Limits / unknowns

- Exact latest patch versions change frequently. Check the official downloads or
  releases page when pinning a runtime image.
- This sample only answers runtime line selection, not framework-specific
  compatibility.

Confidence: high

Why: based on official Node.js release and Release Working Group sources.

What would improve confidence: checking the exact target hosting provider and
framework runtime support for the project being built.
