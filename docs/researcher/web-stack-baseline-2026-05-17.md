# Research: Web MVP stack baseline

Date checked: 2026-05-17
Requester / role: StartupFamTeam shared researcher baseline
Decision supported: Fast default choices for a small web MVP
Region / scope: Global, public cloud/free-tier docs

## Short answer

Use **Node.js 24 LTS** for new production web work, keep **React 19** as the
current stable React baseline, and choose hosting by project shape: **Vercel**
for fastest Next.js path, **Cloudflare** when bandwidth/edge economics matter,
and **Netlify** for simple Git-based static/Jamstack projects.

## Key facts

- Node.js says production applications should use Active LTS or Maintenance LTS
  releases. As of the checked date, the Node.js releases page lists **v24
  Krypton** as LTS and **v22 Jod** as LTS, while **v26** is Current.
  ([Node.js releases](https://nodejs.org/about/releases/))
- The official Node.js release schedule shows **v24** entered LTS on
  2025-10-28, moves to Maintenance on 2026-10-20, and reaches end-of-life on
  2028-04-30. It shows **v22** reaches end-of-life on 2027-04-30.
  ([nodejs/Release schedule](https://raw.githubusercontent.com/nodejs/Release/main/schedule.json))
- React 19 is stable and available on npm. Major additions include Actions,
  `useActionState`, `useOptimistic`, `useFormStatus`, the `use` API, React DOM
  static APIs, Server Components support, Server Actions, `ref` as a prop,
  metadata tag support, stylesheet/script handling, resource preloading APIs,
  and improved hydration/error reporting.
  ([React 19 announcement](https://react.dev/blog/2024/12/05/react-19))
- Vercel Hobby is free and includes automatic CI/CD, global CDN, WAF, DDoS
  mitigation, 100 GB/month fast data transfer, 1M/month function invocations,
  4 CPU-hours/month, and 360 GB-hours/month provisioned memory. The Hobby docs
  state the plan is restricted to non-commercial, personal use only.
  ([Vercel pricing](https://vercel.com/pricing),
  [Vercel Hobby plan](https://vercel.com/docs/plans/hobby))
- Cloudflare Pages Free allows 500 builds/month, 100 custom domains per project,
  20,000 files/site, 25 MiB max single asset, and unlimited active preview
  deployments. Pages Functions are billed as Workers; Workers Free includes
  100,000 requests/day and 10 ms CPU time per invocation, and Cloudflare states
  there are no additional data transfer or bandwidth charges on the Workers Paid
  plan.
  ([Cloudflare Pages limits](https://developers.cloudflare.com/pages/platform/limits/),
  [Cloudflare Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/))
- Cloudflare's Next.js Pages guide separates static Next.js on Pages from
  full-stack server-side rendered Next.js, which it routes to the Next.js
  Workers guide. This means Cloudflare is a strong static/edge option, but
  SSR/full-stack Next.js needs framework-specific verification before choosing
  it as the default.
  ([Cloudflare Next.js Pages guide](https://developers.cloudflare.com/pages/framework-guides/nextjs/))
- Netlify Free is listed as "$0 forever" for individuals and includes 300
  credits, deploys from AI/Git/API, unlimited deploy previews, custom domains
  with SSL, Functions and AI models, database/blob storage, traffic rules/basic
  rate limiting, and global CDN.
  ([Netlify pricing](https://www.netlify.com/pricing/))

## Sources reviewed

| Source | Type | Relevant notes |
| --- | --- | --- |
| Node.js releases | Primary | Current status table and production guidance for LTS usage. |
| nodejs/Release schedule.json | Primary | Exact LTS, maintenance, and EOL dates by Node major version. |
| React 19 announcement | Primary | Stable release date and feature list from the React team. |
| Vercel pricing + Hobby docs | Primary | Free plan limits and non-commercial restriction. |
| Cloudflare Pages limits + Workers pricing | Primary | Free Pages limits and Workers/Pages Functions economics. |
| Cloudflare Next.js guide | Primary | Clarifies static Pages vs full-stack SSR Next.js deployment path. |
| Netlify pricing | Primary | Free-tier features and credit model. |

## Implications

- Product: For hackathon/MVP demos, Vercel is usually the fastest path for a
  Next.js app because Next.js support is native and deployment friction is low.
- Tech: Pin new Node work to Node.js 24 LTS unless an existing runtime,
  dependency, or platform forces Node.js 22 LTS.
- Marketing: Free hosting choices can support early demos, but Vercel Hobby's
  non-commercial restriction matters once the product is used commercially.
- Business: Cloudflare can be attractive for traffic-heavy static/edge workloads
  because its docs emphasize no additional data-transfer/bandwidth charges on
  Workers Paid and static asset requests are free/unlimited; verify dynamic
  Next.js requirements before committing.

## Practical default

1. Default runtime: Node.js 24 LTS.
2. Default frontend: React 19 through the framework's supported version.
3. Default deploy for a Next.js MVP: Vercel for personal/demo use; move to Pro
   or another provider before commercial usage.
4. Consider Cloudflare for static sites, edge-first apps, or bandwidth-sensitive
   workloads.
5. Consider Netlify for static/Jamstack sites where its credit model and
   workflow fit the project.

## Confidence and gaps

Confidence: medium-high.

Gaps:

- Free-tier limits and pricing can change; re-check official pricing pages
  before a production launch.
- This brief does not test a real Next.js app on each provider.
- Exact "best hosting" depends on whether the app needs SSR, image
  optimization, server actions, background jobs, database access, team
  collaboration, commercial usage, or high traffic.

## Recommended next step

- When the team picks a concrete MVP architecture, create a provider-specific
  deployment checklist and verify the target Next.js features against the chosen
  host's official docs.
