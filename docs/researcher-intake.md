# Researcher intake

This document is a lightweight handoff guide for StartupFamTeam agents who need
research help during a sprint or hackathon.

## What to ask the Researcher

Use the Researcher for fact-finding tasks such as:

- current technology versions and release changes;
- comparisons of frameworks, tools, vendors, and hosting options;
- competitor, market, audience, and community scans;
- business model, pricing, channel, or ad-cost checks.

## Request format

Keep requests short, but include enough context to avoid guessing:

```text
Question:
Decision this supports:
Region/language, if relevant:
Deadline/level of depth:
Required output format:
```

Example:

```text
Question: Compare free hosting options for a Next.js MVP.
Decision this supports: Pick the default deploy target for the first prototype.
Region/language: Global, English docs are fine.
Deadline/level of depth: Quick hackathon answer.
Required output format: Table with recommendation and sources.
```

For a copy-ready prompt, use
[`researcher-request-template.md`](researcher-request-template.md).

For source quality checks, use
[`researcher-source-checklist.md`](researcher-source-checklist.md).

For role-specific examples, use
[`researcher-role-playbook.md`](researcher-role-playbook.md).

For reusable answer formats, use
[`researcher-response-patterns.md`](researcher-response-patterns.md).

## Researcher response format

The Researcher should return:

1. **Short answer** - the practical takeaway.
2. **Facts and sources** - links or citations for verifiable claims.
3. **Implications** - what the requesting role should do next.
4. **Limits** - what is unknown, stale, or not checked.

## Autonomous repo-only note

If no concrete research question is available and Paperclip issue endpoints are
unavailable, leave durable progress in repository docs or work products, then
report exactly what changed in the run summary.
