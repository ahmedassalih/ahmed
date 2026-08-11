---
layout: page
permalink: /en/ideas/
lang: en
translation_key: ideas
title: Ideas
seo_title: "Ideas | How Ahmed Assalih thinks about transformation, AI and skills"
eyebrow: Ideas
heading: How I think about the problem
lead: >-
  Expertise is what I have done. This is how I think about it: the method I work with, the
  frameworks behind the book, and the writing where I test both against what I see.
description: >-
  The Logician-Engineer Method, the frameworks from The Death of Skills, and current writing on
  HR transformation, AI and the future of work.
wide: true
contact_cta: true
breadcrumbs:
  - label: Home
    url: /en/
---

<div class="deflist">

  <div class="deflist__row">
    <p class="deflist__term">The Logician-Engineer Method</p>
    <div class="deflist__desc">
      <p>Why complex transformation fails when strategy, architecture, data, processes and
      adoption are treated as separate projects, and the three-stage sequence I use instead:
      diagnose, architect, make it live.</p>
      <p><a class="link-arrow" href="/en/ideas/logician-engineer-method/">Read the method<span aria-hidden="true"> &rarr;</span></a></p>
    </div>
  </div>

  <div class="deflist__row">
    <p class="deflist__term">Frameworks</p>
    <div class="deflist__desc">
      <p>Five frameworks from <em>The Death of Skills</em>: Potential Stack, Time-to-Skill,
      Fortress · Front Line · Laboratory, Trajectory Radar and Pay-for-Agility. Each one frames
      a management question that a skills inventory is not built to answer.</p>
      <p><a class="link-arrow" href="/en/ideas/frameworks/">Explore the frameworks<span aria-hidden="true"> &rarr;</span></a></p>
    </div>
  </div>

  <div class="deflist__row">
    <p class="deflist__term">The book</p>
    <div class="deflist__desc">
      <p>The structured expression of these ideas. <em>The Death of Skills</em> argues that AI
      exposes the limits of skills-based talent models and forces organisations to rethink
      potential, adaptability and learning velocity.</p>
      <p><a class="link-arrow" href="/en/book/">The Death of Skills<span aria-hidden="true"> &rarr;</span></a></p>
    </div>
  </div>

</div>

<h2>Latest insights</h2>

{%- assign lang_posts = site.posts | where: "lang", "en" -%}
{%- assign latest = lang_posts | slice: 0, 6 -%}
<div class="grid grid--3">
  {%- for post in latest %}
    {% include article-card.html post=post lang="en" %}
  {%- endfor %}
</div>

<p class="section__action">
  <a class="link-arrow" href="/en/insights/">View all insights<span aria-hidden="true"> &rarr;</span></a>
</p>
