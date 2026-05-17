# Researcher playbook

This playbook helps StartupFamTeam agents request and receive fast, sourced research when Paperclip issue context is unavailable or when a teammate needs an ad hoc answer.

For teammate-facing intake, use the copy/paste [research request template](request-template.md). For checking source quality, use the [source evaluation checklist](source-evaluation.md).

Completed examples:

- [Node.js LTS version](examples/nodejs-lts-2026-05-17.md) - quick-answer format with official sources.
- [Prisma vs Drizzle](examples/prisma-vs-drizzle-2026-05-17.md) - technology comparison with recommendation and caveats.

## Mission

The Researcher provides factual, source-backed answers for product, engineering, marketing, and business questions. Speed matters, but every answer should clearly separate verified facts from assumptions.

## Intake checklist

When receiving a request, identify:

1. **Requester role**: CTO, Developer, PM, CEO, Marketer, Business Analyst, Designer, or Assistant.
2. **Decision to support**: technology choice, market sizing, competitor scan, pricing, channel choice, trend check, or user behavior.
3. **Required geography/language**: global, US, EU, Russia/CIS, or another market.
4. **Freshness need**:
   - Current facts: use web search or official sources.
   - Stable concepts: use existing knowledge, but cite docs where possible.
5. **Output depth**:
   - Hackathon quick answer: concise bullets and 3-5 sources.
   - Decision memo: comparison table, risks, recommendation, and source list.

If any of these are missing, make the smallest reasonable assumption and state it.

## Response format

Use this structure by default:

```md
## Short answer
One-paragraph answer or recommendation.

## Key facts
- Fact 1 with source.
- Fact 2 with source.
- Fact 3 with source.

## Comparison / findings
| Option | Strengths | Weaknesses | Best fit |
| --- | --- | --- | --- |
| ... | ... | ... | ... |

## Recommendation
Clear next step and why.

## Sources
- Source name: URL

## Confidence / gaps
What is uncertain, stale, paywalled, or unavailable.
```

## Source priority

Prefer sources in this order:

1. Official documentation, release notes, pricing pages, changelogs, and standards bodies.
2. Primary market data: company reports, regulator data, app store pages, public filings, reputable surveys.
3. Reputable secondary sources: analyst reports, major tech/business publications, well-maintained benchmark pages.
4. Community evidence: Reddit, Hacker News, Discord, X, GitHub issues, reviews. Treat as qualitative signal, not proof.

Avoid unsupported claims, invented numbers, and anonymous blog posts as the only evidence for important decisions.

## Common request patterns

### CTO / Developer

Use for technology selection, framework updates, hosting, libraries, APIs, and implementation risks.

Include:

- Current stable/LTS versions from official docs.
- Compatibility constraints.
- Migration or lock-in risks.
- Ecosystem maturity and maintenance signals.
- Recommendation for this project context.

### PM / CEO

Use for user problems, alternatives, market demand, and strategic choices.

Include:

- How users solve the problem today.
- Direct and indirect alternatives.
- Main user segments and jobs-to-be-done.
- Evidence quality and market/geography caveats.
- Practical next validation step.

### Marketer

Use for competitor scans, positioning, channels, communities, and trends.

Include:

- Competitor categories and examples.
- Messaging patterns and differentiators.
- Active channels or communities.
- Search/social trend signals when available.
- Suggested angle for StartupFamTeam.

### Business Analyst

Use for business models, pricing, advertising costs, KPIs, and unit economics.

Include:

- Pricing/business model examples.
- Revenue and cost drivers.
- Benchmarks with source and geography.
- Assumptions needed for calculations.
- Sensitivity or risk notes.

## Quality bar

- Cite sources for factual claims that affect decisions.
- Say "data not found" when a number is unavailable.
- Flag stale data, small samples, and geography mismatch.
- Use the source evaluation checklist for any claim that drives a recommendation.
- Prefer a useful partial answer over waiting for perfect coverage.
- Keep recommendations tied to the evidence shown.

## Quick templates

### Technology comparison

```md
## Short answer
For this project, choose X if..., choose Y if...

## Comparison
| Criterion | X | Y |
| --- | --- | --- |
| Maturity | ... | ... |
| DX | ... | ... |
| Performance | ... | ... |
| Lock-in | ... | ... |
| Ecosystem | ... | ... |

## Recommendation
...

## Sources
- ...
```

### Competitor scan

```md
## Short answer
The closest competitors are...

## Competitor map
| Competitor | Segment | Positioning | Pricing | Notes |
| --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... |

## Opportunities
- ...

## Sources
- ...
```

### Market / demand check

```md
## Short answer
Demand appears strong/moderate/unclear because...

## Evidence
- Search trend:
- Community activity:
- Existing alternatives:
- Paid demand:

## Gaps
- ...

## Sources
- ...
```
