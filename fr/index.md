---
layout: default
title: Accueil
lang: fr
ref: home
---

<!-- 1. HERO SECTION (L'Accroche) -->
<div style="text-align: center; margin: 40px 0 60px 0;">
  <img src="/assets/images/profile.jpg" alt="Ahmed Assalih" style="width: 120px; height: 120px; object-fit: cover; border-radius: 50%; border: 2px solid rgba(255,255,255,0.2); filter: grayscale(100%); margin-bottom: 20px;">
  
  <h1 style="margin-top: 0; line-height: 1.1;">Architecte Stratégique<br>RH & IA</h1>
  
  <p style="font-size: 1.2rem; max-width: 600px; margin: 20px auto; color: #aaa;">
    Allier <strong style="color:white;">Deep Tech</strong>, <strong style="color:white;">Réalité Business</strong> & <strong style="color:white;">Capital Humain</strong> en EMEA.
  </p>

  <!-- Boutons d'action rapides -->
  <div style="margin-top: 30px;">
    <a href="/fr/manifesto" class="btn" style="margin-right: 10px;">La Méthode</a>
    <a href="/fr/contact" class="btn" style="background: transparent; color: white !important; border: 1px solid white;">Demander un Audit</a>
  </div>
</div>

<!-- 2. BENTO GRID (Les Cartes) -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-bottom: 60px;">

  <!-- CARTE 1 : DERNIER ARTICLE (Dynamique FR) -->
  <div class="post-item" style="margin-bottom: 0 !important; display: flex; flex-direction: column; justify-content: space-between;">
    <div>
      <span class="post-meta" style="color: #ff4d4d;">● DERNIÈRE ANALYSE</span>
      <!-- Le code ci-dessous va chercher le dernier article marqué lang: fr -->
      {% assign latest_post = site.posts | where: "lang", "fr" | first %}
      <h3 style="margin-top: 10px; border: none; font-size: 1.4rem;">
        <a href="{{ latest_post.url }}">{{ latest_post.title }}</a>
      </h3>
      <p style="font-size: 0.95rem;">{{ latest_post.excerpt | strip_html | truncatewords: 20 }}</p>
    </div>
    <a href="{{ latest_post.url }}" style="font-size: 0.9rem; font-weight: bold; margin-top: 15px; display: block;">Lire l'analyse →</a>
  </div>

  <!-- CARTE 2 : L'AUTORITÉ (Bio) -->
  <div class="post-item" style="margin-bottom: 0 !important; background: linear-gradient(145deg, rgba(255,255,255,0.05), rgba(255,255,255,0.01));">
    <span class="post-meta">AUTORITÉ</span>
    <h3 style="margin-top: 10px; border: none; font-size: 1.4rem;">Ex-DRH Groupe & Ingénieur</h3>
    <ul style="padding-left: 20px; font-size: 0.95rem; color: #aaa; margin-bottom: 20px;">
      <li style="margin-bottom: 8px;">Gestion de <strong>1 900 départs</strong> (Crise).</li>
      <li style="margin-bottom: 8px;">Architecture HR Tech pour <strong>22 Pays</strong>.</li>
      <li>Olympiades de Mathématiques (Logique).</li>
    </ul>
    <a href="/fr/bio" style="font-size: 0.9rem; font-weight: bold;">Voir la Chronologie →</a>
  </div>

</div>

<!-- 3. THE TICKER (Le Bandeau Défilant en bas) -->
<div class="ticker-wrap">
  <div class="ticker">
    <div class="ticker-item">SOPRA HR <strong>DIRECTEUR RÉGIONAL</strong></div>
    <div class="ticker-item">ROYAL AIR MAROC <strong>EX-DRH GROUPE</strong></div>
    <div class="ticker-item">ENSEEIHT <strong>INGÉNIEUR</strong></div>
    <div class="ticker-item">SPEAKER <strong>FUTURE OF WORK</strong></div>
    <div class="ticker-item">ARCHITECTE <strong>GOUVERNANCE IA</strong></div>
    <div class="ticker-item">LOCALISATION <strong>CASABLANCA / EMEA</strong></div>
    <div class="ticker-item">SOPRA HR <strong>DIRECTEUR RÉGIONAL</strong></div>
  </div>
</div>