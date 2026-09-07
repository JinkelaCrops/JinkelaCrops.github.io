from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,unquote
import json,unittest
ROOT=Path(__file__).resolve().parents[1]
class Document(HTMLParser):
    def __init__(self,path):
        super().__init__();self.ids=set();self.refs=[];self.feed(path.read_text())
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        for key in ('id','name'):
            if key in a:self.ids.add(a[key])
        if tag in ('a','img','script','link'):
            value=a.get('src',a.get('href'))
            if value:self.refs.append(value)
class BlogTests(unittest.TestCase):
    def test_internal_links_assets_and_anchors(self):
        for path in [ROOT/'index.html',*list((ROOT/'blog').glob('*.html'))]:
            doc=Document(path)
            for ref in doc.refs:
                u=urlsplit(ref)
                if u.scheme or u.netloc:continue
                target=ROOT/unquote(u.path).lstrip('/') if u.path.startswith('/') else path.parent/unquote(u.path) if u.path else path
                if target.is_dir():target=target/'index.html'
                self.assertTrue(target.is_file(),f'{path.name}: {ref}')
                if u.fragment and target.suffix=='.html':self.assertIn(unquote(u.fragment),Document(target).ids,f'{path.name}: {ref}')
    def test_complete_listing_and_old_urls(self):
        posts=json.loads((ROOT/'src/blog/posts.json').read_text())
        self.assertEqual(sum(bool(p['date']) for p in posts),9)
        listing=Document(ROOT/'blog/index.html')
        for p in posts:
            self.assertIn(f"/blog/{p['slug']}.html",listing.refs)
            self.assertEqual((ROOT/p['legacy']).read_bytes(),(ROOT/'blog'/f"{p['slug']}.html").read_bytes())
    def test_shared_style_and_no_legacy_scripts(self):
        for p in (ROOT/'blog').glob('*.html'):
            s=p.read_text();self.assertIn('/assets/site.css',s);self.assertIn('/assets/site.js',s)
            self.assertNotIn('cdnjs.cloudflare.com',s);self.assertNotIn('github.io/tree/',s)
