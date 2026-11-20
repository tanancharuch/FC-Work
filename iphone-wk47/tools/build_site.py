"""Build iphone-wk47/index.html from data/sales.json (made by build_sales.py) and tools/template.html."""
import pathlib

root = pathlib.Path(__file__).resolve().parent.parent
payload = (root / 'data' / 'sales.json').read_text(encoding='utf-8').replace('</', '<\\/')
html = (root / 'tools' / 'template.html').read_text(encoding='utf-8').replace('__DATA__', payload)
(root / 'index.html').write_text(html, encoding='utf-8')
print('wrote', root / 'index.html', len(html), 'bytes')
