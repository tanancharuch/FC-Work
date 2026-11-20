"""Build iphone-wk47/index.html from data/sales.json (made by build_sales.py) and tools/template.html."""
import pathlib

root = pathlib.Path(__file__).resolve().parent.parent
import json
data = json.loads((root / 'data' / 'sales.json').read_text(encoding='utf-8'))
tp = root / 'data' / 'targets.json'
if tp.exists():
    data['targets'] = json.loads(tp.read_text(encoding='utf-8'))
np = root / 'data' / 'north_targets.json'
if np.exists():
    data['north'] = json.loads(np.read_text(encoding='utf-8'))
payload = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
html = (root / 'tools' / 'template.html').read_text(encoding='utf-8').replace('__DATA__', payload)
(root / 'index.html').write_text(html, encoding='utf-8')
print('wrote', root / 'index.html', len(html), 'bytes')
