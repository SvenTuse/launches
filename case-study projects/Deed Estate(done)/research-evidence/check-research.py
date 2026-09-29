from pathlib import Path
import json,re
R=Path(__file__).resolve().parent.parent
d=json.loads((R/'research-data.json').read_text(encoding='utf-8'))
expected={'account':(10,1432200,4924,2324,2486),'mention':(169,569515,2542,999,1164)}
for prefix,ee in expected.items():
    rr=d[prefix+'_posts']; got=(len(rr),*[sum(x[k] for x in rr) for k in ['views','likes','reposts','replies']])
    assert got==ee,(prefix,got,ee)
    assert len({x['id'] for x in rr})==len(rr)
    for x in rr: assert abs(x['er_percent']-100*(x['likes']+x['reposts']+x['replies'])/x['views'])<1e-10
    print(prefix,'reconciled',got)
for f in R.glob('*.md'):
    text=f.read_text(encoding='utf-8')
    assert '\ufffd' not in text, f
    bad=[]
    for target in re.findall(r'\]\(([^)]+)\)',text):
        if target.startswith(('http:','https:','#')):continue
        if not (f.parent/target.split('#')[0]).exists():bad.append(target)
    assert not bad,(f,bad)
    print(f.name,'local links checked',len(text),'characters')
why=(R/'whyitsent.md').read_text(encoding='utf-8')
body=why.split('\n\n',1)[1]
sentences=[s for s in re.split(r'(?<=\.)\s+',body.strip()) if s]
assert len(sentences)==3,sentences
assert len(re.findall(r'^### \d+\.',(R/'project-overview.md').read_text(encoding='utf-8'),re.M))==10
assert len(re.findall(r'^### P\d\d —',(R/'X-Flow.md').read_text(encoding='utf-8'),re.M))==10
assert len(re.findall(r'^### M\d\d\d —',(R/'x-mentions-flow.md').read_text(encoding='utf-8'),re.M))==169
assert len(list((R/'research-evidence/crops').glob('*-tile-*.png')))==58
info=json.loads((R/'project-info.json').read_text(encoding='utf-8'))
assert info['gmgn link']=='https://gmgn.ai/robinhood/token/'+info['Contract']
print('Three sentences, ten ideas, every detailed post, 58 crops, JSON validated.')
