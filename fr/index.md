---
layout: default
title: Accueil
lang: fr
ref: home
---

<!-- 1. HERO SECTION IMMERSIVE -->
<div class="hero-container">
  <!-- L'Image de fond -->
  <img src="/assets/images/profile.jpg" alt="Ahmed Assalih" class="hero-image">
  
  <!-- Le Dégradé + Texte par dessus -->
  <div class="hero-overlay">
    <div style="max-width: 800px;">
      <h1 style="margin: 0 0 10px 0; line-height: 1; font-size: 3.5rem; color: white; text-shadow: 0 2px 10px rgba(0,0,0,0.5);">
        Architecte Stratégique<br>RH & IA
      </h1>
      
      <p style="font-size: 1.2rem; color: #ddd; margin-bottom: 25px; font-weight: 300;">
        Allier Deep Tech, Réalité Business & Capital Humain.
      </p>

      <!-- Boutons intégrés dans l'image -->
      <div style="display: flex; gap: 15px;">
        <a href="/fr/manifesto" class="btn" style="background: white; color: black; border: none;">La Méthode</a>
        <a href="/fr/contact" class="btn" style="background: rgba(0,0,0,0.6); color: white !important; border: 1px solid rgba(255,255,255,0.4); backdrop-filter: blur(5px);">Demander un Audit</a>
      </div>
    </div>
  </div>
</div>
<!-- 2. HIGHLIGHT GRID (3 articles par ligne) -->
<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(230px, 1fr)); gap: 20px; margin-bottom: 60px;">

  <!-- BOUCLE : Articles français avec highlight: true, maximum 6 -->
  {% assign featured_posts = site.posts | where: "highlight", true | where: "lang", "fr" | slice: 0, 6 %}

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
      
      <!-- Date FR -->
      <div style="font-size: 0.7rem; color: #ff4d4d; margin-bottom: 5px; font-weight: bold; letter-spacing: 1px; text-transform: uppercase;">
        {{ post.date | date: "%d" }}
        {% assign m = post.date | date: "%-m" %}
        {% case m %}
          {% when '1' %}jan{% when '2' %}fév{% when '3' %}mar{% when '4' %}avr{% when '5' %}mai{% when '6' %}juin{% when '7' %}juil{% when '8' %}août{% when '9' %}sep{% when '10' %}oct{% when '11' %}nov{% when '12' %}déc{% endcase %}
        {{ post.date | date: "%Y" }}
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
      <a href="{{ post.url }}" style="font-size: 0.8rem; font-weight: bold; color: white; text-transform: uppercase; letter-spacing: 0.5px; border-bottom: none;">Lire l'analyse →</a>
    </div>

  </div>
  {% endfor %}

</div>

<!-- 3. THE TICKER (Bandeau défilant) -->
<div class="ticker-wrap">
  <div class="ticker">
    <div class="ticker-item">SOPRA HR SOFTWARE <strong>DIRECTEUR RÉGIONAL HR TRANSFORMATION MEA</strong></div>
    <div class="ticker-item">ROYAL AIR MAROC <strong>EX-RH GROUPE</strong></div>
    <div class="ticker-item">ENSEEIHT <strong>INGÉNIEUR</strong></div>
    <div class="ticker-item">SPEAKER <strong>FUTURE OF WORK</strong></div>
    <div class="ticker-item">ARCHITECTE <strong>GOUVERNANCE IA</strong></div>
    <div class="ticker-item">LOCALISATION <strong>CASABLANCA / EMEA</strong></div>
    <div class="ticker-item">SOPRA HR <strong>DIRECTEUR RÉGIONAL</strong></div>
  </div>
</div>