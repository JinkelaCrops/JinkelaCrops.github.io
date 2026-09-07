"""Build the static homepage and archived writing with one shared page shell."""
from pathlib import Path
from html import escape
from urllib.parse import quote
import json, re, shutil
ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'src'
ORIGIN = 'https://jinkelacrops.github.io'

def build():
    (ROOT/'assets').mkdir(exist_ok=True)
    for name in ('site.css','site.js'):
        shutil.copyfile(SOURCE/name,ROOT/'assets'/name)
    homepage=(SOURCE/'index.html').read_text()
    (ROOT/'index.html').write_text(homepage)
    header=re.search(r'<header>.*?</header>',homepage,re.S).group(0)
    header=header.replace('href="#main"','href="/"').replace('href="#work"','href="/#work"').replace('href="#notes"','href="/#notes"').replace('href="#about"','href="/#about"')
    header=header.replace('<nav aria-label="Main navigation">','<nav aria-label="Main navigation"><a href="/blog/" data-zh="早期博客" data-en="Archive">早期博客</a>')
    footer=re.search(r'<footer>.*?</footer>',homepage,re.S).group(0)
    def page(title,body,url):
        return f'''<!doctype html>
<html lang="zh-CN" data-theme="light"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)} · JinkelaCrops</title><meta name="description" content="{escape(title,quote=True)} — JinkelaCrops 早期博客"><meta name="color-scheme" content="light dark"><link rel="canonical" href="{ORIGIN}{quote(url)}"><link rel="stylesheet" href="/assets/site.css"></head><body><a class="skip" href="#main">跳至正文</a><div class="wrap">{header}<main id="main" class="writing">{body}</main>{footer}</div><script src="/assets/site.js" defer></script></body></html>'''
    posts=json.loads((SOURCE/'blog/posts.json').read_text())
    output=ROOT/'blog';output.mkdir(exist_ok=True)
    shutil.copytree(SOURCE/'blog/assets',output/'assets',dirs_exist_ok=True)
    rows=[];refs=[]
    for post in posts:
        slug=post['slug'];url=f'/blog/{slug}.html';title=post['title']
        body=(SOURCE/'blog'/f'{slug}.html').read_text()
        if not re.search(r'<h1\b',body): body=f'<h1>{escape(title)}</h1>'+body
        date=post['date'] or '资料存档'
        kind='早期博客' if post['date'] else '原文引用资料'
        intro=f'<div class="article-nav"><a href="/blog/" data-zh="← 全部早期博客" data-en="← All earlier writing">← 全部早期博客</a><span>{escape(date)} / {kind}</span></div>'
        notice='<p class="archive-context" data-zh="历史文章，保留原文。" data-en="Historical writing, preserved in its original language.">历史文章，保留原文。</p>'
        article=page(title,intro+notice+'<article class="prose">'+body+'</article><div class="article-end"><a href="/blog/">← 返回文章列表 / Back to archive</a></div>',url)
        (output/f'{slug}.html').write_text(article)
        (ROOT/post['legacy']).write_text(article)
        row=f'<li><a href="{url}"><time>{escape(date)}</time><span>{escape(title)}</span><span aria-hidden="true">↗</span></a></li>'
        (rows if post['date'] else refs).append(row)
    listing='<div class="archive-heading"><p class="eyebrow">EARLIER WRITING / 2016</p><h1 data-zh="早期博客" data-en="Earlier writing">早期博客</h1><p class="lead" data-zh="学习、生活与探索的早期记录。" data-en="Early notes on learning, life and exploration.">学习、生活与探索的早期记录。</p></div><ol class="post-list">'+''.join(rows)+'</ol><section><h2 data-zh="文中引用的资料" data-en="Referenced reading">文中引用的资料</h2><ol class="post-list">'+''.join(refs)+'</ol></section>'
    (output/'index.html').write_text(page('早期博客',listing,'/blog/'))
    paths=['/','/blog/']+[f"/blog/{p['slug']}.html" for p in posts]
    (ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{ORIGIN}{path}</loc></url>' for path in paths)+'</urlset>\n')
    print(f'Built homepage, archive list, {len(posts)} articles and legacy routes.')

if __name__ == '__main__':
    build()
