export function relativeLink(document: string, href: string) {
  const directory = document.split('/').slice(0, -1).map(encodeURIComponent).join('/');
  return decodeURIComponent(new URL(href, `https://library.local/${directory ? directory + '/' : ''}`).pathname).replace(/^\//, '');
}
export function overviewInfo(content: string): Record<string, string> {
  const info: Record<string, string> = {};
  for (const line of content.split('\n').slice(0, 25)) {
    const clean = line.replace(/^\s*-\s+/, '').replace(/\*\*/g, '').replace(/`/g, '');
    const match = clean.match(/^(Name|Ticker|Contract[^:]*|X|Website|ATH[^:]*|Lifetime [Vv]olume|GMGN):\s*(.+)$/i);
    if (!match) continue;
    const key = match[1].toLowerCase();
    let value = match[2].trim();
    if (['x', 'website', 'gmgn'].includes(key)) value = value.match(/https?:\/\/[^\s)]+/)?.[0] || value;
    else if (key.startsWith('contract')) value = value.match(/0x[a-fA-F0-9]{40}/)?.[0] || value;
    else if (['name', 'ticker'].includes(key)) value = value.replace(/\.$/, '');
    else if (key.startsWith('ath') || key === 'lifetime volume') value = value.split(' — ')[0];
    const normalized = key.startsWith('contract') ? 'Contract' : key.startsWith('ath') ? 'ATH' : ({ name: 'Name', ticker: 'Ticker', x: 'X', website: 'Website', gmgn: 'gmgn link', 'lifetime volume': 'Lifetime Volume' } as Record<string, string>)[key];
    if (normalized) info[normalized] = value;
  }
  return info;
}
