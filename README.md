# ahmedassalih.com

Jekyll site for Ahmed Assalih — Executive HR Transformation & AI Strategist.
Bilingual (EN / FR), static, no front-end framework.

## Run it

```bash
bundle install
bundle exec jekyll serve            # http://localhost:4000
bundle exec jekyll build --trace    # production-like build into _site/
```

Google Analytics only loads when `JEKYLL_ENV=production`.

## Structure

```
_config.yml        Site identity, book URL, Formspree endpoint, GA id, plugins, defaults
_data/
  home.yml         All homepage copy, EN + FR (rendered by _layouts/home.html)
  navigation.yml   Header and footer navigation per language
  i18n.yml         Interface strings per language
  topics.yml       The five editorial topics (labels EN/FR)
_layouts/          default · page · home · post
_includes/         header, footer, translation, schema, picture, article-card,
                   contact-cta, date, analytics
en/ fr/            Page content, one file per route
_posts/            Articles (EN and FR, paired by translation_key)
assets/
  main.scss        The whole design system (tokens → components → responsive)
  js/site.js       Mobile navigation toggle. That is all the JavaScript there is.
  images/          Every .jpg/.jpeg has a matching .webp sibling
index.html         Language gateway at / (noindex, follow)
```

## Conventions

**Language pairing.** Every page and post carries `lang:` and `translation_key:`.
`_includes/translation.html` resolves the counterpart for the header language
switch and for the `hreflang` tags. When no counterpart exists the switch falls
back to the other language's homepage.

**URLs.** Article permalinks follow `/:categories/:year/:month/:day/:title.html`
and must not change. `timezone: "Etc/GMT-1"` in `_config.yml` matches the `+0100`
offset in every post date so a build on any machine produces the same URLs.
If a URL ever has to change, keep the old one alive with `redirect_from:`.

**Topics.** `categories:` is legacy and only defines the URL. The editorial
taxonomy shown on the site is the single `topic:` key, validated against
`_data/topics.yml`.

**Sources.** A post can declare references in front matter; the article layout
renders them under "Sources & references". Nothing is auto-generated — add only
sources that genuinely exist.

```yaml
sources:
  - label: "Author, Title, Publisher, 2025"
    url: "https://example.org/report"
```

**Images.** Drop the original in `assets/images/`, then generate the WebP sibling
before referencing it — `_includes/picture.html` always emits a `<source>` for
`.webp` and will 404 without one. Reference images through that include:

```liquid
{% include picture.html src="/assets/images/x.jpg" alt="…" width="1408" height="768" %}
```

**Styling.** No inline `style` attributes, no `!important` outside the
reduced-motion block. Reuse the component classes in `assets/main.scss`
(`panel`, `deflist`, `timeline`, `stack`, `callout`, `measure`, `btn`, `card`).

## Root domain

`/` is a language gateway: `noindex, follow`, canonical to `/en/`, explicit EN
and FR links, and a JavaScript redirect based on the browser language. It works
without JavaScript. If the host supports server-side redirects, replacing it
with a 302 from `/` to `/en/` (and `/fr/` by `Accept-Language`) would be
marginally better for crawl efficiency; the gateway is the safe static fallback.
