# Research sample: free hosting for a Next.js MVP

Date checked: 2026-05-17

## Question

Which free hosting option is best for a Next.js MVP?

## Short answer

For a **non-commercial demo, portfolio, or hackathon prototype**, use
**Vercel Hobby** first. It is the smoothest default for Next.js because the
platform is built around Next.js deployment workflows, and the free tier includes
automatic CI/CD, CDN, Vercel Functions, ISR, image optimization, and common app
delivery features.

For a **startup/commercial MVP that must stay at $0**, do not rely on Vercel
Hobby: Vercel's fair use docs restrict Hobby teams to non-commercial personal
use only. Evaluate **Netlify Free** for a managed Next.js experience or
**Cloudflare Workers/Pages Free** if the team is comfortable with OpenNext and
Cloudflare runtime constraints.

## Comparison

| Option | Free-plan fit | Next.js support | Main risk |
| --- | --- | --- | --- |
| Vercel Hobby | Best for personal/non-commercial prototypes | Strongest default Next.js deployment experience; pricing page includes Functions, ISR, image optimization, CDN, CI/CD | Hobby is non-commercial only; commercial startup use requires Pro/Enterprise |
| Netlify Free | Good for small MVPs within credit limits | Official docs say Netlify supports major Next.js features via OpenNext adapter with zero configuration | Credit model can be less intuitive; free allowance is finite |
| Cloudflare Workers/Pages Free | Best free limits for edge/static-heavy apps and Cloudflare-native stacks | Full-stack Next.js runs on Workers via Cloudflare OpenNext adapter; static Next.js can use Pages | More adapter/runtime complexity than Vercel; Node.js middleware not fully supported |

## Facts and sources

- Vercel pricing lists the **Hobby** plan as free and includes automatic CI/CD,
  global CDN, Vercel Functions, ISR, image optimization, environment variables,
  and unlimited deployments. It also lists typical Hobby allowances such as
  100 GB/month Fast Data Transfer, 1M/month Edge Requests, 1M/month Function
  invocations, and 5K/month image transformations.
  Source: <https://vercel.com/pricing>
- Vercel fair use docs say **Hobby teams are restricted to non-commercial
  personal use only**, and commercial usage requires Pro or Enterprise.
  Source: <https://vercel.com/docs/pricing/fair-use-policy>
- Netlify pricing lists a **Free** plan with a 300 credit limit, deploys from
  AI/Git/API, unlimited deploy previews, custom domains with SSL, Functions,
  Netlify Database, Blob storage, basic firewall/rate limiting, and global CDN.
  Source: <https://www.netlify.com/pricing/>
- Netlify Next.js docs say Netlify supports major Next.js features with zero
  configuration through the open-source OpenNext adapter, including App Router,
  SSR, ISR, SSG, React Server Components, Server Actions, middleware, route
  handlers, image optimization, redirects/rewrites, and more.
  Source: <https://docs.netlify.com/build/frameworks/framework-setup-guides/nextjs/overview/>
- Cloudflare Pages Free limits include 500 builds/month, 1 build at a time,
  100 custom domains per Pages project, 20,000 files per site, and unlimited
  active preview deployments.
  Source: <https://developers.cloudflare.com/pages/platform/limits/>
- Cloudflare Pages docs direct full-stack SSR Next.js apps to the Workers
  Next.js guide, while static Next.js sites can use Pages.
  Source: <https://developers.cloudflare.com/pages/framework-guides/nextjs/>
- Cloudflare Workers Next.js docs say Next.js apps can be deployed to Workers
  using the OpenNext adapter, with support for App Router, Pages Router, Route
  Handlers, React Server Components, SSG, SSR, ISR, Server Actions, streaming,
  middleware, and image optimization via Cloudflare Images. Node.js in
  Middleware is listed as not yet supported.
  Source: <https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/>
- Cloudflare Workers pricing says the Free plan includes 100,000 Worker
  requests/day, 10 ms CPU time per invocation, and that requests to static
  assets are free and unlimited.
  Source: <https://developers.cloudflare.com/workers/platform/pricing/>

## Recommendation by scenario

- **Fastest personal demo:** Vercel Hobby.
- **Startup landing page or simple commercial MVP at $0:** Netlify Free or
  Cloudflare Pages/Workers Free, depending on runtime needs.
- **Static/exported Next.js site:** Cloudflare Pages is attractive because
  static asset requests are free/unlimited and Pages has generous build/domain
  limits.
- **Full-stack Next.js with SSR, Server Actions, ISR:** Vercel is easiest, but
  for commercial use budget for Pro. If $0 is required, compare Netlify Free and
  Cloudflare Workers with a small proof deploy.
- **Cloudflare-native stack or D1/Workers/KV needs:** Cloudflare Workers.

## Implications for StartupFamTeam

- Do not pick "free Vercel" as the default for a commercial startup MVP unless
  the project is clearly non-commercial; budget for Vercel Pro if choosing
  Vercel for production/commercial use.
- For a hackathon demo, Vercel remains the fastest low-friction choice.
- If the team wants a $0 commercial path, create a minimal deploy on Netlify and
  Cloudflare before committing to framework features that may behave differently
  across adapters.
- Decide hosting before choosing database/ORM edge assumptions; Cloudflare,
  Netlify, and Vercel have different runtime and adapter constraints.

## Limits / unknowns

- Pricing and free limits change frequently; re-check official pages before
  making a launch decision.
- This sample does not run a real deployment test for the target app.
- It does not compare paid tiers beyond noting that Vercel commercial use
  requires Pro or Enterprise.

Confidence: medium-high

Why: based on official pricing, fair-use, platform-limit, and Next.js support
docs. Actual fit still depends on the app's runtime features and commercial use
case.

What would improve confidence: deploying the actual app to each candidate and
recording build output, runtime behavior, and usage estimates.
