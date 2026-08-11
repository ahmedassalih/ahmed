---
layout: page
permalink: /en/insights/
lang: en
translation_key: insights
title: Insights
seo_title: "Insights | Writing on HR transformation, AI and the future of work"
eyebrow: Insights
heading: Field notes on transformation, AI and work
lead: >-
  Analysis written from inside programmes rather than from the outside looking in — on HR
  transformation, HR technology architecture, artificial intelligence and skills.
description: >-
  All articles by Ahmed Assalih on HR transformation, AI and HR, HR Tech architecture, the
  future of work and skills, leadership and change.
wide: true
contact_cta: true
redirect_from:
  - /en/blog/
breadcrumbs:
  - label: Home
    url: /en/
---

{%- assign posts = site.posts | where: "lang", "en" -%}

<div class="archive__filters" role="list">
  {%- for topic in site.data.topics %}
    {%- assign count = posts | where: "topic", topic[0] | size -%}
    {%- if count > 0 %}
    <span class="archive__filter" role="listitem">{{ topic[1].en }} <span aria-hidden="true">·</span> {{ count }}</span>
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
        {%- assign topic = site.data.topics[post.topic].en -%}
        {%- if topic %}<span class="tag">{{ topic }}</span>{% endif %}
        <span class="card__date">
          <time datetime="{{ post.date | date_to_xmlschema }}">{% include date.html d=post.date lang="en" %}</time>
          <span aria-hidden="true">·</span> {{ minutes }} min read
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
