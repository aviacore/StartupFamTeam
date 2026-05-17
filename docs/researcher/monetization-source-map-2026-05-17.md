# Research: Monetization and business-model source map

Date checked: 2026-05-17
Requester / role: StartupFamTeam Business Analyst / CEO baseline
Decision supported: Choose and validate monetization assumptions for an MVP
Region / scope: Global digital products, with examples from US/EU payment and
app-store docs

## Short answer

For a digital MVP, start by mapping the product to one of five practical
monetization models: **subscription**, **usage-based**, **one-time purchase**,
**marketplace/transaction fee**, or **ads/sponsorship**. Validate each model
against payment fees, platform rules, customer willingness to pay, and channel
acquisition cost. Do not use generic "market average" numbers unless the source
and methodology are clear.

## Core model options

| Model | Best fit | What to verify first | Common risk |
| --- | --- | --- | --- |
| Flat subscription | Recurring access to SaaS, content, or tools | Churn risk, renewal value, payment failure handling | Users do not see repeated value after first use. |
| Per-seat subscription | Team tools and B2B software | Buyer/user split, seat expansion path, admin controls | Small teams resist per-seat pricing early. |
| Usage-based | API, AI, infrastructure, data, automation | Metering accuracy, margin per unit, abuse controls | Costs scale faster than revenue if metering is wrong. |
| One-time purchase | Utility apps, templates, paid downloads | Refund policy, support burden, update expectations | Weak recurring revenue and harder retention. |
| Marketplace/transaction fee | Matching buyers/sellers or processing payments | Take rate, payout flow, compliance, dispute handling | Liquidity problem: no value until both sides exist. |
| Ads/sponsorship | Content/community products with attention | Traffic quality, ad inventory, brand safety | Requires scale before meaningful revenue. |

## Source facts and caveats

- Stripe lists standard US online card pricing as **2.9% + 30 cents** per
  successful domestic-card transaction, with extra fees for manually entered
  cards, international cards, and currency conversion. Stripe also states that
  standard pricing has no setup fees, monthly fees, or hidden fees.
  ([Stripe US pricing](https://stripe.com/en-US/pricing))
- Stripe Billing supports recurring subscriptions and subscription lifecycle
  handling, including trials, prorations, customer self-service management,
  invoicing, revenue recovery, reporting, and subscription statuses.
  ([Stripe subscriptions overview](https://docs.stripe.com/billing/subscriptions/overview))
- Stripe's recurring pricing-model docs list flat rate, per-seat, tiered, and
  usage-based pricing. Usage-based pricing includes fixed fee plus overage,
  pay-as-you-go, and credit burndown.
  ([Stripe pricing models](https://docs.stripe.com/products-prices/pricing-models.md),
  [Stripe usage-based billing](https://docs.stripe.com/billing/subscriptions/usage-based))
- Apple describes App Store business models as Free, Freemium, Paid, and
  Paymium. Freemium can include consumable purchases, non-consumable purchases,
  auto-renewable subscriptions, and non-renewing subscriptions.
  ([Apple business models](https://developer.apple.com/app-store/business-models/))
- Apple's App Store Small Business Program offers a reduced **15% commission**
  on paid apps and in-app purchases for eligible developers. Existing developers
  who made up to **$1M USD** in prior-calendar-year proceeds, and new developers,
  can qualify; surpassing the threshold makes the standard commission apply to
  future sales.
  ([Apple Small Business Program](https://developer.apple.com/app-store/small-business-program/))
- Google Play states that apps and in-app products sold through Google Play's
  billing system are subject to a service fee. Its overview says 97% of
  developers distribute at no charge, and among developers subject to a service
  fee, 99% are eligible for 15% or less through programs. The table lists 15%
  for the first $1M annual revenue, 30% above $1M, and 15% for automatically
  renewing subscriptions regardless of annual revenue.
  ([Google Play service fees](https://support.google.com/googleplay/android-developer/answer/112622?hl=en))
- For ad-cost research, use the market source map in this folder. Keyword
  Planner gives search-volume and cost estimates, but Google notes campaign
  performance depends on bid, budget, ad quality, location targeting, product,
  abuse trends, customer behavior, and industry factors.
  ([Market research source map](./market-research-source-map-2026-05-17.md))

## Fast workflow: business-model research

1. Define the customer and buyer separately.
   - Who uses the product?
   - Who approves payment?
   - Is payment individual, team, company, or marketplace-side?
2. List 5-10 direct and indirect competitors.
   - Capture pricing page, free tier, trial, billing interval, usage limits,
     and enterprise/contact-sales path.
3. Classify each competitor's model.
   - Subscription, freemium, usage-based, marketplace take rate, ads,
     services, hardware, data/API, or hybrid.
4. Estimate gross revenue mechanics.
   - Price point, billing frequency, expected conversion, payment/platform
     fees, refunds/chargebacks, taxes, support cost, and infrastructure cost.
5. Identify platform constraints.
   - App-store commission, in-app purchase rules, marketplace payout rules,
     payment processor availability by country, tax/VAT obligations.
6. State confidence and gaps.
   - Public pricing pages show list prices, not discounts, churn, margin, or
     actual willingness to pay.

## Fast workflow: pricing-page teardown

For every competitor, capture:

- Plans and price points.
- Free tier/trial terms.
- Included usage or seats.
- Overage model.
- Annual discount.
- Add-ons.
- Enterprise/contact-sales triggers.
- Refund/cancellation language.
- Payment methods and currencies.
- Hidden constraints such as fair-use, non-commercial, or platform-specific
  limits.

## Unit-economics checklist

Minimum inputs for a lightweight BA memo:

- Revenue: price, billing interval, conversion rate, expected expansion.
- Direct costs: payment fee, platform fee, compute/API cost, support cost,
  refunds, chargebacks, tax tooling if applicable.
- Acquisition: channel, estimated CPC/CPM/CPA, conversion assumptions.
- Retention: churn assumption, renewal trigger, value metric.
- Risk: compliance, marketplace rules, platform dependency, abuse/fraud.

## Evidence quality scale

- High: official pricing pages, developer terms, payment processor docs,
  app-store policies, own campaign/payment data.
- Medium: competitor pricing pages, public reviews, marketplace listings,
  ad-library observations, reputable benchmark reports with methodology.
- Low: unsourced "average CAC" blog posts, scraped estimates, social claims,
  old pricing screenshots, market-size numbers without methodology.

## Practical defaults for StartupFamTeam

- If the MVP is B2B SaaS: start with simple subscription or per-seat pricing,
  then validate willingness to pay in interviews before adding complex usage
  pricing.
- If the MVP uses AI/API costs: include usage limits from day one, even if the
  first public plan is flat-rate.
- If the MVP is mobile-first and sells digital goods: check Apple/Google billing
  rules and service fees before designing pricing.
- If the MVP is a marketplace: model liquidity and payout/compliance costs
  before optimizing take rate.
- If data is missing: report ranges and assumptions; do not present a single
  CAC, LTV, or margin number as fact.

## Recommended next step

- For each product idea, create a one-page monetization memo with: target
  customer, proposed model, competitor pricing table, payment/platform fees,
  unit-economics assumptions, and the one experiment needed to validate
  willingness to pay.
