"""Build iphone-wk47/index.html from data/areas.csv and data/wk47_daily.csv.
Usage: python3 build_site.py "<updated label>"
"""
import csv, json, sys, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
read = lambda p: list(csv.DictReader(open(root / 'data' / p, encoding='utf-8')))
data = {
    'updated': sys.argv[1] if len(sys.argv) > 1 else '',
    'areas': read('areas.csv'),
    'daily': [{**r, 'qty': int(r['qty'])} for r in read('wk47_daily.csv')],
}
payload = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
html = (root / 'tools' / 'template.html').read_text(encoding='utf-8').replace('__DATA__', payload)
(root / 'index.html').write_text(html, encoding='utf-8')
print('wrote', root / 'index.html', len(html), 'bytes;', len(data['daily']), 'daily rows')
