# Source evaluation checklist

Use this checklist before citing a source in a Researcher answer. It is designed for fast team research where decisions may be made from partial evidence.

## Quick scoring

Score each important source from 0 to 2 on the criteria below.

| Criterion | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Authority | Unknown author or unclear publisher | Known author, weak publisher signal | Official source, primary data owner, reputable publisher |
| Freshness | No date or likely stale | Dated but still partially relevant | Current enough for the question |
| Evidence | Opinion only | Some examples or weak data | Data, docs, release notes, pricing, filings, or reproducible method |
| Relevance | Different market, user, or technology | Partially matches the question | Directly matches the question and geography |
| Bias | Strong sales/affiliate angle with no caveat | Some bias, usable with caveat | Low conflict or transparent incentives |

Interpretation:

- **8-10**: strong enough for a key claim.
- **5-7**: usable with caveats or supporting sources.
- **0-4**: do not rely on it for decisions; use only as a lead.

## Source types

### Official docs and pricing pages

Best for:

- Product capabilities.
- Current versions.
- Pricing and limits.
- Support windows and compatibility.

Watch for:

- Marketing claims without benchmarks.
- Region-specific pricing.
- Beta features and preview disclaimers.

### Changelogs and release notes

Best for:

- "What changed?" questions.
- Migration impact.
- Deprecations and breaking changes.

Watch for:

- Missing adoption data.
- Features announced but not generally available.

### Market reports and surveys

Best for:

- Market size.
- Adoption trends.
- Budget and spending benchmarks.

Watch for:

- Paywalled methodology.
- Sponsored samples.
- Geography mismatch.
- Old data reused in newer articles.

### Communities and reviews

Best for:

- User pain points.
- Language customers use.
- Workarounds and switching triggers.

Watch for:

- Vocal minority bias.
- Anecdotes presented as representative.
- Astroturfing, affiliate links, or competitor promotion.

### Search trend and keyword tools

Best for:

- Relative demand direction.
- Seasonality.
- Comparing terms.

Watch for:

- Index values instead of absolute volume.
- Low-volume queries hidden or rounded.
- Ambiguous keywords with multiple meanings.

## Rules for numbers

- Always cite the exact source and date for market size, pricing, traffic, search volume, or ad cost numbers.
- State the geography, audience, and time period.
- If sources disagree, show a range and explain why.
- Do not average incompatible numbers.
- If only weak estimates exist, label them as directional.

## Red flags

Do not present a claim as fact when:

- The source has no date and freshness matters.
- The number is copied across many blogs without an original source.
- A vendor compares itself to competitors without methodology.
- The claim depends on a private dataset not described enough to evaluate.
- The source is a single social post, forum comment, or review.

## Citation pattern

Use concise citations in the answer body and list links at the end:

```md
- Node.js 22 is the active LTS release line according to the official Node.js release schedule.

Sources:
- Node.js Release Working Group: https://github.com/nodejs/release
```

## Confidence language

Use explicit confidence labels:

- **High confidence**: multiple strong sources agree or an official source directly answers the question.
- **Medium confidence**: source quality is good, but data is incomplete, narrow, or one-sided.
- **Low confidence**: evidence is anecdotal, stale, or only indirectly related.
