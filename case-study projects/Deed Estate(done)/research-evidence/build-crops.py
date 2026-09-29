from PIL import Image
from pathlib import Path
root=Path(__file__).resolve().parent.parent
out=root/'research-evidence'/'crops'
out.mkdir(parents=True,exist_ok=True)
for p in sorted((root/'x-ca-mentions').glob('*.png')):
    im=Image.open(p)
    print(p.name,im.size)
    # Full-width overlapping tiles preserve the feed and all metrics.
    for i,y in enumerate(range(0,im.height,1400),1):
        im.crop((670,y,1158,min(y+1600,im.height))).save(out/f'{p.stem}-tile-{i:02}.png')
        print(f'{p.stem}-tile-{i:02}.png y={y}:{min(y+1600,im.height)}')
    tiles=sorted(out.glob(f'{p.stem}-tile-*.png'))
    for j in range(0,len(tiles),3):
        sheet=Image.new('RGB',(488*3,1600),'#222222')
        for k,t in enumerate(tiles[j:j+3]):
            sheet.paste(Image.open(t),(k*488,0))
        sheet.save(out/f'{p.stem}-sheet-{j//3+1:02}.png')
for name,filename,box in [
    ('historical-properties','screencapture-x-search-2026-09-27-17_00_11-tile-15.png',(55,705,470,934)),
    ('embedded-followers','screencapture-x-search-2026-09-27-17_00_11-2-tile-05.png',(55,107,470,369)),
    ('historical-home','screencapture-x-search-2026-09-27-17_00_11-3-tile-16.png',(55,465,470,772)),
]:
    im=Image.open(out/filename).crop(box)
    im.resize((im.width*3,im.height*3)).save(out/f'{name}.png')
