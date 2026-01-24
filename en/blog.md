---
layout: page
title: Insights & Doctrine
permalink: /en/blog/
lang: en
---

# The Engineer's Perspective
Analysis on HR Architecture, AI Governance, and Deep Tech Leadership.

<div class="post-list">
  {% for post in site.posts %}
    {% if post.lang == "en" %}
    <div class="post-item" style="margin-bottom: 40px; border-bottom: 1px solid #333; padding-bottom: 20px;">
      <span class="post-meta" style="color: #666; font-size: 0.9rem;">{{ post.date | date: "%b %-d, %Y" }}</span>
      <h3>
        <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
      </h3>
      {% if post.description %}
        <p style="color: #aaa;">{{ post.description }}</p>
      {% else %}
        <p style="color: #aaa;">{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
      {% endif %}
      <a href="{{ post.url | relative_url }}" style="font-size: 0.9rem; text-decoration: underline;">Read Analysis →</a>
    </div>
    {% endif %}
  {% endfor %}
</div>