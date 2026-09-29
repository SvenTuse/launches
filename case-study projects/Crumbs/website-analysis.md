# Crumbs — Website Analysis

Research date: **September 27, 2026**. Supplied website: [crumbs.family](https://crumbs.family/).

## Evidence and access limits

The browser reached the bare homepage at **13:44:33 UTC**, the [www homepage](https://www.crumbs.family/) at **13:58:35 UTC**, and the [onboarding route](https://www.crumbs.family/en/connect) at **14:11:59 UTC**. All displayed Cloudflare **“Web server is down — Error code 521”**; the onboarding navigation initially timed out, and a subsequent browser observation confirmed the same 521 page. The rendered page shows a white/gray diagnostic layout with browser and Cloudflare marked Working and the host marked Error. This is Cloudflare’s design, not Crumbs’ product design.

Search-indexed HTML recovered the homepage, onboarding, terms and privacy pages. This recovers historical copy and exposed routes, not a working app session. No wallet was connected, no receipt was uploaded, and no reward was claimed. Screenshots of social creatives provide visual evidence of the intended interface/branding, but not a complete historical website rendering. Consequently live functionality, exact responsive layouts and animation behavior remain unverified.

## 1. Essence, product and narrative

**Indexed homepage reconstruction:** a consumer rewards landing page leading to an app. Its headline connects shopping with company exposure. Portfolio mockups show dollar holdings, merchant rows, review/history states and a wallet identifier. It advertises manual receipt/email verification, 31 companies, 120+ countries, and example rates: Costco 2%, Netflix 3%, Odeon 4%, e.l.f. 5%. Repeated Get started links and See how it works lead to `/en/connect`; See every brand links to `/en/brands`, whose indexed retrieval redirects to onboarding. A fee/buyback section promises 75% for CRUMBS buybacks and burns; a final pitch uses 1,000 crumbs per share, followed by a stock-price warning, abbreviated CA, Brands, Terms and Privacy links. These are advertised features and sample displays, not measured customer balances or independently verified availability. Source: [indexed homepage](https://www.crumbs.family/).

The account screenshots make the core consumer promise explicit: upload an eligible receipt, receive stock-token rewards after review, and keep using an existing card. The launch examples deliberately use recognizable retailers and tickers. The metaphor is easy to explain: a receipt normally thrown away becomes a small piece of financial exposure to the company bought from. “Crumbs” makes a small fractional reward feel natural; the recurring “Keep your receipts” instruction turns the metaphor into a simple action. Sources: [X-Flow.md](<D:/media/темки/крипто/kai's launches/case-study projects/Crumbs/X-Flow.md>) P01, P03, P05, P12 and P13.

There are two assets to distinguish. CRUMBS is the project’s own token, pitched through buybacks/burns; merchant stock tokens are the promised purchase rewards. Holding CRUMBS is not demonstrated to be the same as holding COST, AAPL or AMZN, and the provided materials do not establish that consumers must buy CRUMBS before submitting a receipt.

## 2. Functionality, in detail

### Public and onboarding surfaces

The indexed [connect page](https://www.crumbs.family/en/connect) exposes Crumbs beta branding, `en de fr` language options, a Get started button, and linked Terms/Privacy. It says proceeding accepts those documents. The deeper login modal, chain-switch prompt, authentication methods and navigation after sign-in were not observable in a live session. A route existing in an index is not proof the feature currently works.

### Receipt intake and review

Official X text supports photographed receipts and forwarded order confirmations, with verification preceding reward delivery. The Amazon post explicitly promises 2% on eligible September 2026 purchases; P13 excludes purchases outside September 2026. The humorous dog-review image exposes a merchant/ticker, amount, receipt date, shortened wallet, payout field and Approve/Reject controls. This appears to visualize an administrative review screen; it does not establish that public users have approval privileges or that these are live controls. Sources: [X-Flow.md](<D:/media/темки/крипто/kai's launches/case-study projects/Crumbs/X-Flow.md>) P03, P04, P12 and P13.

The [indexed Terms](https://www.crumbs.family/en/terms), dated September 8, 2026, describe person-by-person review and rejection of unreadable, reused, unsupported or apparently non-owned receipts. They say stock is paid to a user-controlled wallet, keys are not held by Crumbs, rates/eligible brands may change, and abusive accounts or the service can be closed. They define 1,000 crumbs as one whole token, whereas the landing pitch calls it one share; neither should be confused with a redemption promise for the CRUMBS utility token. No guaranteed value, return or permanent brand support is promised.

### Merchant rewards and expansion

The social UI render shows a grid of merchants and reward labels; Amazon gets its own notification-focused post. McDonald’s/MCD, Starbucks/SBUX, Nike/NKE and Walmart/WMT are announced for “tomorrow” in the Sep 9 capture, making this a proposed Sep 10 addition rather than a verified deployment. Actual eligible merchants, token availability and delivered payouts could not be tested. Company logos and tagged handles demonstrate marketing examples, not commercial agreements. Sources: [X-Flow.md](<D:/media/темки/крипто/kai's launches/case-study projects/Crumbs/X-Flow.md>) P05, P08 and P12.

### Token economics and transparency

The fee-funded buyback/burn claim and 3% burn announcement provide the proposed token-demand loop. The only captured transaction identifier is `0xc29216862c943e42228c9206bf2c7f35e48be511a8f2ff2e129eab445dc24001` in P11; it was not decoded against an explorer. No verified fee rate, treasury balance, reward-funding breakdown, executed buyback amount or accounting for the remaining 25% is available. A burn can reduce a quoted supply metric without proving customer revenue or a sustainable reward business. Sources: [X-Flow.md](<D:/media/темки/крипто/kai's launches/case-study projects/Crumbs/X-Flow.md>) P05, P10 and P11.

### Privacy and implementation clues

The [indexed Privacy page](https://www.crumbs.family/en/privacy), dated September 8, 2026, names **Privy** for sign-in. It says the app stores wallet addresses, optional sign-in email and claim brand/date/amount/decision; reviewers see submitted receipts and hosting/database providers store app data. It describes a random-token sign-in cookie lasting 30 days, no advertising or analytics cookies, retention while an account exists, and options to request data or account deletion. These are policy statements, not a technical audit of collection or storage behavior. The policy also distinguishes deletion of app records from immutable public-chain payments.

### Stock-token wording

Crumbs’ “ownership” language needs qualification. [Robinhood’s own Stock Tokens page](https://robinhood.com/rhj/stocktokens/) describes its instruments as tokenized debt securities issued by Robinhood Assets (Jersey) Limited, providing economic exposure rather than legal or beneficial ownership rights in the underlying companies, with regional restrictions. This clarifies the asset category, but it does not verify that Crumbs procured or delivered those instruments. It also means broad accessibility slogans are insufficient evidence of eligibility for a particular consumer.

## 3. Design and branding

### Direct visual evidence: supplied social/product creatives

- **Palette:** white and pale mint backgrounds, lime highlights and dark forest-green identity text. Black is mainly used for the illuminated-device display; the dog-review mockup uses a brighter green action button. Transparent green discs and soft glows convey small digital rewards. These observations come from images, not extracted website CSS.
- **Typography:** the recurring lowercase crumbs wordmark has soft, rounded sans-serif forms; large marketing statements are sparse and easy to scan. The C is partially decomposed into small square pixels, creating a symbol that also works at avatar size. The exact typeface is not identifiable from the evidence.
- **Layout:** account creatives are centered in rounded rectangular image frames. P05 places a tilted phone in the center with reward labels around it; P12 puts a floating notification above a cropped phone; P04 places the uploaded image on the left and review details/actions on the right. This makes the product story understandable without explaining chain mechanics.
- **Recurring objects:** glossy green coins/discs, transparent notification panels, the black-screen lime device, familiar merchant logos and white/mint pixel mosaics. P08’s saturated red/green/black/blue merchant buttons break the green palette while retaining the glossy style.
- **Buttons and UI detail:** the review render visibly labels Approve and Reject; brand tiles and the phone screen suggest browsing supported companies. Exact click behavior cannot be established from a still image. The indexed site exposes action labels and routes, but their precise on-screen placement and dimensions were not inspected on the unavailable site.
- **Video formats:** two high-reach official explainer previews use a mint wordmark or short everyday-spending sentence. The launch preview establishes a 30-second player duration; the teaser’s 0:10 is only its displayed counter. Full motion, transitions, sound and the complete scripts were not reviewed.

Sources for these visual observations: [Screenshot_1.jpg](<D:/media/темки/крипто/kai's launches/case-study projects/Crumbs/x-posts/Screenshot_1.jpg>), [Screenshot_2.jpg](<D:/media/темки/крипто/kai's launches/case-study projects/Crumbs/x-posts/Screenshot_2.jpg>), [Screenshot_4.jpg](<D:/media/темки/крипто/kai's launches/case-study projects/Crumbs/x-posts/Screenshot_4.jpg>), [Screenshot_5.jpg](<D:/media/темки/крипто/kai's launches/case-study projects/Crumbs/x-posts/Screenshot_5.jpg>), [Screenshot_7.jpg](<D:/media/темки/крипто/kai's launches/case-study projects/Crumbs/x-posts/Screenshot_7.jpg>), [Screenshot_8.jpg](<D:/media/темки/крипто/kai's launches/case-study projects/Crumbs/x-posts/Screenshot_8.jpg>) and [Screenshot_16.jpg](<D:/media/темки/крипто/kai's launches/case-study projects/Crumbs/x-posts/Screenshot_16.jpg>).

### Branding conclusion and marketing role

The strongest observed design choice is consistency across avatar, banner, explainer previews, mobile renders, coins and thread-ending tiles. Green creates a consumer-finance association; the fragmented C gives the project a repeatable visual signature; familiar logos allow a reader to understand “shop here, get this stock token” quickly. Repetition across official posts and third-party creatives makes this a plausible recognition mechanism, although no controlled study isolates its effect on views or buying. Website copy and social imagery tell the same receipt-reward story; exact visual consistency between the historical rendered site and X cannot be fully confirmed while the site is down.

**Completion limit:** content, exposed routes, policy functionality and screenshot-supported design have been researched. Live app navigation, actual reward settlement, full desktop/mobile rendering and animations require a working website or historical page captures; they are explicitly unverified rather than filled in from imagination.
