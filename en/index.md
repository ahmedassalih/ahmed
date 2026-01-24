---
layout: default
title: Home
lang: en
ref: home
---

<!-- 1. HERO SECTION -->
<div style="text-align: center; margin: 40px 0 60px 0;">
  <!-- Photo de profil avec effet lueur -->
  <img src="/assets/images/profile.jpg" alt="Ahmed Assalih" style="width: 120px; height: 120px; object-fit: cover; border-radius: 50%; border: 2px solid rgba(255,255,255,0.2); filter: grayscale(100%); margin-bottom: 20px;">
  
  <h1 style="margin-top: 0; line-height: 1.1;">Strategic HR & AI<br>Architect</h1>
  
  <p style="font-size: 1.2rem; max-width: 600px; margin: 20px auto; color: #aaa;">
    Bridging <strong style="color:white;">Deep Tech</strong>, <strong style="color:white;">Business Reality</strong> & <strong style="color:white;">Human Capital</strong> across EMEA.
  </p>

  <!-- Boutons d'action -->
  <div style="margin-top: 30px;">
    <a href="/en/manifesto" class="btn" style="margin-right: 10px;">The Method</a>
    <a href="/en/contact" class="btn" style="background: transparent; color: white !important; border: 1px solid white;">Audit Request</a>
  </div>
</div>

<!-- 2. HIGHLIGHT GRID (3 articles par ligne) -->
<!-- On utilise minmax(230px) pour faire tenir 3 colonnes dans ton wrapper de 800px -->
<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(230px, 1fr)); gap: 20px; margin-bottom: 60px;">

  <!-- BOUCLE : Articles anglais avec highlight: true, maximum 6 -->
  {% assign featured_posts = site.posts | where: "highlight", true | where: "lang", "en" | slice: 0, 6 %}

  {% for post in featured_posts %}
  <div class="post-item" style="margin-bottom: 0 !important; padding: 0; overflow: hidden; display: flex; flex-direction: column; border: 1px solid rgba(255,255,255,0.1); background: rgba(255,255,255,0.03);">
    
    <!-- IMAGE (Haut de carte) -->
    <a href="{{ post.url }}" style="border-bottom: none;">
      <div style="height: 140px; overflow: hidden; border-bottom: 1px solid rgba(255,255,255,0.1);">
        <img src="{{ post.image | default: '/assets/images/profile.jpg' }}" alt="{{ post.title }}" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s ease;">
      </div>
    </a>

    <!-- CONTENU (Bas de carte) -->
    <div style="padding: 15px; flex-grow: 1; display: flex; flex-direction: column;">
      
      <!-- Date -->
      <div style="font-size: 0.7rem; color: #ff4d4d; margin-bottom: 5px; font-weight: bold; letter-spacing: 1px; text-transform: uppercase;">
        {{ post.date | date: "%b %d, %Y" }}
      </div>

      <!-- Titre -->
      <h3 style="margin: 0 0 8px 0; font-size: 1.1rem; line-height: 1.3; border: none;">
        <a href="{{ post.url }}" style="border: none; color: white;">{{ post.title }}</a>
      </h3>

      <!-- Description -->
      <p style="font-size: 0.85rem; color: #999; margin-bottom: 15px; flex-grow: 1; line-height: 1.5;">
        {% if post.description %}
          {{ post.description | truncate: 80 }}
        {% else %}
          {{ post.excerpt | strip_html | truncatewords: 12 }}
        {% endif %}
      </p>

      <!-- Lien -->
      <a href="{{ post.url }}" style="font-size: 0.8rem; font-weight: bold; color: white; text-transform: uppercase; letter-spacing: 0.5px; border-bottom: none;">Read Analysis →</a>
    </div>

  </div>
  {% endfor %}

</div>

<!-- 3. THE TICKER (Bandeau défilant) -->
<div class="ticker-wrap">
  <div class="ticker">
    <div class="ticker-item">SOPRA HR SOFTWARE <strong>HR TRANSFORMATION MEA REGIONAL DIRECTOR</strong></div>
    <div class="ticker-item">ROYAL AIR MAROC <strong>EX-GROUP HR</strong></div>
    <div class="ticker-item">ENSEEIHT <strong>ENGINEER</strong></div>
    <div class="ticker-item">SPEAKER <strong>FUTURE OF WORK</strong></div>
    <div class="ticker-item">ARCHITECT <strong>AI GOVERNANCE</strong></div>
    <div class="ticker-item">LOCATION <strong>CASABLANCA / EMEA</strong></div>
    <div class="ticker-item">SOPRA HR <strong>REGIONAL DIRECTOR</strong></div>
  </div>
</div>