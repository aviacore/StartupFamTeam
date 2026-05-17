# Research: Market research source map

Date checked: 2026-05-17
Requester / role: StartupFamTeam shared researcher baseline
Decision supported: Fast PM, CEO, Marketer, and BA research requests
Region / scope: Global public tools, with notes for country-specific checks

## Short answer

Use a layered approach: **Google Trends** for relative interest, **Keyword
Planner** for search-volume and ad-cost estimates, **ad libraries** for live
competitor positioning, **Reddit/TikTok/community sources** for user language,
and product directories/review sites for analogs. Treat all public signals as
proxies, not ground truth.

## When to use each source

| Question type | Fast source set | What it can answer | Main limitation |
| --- | --- | --- | --- |
| "Do people search for this problem?" | Google Trends, Google Ads Keyword Planner | Relative trend, keyword ideas, monthly search estimates, bid estimates | Trends is normalized 0-100, not absolute volume; Keyword Planner needs Google Ads setup and returns estimates. |
| "What words do users use?" | Reddit search/Reddit Pro Trends, TikTok Creative Center, Google autocomplete, competitor reviews | Pain-point language, feature requests, objections, niche vocabulary | Community posts overrepresent vocal users and may not reflect the whole market. |
| "Who are competitors?" | Google search, Product Hunt, G2/Capterra, app stores, GitHub, ad libraries | Direct/indirect analogs, positioning, pricing pages, launch patterns | Directories are incomplete and rankings can be biased by SEO, sponsorship, or review sampling. |
| "What ads are competitors running?" | Meta Ad Library, Google Ads Transparency Center, LinkedIn Ad Library, TikTok Creative Center | Creative angles, copy, offers, landing-page promises, channel usage | Most libraries do not show full spend or performance for normal commercial ads. |
| "How much might ads cost?" | Google Ads Keyword Planner, platform benchmark docs/tools, small test campaign | Bid estimates, search competition, rough CAC inputs | Forecasts depend on bid, budget, ad quality, targeting, seasonality, and market behavior. |

## Source facts and caveats

- Google Trends uses a sample of anonymized, categorized, aggregated Google
  searches. Google normalizes each data point by geography/time, then scales
  values from 0 to 100. Equal Trends scores in two regions do not imply equal
  search volume.
  ([Google Trends FAQ](https://support.google.com/trends/answer/4365533?hl=en))
- Google explicitly says Trends is not polling data and should be one data point
  among others before drawing conclusions.
  ([Google Trends FAQ](https://support.google.com/trends/answer/4365533?hl=en))
- Google Keyword Planner can discover new keyword ideas, estimate monthly
  searches, estimate costs, and forecast campaign performance. Google notes
  forecasts depend on bid, budget, ad quality, location targeting, product,
  abuse trends, customer behavior, and industry factors.
  ([Google Ads Keyword Planner help](https://support.google.com/google-ads/answer/7337243))
- Meta Ad Library is a searchable ad-transparency hub for ads across Meta
  technologies. It supports searching all active ads across Meta products; for
  social issue, election, or political ads, Meta provides extra information such
  as spend, reach, and funding entities and keeps those ads for seven years.
  ([Meta Ad Library tools](https://transparency.meta.com/researchtools/ad-library-tools/))
- Google Ads Transparency Center is the official Google interface for searching
  ads and advertisers shown on Google surfaces. It is useful for competitor
  creative discovery, but public details vary by advertiser, region, and ad type.
  ([Google Ads Transparency Center](https://adstransparency.google.com/))
- LinkedIn's Ad Library is public and searchable by company/advertiser name,
  payer name, keyword, country, and date range. It includes ads that ran after
  2023-06-01 and keeps ads for one year after their last impression.
  ([LinkedIn Help](https://www.linkedin.com/help/linkedin/answer/a1517918))
- TikTok Creative Center is a free public hub for trends, high-performing ad
  examples, keyword insights, creative patterns, and top products. TikTok says
  Top Ads can be filtered by region, industry, campaign objective, and more, and
  includes performance views such as engagement moments in videos.
  ([TikTok Creative Center](https://ads.tiktok.com/help/article/creative-center?lang=en),
  [TikTok Top Ads](https://ads.tiktok.com/help/article/top-ads?lang=en))
- Reddit Pro Trends lets businesses track keywords and phrases to see when,
  where, and how Reddit users discuss topics in real time. It is useful for
  community discovery and qualitative language, not a full-market measurement.
  ([Reddit Pro Trends launch](https://www.business.reddit.com/blog/reddit-pro-trends-launch))

## Fast workflows

### Demand signal check

1. Define 3-7 query variants: problem phrase, job-to-be-done phrase, product
   category, competitor names, and "how to" phrase.
2. Check Google Trends by target country and compare against a known baseline
   term to understand relative scale.
3. Check Keyword Planner for average monthly searches and bid ranges if Google
   Ads access is available.
4. Search Reddit, TikTok, YouTube, app stores, and review sites for recent user
   language and repeated pain points.
5. Report only directional confidence unless there is real volume data.

### Competitor scan

1. Search category terms, problem phrases, and "alternative to <known tool>".
2. Group findings into direct competitors, indirect substitutes, manual
   workarounds, and incumbent platforms.
3. For each competitor, capture: promise, audience, pricing, onboarding path,
   integrations, visible traction, and strongest/weakest positioning claim.
4. Check ad libraries for current copy and landing pages.
5. Finish with "where we can differentiate" and "where we need proof".

### Community scan

1. Search problem terms in Reddit, Discord/forum directories, Telegram/Slack
   directories where public, X/LinkedIn, YouTube comments, and niche forums.
2. Rank communities by recency, discussion quality, member count if visible,
   and whether people ask for recommendations or complain about current tools.
3. Capture exact user quotes only when public and safe to cite.
4. Separate organic user discussion from promotional posts.

### Ad-cost estimate

1. Use Keyword Planner for search terms: average monthly searches, competition,
   and bid estimates.
2. Use ad libraries to identify whether competitors are actively testing paid
   messaging in Google, Meta, LinkedIn, and TikTok.
3. If budget permits, recommend a small controlled campaign test instead of
   treating public estimates as CAC.
4. Report a range and the assumptions behind it; never present public planner
   estimates as guaranteed acquisition cost.

## Evidence quality scale

- High: primary source, official pricing/docs, direct product page, repeatable
  dataset, or campaign data owned by the team.
- Medium: public ad library, app-store/review data, visible community threads,
  search-volume estimates, reputable industry reports with methodology.
- Low: SEO blogs without methodology, anonymous social posts, scraped rankings,
  anecdotal founder claims, unsupported market-size numbers.

## Output checklist

- State the decision the research supports.
- Name date checked and region/scope.
- Distinguish facts, interpretation, and assumptions.
- Link sources inline.
- Include confidence and gaps.
- If exact data is not available, say so and use a clearly labeled proxy.

## Recommended next step

- For every concrete product idea, create a one-page "problem demand memo" using
  this source map: demand signals, competitors, communities, ad signals, and
  unknowns that require interviews or experiments.
