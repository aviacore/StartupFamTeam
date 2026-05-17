# Research answer examples

These examples show the expected shape of fast Researcher/BA responses. They are
format examples, not final live research. Before sending a real answer, verify
current facts, pricing, limits, and release status from the sources listed in
`docs/research-source-catalog.md`.

## Example: technical version question

```markdown
## Short answer

Use the current active LTS line unless the project has a specific dependency
that requires another version. Verify the exact LTS line on the Node.js release
schedule before implementation.

## Facts and sources

- Node.js publishes release lines, LTS dates, and end-of-life dates in the
  official release schedule:
  https://github.com/nodejs/release#release-schedule
- The public Node.js website lists current download options:
  https://nodejs.org/en

## Implications

- For production defaults, prefer active LTS over Current releases.
- Check hosting/runtime support before pinning the version.

## Recommendation / next step

Pin the active LTS major version in `.nvmrc`, package `engines`, and deployment
settings after verifying the current schedule.
```

## Example: tool comparison

```markdown
## Short answer

For a hackathon MVP, choose the tool that best matches the team's existing
stack and migration comfort. If the team already knows Prisma, default to
Prisma; if it wants lightweight SQL-first TypeScript, evaluate Drizzle.

## Facts and sources

- Prisma documentation: https://www.prisma.io/docs
- Prisma pricing: https://www.prisma.io/pricing
- Drizzle documentation: https://orm.drizzle.team/docs
- Drizzle project site: https://orm.drizzle.team

## Comparison

| Criterion | Prisma | Drizzle | Notes |
| --- | --- | --- | --- |
| Developer experience | Schema-first ORM with generated client | SQL-like TypeScript query builder/ORM | Verify current feature set |
| Migration flow | Prisma Migrate | Drizzle migrations | Compare against project workflow |
| Ecosystem | Large ecosystem and docs | Smaller, lightweight ecosystem | Use current package stats only as secondary evidence |
| MVP risk | Lower if team already knows Prisma | Lower if team prefers SQL-first control | Team familiarity matters most |

## Recommendation / next step

Pick one default for the MVP, then create a tiny proof-of-concept with one
model, one migration, and one query before committing the whole codebase.
```

## Example: competitor scan

```markdown
## Short answer

There are likely direct competitors, indirect workflow substitutes, and manual
workarounds. Separate them before deciding positioning.

## Facts and sources

- Product Hunt can surface recently launched alternatives:
  https://www.producthunt.com
- G2 and Capterra can show established B2B categories:
  https://www.g2.com
  https://www.capterra.com
- AlternativeTo can reveal user-perceived substitutes:
  https://alternativeto.net

## Implications

- Direct competitors define feature expectations.
- Indirect competitors reveal the user's current workflow.
- Manual workarounds reveal what users may already accept without paying.

## Recommendation / next step

Build a table with direct competitors, indirect substitutes, target segment,
pricing, main promise, and visible traction signals. Do not treat launch-site
likes or community comments as market size.
```

## Example: BA channel cost answer

```markdown
## Short answer

Paid channel costs vary heavily by geography, audience, and creative quality.
Use benchmark ranges only to create a sensitivity model, then validate with a
small test or platform estimator.

## Facts and sources

- Platform help centers and ad tools are the primary sources for available
  objectives, targeting, and billing mechanics.
- Benchmark reports from agencies or ad-tech vendors can provide directional
  CPC/CPM ranges, but they are estimates and may not match a new account.

## Working model

Variables:

- CPM or CPC
- Landing-page conversion rate
- Signup-to-paid conversion rate
- Average revenue per paying customer
- Gross margin

Formula:

    CAC = ad spend / paying customers
    Payback period = CAC / monthly gross profit per customer

## Recommendation / next step

Create low/base/high cases and define the maximum CAC the business can tolerate
before running paid acquisition. If the model only works with optimistic
conversion rates, start with organic/community channels first.
```

## Example: trend question

```markdown
## Short answer

Use Google Trends for relative interest, not exact search volume. If exact
volume matters, combine it with a keyword tool and state the geography,
language, and date range.

## Facts and sources

- Google Trends reports indexed relative search interest:
  https://trends.google.com/trends
- Keyword planners/tools estimate absolute volume and paid competition, but
  methods vary by tool.

## Implications

- A rising trend can support timing, but it does not prove willingness to pay.
- Low volume can still be acceptable for niche B2B if deal size is high.

## Recommendation / next step

Report trend direction, region, related queries, and the exact query terms used.
Add a caveat when volume is unavailable or estimated.
```
