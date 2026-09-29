# Touch Grass — website analysis

Research date: **27 September 2026, Europe/Moscow**. Site: [touchgrass.family](https://www.touchgrass.family/). Identity was checked against the supplied overview, the Sep 3 launch screenshot and the site's footer contract link: **0x16391c40e85fb2246a2c8c17bfa2594c5d3ef84b**.

This is a browser-based inspection of publicly accessible pages and controls. Map, navigation, prices and published status labels were observed. Authenticated catching, location/camera checks, wallet creation, receipts, payments, withdrawals and Android installation were not exercised. Descriptions of their internal behavior are attributed to the project's published documentation, not an audit or an end-to-end transaction test.

## 1. Essence, product and narrative

The site combines a promotional landing page with a functioning public map interface. Its story turns familiar company brands into outdoor loot: discover a nearby marker, walk there, and collect a token with stock-price exposure. The landing page makes the location-to-company relationship immediately understandable, then routes visitors into the app, Android distribution and documentation. The collectible inventory, rarity hierarchy and rare events give the concept a recognizable game structure. A second audience is local venues, which can fund rewards to attract physical visitors. [Homepage](https://www.touchgrass.family/)

The strongest framing is “Pokémon GO for stocks,” independently visible in the supplied mentions and quoted user demo. The meme “touch grass” adds humor and an instruction the user can act on. The product moves from a single stock-hunting idea toward proof of physical presence for venue rewards, visits, reviews and receipts. The latter features have conflicting delivery states, addressed below.

The consumer promise and the token's purpose should be separated. GRASS is the project token; the loot consists of other stock tokens or sponsored rewards. The launch screenshots describe token holding gates, fee-funded replenishment and buybacks. Calling the loot equity or literal company ownership overstates what stock tokens confer; the official issuer's documentation is discussed in [other-info.md](other-info.md).

## 2. Technical functionality and observed availability

### Public app and map

The [web app](https://www.touchgrass.family/app) rendered a large navigable map beside a city/drop sidebar. Public controls included Map, Profile, Leaderboard, Legendary, Shop, Receipts, Sponsor, Proof, a language picker, sign-in and location enablement. Additional sidebar tabs were Drops, Vault, You and Friends. The language picker offered English, Japanese, Korean, Simplified Chinese, Thai, Vietnamese, Indonesian and Hindi.

The map displayed clustered company icons, numeric cluster counts, city labels, zoom controls, a four-level rarity legend and World/Near me controls. At inspection it advertised **164 cities and 864 spawn points**. A city search accepted “Paris”; the captured state did not establish that the full city list actually filtered. Sign-in and enabled location were both shown as necessary before a catch. No user location was disclosed.

Live UI values changed: the shared hourly payout factor displayed 7% on the homepage and later 15% in the app. These are time-dependent snapshots, not fixed rewards. The app's small rule line showed **60 m, one every 2 h, 3 a day**, which conflicts with some documentation and shop copy.

The [public leaderboard](https://www.touchgrass.family/app/board) also loaded without sign-in. It shows weekly/all-time tabs, a closing countdown, ranked profiles, catch counts, cities and companies, and the $150/$100/$50 prize schedule. It describes a ten-catch eligibility threshold, ties sharing prizes, and five distinct catch days plus a public profile for ranking. Prior winners are labelled paid, but those labels were not independently reconciled to transfers.

### Claim architecture, according to documentation

Published architecture has a spawn registry, a server that verifies a claim and signs a voucher, and a funded ERC-20 vault. The voucher binds recipient, token, amount, spawn identifier, single-use nonce and a 15-minute deadline. EIP-712 domain separation prevents reuse across vaults; tokens go to the named recipient even if someone relays the claim. The docs describe owner powers to rotate the signer, pause, withdraw and transfer ownership. Thus the payout vault has administrative controls; an ownerless buyback claim does not imply every contract is ownerless.

The docs describe GPS accuracy and trail checks, movement and travel consistency, network/device limits, live door-camera frames, email checks, wallet history and a refundable GRASS deposit. Their claim radius scales with reported position error. Device attestation is described as future work despite the homepage implying it is already used. These mechanisms were not tested. [Technical docs](https://www.touchgrass.family/docs)

### Reserves, payouts and token-fee accounting

The [proof page](https://www.touchgrass.family/proof) visibly displayed **53,591 settled payouts**, **34,562 distinct wallets paid**, and **8 stock types**, through block **73,409,893**. It listed recent payout rows with token, amount, age, place, walker, block and transaction links, and provided an explorer route and a query example. The site itself says wallets are not people. These are figures rendered by the project; an independent complete chain recount was not performed.

It also displayed approximately **17,684,291 GRASS destroyed**, **982,315,709 remaining supply** and **29.5459 ETH spent on buybacks**. Published trading-fee allocations are 37.5% buyback/burn, 37.5% stock treasury and 25% team. These are shares of fee receipts, not percentages of trading volume. The separate buyback and treasury addresses help distinguish funding destinations. An explorer URL was reached, but its text extraction returned no usable content; source-code/security claims remain unverified.

### Sponsorship

The [sponsor page](https://www.touchgrass.family/sponsor) exposes a four-stage form: Where, What, Budget and The Pin. The visible opening fields request a place and town/city. It advertises stock-funded campaigns, own-token campaigns on Robinhood Chain or Solana, and venue-served rewards. Sponsoring checks a **10,000-GRASS holding**, described as retained by the sponsor. Stock budgets range from **$10 to $2,000**, with a **20% daily spending ceiling** and a **14-day campaign**; refunds require contacting the operator.

At inspection it listed two running doors: a PFWA token campaign in California and a funded campaign in Oslo. The homepage displayed two doors, two towns and **$3.41 already distributed**. That is reward spend shown for currently displayed campaigns, not total historical sponsorship revenue. The page says stock funding passes through to the treasury without a markup; sponsor deposits therefore cannot automatically be counted as platform profit.

### Shop

The [shop](https://www.touchgrass.family/shop) rendered three products with sign-in-to-buy buttons: **The Alarm ($4)** wakes a dormant door while consuming an existing catch; **Second Wind ($15)** shortens spacing from two hours to 30 minutes for the day; **One More ($10)** adds a seventh catch to the stated base six. At inspection, illustrative quotes were 2,070, 9,200 and 5,960 GRASS respectively, each plus 0.0003 ETH; quotes are variable, not fixed token prices.

The page says prices are dollar-denominated, converted using the pool, with quotes held for 15 minutes after Buy. It describes halves allocated to burn and the shop wallet, and links a shop contract/wallet. No purchase was initiated. Sep 10's screenshot advertised 12 catches/day and a sponsored-door product, demonstrating that the visible offering has changed.

### Distribution

The [download page](https://www.touchgrass.family/download) offers a direct Android APK, version **1.3.0**, **184 MB**, package **family.touchgrass.app**, for **Android 7.0+**. It describes foreground location use and OAuth sign-in. iOS remains **coming soon**; the page points iPhone users to the browser app. Android availability is therefore a direct-download claim, not evidence of a Google Play listing. The file was not downloaded, installed or analyzed. The page also describes account splitting if different providers are used, with no account merge.

### Roadmap, reviews and receipts

The [roadmap](https://www.touchgrass.family/roadmap) uses explicit states: live, built but switched off, building, next, open question and not planned. Android and Asia are labelled live; iOS is building. Reviews/stickers and receipt NFTs are labelled building or disabled, despite Sep 12 and Sep 23 posts calling features live. The roadmap also says a Solana funding rail is built but switched off, while sponsor copy and Sep 8 posts present Solana support as live. This may reflect different flows or stale pages; deployment flags were not verified.

Receipt descriptions include ERC-721 minting, fingerprint deduplication, camera capture, arithmetic checks and initial human review. Review features require an in-person shopkeeper interaction. These are published descriptions, not demonstrated production features.

### Privacy, support and operator identity

The [privacy page](https://www.touchgrass.family/privacy) identifies Privy for identity/wallets, Vercel hosting, Upstash Redis storage, Expo app updates and OpenFreeMap tiles. It describes limited location collection during catching and acknowledges the operator's legal name and postal address are not yet published. These disclosures are evidence of what the project says, not an independently verified dependency inventory.

The [terms](https://www.touchgrass.family/terms) say the company is being formed and users currently contract with the individual operator. [Support](https://www.touchgrass.family/support) offers human email support and a 72-hour target for contested catch refusals. The account screenshots also discuss new support arrangements and incorporation in progress.

## 3. Design and branding

### First screen

The desktop hero fills the viewport with a saturated blue sky fading into a much paler horizon, large soft white clouds and floating company-logo cubes. Enormous inflated lime TOUCH GRASS lettering sits centrally; the tiny TG mark is at top left. The hero artwork has glossy highlights, soft surfaces and depth, resembling a toy, balloon or collectible. Familiar logos sit on black, orange, red and green rounded cubes.

A translucent rounded navigation capsule stretches across the upper center. Its uppercase, widely spaced labels are compact and dark; the selected item sits on a white pill. A separate bright lime Open App button is at top right. The lower hero contains a concise white value proposition, an italic serif accent in the copy, and a horizontal action row: lime Open the App, then pale Android, Docs and X buttons. The map begins before the user finishes the first screen, making the product visible immediately.

### Sections and interactions

Information pages retain the sky/cloud scene, TG mark and capsule navigation. Their headlines pair a bold sans-serif statement with a lighter italic serif phrase. Large translucent white panels use generous padding, rounded corners and subtle pale borders; dark body text provides a practical counterweight to the playful artwork. Shop cards place the product name, duration and dollar price close together, followed by effect copy and a sign-in action.

The app uses a roughly two-thirds-width map on the left and a narrow panel on the right. The panel stacks prominent lime sign-in/location buttons, segmented tabs, search and rounded city rows. Cluster markers combine company icons and a lime count badge. Rarity uses small distinct dots rather than changing the whole interface's color. This keeps both the token story and the physical place legible.

Navigation, FAQ expansion, map controls and typed city input responded at the interface level. The live map data, payout factor and event countdown provide changing content. Still screenshots establish the floating visual composition but do not establish a specific video, scroll animation or animation duration; those details were not independently timed. Mobile responsive layouts were not tested.

### Creative consistency with X

The same lime inflated typography, sky, brand cubes and city scenes recur in the supplied X artwork. A user seeing the avatar, a MIAMI/ASIA/102/75% post and the website can recognize one identity. Each creative generally communicates a single noun or number. The clear recipe is a real place plus an oversized branded object plus one message. Its value is recognizability and instant comprehension; the research does not establish whether the artwork was AI-generated.

Humor appears in both brand voice and product instructions. Outdoor movement, familiar companies and simple verbs make the pitch accessible without requiring the reader to understand contract architecture first. The public proof page then serves visitors who need evidence. That contrast between playful acquisition and inspectable accounting is a useful design pattern.

## 4. Material inconsistencies to preserve

| Topic | Evidence A | Evidence B | Research conclusion |
| --- | --- | --- | --- |
| Geography | Live map: 164 cities / 864 points | Docs/roadmap: 163 cities / 862 points | Mixed live and static counts; do not harmonize silently. |
| Rewards | Homepage table includes 0.02 AMZN, 0.025 AAPL, 0.03 TSLA | Docs/current vault use 0.008, 0.011, 0.013; hourly multiplier varies | Advertised, base and payable amounts differ. |
| Daily cap / radius | App footer: 3/day and 60 m; homepage: 30 m | Docs/Shop: 6/day; docs radius 40–73 m | User-visible rules disagree; actual enforcement not tested. |
| Shop model | Sep 10 screenshot: 12/day and shorter cooldown | Current shop: seventh catch; roadmap: future shop should not alter caps/cooldowns | Versions or plans conflict; current UI is observable, enforcement unknown. |
| Wallet standing | Sep 4 screenshot: full size on third catch within about half an hour | Docs: three different days, first-payout delay and deposit | Anti-abuse rules have tightened or become inconsistent. |
| Legendary winners | Early posts: first arrival wins | Current docs: draw after the window | A material evolution in event mechanics. |
| Receipts and reviews | Sep 12/Sep 23 posts describe live features | Docs/roadmap describe disabled/not deployed states | Availability unresolved without authenticated testing. |
| Solana | Sep 8 posts and sponsor page describe live support | Roadmap labels a payment rail built but off | Possibly separate flows, but wording is insufficient to settle it. |
| Device attestation | Homepage includes it in presence checks | Docs say native attestation is next | Do not treat it as proven deployed. |
| US access / asset nature | Project promotes US locations and uses stock/equity language | Issuer docs distinguish stock tokens and restrict US delivery | Material constraint on copying the model; see other-info. |

## 5. Overall assessment

This is more developed than a one-screen token landing page: public map data, product routes, paid products and visible transaction references form a tangible product surface. The clearest attention advantage is the match between narrative, artwork and a place-based action users can demonstrate. The principal weakness is consistency between marketing, roadmap, docs and live rules. For replication, copy the coherent hook and public evidence pattern, then make rewards, availability and rule changes come from one maintained source of truth.
