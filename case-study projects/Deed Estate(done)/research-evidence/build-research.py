from pathlib import Path
import json, statistics
R=Path(__file__).resolve().parent.parent
CA='0x5e55f18453545d0d4314c5106a2d8db934298e95'
rows=[]
def m(name,handle,day,v,l,r,c,text,attachment='None.',tile='',badge='blue',note=''):
    rows.append(dict(id=f'M{len(rows)+1:03}',name=name,handle=handle,day=day,views=v,likes=l,reposts=r,replies=c,text=text.replace('{CA}',CA),attachment=attachment,source=tile,badge=badge,note=note))
def g(name,handle,day,v,listing,host,tile):
    m(name,handle,day,v,1,1,0,f'Attention $DEED Family! YOUR vote matters!\n\nLess than 100 votes are needed to list $DEED on the Robinhood Top 100 Leaderboard.\n\n- Listing ID: {listing}\n\nEvery vote counts - Robinhood would be huge for community growth [direction emoji]',f'Link preview: green circular DEED building logo, thin lime rule, black grid background, white "$DEED GIVEAWAY", lime "ROBINHOOD NETWORK EXCLUSIVE", gray "GUARANTEED REWARD POOL"; host {host}. This is third-party giveaway/leaderboard bait, not a verified official campaign.',tile,note='Template text transcribed; the final direction emoji varies. No contract is visible in this outer post despite appearing in contract-search results; relevance is via DEED imagery. External site was not used.')
launch='The door is open.\n\nThe $DEED vault is live on Robinhood Chain.\n\nCA: {CA}\n\nHold a share of the apartment portfolio without the landlord work. Rent after costs stays in the vault each month.\n\nOn the 1st, we publish The Roll, apartment by [Show more]'
launchvideo='The post contains a video. Preview: curved apartment tower overlooking a tree-lined road at dusk, warm lights against dark green/gray architecture; 0:31 indicator. Likely a cinematic rental-property launch film; only the frame is observed.'
promo='Visit the link below to learn more about your high yield journey.\n\ndeed.estate'
propertytext='You don’t need to buy the whole building.\n\nHold $DEED for a share of the apartment vault.\n\nRent after costs stays in the vault each month.\n\nOur property map tracker is now live.\n\nExplore the portfolio: deed.estate/properties'
fomotext='⚡ $DEED — $1.9M MC 🚀🔥\n\nFrom $64K → $1.9M — now around 29.7x. 📈\n\nStill looking for early movers? Hit the Telegram link in my bio to join.\n\nCA: "{CA}"\n\n#DEED #Crypto #Memecoin'
fomoimg='Market screenshot using DEED’s green/cream upward-looking buildings preview: price $0.001997, liquidity $139K, FDV/market cap $1.9M, lightning badge 100, #7; quoted earlier $64K Telegram call. The quoted call’s text is truncated and its own metrics are not separately visible.'
m('Michael Lerro','MichaelLerro',22,2400,5,0,1,'$deed ( @DeedEstate ) is a scam\nDo not buy\nThis is the CA\n\n{CA}\n\nThey hacked @virtualbacon x account to shill it and @theunipcs was sent supply to bait people\nThe x account also has a gold check bait people.', 'The post contains a video inside a quoted blue-checked VirtualBacon post: man speaking in a blue-lit studio; caption warns his X account was hacked and to ignore its posts/DMs. Quoted visible text says the main @virtualbacon account was hacked around 8PM ET and a YouTube copy provides verification.', 'A01')
m('Sajad','SajadFlips',22,47000,529,56,41,'How to spot bundled scams like $DEED Fast\n\nvery easy to identify using any of these 8 signs...\n\nca: {CA}', 'The post contains a video. 4:32 chart/screener tutorial preview with a falling GMGN chart; likely a walkthrough of alleged bundling signals. Also an automatic ticker card for First Trust Securitized Plus E… DEED $20.46 +0.12%, which is a different security.', 'A01')
m('Jh','AminTabaFuriju',22,841,4,2,0,'Money laundry, don’t buy this token\n\n{CA}','Two mobile trading screenshots: first around $3.61M cap/$9.24M turnover, 86% snipers, 83% bundlers, 2.95K holders, 296 pro traders, 100% LP burned and Paid Dex Paid; second falling chart around $51.6K cap. These are interface labels and an accusation, not audited chain conclusions.','A01–02')
m('AlphaImds','AlphaImds',25,6900,3,0,1,'Can we start a list of people that have led their followers to the slaughterhouse? I used to look up to @virtualbacon until the recent post which seems to have been deleted on @DeedEstate.\n\nDon’t even look at the chart now.\n\nHere’s the CA:\n[Show more]','None. Text is truncated before the CA.','A02')
m('Degenerator','Degenerator',24,5000,71,13,2,'How to spot bundled scams like $DEED Fast\n\nvery easy to identify using any of these 8 signs...\n\nca: {CA}','The post contains a video. Reuses Sajad’s 4:32 GMGN chart tutorial, explicitly credited “From Sajad”; a distinct outer post, not a duplicate of its source.','A02')
m('SmartMoneyCrypto','SmartMoneyCrpto',22,6600,49,2,10,'There is a bunch of kols shilling $DEED\n\nBe careful, looks like a rug\n\n{CA}','Dark wallet/trade table with many red loss values. This image supports the warning’s framing, not proof of wrongdoing.','A02')
m('DeFade','DeFade_',22,1500,15,0,4,'$DEED\n{CA}\n\nAnother revolutionary tech down over 90% in a few hours. Truly groundbreaking innovation. Deed Estate, RIP.','Large falling price chart, displayed $0.00002048 and −96.42%; quotes another DeFade post beginning “75 fresh wallets hold 52.64% of supply, A 10 wallet insider cluster linked via shared funding/ETH activity ...”, truncated.','A02–03')
m('RED FOX.eth','leeon20',22,73,0,0,0,'Check out $DEED on fomo:','Fomo card: DEED logo, $84.3K MC, −91.66% 24H, Sep 22, 2026, 1:35 PM UTC. That is a card timestamp, not necessarily the post’s time.','A03')
m('DigitalBag™','Digitalbag_ [truncated]',22,1400,8,0,1,'🚨:\n\n@DeedEstate has launched its rental-property vault on Robinhood Chain, with $DEED now trading on Pons.\n\nCA: {CA}','Quotes the gold-checked DEED launch with '+launchvideo,'A03',note='Handle truncated in image; do not infer the missing suffix.')
m('SamRaiders','BlootyRx',22,759,0,0,1,'Replying to @BlootyRx and @yenperps\n$DEED SCAM ⚠️⚠️⚠️\n{CA}',tile='A03',badge='none')
m('SolBull','Solguybull',22,541,2,0,1,'Bought some $DEED ca\n{CA}\n\nDYOR nfa','Mobile position screenshot: roughly $2M cap, $605.91 value, −$405.08/−20.03%, $1,900.11 invested, average entry $2.3M MC; quotes DEED launch with 0:31 video thumbnail.','A03–04')
m('Sol Ficra','Sol_Ficra',22,132,1,0,0,fomotext,fomoimg,'A04')
m('DEED','DeedEstate',22,403000,1300,773,865,launch,launchvideo,'A04–05',badge='gold')
m('SRJ','SRJ_Crypto',22,18000,179,18,28,'Got another scam on our hands⚠️\n\n{CA}\n\n$DEED\n\nDo not buy you will get rugged',tile='A05')
m('Pons | FOMO Radar','ponsdesk',22,281,0,0,0,'5x their normal size — @_zeldr1ss into $DEED\n$819K cap\n{CA}\n\nwatching it here ↓\ngmgn.ai/robinhood/toke...','GMGN card: $819K bought, tracked @_zeldr1ss wallet, sniper 3%, bundler 0%; falling chart. Also unrelated First Trust ticker card.','A05')
m('Oxrime','Oxrime',22,286,0,0,1,'#{CA}\n1 m mc den alım yapılabilir',tile='A05',note='Turkish: says a buy could be made at 1M market cap.')
m('qenn⁸','usermyn_',22,422,4,0,0,'👀 $DEED\n{CA}','Quotes gold-checked DEED property-map post, including green “Rented apartments. Held onchain.” apartment creative.','A05–06')
m('Patrick Cryptoman','Pat_Cryptoman',22,798,5,0,0,'@DeedEstate disabled comments, bundled, team selling, no tokenomics\n\nthis shit a scam\n\n{CA}',tile='A06',badge='none')
m('1000x Gem Hunter','itsmeflow18',22,114,0,0,0,fomotext,fomoimg,'A06')
m('bulogg','arhGA333',22,191,0,0,0,'Mungkin ini akan pump keras di kemudian hari\n\n{CA}',tile='A06',badge='none',note='Indonesian: “Maybe this will pump hard later.”')
g('Vesperglass Reliquary','vesperglass',22,65,2264,'robinhood-main-dex-rht.netlify.app','A06–07')
g('Windfolio Library','windfoliosETH',22,90,5629,'robinhood-main-dex-rht.netlify.app','A07')
g('Windfolio Library','windfoliosETH',24,21,8313,'robinhood-main-dex-rht.netlify.app','A07')
m('大球🌐','daqiu02',22,191,0,0,0,'$deed 推特还是个金标 有点意思 租金分成，但不包括房屋所有权\n{CA}','Quotes DEED launch and 0:30 apartment video preview.','A07–08',badge='none',note='Chinese: notes the gold badge, calls rent sharing interesting, but says it does not include property ownership.')
m('butter cookies','0xbutterCookies',22,130,0,0,0,'I read the X handle written into every token launched on Robinhood Chain in 24 hours. All 11,793.\n\n58% declare a handle another deployer also declared. @vladtenev is claimed by 104 separate addresses.\n\nThe handle is a text box. Nothing checks it.','X Article preview: “Twenty-eight tokens called DEED. Twenty-seven are not it.” Dark page with red 58%, white 11,793, red 104; excerpt says 28 DEED tokens point to the same X account and 27 are not the one people are buying. An author’s analysis, not independently recomputed here.','A08')
g('JPEG Nomad','JPEGNomadsNFT',22,27,5076,'robinhood-main-dex-pwj.netlify.app','A08')
m('1000x Gem Hunter','itsmeflow18',22,115,0,0,0,'⚡ $DEED — $81K MC 🚀\n\nFrom $64K → $81K — now around 1.3x. 🔥\n\nMore early setups? Tap the Telegram link in my bio to join.\n\nCA: "{CA}"\n\n#DEED #Crypto #Memecoin','Screener card $81K cap/FDV, $23K liquidity, $61K volume, 918 transactions, token age 10m; quotes earlier $64K call.','A08–09')
m('Sol Ficra','Sol_Ficra',22,115,1,0,0,'⚡ $DEED — $2.4M MC 🔥🚀\n\nFrom $64K → $2.4M — about 37.5x. 📈\n\nWant more early moves like this? Join through the Telegram link in my bio.\n\nCA: {CA}\n\n#DEED #Crypto #Memecoin','Screener screenshot: $0.002467, $152K liquidity, $2.4M cap/FDV, $7.5M volume, 9,279 txns, 1,793 traders, #3 and lightning 100; quotes earlier $64K call.','A09')
g('seaborn','seaborn7',22,64,6804,'robinhood-main-dex-xmv.netlify.app','A09–10')
g('Violet Noir','violetnoirNFT',22,37,9730,'robinhood-main-dex-bqk.netlify.app','A10')
g('Libtards.R.US','Libtardville77',22,53,2660,'robinhood-main-dex-xmv.netlify.app','A10')
g('Onchain Owl','OnchainOwlX',23,14,8036,'robinhood-main-dex-xmv.netlify.app','A10–11')
g('Vesperglass Reliquary','vesperglass',22,98,9889,'robinhood-main-dex-zkc.netlify.app','A11')
g('Killajoy','killajoyy',22,68,4542,'robinhood-main-dex-bqk.netlify.app','A11')
g('Patriot1966','headonaswivel57',22,32,9313,'robinhood-main-dex-bqk.netlify.app','A11–12')
g('Violet Noir','violetnoirNFT',22,49,8691,'robinhood-main-dex-bqk.netlify.app','A12')
m('Marco Alpha','Marco_Alpheok',22,356,1,1,0,'$DEED⚡ $DEED — $64K MC 🔥👀\n\nEarly setup spotted— $DEED is on the radar.\n\nWant more early finds? Click the Telegram link in my bio to join.\n\nCA: "{CA}"\n\n#DEED #Crypto #Memecoin','Screener screenshot: price $0.00006410, $24K liquidity, $64K cap/FDV, $225K turnover, 1,199 txns, 263 traders.','A12')
g('Crypto Koi 錦鯉','CryptoKoiX',22,41,2771,'robinhood-main-dex-xmv.netlify.app','A12–13')
g('puppymom15','VeyroshadeETH',23,42,2648,'robinhood-main-dex-zkc.netlify.app','A13')
g('Emberbloom Garden','emberbloomsETH',22,92,5405,'robinhood-main-dex-zkc.netlify.app','A13')
m('Crypto老鹰','laoyingkhq',22,842,0,0,2,'[X-rendered translation from Chinese]\n🚨 $DEED now at 1.25M, DYOR, don’t get carried away.\n\nAI coin selection system hits with precision, locks on directly.\n\nTrading memecoins, AI coin picking leads you to a comeback turnaround.\n\nThis bro caught a potential opportunity on-chain through GMGN’s chain scanning feature,\n[Show more]','DEED cream building logo on dark green beside a Chinese screenshot of the property-map post; unrelated First Trust ticker card; quotes Crypto老鹰’s Sep 21 post about 10 GPT-6 Astra agents receiving $52 each, with a 0:25 video thumbnail and truncated text.','A13–14',note='Rendered translation recorded as displayed, not substituted for an unavailable original.')
g('Chrome Warden','ChromeWardenNFT',22,63,7340,'robinhood-main-dex-zkc.netlify.app','A14')
g('Murphy Bannerman','CupidUnleashNFT',22,80,1015,'robinhood-main-dex-xmv.netlify.app','A14')
g('Memory Hive Collective','memhivesETH',22,29,8305,'robinhood-main-dex-zkc.netlify.app','A14–15')
m('Labs | web3猎手','A9_Labs_MeMe',22,147,0,0,0,'$DEED\n\n市值：540k\n\nCA:\n{CA}\n\nokx 钱包： web3.okx.com/u/h2nyrL8?ref...\n\n一个房地产收益金库项目。其核心卖点是，你可以间接赚取出租公寓的净租金收入，而无需自己做房东、收取租金或处理物业维修。\n[Show more]','Historical website screenshot: dark green property page, cream title “Where the rent comes from.”, header links Portfolio / The Roll / Certificates / FAQ / Docs and Connect Wallet at right; cards 62 Apartments, 5 Buildings, 5 States, 92% Occupied, $78,656 Rent collected last month; US map with green/yellow location markers. Also an unrelated First Trust ticker card.','A15',note='Chinese: $540K cap and indirect net rental income without landlord work. Figures are displayed project claims, not independently verified assets or cash flow.')
g('Grave Gobbler','GravegobbNFT',22,48,3584,'robinhood-main-dex-xmv.netlify.app','A15')
g('MetaHorizon','MetaHorizonNFT',22,52,5934,'robinhood-main-dex-bqk.netlify.app','A15–16')
g('Chris Wrona','ChrisWrona04',22,31,1125,'robinhood-main-dex-xmv.netlify.app','A16')
g('Woman & Guardian','WomanGuardianHQ',22,110,7063,'robinhood-main-dex-pwj.netlify.app','A16')
rolltext='Every building has a rent roll. Ours is public.\n\n$DEED represents your share of the apartment vault.\n\nRent after costs stays in the vault each month.\n\nOn the 1st, The Roll shows what each unit paid.\nLate rent and vacant units included.\n\nSee the buildings: deed.estate/properties'
rollimg='Cream architectural model of an apartment block on the right, one dark green vacant window; dark green left panel with cream DEED logo, “• Vacant”, “An empty apartment still makes the Roll.” and “Vacancy doesn’t disappear because the rent didn’t arrive.” Transparency is the message.'
m('DEED','DeedEstate',22,26000,127,24,110,rolltext,rollimg,'A16–17',badge='gold')
g('Onchain Maven','OnchainMavenNFT',22,42,9722,'robinhood-main-dex-xmv.netlify.app','A17')
m('Tougii','f4rwardx',22,69,0,0,0,'$DEED\n\n{CA}\n\nThis project is quite unique in the crypto world and probably one of the first!\n\nIt is highly similar in its core investment philosophy to a REIT, as both allow you to invest in a diversified pool of income-producing rental\n[Show more]','Blue Fomo position/referral card: +22.12%, average entry $92.7K, current $113.2K, 10% off fees with code f4rwardx; declining price trace with green entry markers.','A17–18')
m('DeFade','DeFade_',22,2100,9,2,0,'$DEED\n{CA}\n\n75 fresh wallets hold 52.64% of supply, A 10 wallet insider cluster linked via shared funding/ETH activity holds another 11.4%.','Two risk-analysis screenshots: DEED “ELEVATED RISK”, DEX PAID, 21 scans, falling chart; Fresh Wallet Detection “CRITICAL RISK”, 75 fresh wallets, 52.64% fresh holdings, sold 28.3%, 44 retaining / 31 still holding. Author/tool allegations, not a fresh independent audit.','A18')
m('Drogon（卓金）','meta9113meta',23,204,0,0,0,'$DEED 复盘：视频里教的识别方法，现在都应验了。\n{CA}\n\n上线没多久就有人做了条 4 分半的视频，标题就是——如何快速识别像 $DEED 这样的捆绑骗局。判断标准很简单：下面 8 条里，中任意一条，就不要碰。\n\n先看推特。\n第一步不是看 K\n[Show more]','The post contains a video. Reuses Sajad’s 4:32 chart warning, with Chinese subtitle; also quotes Sajad’s blue-checked post and shows unrelated First Trust ticker card.','A18–19',note='Chinese: says warning signs taught in the launch-day video came true; advises checking X before price charts.')
g('Cathy Essigmann','Cathye2017',22,67,6259,'robinhood-main-dex-pwj.netlify.app','A19')
g('Vesperglass Reliquary','vesperglass',22,83,1639,'robinhood-main-dex-pwj.netlify.app','A19')
m('butter cookies','0xbutterCookies',22,145,0,0,0,'Twenty-six wallets bought the entire starting supply of DEED one block after it was created. Twenty-five of them have since sold out.\n\nDEED, {CA}. Created 23:51 UTC / 19:51 ET on 21 September. It reached the open market in the very next\n[Show more]','Dark infographic “DEED: 26 wallets took the whole starting supply in one block”: 71.43% of all buys in that block, 95.8% of their tokens sold, 1 of 26 holding anything, 2.99% held by last original buyer; 2,039 wallets hold today, 26,562 transfers in about ten hours, 12.27% in known system contracts, 1.50% largest holder who is a person. The screenshot distinguishes these analysis categories.','A19')
m('Talentre DEX · AI Copy Trading','Talentre_',22,5300,39,7,9,'$DEED 25 launch-listed wallets are empty. Their transaction trail leads to 80 addresses holding about 67.3% of the supply.\n\nThe launch input named those 25 addresses for snipe-tax exemptions. They bought 83% of supply in one bundled transaction. We traced two rounds of\n[Show more]','Infographic “DEED’s launch wallet trail”: 25 launch-listed wallets 83.00% → 37 recipient wallets 79.88% → 85 recipient wallets 71.50%; latest balances +67.27%, 80 addresses with positive balances. Footer says sequential transfers, not additive holdings, and transaction links do not establish common ownership.','A19–20')
m('Sorcery Meme','Legend_Britney',22,63,0,0,0,'🚨 $DEED JUST RAN 🚨\n$64K → $2.3M MC 📈💰\nThat’s roughly a 35.9X move.\nTiming. Patience. Execution. 🎯\n❌ No FOMO\n❌ No chasing\n✅ Wait for the right setup\nOne move done. The next setup is already on watch. 👀\n📩 Follow + DM for VIP TG access.\nCA:\n[Show more]','Side-by-side screener cards: $64K/$24K liquidity and $2.3M/$148K liquidity, latter $6.9M volume, 5,924 txns, lightning100.','A20')
g('Charles C Baldwin','NotHairLoss',22,35,7885,'robinhood-main-dex-zkc.netlify.app','A20')
g('Jesse13','HODLto0',22,70,3555,'robinhood-main-dex-bqk.netlify.app','A20–21')
m('Jeff','cfm_sol',22,6900,19,5,12,'$DEED 540k dyor\n\n{CA}\n\nokx wallet:web3.okx.com/u/h2nyrL8?ref...\n\nA real estate yield vault project. Its core selling point is that you can indirectly earn the net rental income from rental apartments without being a landlord yourself, collecting\n[Show more]','Two historical website screenshots: dark-green US property map and a pale table/report view. Visible footer label “Paid partnership”.','A21',note='The X Paid partnership label is observed evidence of a disclosed promotional partnership for this post; sponsor, compensation, impressions bought through X Ads and campaign spend are not shown.')
g('愛瑠Airu5','airu0605',22,91,1703,'robinhood-main-dex-rht.netlify.app','B01')
g('Root Aria Duels','rootariasETH',22,68,3072,'robinhood-main-dex-zkc.netlify.app','B01')
g('Anita1/20/2024','AnitaOHara4',22,86,1344,'robinhood-main-dex-bqk.netlify.app','B01')
g('Nyxara Flux','NyxFluxETH',22,44,9662,'robinhood-main-dex-pwj.netlify.app','B01–02')
g('Spirit Grove','spiriresETH',22,38,8111,'robinhood-main-dex-bqk.netlify.app','B02')
g('Woman & Guardian','WomanGuardianHQ',22,57,3116,'robinhood-main-dex-pwj.netlify.app','B02')
g('DTX Booty','dtxbooty',22,90,7902,'robinhood-main-dex-rht.netlify.app','B02–03')
g('Bubblegum Blue Cat','BubblegumCatNFT',23,43,9143,'robinhood-main-dex-rht.netlify.app','B03')
m('Marco Alpha','Marco_Alpheok',22,51,0,0,0,'⚡ $DEED — $81K MC 🚀\n\nFrom $64K → $81K — now around 1.3x. 🔥\n\nMore early setups? Tap the Telegram link in my bio to join.\n\nCA: "{CA}"\n\n#DEED #Crypto #Memecoin','Screener $81K cap/FDV, $23K liquidity, $61K turnover, 918 txns, age10m; quotes earlier Marco $64K call.','B03')
g('Longg','itsLongg',22,50,5255,'robinhood-main-dex-bqk.netlify.app','B03–04')
rows[-1]['replies']=1
g('Gilded Siren of Echoes','GildedSirenETH',22,84,4601,'robinhood-main-dex-bqk.netlify.app','B04')
g('Desert Degenerate','DesertDegenNFT',23,16,9061,'robinhood-main-dex-bqk.netlify.app','B04')
g('Woman & Guardian','WomanGuardianHQ',22,63,6708,'robinhood-main-dex-pwj.netlify.app','B04')
m('Crypto北斗 · alpha','btc2ai',22,11000,15,1,9,'[X-rendered translation from Chinese]\n$DEED Real Estate RWA\nCA: {CA}\n\nThis is essentially turning real estate rentals into an ETF. Token holders don’t need to own the property itself. But after RWA, there’s rental income on the 1st of every month.\n\nFollowers are decent, but\n[Show more]','DEED profile/follower screenshot, highlighting S8Security among followers; quotes DEED launch video thumbnail.','B04–05')
g('Anita1/20/2024','AnitaOHara4',22,33,1352,'robinhood-main-dex-rht.netlify.app','B05')
m('butter cookies','0xbutterCookies',25,16,0,0,0,'11,793 tokens launched in a day, 149 finished the curve, and 5 were still being traded two days later.\n\nI counted the same 149 graduates three times, in the same hour of the day, on 22, 23 and 24 September. Same window, same method, Transfer events read straight off the chain.\n[Show more]','Dark green/red infographic: 149 tokens finished bonding curve, measured three days; 6,184 → 2,798 → 1,619 transfers; 20 → 9 → 5 tokens with >=100 transfers/hour; 82 → 109 → 110 with zero transfers. Line chart shows token activity diverging. This is chain-wide context in search results, not all DEED-specific data.','B05')
g('LunarMint','LunarMintHQ',23,12,5108,'robinhood-main-dex-pwj.netlify.app','B05–06')
g('Orchard Clue Bureau','orchardclueETH',22,75,5992,'robinhood-main-dex-xmv.netlify.app','B06')
g('Only Emma','bemma2200',23,12,7075,'robinhood-main-dex-xmv.netlify.app','B06')
m('AlphaPulse','AlphaPulsevw',22,1000,2,2,0,'$DEED⚡ $DEED — $64K MC 🔥👀\n\nEarly setup spotted— $DEED is on the radar.\n\nWant more early finds? Click the Telegram link in my bio to join.\n\nCA: "{CA}"\n\n#DEED #Crypto #Memecoin','Same $64K/$24K liquidity screener card as Marco’s early call.','B06–07')
g('Jacob Perritt','JacobPerritt',22,71,9605,'robinhood-main-dex-zkc.netlify.app','B07')
g('•Filo•','filipposerra_',22,60,8227,'robinhood-main-dex-pwj.netlify.app','B07')
g('Bandit Bearlock','BearlockNFT',22,83,7854,'robinhood-main-dex-rht.netlify.app','B07–08')
g('Patriot1966','headonaswivel57',22,71,1489,'robinhood-main-dex-rht.netlify.app','B08')
g('Tidewraith Covenant','tidewraithsnft',22,39,3620,'robinhood-main-dex-zkc.netlify.app','B08')
m('区块链行情研究','qkl2058',22,1500,0,0,4,'[X-rendered translation from Chinese]\n🎉 $DEED Current Price: 1.2M DYOR\n\nSniped precisely by this GEM using GMGN, from $143 → $37.8K, successfully cashed out\n\nOne-click copy trading pro wallet: gmgn.ai/robinhood/addr...\n\nIntelligence tools dual-drive, helping you capture the next hot spot.\n\nUltimate guide to profiting\n[Show more]','Profit card over banknote portrait: +$37.65K/+25,855.33%, $37.8K sold, $143.51 cost; Chinese project post alongside, headed “Three steps. No landlord work.”; quoted author’s video/referral post with 1:28 preview and FOMO cheat-code link.','B08–09',note='A claimed trade result, not proof of project revenue or the author’s wallet ownership.')
m('RH Master','MintDetector1',22,158,1,0,1,'🚀 Hot pick on Robinhood Chain #robinhood\n\nDeed Estate $DEED going parabolic\n\nContract Address:\n{CA}\n\nAFMCJN\n🎯','GMGN preview: DEED logo/wordmark on dark moon/cloud background; unrelated First Trust ticker card.','B09',badge='none')
g('ChainCanvas','ChainCanvasHQ',22,60,2316,'robinhood-main-dex-xmv.netlify.app','B09')
m('RH Master','MintDetector1',22,105,0,0,0,'☀️ Momentum building for on Robinhood Chain $HOOD\n\nDeed Estate $DEED pumping\n\nContract: {CA}\n\nEGPEKS\n☀️','GMGN DEED logo link preview and unrelated First Trust DEED ticker card.','B09–10',badge='none')
m('Marco Alpha','Marco_Alpheok',22,91,0,0,0,'⚡ $DEED — $2.4M MC 🔥🚀\n\nFrom $64K → $2.4M — about 37.5x. 📈\n\nWant more early moves like this? Join through the Telegram link in my bio.\n\nCA: "{CA}"\n\n#DEED #Crypto #Memecoin','Same $2.4M cap / $152K liquidity / $7.5M turnover screener image as Sol Ficra; quotes own earlier $64K call.','B10')
g('أبو باسل المزيني / محب العالمي [Arabic display name]','1718Mr',22,65,8950,'robinhood-main-dex-xmv.netlify.app','B10–11')
g('Orbit Feathers','OrbetfeathETH',22,33,2444,'robinhood-main-dex-rht.netlify.app','B11')
g('Mint Signal','MintSignalNFT',22,48,7372,'robinhood-main-dex-rht.netlify.app','B11')
g('Patriot1966','headonaswivel57',22,54,4760,'robinhood-main-dex-bqk.netlify.app','B11–12')
g('Uekobo Protocol','uekobuprotocol',22,29,5380,'robinhood-main-dex-xmv.netlify.app','B12')
m('FomoChemist','FomoChemist',22,387,1,1,0,'I introduced $DEED at a $64k market cap and strategically shared it with my community, highlighting its early-entry edge and strong upside potential.\n\nCa:\n{CA}\n\n#Robinhood','Cropped $64K market cap, $24K liquidity DEED screener card.','B12')
g('Neon Dreamwave','NeonDreamNFT',23,32,1845,'robinhood-main-dex-xmv.netlify.app','B12–13')
g('Plushark Works','plushrksETH',23,47,9765,'robinhood-main-dex-pwj.netlify.app','B13')
m('0xAptα','0xApta',22,216,1,0,2,'🚀 New trending coin detected:\n${CA}\nContract address: {CA}\nAsset type: utility token\nPrice: $0.00257 | MCap: $2.57M | Vol24h: $1.90M\nFirst activity: 2 hours ago\nTags: Broad, new project, Mid MC',tile='B13',badge='none')
g('Ben','iamkuni',22,89,6318,'robinhood-main-dex-xmv.netlify.app','B13')
g('Nyxara Flux','NyxFluxETH',22,55,6085,'robinhood-main-dex-zkc.netlify.app','B13–14')
g('farah','arlsunshine',22,56,6754,'robinhood-main-dex-xmv.netlify.app','B14')
g('Smoke Lingo Accord','smokelingoETH',22,20,8724,'robinhood-main-dex-zkc.netlify.app','B14')
g('محمد','moo_dy11',22,38,1134,'robinhood-main-dex-pwj.netlify.app','B14–15')
m('MAX SIGNALS 1000x','max_signals',22,83,1,0,0,'🚨 $DEED EARLY CALL 🚨\n\nI introduced $DEED to my community at just $3.2K MC 👀📈\n\nThe setup was shared early, giving members a chance to watch the momentum develop from the ground up. 🔥\n\nEarly entries. Clear setup. Strong execution. 🎯\n\nCA:\n[Show more]','Large cream building DEED logo on green; quotes own “$DEED JUST SENT / $3.2K MC → $1.5M MC” post, truncated.','B15')
m('butter cookies','0xbutterCookies',22,121,0,0,0,'Twenty-eight different tokens on Robinhood Chain are all called DEED and all point at the same X account. Twenty-seven of them are not it.\n\nI pulled every token launched on this chain in 24 hours and read the X handle written into each contract. 11,793 tokens. 9,901 of them\n[Show more]','Infographic “Who else is claiming that X account?”: @robinhoodapp 547 tokens/36 deployers, @vladtenev 123/104, @jolt…134/2, @ponsdotfamily64/40, @deedestate28/27; 58% share a claimed handle; footer says handles are text fields anyone can type.','B15',note='Same analysis theme as M025 but distinct post and attachment; preserve separately.')
g('Jesse13','HODLto0',22,102,8802,'robinhood-main-dex-zkc.netlify.app','B15–16')
m('Punch','XPnftclub',22,2300,11,1,19,'[X-rendered translation from Chinese]\nThe Robinhood chain is still too dominant.\n\nThere are golden dogs every day.\n\n$PONS, although the returns are much lower than in early September, it’s still very stable, with buybacks continuing. If it can drop back below 0.6 price, I’ll add some more to the position.\n\nCurrently,\n[Show more]','PONS DeFiLlama-style card: $142.92M fees30d, $25M revenue30d, $15.02M holder revenue30d, $2.373B DEX volume30d, cap $438.67M, price$0.64, 24hvolume$78.43M. This is about PONS, not DEED; included because it is in the supplied search capture.','B16')
g('Chilly Penguins','ChillyPenguinsX',23,18,9637,'robinhood-main-dex-zkc.netlify.app','B16')
m('jimmy007','Jimmy0089588573',22,185,3,0,1,'Replying to @b_cosman\nYes — there are very strong signs that @DeedEstate / deed.estate is a high-risk crypto scheme and, most likely, a scam or rug pull. There is no public evidence that this is a real real-estate product backed by Robinhood.\nWhat they claim\nThey say $DEED (contract\n[Show more]',tile='B16–17')
g('NFT Navigator','NFTNavigatorHQ',22,32,5219,'robinhood-main-dex-bqk.netlify.app','B17')
rows[-1]['reposts']=0
g('Charles C Baldwin','NotHairLoss',22,90,5096,'robinhood-main-dex-rht.netlify.app','B17')
g('Sauce Sprout Society','saucesproutsETH',23,46,7061,'robinhood-main-dex-pwj.netlify.app','B17–18')
m('柳智敏','liuzhimin_bot',22,491,0,0,0,'[X-rendered translation from Chinese]\n$DEED\n\n{CA}\n\nNew RWA real estate rental token launched on Pons launchpad on Robinhood Chain, @virtualbacon’s retweet with endorsement draws attention—it’s all about bundling net rents from U.S. rental apartments into an on-chain vault.\n[Show more]',tile='B18',note='This is a contemporaneous endorsement claim; the hacked-account warning means authentic approval by VirtualBacon is not established.')
g('Bunova Mission','bunovasETH',22,63,7237,'robinhood-main-dex-zkc.netlify.app','B18')
m('butter cookies','0xbutterCookies',22,148,1,0,0,'The holder count on DEED went from 2,039 to 2,990 in three hours. I said I would publish that number either way, so here it is.\n\nDEED, {CA}.\n\nAt 01:48 UTC / 21:48 ET: 2,039 wallets holding, 26,562 transfers.\nAt 04:58 UTC / 00:58 ET: 2,990\n[Show more]','Infographic “DEED: the holder count kept climbing”: 2,039 → 2,990, +951 wallets in three hours; 26 original wallets, 25/26 still completely gone, 2.99% remaining, 51,367 transfers. Time pairs are author’s comparison, not the post timestamp.','B18')
g('MetaHorizon','MetaHorizonNFT',22,36,6471,'robinhood-main-dex-xmv.netlify.app','B18–19')
m('Marco Alpha','Marco_Alpheok',22,72,0,0,0,fomotext,fomoimg,'B19')
g('Signal Loom Atelier','sigloomsETH',24,23,4712,'robinhood-main-dex-xmv.netlify.app','B19–20')
g('أبو باسل المزيني / محب العالمي [Arabic display name]','1718Mr',22,85,3116,'robinhood-main-dex-xmv.netlify.app','B19–20')
g('Crumbkin Social Club','crumbkinsnft',22,34,1269,'robinhood-main-dex-bqk.netlify.app','B20')
m('AlphaPulse','AlphaPulsevw',22,292,2,0,0,'⚡ $DEED — $81K MC 🚀\n\nFrom $64K → $81K — now around 1.3x. 🔥\n\nMore early setups? Tap the Telegram link in my bio to join.\n\nCA: "{CA}"\n\n#DEED #Crypto #Memecoin','Screener $81K cap, $23K liquidity, $61K turnover; quotes own earlier $64K call.','B20–21')
g('Nyxara Flux','NyxFluxETH',22,42,3927,'robinhood-main-dex-bqk.netlify.app','B21')
g('Prismhorn Jax','PrismhornETH',22,52,6834,'robinhood-main-dex-zkc.netlify.app','B21–C01')
g('NFT Navigator','NFTNavigatorHQ',22,57,3736,'robinhood-main-dex-bqk.netlify.app','C01')
g('The Boxhead Guardian','BoxheadETH',22,81,2967,'robinhood-main-dex-zkc.netlify.app','C01')
g('Brooks Klutts','brookskklutts',24,13,1792,'robinhood-main-dex-pwj.netlify.app','C01–02')
g('Chain Kelp','chainkelpNFT',22,82,3852,'robinhood-main-dex-rht.netlify.app','C02')
m('0xtarunna','tarunnamana1',22,99,1,0,0,'$DEED 2.2M\n\n{CA}\ngmgn.ai/robinhood/toke...\n\n$DEED 把“房地产”这个全球最成熟的现实资产之一搬进链上叙事。\n\n房地产一直是传统金融最核心的资产类别之一。\n\n但过去的房地产投资有一个很明显的问题：门槛高、流动性低、参与方式重。\n\nRWA\n[Show more]','Historical website hero: green background, centered cream “Rental property, without the property.”, thin concentric outline rings, lime Connect wallet button and outlined See how it works; header Portfolio / The Roll / Dashboard / FAQ / Docs, white Connect wallet top right; lower heading “The money comes from tenants.” Visible “Paid partnership” label.','C02',note='Chinese: mature real estate asset class brought onchain, with high thresholds/low liquidity as the problem. Disclosed paid partnership; sponsor and compensation are not shown.')
m('Robinhood Migration Radar','RobinhoodRadar',22,440,0,0,0,'🚨 MIGRATION DETECTED | $DEED\n\n{CA}\n\ndeed estate\n\n• Migration MC: 20.58 ETH | ATH MC: $3.36M\n• Liquidity: $136.40K | Holders: 237\n• DEX Paid: No | CTO: No\n• Audit: Passed | Honeypot: No\n• Snipers: 35 | Top10: 26.98% | Rug: 0%\n\n⚡ Quick\n[Show more]','GMGN logo/wordmark link preview; unrelated First Trust ticker card.','C02–03',note='Automated-style tool claims, including “audit passed” and “Rug:0%”, are not an identified independent security audit; DEX Paid No is a separate snapshot from later Paid labels.')
m('RH Master','MintDetector1',23,135,0,0,0,'⚡ Momentum building for on Robinhood Chain #robinhood\n\nDeed Estate $DEED mooning\n\nContract: {CA}\n\n5GREHM\n💎','GMGN DEED logo card plus unrelated First Trust ticker card.','C03',badge='none')
soltext='🚨 $DEED JUST SENT! 🚀🔥\n\n$64K MC → $2.2M MC\nThat’s a massive 34,375 profit return 📈💰\n\n👉 Follow + DM me to join the private TG & Discord and catch upcoming setups early.🚀\n\n{CA}\n\n#Robinhood #CryptoAlpha #Crypto'
solimg='Side-by-side screener screenshots: $2.2M cap/$147K liquidity/$7.0M volume/6,315 txns versus $64K cap/$24K liquidity/$225K volume. The text’s “34,375 profit return” lacks a unit and is not a verified profit calculation.'
m('SOL EXPERT','collin_har23192',22,21,0,0,0,soltext,solimg,'C03–04')
m('Tokeinho','tokeinho',22,399,5,1,1,'$DEED is the worst scam trash I have ever seen. Not only is the utility complete garbage.\n\nWhat is most important: This project is a complete bundled scam from a notorious serial scammer team, which is continuously dumping their proxima bundles.\n\nI am following this scam team for\n[Show more]',tile='C04')
g('John Steinbeck','fedmech',22,40,4456,'robinhood-main-dex-pwj.netlify.app','C04')
g('Frost Relay','frostrelayNFT',22,73,2554,'robinhood-main-dex-pwj.netlify.app','C04')
m('RH Master','MintDetector1',22,194,0,0,0,'💎 Eyes on on Robinhood Chain $HOOD\n\nDeed Estate $DEED surging\n\nCA: {CA}\n\nE7VBJM\n☀️','GMGN DEED logo card and unrelated First Trust ticker card.','C04–05',badge='none')
g('Signal Loom Atelier','sigloomsETH',24,29,4088,'robinhood-main-dex-bqk.netlify.app','C05')
m('Teddy Lynch','TeddyLynch7',22,19,0,0,0,'🚨 R Smart Money Alert\n\n🚀$DEED\n📊 MC: $2.82M\n\n🟢 3 smart money wallets detected.\n\n💰 Total bought: 0.26506 ETH\n\n{CA}',tile='C05',badge='none')
g('just me','nrthndbtch',22,38,1859,'robinhood-main-dex-rht.netlify.app','C05')
g('Block Bloom','BlockBloomX',23,38,5429,'robinhood-main-dex-bqk.netlify.app','C05–06')
m('Rame','RamenOracle',22,153,1,0,1,'$DEED 2M\n\n{CA}\n\n$DEED Turning an apartment portfolio into an on-chain “rental income ETF”: 100 USDG goes into the vault in exchange for shares. You don’t get a property deed, you don’t deal with tenants, and after taxes, fees, and insurance\n[Show more]','Green/cream skyward building website preview; unrelated First Trust ticker card.','C06')
m('RH Master','MintDetector1',22,112,0,0,0,'🚀 People watching on Robinhood Chain #robinhood\n\nDeed Estate $DEED mooning\n\nToken CA: {CA}\n\nB9XD0Q\n✨','GMGN DEED logo card and unrelated First Trust ticker card.','C06',badge='none')
m('SOL MONSTER','SOLMONSTER01',22,79,0,0,0,soltext,solimg,'C06–07')
m('Runner Radar','Runner_Radar',22,186,0,0,0,'Interesting activity around $DEED.\n\n405 views on Robinhood with 31 smart and 38 fresh wallets in the mix.\n\n237 holders • $136.40K liq • $3.36M ATH\n\nCA: {CA}\n\n⚡ Quick Buy ⚡:','Axiom “The Gateway to DeFi” trading-interface link preview; unrelated First Trust ticker card.','C07')
m('RHC Radar','RHCRadar',22,321,1,0,0,'When it comes to $DEED, I think two things need to be separated completely:\n\nWhat the project actually is\n\nand\n\nWhat I think about putting real estate onchain\n\n1. First, $DEED itself\n\nCA:\n{CA}\n\nDeed isn’t simply launching another “real estate\n[Show more]','Unrelated First Trust ticker card.','C07')
g('Lotus Marsh Guild','lotusmarshs',22,51,6172,'robinhood-main-dex-bqk.netlify.app','C07–08')
m('RH Master','MintDetector1',22,212,0,0,1,'📈 Alpha spotted on Robinhood Chain #robinhood\n\nDeed Estate $DEED flying\n\nContract: {CA}\n\nDFN4HM\n✨','GMGN DEED logo card and unrelated First Trust ticker card.','C08',badge='none')
g('Bubble Kaiju Club','bubkaisETH',22,93,5006,'robinhood-main-dex-bqk.netlify.app','C08')
m('Nuno','Nuno_BTC',22,1000,23,0,24,'[X-rendered translation from Vietnamese]\n$DEED Crypto + REAL ESTATE\n\n{CA}\n\nA pretty interesting model: real estate yield vault — accessing rental cash flow for real estate without needing to directly own or manage apartments.\n\nThe most important point is to distinguish:\n\n• vDEED =\n[Show more]','Screener price $0.001082, $100K liquidity, $1.0M cap/FDV, age8h, #3/lightning100.','C08–09',note='vDEED distinction is truncated in the visible text; do not complete it from assumptions.')
m('0Xgcy','Kalijahsmith1',22,227,2,0,0,'$DEED | 四个字母的地契\n\n2.2M\n\nca: {CA}\n\nDeed 本身就是产权文件。不需要第二句设定。\n\n公寓组合、净租金进库、份额可交易——故事完整，落地另说。刚打出来就有站点和账号在发，注意力已经从发射台溢出去。同名协议、卡牌盘都有，认这条 Robinhood\n[Show more]','Large DEED cream building logo on dark green; unrelated First Trust ticker card; visible Paid partnership label.','C09',note='Chinese: DEED name is self-explanatory as a title document; apartments/net rent/tradable shares make a complete story, implementation is another matter; warns of similarly named projects. Disclosed paid partnership.')
g('محمد','moo_dy11',22,74,6200,'robinhood-main-dex-zkc.netlify.app','C09–10')
g('Mossbyte Assembly','mossbytesnft',23,16,6398,'robinhood-main-dex-rht.netlify.app','C10')
m('Runner Radar','Runner_Radar',22,177,0,0,0,'Interesting activity around $DEED.\n\n407 views on Robinhood with 57 smart and 109 fresh wallets in the mix.\n\n461 holders • $140.19K liq • $4.28M ATH\n\nCA: {CA}\n\n🔗 Quick Swap:','Axiom “The Gateway to DeFi” link preview and unrelated First Trust ticker card.','C10')
m('金石','BTC886_',22,1200,2,1,5,'[X-rendered translation from Chinese]\n$DEED is a project on Robinhood that tokenizes real apartment rental income into on-chain shares. Invest funds to buy shares for ongoing returns. $DEED is the project’s share token.\n\nThe project claims to have 5 buildings and 62 apartments across 5 cities, with monthly rental\n[Show more]','Quotes author’s unrelated Sep21 $FAMILY launchpad-research post with a rising/falling candlestick chart; automatic unrelated First Trust DEED ticker card.','C10–11')
g('Block Bloom','BlockBloomX',22,56,5167,'robinhood-main-dex-pwj.netlify.app','C11')
g('Block Bloom','BlockBloomX',23,19,4066,'robinhood-main-dex-rht.netlify.app','C11')
g('محمد','moo_dy11',22,51,1264,'robinhood-main-dex-pwj.netlify.app','C11–12')
m('VictorCalls','thexcaller',22,217,0,0,0,'📡 MULTICHAIN TOKEN RADAR\n\n$DEED — Deed Estate\nNetwork: Robinhood\n\n👀 407 views\n💰 ATH: $4.28M\n💧 Liq: $140.19K | Holders: 461\n\nSmart 57 | Fresh 109 | Renowned 2\n\nCA: {CA}\n\nCheck Chart - Signal:','GMGN DEED logo card and unrelated First Trust ticker card.','C12')
m('@SolanaTrending','SolanaTren59241',22,605,0,0,0,'🚨 FRESH ROBINHOOD MIGRATION\n$DEED — deed estate\n\nLiq $140.19K | Holders 461\nATH MC $4.28M | Rug 0%\nDEX Paid Yes | CTO No | Snipers 35\nCA: {CA}\n\nCheck Chart - Signal:','GMGN DEED logo card and unrelated First Trust ticker card.','C12–13',note='Tool-generated-style statistics; no guarantees follow from its “Rug 0%” label.')
g('just me','nrthndbtch',22,57,3030,'robinhood-main-dex-xmv.netlify.app','C13')
m('REX','inizizi_',23,109,1,0,0,'$DEED just ran from $64K → $2.3M. 🚀💰\nTiming. Patience. Execution.\nNo FOMO.\nNo chasing.\nJust waiting for the right setup.\nNext setup 👀\nFollow + DM for VIP TG.\nCA:\n{CA}\n#bbvipks4 #memecoin #Robinhood','Side-by-side $2.3M/$148K liquidity/$6.9M turnover and $64K/$24K liquidity market screenshots.','C13')
m('Degen','oimarcuziinho',22,239,2,0,1,'$DEED MC:2.1M\n\n{CA}\n\nThe slogan is just one line: Rent is due. Shouldn’t you get a cut?\n\nTurn an apartment portfolio into an on-chain “rental income ETF”: 100 USDG goes into the vault in exchange for shares. You don’t get a property deed,\n[Show more]','Large cream DEED building mark on green; unrelated First Trust ticker card.','C13–14')
m('meliboi sama','meliboi_sama',22,846,2,0,5,'$DEED\n\nmcap: $656K\n\nrobinhood cooked up deed estate from that rent is due shouldn’t you get a cut vibe wrapping traditional property investing into tokens so you can snag a community cut of the rents and push for listings instead of just handing cash to landlords. dyor\n[Show more]','Falling GMGN trading chart; unrelated First Trust ticker card.','C14',note='“robinhood cooked up” is the author’s attribution; no official Robinhood backing is established.')
m('0xSamer','Samerharisha8',22,139,1,0,0,'$DEED 2.2M\n\n{CA}\ngmgn.ai/robinhood/toke...\n\n$DEED 讲房地产，它出现的位置非常关键。\n\nRobinhood Chain。\n\n$DEED 选择的关键词很明确：\n\nReal Estate。\n\nRWA。\n\nYield。\n\n这三个方向本身就有成熟的金融叙事，而 Robinhood\n[Show more]','Historical dark-green homepage hero with “Rental property, without the property.”, lime wallet CTA and thin rings; unrelated ticker card; Paid partnership label.','C14–15',note='Chinese: stresses Robinhood Chain positioning and Real Estate/RWA/Yield keywords. Disclosed paid partnership.')
m('0xLago','Lago_ale',22,83,1,0,0,'$DEED 1.9M\n\n{CA}\n\ngmgn.ai/robinhood/toke...\n\n$DEED 抓住了房地产最容易让普通人理解的一层：\n\nRent。\n\n房子可以涨跌。\n\n但租金是房地产最直观的现金流叙事之一。\n[Show more]','Cream building DEED logo on green; Paid partnership label.','C15',note='Chinese: rent is the easiest layer of real estate for ordinary people to understand; property prices move but rent is intuitive cash flow. Disclosed paid partnership.')
m('Viral Pair Watcher','ViralPairs',22,218,0,0,0,'⚡ MOST VIEWED TOKEN | Robinhood\n\n$DEED (Deed Estate)\n\nViews: 405\nATH MC: $3.36M\nLiquidity: $136.40K\nHolders: 237\n\nTop10: 26.98%\nSniper Hold: 9.35%\nBot Rate: 4.95%\n\nCA: {CA}\n\n🔗 Quick Swap:','GMGN logo card and unrelated First Trust DEED ticker card.','C15–16')
m('0x ka','kazikd89',22,148,1,0,0,'$DEED 2.2M\n\n{CA}\n\ngmgn.ai/robinhood/toke...\n\n$DEED is positioned at the intersection of a new narrative combining the Robinhood Chain, real estate yield, and ETFs.\n\nIts value proposition is straightforward: "Rent is due. Shouldn’t you get a\n[Show more]','Historical green homepage hero, lime Connect wallet button, cream title and concentric rings; unrelated ticker card; Paid partnership label.','C16',note='Disclosed paid partnership; sponsor/compensation not visible.')

posts=[]
def p(day,v,l,r,c,title,text,attachment,source):
    posts.append(dict(id=f'P{len(posts)+1:02}',day=day,views=v,likes=l,reposts=r,replies=c,title=title,text=text.replace('{CA}',CA),attachment=attachment,source=source))
banner='Cream high-rise buildings seen from below, converging around an emerald-green sky; architectural perspective creates an aspirational real-estate identity.'
p(18,757000,2000,893,823,'Introduction / waitlist','Meet DEED, built on Robinhood Chain.\n\nReal estate income. Without becoming a landlord.\n\nA yield-bearing real estate ETF coming to @RobinhoodCrypto. Earn income from a diversified portfolio of real-world assets, with the freedom to withdraw whenever you want.\n\nGet notified when\n[Show more]','The post contains a video. Preview shows a red-brick apartment facade at night with several warmly lit windows and dark windows; 0:10 indicator. Likely an introduction to apartments producing rental income; full video content not available from a still.','Screenshot_6.jpg, upper post')
p(18,29000,111,14,14,'Website conversion reminder',promo,'Website link preview: '+banner,'Screenshot_6.jpg, lower post')
p(19,114000,833,504,479,'Long-form product story','[X Article preview]\nA New Standard for Tokenized Real Estate\n\nOn the first of the month, a landlord starts checking who has paid. One tenant pays on time, another on the ninth. A unit sits empty because the last tenant left in a hurry and the next hasn’t signed....','X Article card with a cream miniature cityscape against deep green, emphasizing a recognizable real-estate investment category. The full article is not in the supplied image.','Screenshot_5.jpg, upper post')
p(19,28000,115,12,23,'Website conversion reminder',promo,'Website link preview: '+banner,'Screenshot_5.jpg, lower post')
p(22,403000,1300,773,865,'Pinned launch / token contract',launch,launchvideo,'Screenshot_1.jpg, pinned post')
p(22,21000,190,62,63,'Property map / fractional access',propertytext,'Green landscape panel with large cream “Rented apartments. Held onchain.” at left and cream apartment-block render at right. Small subline: “Deposit USDG. Hold DEED. Read the Roll every month.”','Screenshot_4.jpg, upper post')
p(22,9200,38,3,11,'Website conversion reminder',promo,'Website link preview: '+banner,'Screenshot_4.jpg, lower post')
p(22,32000,159,31,79,'Robinhood wallet meme / quote tweet','[checks robinhood wallet]\n\nMemes ✅\nStock Tokens ✅\nReal Estate ✅\nPassive Income ✅\n\n[returns to deed.estate]','Quotes gold-checked Robinhood Crypto @RobinhoodCrypto, Sep21: “[checks robinhood wallet] Memes ✅ Stock Tokens ✅ ...”. No media attachment is visible in the quote card. DEED extends the original checklist with real estate and passive income; this does not demonstrate Robinhood endorsed DEED.','Screenshot_3.jpg, upper post')
p(22,13000,51,8,19,'Website reminder plus contract','Visit the link below to learn more about your high yield journey.\n\nCA: {CA}\n\ndeed.estate','Website link preview: '+banner,'Screenshot_3.jpg, lower post')
p(22,26000,127,24,110,'Public rent roll / vacancy disclosure',rolltext,rollimg,'Screenshot_2.jpg')

warning_handles={'MichaelLerro','SajadFlips','AminTabaFuriju','AlphaImds','Degenerator','SmartMoneyCrpto','DeFade_','BlootyRx','SRJ_Crypto','Pat_Cryptoman','meta9113meta','Jimmy0089588573','tokeinho'}
alert_handles={'MintDetector1','RobinhoodRadar','Runner_Radar','ViralPairs','TeddyLynch7','0xApta','thexcaller','SolanaTren59241','ponsdesk','leeon20'}
plain_giveaways={3072,3555,5255,4601,9061}
for x in rows:
    x['category']='giveaway/leaderboard template' if 'Listing ID:' in x['text'] else 'project account' if x['handle']=='DeedEstate' else 'warning/negative' if x['handle'] in warning_handles else 'wallet/chain investigation' if x['handle'] in {'0xbutterCookies','Talentre_'} else 'market/trading alert' if x['handle'] in alert_handles else 'other-chain context' if x['handle']=='XPnftclub' else 'narrative/promotion'
    x['paid_label']='Paid partnership' in x['attachment']
    if x['category']=='giveaway/leaderboard template':
        listing=int(x['text'].split('Listing ID: ')[1].split('\n')[0])
        if listing in plain_giveaways:
            x['attachment']=x['attachment'].replace('Link preview: green circular DEED building logo, thin lime rule, black grid background, white "$DEED GIVEAWAY", lime "ROBINHOOD NETWORK EXCLUSIVE", gray "GUARANTEED REWARD POOL";', 'Text-only link preview with an unloaded image placeholder, title "Deed Estate ($DEED) Giveaway" and guaranteed-reward description;')
    x['attachment']=x['attachment'].replace('5 States','5 Cities').replace('Portfolio / The Roll / Certificates / FAQ / Docs','Portfolio / The Roll / Dashboard / FAQ / Docs').replace('S8Security','SBSecurity [handle partly unreadable]')
    x['er_percent']=100*(x['likes']+x['reposts']+x['replies'])/x['views']
for x in posts:
    x['er_percent']=100*(x['likes']+x['reposts']+x['replies'])/x['views']
def totals(rr):
    d={k:sum(x[k] for x in rr) for k in ['views','likes','reposts','replies']}
    d.update(posts=len(rr),interactions=d['likes']+d['reposts']+d['replies'],mean_er_percent=statistics.mean(x['er_percent'] for x in rr),aggregate_er_percent=100*(d['likes']+d['reposts']+d['replies'])/d['views'])
    return d
def table(rr):
    d=totals(rr)
    return '| Posts | Views | Likes | Reposts | Replies | Interactions |\n| ---: | ---: | ---: | ---: | ---: | ---: |\n'+f"| {d['posts']} | {d['views']:,} | {d['likes']:,} | {d['reposts']:,} | {d['replies']:,} | {d['interactions']:,} |\n"
def mt(x):
    return '| Views | Likes | Reposts | Comments/replies |\n| ---: | ---: | ---: | ---: |\n'+f"| {x['views']:,} | {x['likes']:,} | {x['reposts']:,} | {x['replies']:,} |\n\n**Engagement rate:** {x['er_percent']:.4f}% (likes + reposts + replies) / views.\n"
base='screencapture-x-search-2026-09-27-17_00_11'
stems={'A':base,'B':base+'-2','C':base+'-3'}
def source_link(code):
    import re
    bits=code.split('–'); letter=bits[0][0]; links=[]
    for b in bits:
        if b[0].isalpha(): letter=b[0]
        n=int(re.sub('[ABC]','',b))
        links.append(f'[{letter}{n:02}](research-evidence/crops/{stems[letter]}-tile-{n:02}.png)')
    return ', '.join(links)
def quote(s):
    return '\n'.join('> '+v for v in s.split('\n'))
def write_reports():
    a=totals(posts); mm=totals(rows)
    x=f'''# DEED — X-Flow

Research date: **27 September 2026, Europe/Moscow**. All **seven JPGs** in `x-posts` were inspected: six post images contain **10 distinct account posts**, and Screenshot_23 contains the profile. The profile shows **15 posts**; the supplied sample therefore is not the full account history.

## Account information

- **Name:** DEED.
- **Handle:** [@DeedEstate](https://x.com/DeedEstate).
- **Avatar:** cream stacked roof/floor chevrons forming a high-rise silhouette on a dark green square.
- **Banner:** cream modern towers viewed from below, converging around dark emerald sky.
- **Bio:** “Rent is due. Shouldn’t you get a cut? Built on Robinhood.”
- **Location / joined:** Robinhood; September 2026.
- **Website:** [deed.estate](https://deed.estate/).
- **Following / followers:** **1 / 8,597**.
- **Smart followers:** **45**, classified by the @frontrunpro extension, not X itself. This is not a count of verified investors or paying customers.
- **Verification:** **gold checkmark**; no blue project-account checkmark is shown. A badge does not establish property backing or Robinhood endorsement.
- **Extension category:** Onchain Real Estate Vault; wallet lookup says wallets not found.
- **Profile source:** [Screenshot_23.jpg](x-posts/Screenshot_23.jpg).

## Totals from captured account posts

{table(posts)}
- **Mean per-post engagement rate:** **{a['mean_er_percent']:.4f}%**.
- **Aggregate engagement rate:** **{a['aggregate_er_percent']:.4f}%**.
- **Followers/views ratio:** `8,597 / {a['views']:,} = {8597/a['views']:.6f}`, or **{100*8597/a['views']:.4f}%**. This compares one follower snapshot with cumulative post views; it is not unique reach or conversion.
- **Two videos:** the introduction and pinned launch together account for approximately **1,160,000 views / {1160000/a['views']*100:.2f}%** of captured views.
- **Largest post:** introduction video P01, **757,000 views / {757000/a['views']*100:.2f}%**.
- **Highest captured ER:** the September 19 article P03, **{posts[2]['er_percent']:.4f}%**; the September 22 property-map post P06 has **{posts[5]['er_percent']:.4f}%**.

### Method, chronology and limitations

Displayed K counts are expanded to thousands, so totals remain approximate. Interactions exclude bookmarks. Mean ER averages each post’s `(likes + reposts + replies) / views × 100`; aggregate ER divides summed interactions by summed views. No paid/organic impression split, unique viewers, click-through, waitlist signups or funded users was supplied.

Dates are visible as Sep18, Sep19 and Sep22; the year is supported by the joined date and September2026 source context. No post clock times are visible. Posts are grouped oldest date first; same-day ordering is unresolved, and the pinned launch’s feed position is not treated as its publication order. Repeated website reminders are retained as distinct posts because their dates, metrics and/or contract text differ. Two standalone account posts also occur in the mention images: **P05/M013** and **P10/M050**; their metrics match in both supplied captures and should not be added twice in a combined total.

Visible text is transcribed with normalized line breaks. `[Show more]` marks a genuine cutoff; unavailable text and the full X Article/video content are not invented. Embedded quote cards are described inside their outer post, rather than assigned additional engagement that the screenshots do not display.

## Brief date-ordered posting sequence

| ID | Date / time | Brief idea | Creative | Views |
| --- | --- | --- | --- | ---: |
'''
    for pp in posts:
        creative='Video' if 'The post contains a video.' in pp['attachment'] else 'X Article / cream cityscape' if pp['id']=='P03' else 'Robinhood quote card' if pp['id']=='P08' else 'Vacant-apartment poster' if pp['id']=='P10' else 'Apartment product poster' if pp['id']=='P06' else 'Skyward-building link preview'
        x+=f"| {pp['id']} | Sep {pp['day']}, 2026; time unavailable | {pp['title']} | {creative} | {pp['views']:,} |\n"
    x+='\n## Every captured account post\n\n'
    for pp in posts:
        file=pp['source'].split(',')[0]
        x+=f"### {pp['id']} — {pp['title']}\n\n**Date:** September {pp['day']}, 2026. **Time:** not shown. **Source:** [{pp['source']}](x-posts/{file}).\n\n**Attachment:** {pp['attachment']}\n\n**Visible post text:**\n\n{quote(pp['text'])}\n\n{mt(pp)}\n"
    x+='''## Campaign interpretation

The visible campaign moved from an apartment-income teaser and repeated website CTA on September18 to an article on September19, then the live token, property map, rent-roll transparency and a Robinhood-wallet meme on September22. The two cinematic property videos supplied most captured reach; the article and map creative generated higher interaction rates at smaller reach. This suggests that the broad promise attracted initial attention while detail-rich posts gave people a reason to engage, but source views alone cannot establish which viewers bought tokens.

The consistent cream building icon, forest-green backgrounds, bold cream type and repeated architecture gave each post a family resemblance. “No landlord work” removed an obvious objection; “The Roll” and the vacant-window visual addressed transparency concerns. The quote of Robinhood Crypto borrowed a familiar wallet/meme format, without proving a project partnership.

Paid distribution evidence is assessed in [x-mentions-flow.md](x-mentions-flow.md) and [other-info.md](other-info.md): six labeled paid partnerships and paid screener-boost signals exist, but the account screenshots do not reveal an X Ads spend or bought-impression count. The research also records subsequent warnings and drawdown, so high launch reach is not treated as evidence of lasting product success.
'''
    (R/'X-Flow.md').write_text(x,encoding='utf-8')
    cats=sorted({v['category'] for v in rows})
    ext=[v for v in rows if v['handle']!='DeedEstate']
    filtered=[v for v in rows if v['handle']!='DeedEstate' and v['category']!='giveaway/leaderboard template']
    paid=[v for v in rows if v['paid_label']]
    mdoc=f'''# DEED — contract-search mentions flow

Research date: **27 September 2026, Europe/Moscow**. Search contract: **{CA}**. All **three long PNGs** were inspected with **58 overlapping crops**. The supplied **Top** search feed contains **169 distinct outer posts** dated September22–25, from **129 distinct visible author labels** (one handle is truncated). This is the supplied sample, not all X mentions or a complete historical timeline.

## Overall statistics and scope

{table(rows)}
- **Mean per-post ER:** **{mm['mean_er_percent']:.4f}%**; **aggregate ER:** **{mm['aggregate_er_percent']:.4f}%**.
- **Total interactions:** **{mm['interactions']:,}**, excluding bookmarks.
- **Non-project posts:** **{len(ext)}**, with **{sum(v['views'] for v in ext):,} views**. The project’s launch and rent-roll posts contribute **429,000 / {429000/mm['views']*100:.2f}%** of all captured mention views.
- **Giveaway/leaderboard templates:** **90 posts / 4,806 views**, or **{90/len(rows)*100:.2f}% of post count** but only **{4806/mm['views']*100:.2f}% of views**. Treating their volume as community adoption would be misleading.
- **Excluding project posts and giveaway templates:** **{len(filtered)} posts / {sum(v['views'] for v in filtered):,} views**; aggregate ER **{totals(filtered)['aggregate_er_percent']:.4f}%**.
- **Disclosed paid-partnership posts:** **six**, totaling **7,596 views, 25 likes, five reposts and 12 replies**. The labels disclose a commercial relationship; payer, spend and X Ads impressions are unavailable.
- **Checkmarks on outer authors:** **121 blue author labels** (120 fully readable handles and one truncated handle), **one gold author (@DeedEstate)**; **122 unique checked outer-author identities** in total. Four additional checked identities appear only in a quote/nested screenshot, listed below.
- **Account reference:** DEED’s supplied profile has **8,597 followers, one following and 45 smart followers**, a cream building-mark avatar, tower banner, gold badge and rent-cut bio; see [X-Flow.md](X-Flow.md). Individual mention-author follower/following/bio data are not visible, so a collection-level followers/views ratio cannot be measured. Reusing the project’s follower count gives only `8,597 / {mm['views']:,} = {100*8597/mm['views']:.4f}%`, which is not an author-audience or conversion ratio.

## Sentiment and marketing

The sample mixes an understandable RWA/rental-income pitch with price-driven promotion and subsequent warnings. Positive/narrative posts stress earning rent without managing apartments; traders celebrate $64K to $1.9M/$2.4M moves and funnel viewers into Telegram or Discord. Chinese, English and Vietnamese-rendered posts reuse the project logo, homepage, portfolio map or its tower banner, giving external distribution the same visual identity.

**Negative sentiment is substantial:** 14 direct warning/negative posts have **92,686 views**, approximately **{92686/sum(v['views'] for v in ext)*100:.2f}% of non-project captured views**; this does not measure sentiment of all viewers or all of X. Warnings mention a collapse, alleged bundling, influencer allocation and a purported hacked account. Sajad’s chart-warning tutorial alone has **47,000 views**, exceeding any captured external promotional post. Six other wallet/chain-investigation entries add context without being classified automatically as negative.

**Six disclosed partnerships** use the same apartment-income talking points, logo and green website screenshots. Paid screener visibility is supported by lightning100/Boost100 and DEX-paid labels, corroborated by [DEX Screener’s documentation](https://docs.dexscreener.com/boosting). No platform-served DEED X Ad is shown. Undisclosed trading calls, referral links and giveaway bait cannot all be called organic or project-sponsored merely from their appearance. The 90 nearly identical giveaway messages use unrelated Netlify subdomains and inconsistent listing IDs; official authorization, incentive payments and fulfilled prizes were not established.

**Credibility dispute:** Michael Lerro quotes a VirtualBacon hacked-account video warning and accuses people of using the account to promote DEED; another post attributes attention to VirtualBacon’s endorsement. These are conflicting contemporaneous claims, so authentic endorsement is not established. The supplied chain analyses raise concentration concerns, but shared transfers do not alone prove common ownership. The report attributes allegations to their authors rather than presenting them as a completed fraud investigation.

### Content classification (manual research categories)

| Category | Posts | Views | Likes | Reposts | Replies |
| --- | ---: | ---: | ---: | ---: | ---: |
'''
    for cat in cats:
        dd=totals([v for v in rows if v['category']==cat])
        mdoc+=f"| {cat} | {dd['posts']} | {dd['views']:,} | {dd['likes']:,} | {dd['reposts']:,} | {dd['replies']:,} |\n"
    mdoc+='''
## Source order, deduplication and measurement

Capture A is the unsuffixed PNG; B is `-2.png`; C is `-3.png`. A and B are 1920×28800; C is 1920×22064. Feed crops retain original horizontal coordinates x670–1158 and cover the entire height in 1600-pixel windows starting every1400 pixels (200-pixel overlap). All original files are retained; contact sheets are viewing aids only. **M001–M062** start in A, **M063–M126** in B, **M127–M169** in C; M126 crosses the B/C boundary and is counted once.

M IDs record first appearance in the supplied ranked feed. The complete list below groups dates oldest first and retains encounter order within each date because clock times are unavailable; it does not claim a precise intraday publication sequence. Image/card timestamps are explicitly distinguished from post timestamps. Repeated templates from the same author with different listing IDs are separate posts. Cropping overlaps and quote-card repeats are not separate outer posts. Embedded quoted posts have no separately visible engagement in most cards, so are described within the outer entry and excluded from standalone totals.

Empty numeric metric icons are treated as zero displayed interactions, not as unknown lifetime interactions. K counts are rounded. CA capitalization and line breaks are normalized; visible truncation stays marked `[Show more]`. Where X displays a translation, that version is explicitly labeled. Final direction emojis in repetitive giveaway templates are summarized as varying direction emojis; the words, listing ID, host, author, date and metrics are preserved. The quoted-video contents are inferred only from visible previews and text.

The unrelated **First Trust DEED $20.46** stock card repeatedly appears because of the ticker; its stock price is excluded from crypto statistics. “Views405/407” inside radar text are platform/tool views, not the outer X post’s view count. The category table includes one PONS-focused and several chain-wide posts because the guide requires every visible result, while describing their limited DEED relevance.

## Every checked outer author

| Display name | Visible handle | Badge | Captured posts |
| --- | --- | --- | ---: |
'''
    from collections import Counter
    counts=Counter(v['handle'] for v in rows)
    checked={v['handle']:v for v in rows if v['badge']!='none'}
    for handle,v in sorted(checked.items(),key=lambda z:z[0].lower()):
        h='@'+handle
        if '[truncated]' not in handle: h=f'[{h}](https://x.com/{handle})'
        mdoc+=f"| {v['name'].replace('|','/')} | {h} | {v['badge']} | {counts[handle]} |\n"
    mdoc+='''
### Additional checkmarks inside quotes or embedded images

- **VirtualBacon, visible @virtualbacon**, blue; quoted hacked-account video in M001. It is not a standalone contract-search outer post here.
- **Felix**, blue, visible handle begins **@0xFelix…**, suffix unreadable; follower screenshot embedded in M076.
- **Tachi**, blue, handle partly unreadable in the same screenshot; listed by its visible display name rather than an invented username.
- **SBSecurity**, blue, visible handle begins **@SBSecurit…**, suffix unreadable; highlighted in the same embedded follower screenshot. These three account identities are not counted as paid promoters or as evidence of endorsement from following alone. See [enlarged nested screenshot](research-evidence/crops/embedded-followers.png).
- Embedded checked quotes by **DEED, Sajad, Crypto老鹰, 金石, Marco Alpha, Sol Ficra, 1000x Gem Hunter, AlphaPulse and MAX SIGNALS** repeat checked outer identities already counted above.

Thus **126 checked visible identities** are represented when the four additional nested identities are included, of which **four handles are partly unreadable or truncated** (DigitalBag, Felix, Tachi and SBSecurity). The reliable count for fully readable outer checked handles is **121** (120 blue plus DEED gold). The nested screenshot also shows KAGE as a follower, but no checkmark is clearly legible beside that name, so it is not counted as checked.

## Brief date-ordered sequence and metrics index

| ID | Date / time | Author | Brief idea / format | Views | Likes | Reposts | Replies |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: |
'''
    for v in sorted(rows,key=lambda q:(q['day'],q['id'])):
        brief='Giveaway / leaderboard '+v['text'].split('Listing ID: ')[1].split('\n')[0] if v['category']=='giveaway/leaderboard template' else v['category']+' — '+v['text'].split('\n')[0]
        fmt='video' if 'The post contains a video.' in v['attachment'] else 'text' if v['attachment'].startswith('None.') else 'image/link/quote'
        brief=brief.replace('|','/').replace('\n',' ')[:135]
        mdoc+=f"| [{v['id']}](#{v['id'].lower()}) | Sep {v['day']}, 2026; time unavailable | @{v['handle']} | {brief} / {fmt} | {v['views']:,} | {v['likes']:,} | {v['reposts']:,} | {v['replies']:,} |\n"
    mdoc+='\n## Complete captured posts, date-ordered\n\n'
    for v in sorted(rows,key=lambda q:(q['day'],q['id'])):
        mdoc+=f"<a id=\"{v['id'].lower()}\"></a>\n\n### {v['id']} — {v['name']} (@{v['handle']})\n\n**Date:** September {v['day']}, 2026. **Time:** not shown. **Badge:** {v['badge']}. **Source crops:** {source_link(v['source'])}. **Category:** {v['category']}.\n\n**Attachment / quoted context:** {v['attachment']}\n\n**Visible post text:**\n\n{quote(v['text'])}\n\n{mt(v)}"
        if v['note']: mdoc+='\n**Research note:** '+v['note']+'\n'
        mdoc+='\n'
    (R/'x-mentions-flow.md').write_text(mdoc,encoding='utf-8')
    info={'Name':'Deed Estate','Ticker':'DEED','Contract':CA,'X':'https://x.com/DeedEstate','Website':'https://deed.estate/','ATH':'$4.28M','Lifetime Volume':'$9.29M','gmgn link':f'https://gmgn.ai/robinhood/token/{CA}'}
    (R/'project-info.json').write_text(json.dumps(info,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    data=dict(research_date='2026-09-27',timezone='Europe/Moscow',contract=CA,method='Supplied screenshots; displayed K values expanded; dates without clocks; outer posts deduplicated; nested quotes excluded from totals',account_posts=posts,mention_posts=rows,account_totals=a,mention_totals=mm,reported_market_metrics={'ath_market_cap_usd':4280000,'lifetime_volume_usd':9290000,'status':'Supplied; ATH repeated in captured radar reports; exact lifetime volume not independently verified'})
    (R/'research-data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
if __name__=='__main__':
    print('account',totals(posts))
    print('mentions',totals(rows))
    print('authors',len({x['handle'] for x in rows}),'blue',len({x['handle'] for x in rows if x['badge']=='blue'}),'gold',len({x['handle'] for x in rows if x['badge']=='gold'}))
    for cat in sorted({x['category'] for x in rows}):
        print(cat,totals([x for x in rows if x['category']==cat]))
    print('paid',[(x['id'],x['handle'],x['views']) for x in rows if x['paid_label']])
    write_reports()
