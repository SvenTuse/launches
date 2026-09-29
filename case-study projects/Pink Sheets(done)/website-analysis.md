# Pink Sheets — Website Analysis

**Website:** [pinksheets.fi](https://pinksheets.fi/). **Research date:** September 27, 2026.

## Inspection status and evidence

Live visual inspection was attempted in the browser for HTTPS on the bare domain and www hostname: both returned **ERR_CONNECTION_CLOSED**. HTTP returned **ERR_BLOCKED_BY_CLIENT**. An independent public-web fetch also failed (the www hostname returned 502); an authorized direct HTTPS request failed during SSL connection setup. An archive-index retrieval was inaccessible. These are access failures observed during this research, not proof that every visitor sees an outage or that the site is permanently offline.

The search engine still exposes [indexed homepage content](https://pinksheets.fi/), reportedly crawled about two weeks earlier. That supports a limited reconstruction of the public pitch; it does not reproduce a working browser session. No website screenshot is included in the supplied project folder. Accordingly, colors, exact typography, animations, click behavior, button positioning and responsive layout **cannot be verified for the website**. The social branding is independently visible in the supplied screenshots and is described separately below.

## 1. Overall essence and narrative

The indexed homepage presents an OTC block desk on Robinhood Chain for orders too large for ordinary liquidity pools. Its commercial story is specialized execution for large memecoin and stock-token trades, with counterparties competing for an order. The surviving indexed material supports a landing/demo presentation; a functioning trading app was not established. [Source: indexed homepage](https://pinksheets.fi/).

## 2. Technical functionality

The indexed presentation describes three stages: submit an intent, makers bid privately, and the best quote settles. A block-quotation example includes status stages, ticker $HOOD-x, a SELL of 480,000 USDG, a 00:04:12 window, masked quotes and settlement in a single transaction outside the pool. Repeated awaiting/filled labels suggest a demonstration sequence, but do not prove an animation or an executed trade. A notification CTA and the X handle are present in the indexed text. [Source: indexed homepage](https://pinksheets.fi/).

The official launch posts make the stronger claim that the desk is live and handles memecoins and tokenized stocks; see [P03/P04 in X-Flow.md](X-Flow.md). Those screenshots do not establish a wallet connection, an order-submission form, a maker registry, deposits/approvals, actual matching, quotation expiry, contract settlement or a completed OTC fill. The token's CA identifies PINK, but no separately identified desk/settlement contract is supplied. An ERC-20 token existing does not by itself establish the execution product.

**Technical questions left unresolved by the available evidence:**

- Is the quotation sequence illustrative or connected to actual orders?
- Who can provide quotes, and how are bidding access and available balances checked?
- Are bids committed and revealed cryptographically, or kept private by a server?
- What prevents stale quotes, failed approvals or maker default?
- Which contract settles both assets, and where are completed transactions documented?
- What fee is charged, and how does it fund the promised PINK buybacks?

These are limits of product verification, not findings that the claimed functionality is impossible.

## 3. Design and branding

### Website elements recoverable from the index

The page's surviving text uses desk/quotation vocabulary, numbered paperwork and uppercase status labels. This aligns conceptually with a professional trading-counter identity. Exact rendering, colors, font families, hierarchy, positions, hover states, mobile behavior and transitions remain unavailable. [Source: indexed homepage](https://pinksheets.fi/).

### Visually verified campaign assets, not a claimed website rendering

The supplied X images establish the following design language:

- **Palette:** saturated hot pink on mostly black, grayscale and warm cream. The pink papers and streamers provide the only strong color in many images; no exact CSS color values are asserted.
- **Symbol:** four stacked pink sheets drawn as dark-outlined diamond shapes. It repeats in the avatar, the physical pink slip, the desk-opening image and GMGN link previews.
- **Typography:** social image captions use heavy black uppercase sans-serif letters on torn cream-paper strips; the volume milestone uses huge distressed pink numerals. X's native UI type is not counted as project typography.
- **Images and texture:** torn-paper collage, old telephones, monitors, office workers, institutional marble, iron grilles, bells, financial-district crowds and classical columns. The video presenter wears a pink tie and pocket square, keeping the accent color in a different medium.
- **Composition:** “POST THE INTENT.” sits above a pink order slip being passed through a counter; “THE DESK IS OPEN.” sits along the lower-right of a desk scene. These placements and physical props make abstract trading actions readable.
- **Motion:** the two posts contain videos, but their full motion, cuts, audio, duration and production method were not inspected. Nothing proves they are AI-generated or establishes website animations.

Sources: [launch and volume](x-posts/Screenshot_1.jpg), [intent creative](x-posts/Screenshot_2.jpg), [desk and teaser](x-posts/Screenshot_3.jpg), [collage](x-posts/Screenshot_4.jpg), [profile](x-posts/Screenshot_6.jpg), [GMGN previews](x-ca-mentions/Screenshot_6.jpg).

### Branding conclusion and marketing role

The visual identity gives the token a recognizable physical metaphor: a pink quotation slip moving through a Wall Street-style desk. The website's indexed desk terminology and the social copy share this metaphor, while **visual consistency between the live website and social posts remains unverified**. Reusing the symbol across account identity, explainer posts and trader previews likely aided recognition; that contribution is an interpretation, not measured causal attribution.

## Product and token-economics gap

A separate indexed user comment asks why the site appeared to charge no desk fee while the project promised fee-funded buybacks. The original page wording and any subsequent fee-policy change could not be verified; this is a reported inconsistency, not a confirmed current website term. See [other-info.md](other-info.md#2-fee-and-value-capture-question) for the source and interpretation.

**Conclusion:** the surviving evidence establishes the pitch and a coherent social campaign. It does not establish a working OTC product, a verified fee model or a complete visual audit of the live website. This report documents the access limitation explicitly instead of substituting imagined functionality or design.

