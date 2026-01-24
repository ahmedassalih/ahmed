---
layout: page
title: Analyses & Doctrine
permalink: /fr/blog/
lang: fr
---

# La Perspective de l'Ingénieur
Analyses sur l'Architecture RH, la Gouvernance IA et le Leadership Deep Tech.

<div class="post-list">
  {% for post in site.posts %}
    {% if post.lang == "fr" %}
    <div class="post-item" style="margin-bottom: 40px; border-bottom: 1px solid #333; padding-bottom: 20px;">
      <span class="post-meta" style="color: #666; font-size: 0.9rem;">
        {% assign m = post.date | date: "%-m" %}
        {{ post.date | date: "%-d" }}
        {% case m %}
          {% when '1' %}janvier
          {% when '2' %}février
          {% when '3' %}mars
          {% when '4' %}avril
          {% when '5' %}mai
          {% when '6' %}juin
          {% when '7' %}juillet
          {% when '8' %}août
          {% when '9' %}septembre
          {% when '10' %}octobre
          {% when '11' %}novembre
          {% when '12' %}décembre
        {% endcase %}
        {{ post.date | date: "%Y" }}
      </span>
      <h3>
        <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
      </h3>
      {% if post.description %}
        <p style="color: #aaa;">{{ post.description }}</p>
      {% else %}
        <p style="color: #aaa;">{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
      {% endif %}
      <a href="{{ post.url | relative_url }}" style="font-size: 0.9rem; text-decoration: underline;">Lire l'analyse →</a>
    </div>
    {% endif %}
  {% endfor %}
</div>