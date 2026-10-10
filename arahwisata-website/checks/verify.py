from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import re,json
ROOT=Path(__file__).resolve().parents[1];D=ROOT/'dist';errors=[];pages={}
class Doc(HTMLParser):
 def __init__(self):super().__init__();self.ids=set();self.refs=[];self.labels=[];self.alts=0;self.duplicates=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if 'id' in d:
   if d['id'] in self.ids:self.duplicates.append(d['id'])
   self.ids.add(d['id'])
  if tag=='label' and 'for' in d:self.labels.append(d['for'])
  for k in ['src','href']:
   if k in d:self.refs.append(d[k])
  if tag=='img' and 'alt' not in d:self.alts+=1
for path in D.glob('*.html'):
 p=Doc();p.feed(path.read_text());pages[path.name]=p
 for d in p.duplicates:errors.append(f'{path.name}: duplicate id {d}')
 if p.alts:errors.append(f'{path.name}: missing image alt')
 for lab in p.labels:
  if lab not in p.ids:errors.append(f'{path.name}: label {lab} missing input')
for file,p in pages.items():
 for ref in p.refs:
  u=urlsplit(ref)
  if u.scheme or u.netloc:continue
  local=unquote(u.path) or file;target=D/local
  if not target.exists():errors.append(f'{file}: missing {local}')
  if u.fragment and target.suffix=='.html':
   known=pages.get(target.name)
   if known and u.fragment not in known.ids and not(target.name=='program.html' and u.fragment in ['jejak','penjaga','jeda']):errors.append(f'{file}: missing fragment {ref}')
for code in ['app.js','data.js']:
 for asset in re.findall(r"['\"]([a-z0-9-]+\.(?:webp|jpg))['\"]",(D/code).read_text()):
  if not (D/'assets'/asset).exists():errors.append('Missing JS asset '+asset)
assert len(json.loads((ROOT/'taxa.json').read_text()))==37
assert not errors,'\n'.join(errors)
print(f'PASS: {len(pages)} pages; assets, links, label associations, unique IDs, 37 taxa.')
print(f'Website size: {sum(f.stat().st_size for f in D.rglob("*") if f.is_file())/1024/1024:.2f} MiB')
