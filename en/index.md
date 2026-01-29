---
layout: default
title: Home
lang: en
ref: home
---

<!-- 1. HERO SECTION IMMERSIVE (RESPONSIVE) -->
<div class="hero-container" style="border-radius: 0 !important; overflow: hidden;">
  <!-- Image centrée sur le visage -->
  <img src="/assets/images/profile.jpg" alt="Ahmed Assalih" class="hero-image" style="border-radius: 0 !important; object-position: 50% 20% !important;">
  
  <div class="hero-overlay">
    <!-- Utilisation de la nouvelle classe CSS -->
    <div class="hero-content">
      
      <h1 class="hero-title">
        Strategic HR & AI<br>Architect
      </h1>
      
      <p class="hero-subtitle">
        Bridging Deep Tech, Business Reality & Human Capital.
      </p>

      <!-- BOUTONS -->
      <div style="display: flex; gap: 10px; flex-wrap: wrap;">
        <a href="/en/manifesto" class="btn" style="background: white; color: black; border: none; border-radius: 0 !important; text-transform: uppercase; letter-spacing: 1px; font-weight: 800;">The Method</a>
        <a href="/en/contact" class="btn" style="background: rgba(0,0,0,0.6); color: white !important; border: 1px solid rgba(255,255,255,0.4); backdrop-filter: blur(5px); border-radius: 0 !important;">Audit Request</a>
      </div>
    </div>
  </div>
</div>

<!-- 2. HIGHLIGHT GRID (Reste du contenu) -->
<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 25px; margin-bottom: 60px;">
  <!-- BOUCLE : Articles anglais avec highlight: true -->
  {% assign featured_posts = site.posts | where: "highlight", true | where: "lang", "en" | slice: 0, 6 %}

  {% for post in featured_posts %}
  <div class="post-item" style="margin-bottom: 0 !important; padding: 0; overflow: hidden; display: flex; flex-direction: column; border-radius: 0 !important;">
    <a href="{{ post.url }}" style="border-bottom: none;">
      <div style="height: 160px; overflow: hidden; border-bottom: 1px solid rgba(255,255,255,0.1);">
        <img src="{{ post.image | default: '/assets/images/profile.jpg' }}" alt="{{ post.title }}" style="width: 100%; height: 100%; object-fit: cover; border-radius: 0 !important; transition: transform 0.3s ease;">
      </div>
    </a>
    <div style="padding: 20px; flex-grow: 1; display: flex; flex-direction: column;">
      <div style="font-size: 0.75rem; color: #ff4d4d; margin-bottom: 8px; font-weight: bold; letter-spacing: 1px; text-transform: uppercase;">
        {{ post.date | date: "%b %d, %Y" }}
      </div>
      <h3 style="margin: 0 0 10px 0; font-size: 1.2rem; line-height: 1.3; border: none;">
        <a href="{{ post.url }}" style="border: none; color: white;">{{ post.title }}</a>
      </h3>
      <p style="font-size: 0.9rem; color: #aaa; margin-bottom: 20px; flex-grow: 1;">
        {% if post.description %}
          {{ post.description | truncate: 100 }}
        {% else %}
          {{ post.excerpt | strip_html | truncatewords: 15 }}
        {% endif %}
      </p>
      <a href="{{ post.url }}" style="font-size: 0.85rem; font-weight: bold; color: white; text-transform: uppercase; letter-spacing: 0.5px;">Read Analysis →</a>
    </div>
  </div>
  {% endfor %}
</div>

<!-- 3. THE TICKER -->
<div class="ticker-wrap">
  <div class="ticker">
    <div class="ticker-item">SOPRA HR <strong>REGIONAL DIRECTOR</strong></div>
    <div class="ticker-item">ROYAL AIR MAROC <strong>EX-GROUP CHRO</strong></div>
    <div class="ticker-item">ENSEEIHT <strong>ENGINEER</strong></div>
    <div class="ticker-item">SPEAKER <strong>FUTURE OF WORK</strong></div>
    <div class="ticker-item">ARCHITECT <strong>AI GOVERNANCE</strong></div>
    <div class="ticker-item">LOCATION <strong>CASABLANCA / EMEA</strong></div>
  </div>
</div>