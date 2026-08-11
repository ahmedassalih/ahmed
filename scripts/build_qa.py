#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Build QA for ahmedassalih.com. Run after `bundle exec jekyll build`.

    python scripts/build_qa.py

Checks the generated _site:
  * one H1 per real page, no heading-level jumps
  * <title>, canonical, meta description, hreflang en/fr/x-default
  * every internal href resolves to a real generated file — percent-encoded
    paths are URL-DECODED before being tested against the filesystem, so
    /le-mariage-bris%C3%A9-... is checked against the real accented file
  * every <img src> and <source srcset> resolves; every <img> has alt
  * no escaped structural HTML (&lt;/div&gt; etc.) leaking from malformed markup
  * source pages have balanced <p> and <div> tags
  * sitemap entries resolve to generated files

Standard library only. Exit code 1 on any failure.
"""
from __future__ import print_function

import io
import os
import re
import sys
import collections

try:
    from urllib.parse import unquote, urlsplit
except ImportError:                                    # Python 2
    from urlparse import urlsplit
    from urllib import unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, '_site')

V2_PAGES = [
    'en/index.md', 'en/about.md', 'en/insights.md', 'en/book.md', 'en/speaking.md',
    'en/contact.md', 'en/media-kit.md',
    'en/expertise/index.md', 'en/expertise/executive-leadership.md',
    'en/expertise/hr-transformation.md', 'en/expertise/hr-tech-ai.md',
    'en/ideas/index.md', 'en/ideas/logician-engineer-method.md', 'en/ideas/frameworks.md',
    'fr/index.md', 'fr/a-propos.md', 'fr/analyses.md', 'fr/livre.md',
    'fr/conferences-enseignement.md', 'fr/contact.md', 'fr/media-kit.md',
    'fr/expertise/index.md', 'fr/expertise/leadership-executif.md',
    'fr/expertise/transformation-rh.md', 'fr/expertise/hr-tech-ia.md',
    'fr/idees/index.md', 'fr/idees/methode-ingenieur-logicien.md', 'fr/idees/frameworks.md',
]

# Canonical article URLs that must physically resolve. These are live URLs:
# the source filenames are ASCII, the public URLs stay accented.
ACCENTED_ARTICLE_URLS = [
    '/architecture/2023/02/14/le-mirage-de-la-vitesse-arrêtez-les-chatbots-nettoyez-vos-données.html',
    '/crisis-management/2023/05/22/les-mathématiques-de-lempathie-leçons-de-1-900-départs.html',
    '/strategy/2023/09/10/le-mariage-brisé-pourquoi-dsi-et-drh-ne-parlent-pas-la-même-langue.html',
    '/ai-governance/2024/01/20/la-fuite-invisible-la-montée-du-shadow-ai-en-emea.html',
    '/future-of-work/2024/06/08/brûler-léchelle-la-fin-de-lanalyste-junior.html',
    '/leadership/2024/08/30/adaptabilité-vs-transformation-pourquoi-les-projets-sont-morts.html',
    '/data/2024/11/12/lontologie-du-talent-pourquoi-votre-architecture-de-compétences-échoue.html',
]

ESCAPED_TAGS = re.compile(r'&lt;/?(?:div|p|h[1-6]|section|ul|li|span)&gt;')

problems = collections.defaultdict(list)
stats = collections.Counter()


def resolve(url):
    """Map an internal href to a generated file. Returns a path or None.

    The path component is URL-decoded first: an href written as
    %C3%A9 must be tested against the real 'é' on disk, not compared
    as a literal string.
    """
    parts = urlsplit(url)
    path = unquote(parts.path)
    if not path:
        return 'self'
    fs = os.path.join(SITE, path.lstrip('/').replace('/', os.sep))
    if os.path.isfile(fs):
        return fs
    index = os.path.join(fs, 'index.html')
    if os.path.isdir(fs) and os.path.isfile(index):
        return index
    if os.path.isfile(fs.rstrip(os.sep) + '.html'):
        return fs + '.html'
    return None


def is_redirect(html):
    return 'http-equiv="refresh"' in html


def load_pages():
    pages, redirects = [], []
    for dirpath, _dirs, files in os.walk(SITE):
        for fn in files:
            if not fn.endswith('.html'):
                continue
            p = os.path.join(dirpath, fn)
            html = io.open(p, encoding='utf-8', errors='replace').read()
            (redirects if is_redirect(html) else pages).append((p, html))
    return pages, redirects


def rel(p):
    return os.path.relpath(p, SITE).replace(os.sep, '/')


def main():
    if not os.path.isdir(SITE):
        print('No _site. Run: bundle exec jekyll build')
        return 1

    pages, redirects = load_pages()
    print('Generated: %d content pages, %d redirect stubs\n' % (len(pages), len(redirects)))

    # ---- structure, metadata -------------------------------------------
    for p, html in pages:
        r = rel(p)
        h1 = re.findall(r'<h1[^>]*>', html)
        if len(h1) != 1:
            problems['h1-count'].append('%s -> %d' % (r, len(h1)))
        if not re.search(r'<title>\s*\S', html):
            problems['title'].append(r)
        if 'rel="canonical"' not in html:
            problems['canonical'].append(r)
        if 'name="description"' not in html:
            problems['description'].append(r)
        for lang in ('en', 'fr', 'x-default'):
            if 'hreflang="%s"' % lang not in html:
                problems['hreflang'].append('%s (%s)' % (r, lang))
        levels = [int(m) for m in re.findall(r'<h([1-6])[^>]*>', html)]
        prev = 0
        for lv in levels:
            if prev and lv > prev + 1:
                problems['heading-jump'].append('%s h%d after h%d' % (r, lv, prev))
                break
            prev = lv
        for m in ESCAPED_TAGS.finditer(html):
            problems['escaped-html'].append('%s -> %s' % (r, m.group(0)))

    # ---- links, images --------------------------------------------------
    broken_targets = set()
    for p, html in pages + redirects:
        r = rel(p)
        for m in re.finditer(r'<a\b[^>]*href="([^"]*)"', html):
            href = m.group(1).strip()
            if not href:
                problems['empty-href'].append(r)
                continue
            if href.startswith(('http://', 'https://', 'mailto:', 'tel:', '#')):
                stats['external'] += 1
                continue
            stats['internal'] += 1
            if resolve(href) is None:
                problems['broken-link'].append('%s -> %s' % (r, href))
                broken_targets.add(href)
        for m in re.finditer(r'<img\b[^>]*>', html):
            tag = m.group(0)
            src = re.search(r'src="([^"]*)"', tag)
            if not src or not src.group(1).strip():
                problems['img-no-src'].append(r)
                continue
            stats['img'] += 1
            if not src.group(1).startswith('http') and resolve(src.group(1)) is None:
                problems['broken-img'].append('%s -> %s' % (r, src.group(1)))
                broken_targets.add(src.group(1))
            if 'alt=' not in tag:
                problems['img-no-alt'].append('%s -> %s' % (r, src.group(1)))
        for m in re.finditer(r'<source\b[^>]*srcset="([^"]*)"', html):
            for cand in m.group(1).split(','):
                cand = cand.strip().split(' ')[0]
                if cand and not cand.startswith('http'):
                    stats['source'] += 1
                    if resolve(cand) is None:
                        problems['broken-source'].append('%s -> %s' % (r, cand))
                        broken_targets.add(cand)

    # ---- the seven accented article URLs --------------------------------
    for url in ACCENTED_ARTICLE_URLS:
        target = resolve(url)
        if target is None:
            problems['accented-url-missing'].append(url)
            continue
        html = io.open(target, encoding='utf-8', errors='replace').read()
        can = re.search(r'rel="canonical" href="([^"]+)"', html)
        if not can or unquote(urlsplit(can.group(1)).path) != url:
            problems['accented-url-canonical'].append(url)
        fr = re.search(r'hreflang="fr" href="([^"]+)"', html)
        if not fr or unquote(urlsplit(fr.group(1)).path) != url:
            problems['accented-url-hreflang'].append(url)
        en = re.search(r'hreflang="en" href="([^"]+)"', html)
        if not en or resolve(urlsplit(en.group(1)).path) is None:
            problems['accented-url-en-counterpart'].append(url)
        sw = re.search(r'class="lang-switch" href="([^"]+)"', html)
        if not sw or resolve(sw.group(1)) is None:
            problems['accented-url-switch'].append(url)

    # ---- sitemap --------------------------------------------------------
    sm = os.path.join(SITE, 'sitemap.xml')
    if os.path.isfile(sm):
        xml = io.open(sm, encoding='utf-8').read()
        locs = re.findall(r'<loc>([^<]+)</loc>', xml)
        stats['sitemap'] = len(locs)
        for loc in locs:
            if resolve(urlsplit(loc).path) is None:
                problems['sitemap-unresolved'].append(loc)
    else:
        problems['sitemap-missing'].append('sitemap.xml')

    # ---- source tag balance ---------------------------------------------
    for rel_src in V2_PAGES:
        p = os.path.join(ROOT, rel_src.replace('/', os.sep))
        if not os.path.isfile(p):
            problems['v2-page-missing'].append(rel_src)
            continue
        body = io.open(p, encoding='utf-8').read().split('---', 2)[-1]
        for tag in ('p', 'div'):
            opens = len(re.findall(r'<%s\b' % tag, body))
            closes = len(re.findall(r'</%s>' % tag, body))
            if opens != closes:
                problems['unbalanced-tags'].append(
                    '%s <%s> open=%d close=%d' % (rel_src, tag, opens, closes))

    # ---- report ----------------------------------------------------------
    print('Internal links checked : %d' % stats['internal'])
    print('External links skipped : %d' % stats['external'])
    print('Images checked         : %d' % stats['img'])
    print('WebP sources checked   : %d' % stats['source'])
    print('Sitemap URLs checked   : %d' % stats['sitemap'])
    print('V2 source pages checked: %d' % len(V2_PAGES))
    print('Unique broken targets  : %d\n' % len(broken_targets))

    if problems:
        for key in sorted(problems):
            items = problems[key]
            print('[%s] %d' % (key.upper(), len(items)))
            for item in items[:15]:
                print('   ', item)
            if len(items) > 15:
                print('    ... +%d more' % (len(items) - 15))
            print('')
        return 1

    print('PASS — no problems found.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
