---
layout: page
permalink: /fr/analyses/
lang: fr
translation_key: insights
title: Analyses
seo_title: "Analyses | Transformation RH, IA et futur du travail"
eyebrow: Analyses
heading: Notes de terrain sur la transformation, l’IA et le travail
lead: >-
  Ce que j’écris entre deux programmes, sur la transformation RH, la technologie RH,
  l’intelligence artificielle et les compétences.
description: >-
  Toutes les analyses d’Ahmed Assalih sur la transformation RH, l’IA et les RH, l’architecture
  HR Tech, le futur du travail et les compétences, le leadership et le changement.
wide: true
contact_cta: true
redirect_from:
  - /fr/blog/
breadcrumbs:
  - label: Accueil
    url: /fr/
---

{%- assign posts = site.posts | where: "lang", "fr" -%}

<div class="archive__filters" role="list">
  {%- for topic in site.data.topics %}
    {%- assign count = posts | where: "topic", topic[0] | size -%}
    {%- if count > 0 %}
    <span class="archive__filter" role="listitem">{{ topic[1].fr }} <span aria-hidden="true">·</span> {{ count }}</span>
    {%- endif %}
  {%- endfor %}
</div>

<div class="archive__list">
  {%- for post in posts %}
  {%- assign words = post.content | number_of_words -%}
  {%- assign minutes = words | divided_by: 200 | plus: 1 -%}
  <article class="archive__item">
    <div>
      <p class="archive__meta">
        {%- assign topic = site.data.topics[post.topic].fr -%}
        {%- if topic %}<span class="tag">{{ topic }}</span>{% endif %}
        <span class="card__date">
          <time datetime="{{ post.date | date_to_xmlschema }}">{% include date.html d=post.date lang="fr" %}</time>
          <span aria-hidden="true">·</span> {{ minutes }} min de lecture
        </span>
      </p>
      <h2 class="archive__title"><a href="{{ post.url }}">{{ post.title }}</a></h2>
    </div>
    <div>
      <p class="archive__summary">
        {%- if post.description %}{{ post.description | strip_html | truncate: 190 }}
        {%- else %}{{ post.excerpt | strip_html | normalize_whitespace | truncate: 190 }}{% endif %}
      </p>
    </div>
  </article>
  {%- endfor %}
</div>
