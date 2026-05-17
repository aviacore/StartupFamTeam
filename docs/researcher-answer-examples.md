# Researcher answer examples

These examples show the expected shape and level of detail for Researcher
responses. Replace placeholder facts with verified current sources before sending
an answer.

## Example: technical version check

```md
## Short answer

The current Node.js LTS line is `<version line>`. Use it for new backend or
Next.js work unless the framework or hosting provider requires a newer runtime.

## Findings

- Node.js lists `<version line>` as LTS in its official release schedule.
- `<hosting provider>` supports Node.js `<supported versions>` for deployments.
- `<framework>` requires Node.js `<minimum version>` according to official docs.

## Sources

- Node.js release schedule: <url>, accessed YYYY-MM-DD.
- Hosting runtime docs: <url>, accessed YYYY-MM-DD.
- Framework install/docs: <url>, accessed YYYY-MM-DD.

## Implications for StartupFamTeam

- Default new services to `<version line>`.
- Avoid older runtimes unless a dependency forces them.

## Confidence / gaps

- Confidence: High if official runtime, framework, and hosting docs agree.
- Recheck before implementation if the deployment target changes.
```

## Example: technical comparison

```md
## Short answer

For a small Next.js + Postgres MVP, choose `<option>` if the priority is
`<priority>`. Choose `<other option>` if the priority is `<other priority>`.

## Findings

| Option | Best for | Strengths | Risks / limits | Sources |
| --- | --- | --- | --- | --- |
| Prisma | Teams wanting mature ORM ergonomics | Schema workflow, migrations, ecosystem | Runtime/client complexity, abstraction overhead | Official docs, pricing/docs, community issues |
| Drizzle | Teams wanting SQL-like TypeScript control | Lightweight, explicit SQL model, type safety | More manual patterns, smaller ecosystem in some areas | Official docs, examples, GitHub |

## Implications for StartupFamTeam

- Pick the option that reduces implementation risk for the assigned developer.
- Revisit if the project needs complex migrations, multi-tenant data, or edge
  runtime support.

## Confidence / gaps

- Confidence: Medium until checked against the exact deployment runtime and
  database provider.
```

## Example: competitor scan

```md
## Short answer

The closest competitors appear to be `<competitor A>`, `<competitor B>`, and
`<competitor C>`. They differ mostly by target user, workflow depth, and pricing
model.

## Findings

| Competitor | Target audience | Positioning | Pricing model | Differentiation notes | Sources |
| --- | --- | --- | --- | --- | --- |
| A | ... | ... | ... | ... | Official site/pricing |
| B | ... | ... | ... | ... | Official site/pricing |
| C | ... | ... | ... | ... | Official site/pricing |

## Implications for StartupFamTeam

- Position around the gap that competitors underserve.
- Avoid claims that cannot be supported by competitor public pages.

## Confidence / gaps

- Confidence: Medium if based on public positioning only.
- Gap: traction and revenue usually require third-party or paid data.
```

## Example: market pain-point research

```md
## Short answer

Users currently solve `<problem>` with a mix of `<workaround A>`,
`<workaround B>`, and `<tool category C>`. The repeated pain points are
`<pain 1>`, `<pain 2>`, and `<pain 3>`.

## Findings

- Community thread/review examples show users describing `<pain 1>`.
- Product reviews mention `<pain 2>` when using `<tool category>`.
- Existing tools solve part of the workflow but leave `<gap>`.

## Sources

- Community thread or review: <url>, accessed YYYY-MM-DD.
- Product review/listing: <url>, accessed YYYY-MM-DD.
- Vendor docs or landing page: <url>, accessed YYYY-MM-DD.

## Implications for StartupFamTeam

- Use user language from sourced examples in problem statements.
- Validate whether the pain is frequent enough before building a full feature.

## Confidence / gaps

- Confidence: Low to Medium unless backed by many independent examples.
- Gap: community posts show pain, not market size.
```

## Example: channel cost research

```md
## Short answer

`<channel>` can fit `<audience>` if the team can measure `<conversion event>`.
Public cost data is limited, so use the available benchmark as a planning proxy,
not a forecast.

## Findings

- Official platform docs confirm targeting options for `<audience/interest>`.
- Public benchmark reports estimate `<cost metric>` around `<range>`.
- The channel requires `<creative or tracking constraint>`.

## Sources

- Platform advertising docs: <url>, accessed YYYY-MM-DD.
- Benchmark source with methodology: <url>, accessed YYYY-MM-DD.
- Tracking/measurement docs: <url>, accessed YYYY-MM-DD.

## Implications for StartupFamTeam

- Start with a small test budget only after tracking is in place.
- Treat benchmark cost ranges as assumptions for BA, not guaranteed CAC.

## Confidence / gaps

- Confidence: Medium if benchmark methodology is visible; Low if only listicles
  are available.
```
