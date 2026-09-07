from pathlib import Path
from html.parser import HTMLParser
import unittest
ROOT = Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.ids=set(); self.links=[]; self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.add(a['id'])
        if tag in ('a','link','script'):
            self.links.append(a.get('href',a.get('src','')))
class WebsiteTests(unittest.TestCase):
    def test_navigation_and_local_assets(self):
        p=Page((ROOT/'index.html').read_text())
        for link in p.links:
            if link.startswith('#'): self.assertIn(link[1:],p.ids)
            elif link.startswith('/'): self.assertTrue(((ROOT/link.lstrip('/')).is_file() or (ROOT/link.lstrip('/')/'index.html').is_file()),link)
    def test_published_copy_matches_source(self):
        self.assertEqual((ROOT/'index.html').read_bytes(),(ROOT/'src/index.html').read_bytes())
        for name in ['site.css','site.js']:
            self.assertEqual((ROOT/'assets'/name).read_bytes(),(ROOT/'src'/name).read_bytes())
    def test_release_boundary(self):
        s=(ROOT/'index.html').read_text()
        self.assertNotIn('noindex',s);self.assertNotIn('DESIGN PREVIEW',s)
        self.assertIn('公开版规划',s)
        self.assertNotIn('github.com/JinkelaCrops/codex_audit_loop',s)
        self.assertIn('https://jinkelacrops.github.io/',s)
        self.assertEqual(s.count('<details>'),6)
