#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Editorial and identity guard for ahmedassalih.com.

Run from the repository root:

    python scripts/editorial_qa.py          # source files
    python scripts/editorial_qa.py --site   # also scan the generated _site

FAIL  — incorrect identity data or a claim we have decided not to make.
WARN  — absolute or quantified phrasing worth re-reading in context. Warnings
        are informational: hedged usage ("tends to", "often") is fine, and the
        script cannot judge context on its own.

Standard library only, no dependencies.
"""
from __future__ import print_function

import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOURCE_DIRS = ['en', 'fr', '_data', '_includes', '_layouts', 'scripts']
SOURCE_FILES = ['_config.yml', 'index.html', '404.html', 'robots.txt', 'README.md']
POSTS_DIR = '_posts'
EXTENSIONS = ('.md', '.html', '.yml', '.yaml', '.txt')

# --------------------------------------------------------------------------
#  Must never appear: wrong identity data, or positioning we have retired.
# --------------------------------------------------------------------------
FORBIDDEN = [
    (r'linkedin\.com/in/ahmedassalih',   'wrong LinkedIn slug — the profile is linkedin.com/in/aassalih'),
    (r'(?i)\bex-?group chro\b',          'inaccurate title'),
    (r'(?i)\bgroup chro\b',              'inaccurate title — use "Head of HR"'),
    (r'(?i)\bex-?drh groupe\b',          'titre inexact'),
    (r'(?i)\bdrh groupe\b',              'titre inexact — utiliser "responsable RH"'),
    (r'(?i)€\s?2[.,]5\s?M',              'retired P&L figure'),
    (r'(?i)not accepting full-time',     'retired positioning'),
    (r"(?i)n[’']accepte pas de rôles",   'positionnement retiré'),
    (r'(?i)order of magnitude',          'unsupported quantification'),
    (r'(?i)un ordre de grandeur',        'quantification non étayée'),
    (r'(?i)\(draft\)',                   'draft marker in public content'),
    (r'(?i)\(brouillon\)',               'marqueur brouillon en contenu public'),
    (r'(?i)audit request',               'retired global CTA'),
    (r'(?i)demander un audit',           'CTA global retiré'),
]

# --------------------------------------------------------------------------
#  Must be present exactly as configured.
# --------------------------------------------------------------------------
REQUIRED_IN_CONFIG = [
    ('https://www.linkedin.com/in/aassalih/', 'canonical LinkedIn URL'),
    ('twitter: aassalih',                     'X / Twitter handle'),
    ('contact@ahmedassalih.com',              'contact email'),
    ('G-EYSSJGHC2F',                          'Google Analytics id'),
    ('https://formspree.io/f/mbdgwvnl',       'Formspree endpoint'),
]

# --------------------------------------------------------------------------
#  Worth a second look. Not failures.
# --------------------------------------------------------------------------
WATCH = [
    r'\balways\b', r'\bnever\b', r'\binevitably\b', r'\bguarantees\b',
    r'\bensures\b', r'\bproves\b', r'the reality is', r'the truth is',
    r'\bmost (?:organisations|companies|programmes|executives)\b',
    r'\btoujours\b', r'\bjamais\b', r'\binévitablement\b', r'\bgarantit\b',
    r'\bprouve\b', r'la réalité est', r'la vérité est',
    r'la plupart des (?:organisations|entreprises|programmes|dirigeants)',
]


def collect(scan_site):
    files = []
    for name in SOURCE_FILES:
        p = os.path.join(ROOT, name)
        if os.path.isfile(p):
            files.append(p)
    dirs = list(SOURCE_DIRS) + [POSTS_DIR]
    if scan_site:
        dirs.append('_site')
    for d in dirs:
        base = os.path.join(ROOT, d)
        for dirpath, _dirnames, filenames in os.walk(base):
            for fn in filenames:
                if fn.endswith(EXTENSIONS) or (scan_site and fn.endswith('.html')):
                    files.append(os.path.join(dirpath, fn))
    return files


def main():
    scan_site = '--site' in sys.argv
    files = collect(scan_site)
    failures, warnings = [], []

    self_path = os.path.abspath(__file__)
    for path in files:
        if os.path.abspath(path) == self_path:
            continue          # this file quotes the patterns it looks for
        rel = os.path.relpath(path, ROOT).replace('\\', '/')
        try:
            text = io.open(path, encoding='utf-8', errors='replace').read()
        except IOError:
            continue
        lines = text.split('\n')
        for pattern, reason in FORBIDDEN:
            rx = re.compile(pattern)
            for i, line in enumerate(lines, 1):
                if rx.search(line):
                    failures.append((rel, i, reason, line.strip()[:100]))
        if not scan_site or not rel.startswith('_site'):
            for pattern in WATCH:
                rx = re.compile(pattern, re.IGNORECASE)
                for i, line in enumerate(lines, 1):
                    if rx.search(line):
                        warnings.append((rel, i, line.strip()[:100]))

    config = io.open(os.path.join(ROOT, '_config.yml'), encoding='utf-8').read()
    for needle, label in REQUIRED_IN_CONFIG:
        if needle not in config:
            failures.append(('_config.yml', 0, 'missing %s' % label, needle))

    print('Scanned %d files.\n' % len(files))
    if warnings:
        print('WARN — review in context (%d):' % len(warnings))
        for rel, i, line in warnings:
            print('  %s:%d  %s' % (rel, i, line))
        print('')
    if failures:
        print('FAIL (%d):' % len(failures))
        for rel, i, reason, line in failures:
            print('  %s:%d  %s' % (rel, i, reason))
            print('      %s' % line)
        return 1
    print('PASS — no forbidden identity strings or retired claims found.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
