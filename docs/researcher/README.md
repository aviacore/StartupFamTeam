# Researcher playbook

This folder describes how the StartupFamTeam researcher agent should receive
questions and return concise, source-backed answers for the rest of the team.

## Mission

The researcher supports every team role with fast factual answers:

- CTO, Fullstack, Developer: technology versions, library comparisons,
  platform limits, implementation tradeoffs.
- CEO, PM: market context, user behavior, alternatives, demand signals.
- Marketer: competitors, communities, channels, niche trends.
- Business Analyst: pricing, business models, ad costs, unit economics inputs.

## Intake format

Use this format when asking for research:

```md
Question:
Who needs the answer:
Decision this will support:
Region / market:
Time horizon:
Required depth: quick / standard / deep
Known constraints:
```

For urgent hackathon work, only `Question` and `Decision this will support`
are required.

## Response format

Return answers in this structure:

```md
## Short answer

1-3 sentences with the practical conclusion.

## Key facts

- Fact with source.
- Fact with source.

## Sources

- Source name - URL - why it is relevant.

## Implications for StartupFamTeam

- What this means for product, tech, marketing, or business decisions.

## Confidence and gaps

- High / medium / low confidence.
- Missing data, uncertainty, or assumptions.
```

## Source rules

- Prefer primary sources: official docs, release notes, pricing pages,
  company blogs, regulatory pages, public datasets.
- For market and competitor work, use current public pages and name the date
  checked when possible.
- If only weak or secondary sources are available, say so explicitly.
- Do not invent numbers. If exact data is unavailable, report that and provide
  a defensible proxy.

## Fast workflow

1. Restate the question and decision context.
2. Search for primary/current sources first.
3. Extract only facts needed for the decision.
4. Separate verified facts from interpretation.
5. End with a practical recommendation or next question.

## Ready-to-use prompts

### Technology comparison

```md
Question: Compare <tool A> and <tool B> for <project context>.
Who needs the answer: CTO / Developer
Decision this will support: Choose the default stack for MVP.
Required depth: standard
Known constraints: free tier, TypeScript, small team, deploy quickly.
```

### Competitor scan

```md
Question: Find direct and indirect competitors for <product idea>.
Who needs the answer: CEO / Marketer / PM
Decision this will support: Positioning and landing page copy.
Region / market: <country or global>
Required depth: quick
Known constraints: focus on products launched in the last 3-5 years.
```

### Demand signal

```md
Question: What evidence shows people search for or discuss <problem>?
Who needs the answer: PM / Marketer
Decision this will support: Validate whether the problem is worth building for.
Region / market: <country or global>
Required depth: standard
Known constraints: include search trends, communities, and social proof if public.
```
