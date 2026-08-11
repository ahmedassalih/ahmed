---
layout: page
permalink: /fr/contact/
lang: fr
translation_key: contact
title: Contact
seo_title: "Contacter Ahmed Assalih | Direction, conseil, conférences, enseignement"
eyebrow: Contact
heading: Engager la conversation
lead: >-
  Ouvert à des opportunités de direction sélectionnées, des missions stratégiques, des
  conférences et des collaborations académiques sur la zone EMEA.
description: >-
  Contacter Ahmed Assalih pour une opportunité de direction, une mission de conseil ou de
  transformation, une conférence ou une collaboration académique.
wide: true
breadcrumbs:
  - label: Accueil
    url: /fr/
---

<div class="stack stack--2">
  <div>
    <div class="measure">
      <p>Plus le contexte est précis (organisation, situation, calendrier), plus la première
      réponse sera utile. Les messages me parviennent directement.</p>
    </div>

    <form class="form" action="{{ site.forms.contact_action }}" method="POST">
      <input type="hidden" name="_language" value="fr">
      <input type="hidden" name="_source_page" value="{{ page.url }}">
      <input type="hidden" name="_subject" value="ahmedassalih.com: nouveau message (FR)">

      <div class="field">
        <label class="field__label" for="name">Nom <span class="field__req" aria-hidden="true">*</span></label>
        <input type="text" id="name" name="name" autocomplete="name" required>
      </div>

      <div class="field">
        <label class="field__label" for="email">Email professionnel <span class="field__req" aria-hidden="true">*</span></label>
        <input type="email" id="email" name="email" autocomplete="email" required>
      </div>

      <div class="field">
        <label class="field__label" for="organisation">Organisation</label>
        <input type="text" id="organisation" name="organisation" autocomplete="organization">
      </div>

      <div class="field">
        <label class="field__label" for="reason">Motif du contact <span class="field__req" aria-hidden="true">*</span></label>
        <select id="reason" name="reason" required>
          <option value="Opportunité de direction">Opportunité de direction</option>
          <option value="Conseil / transformation stratégique">Conseil / transformation stratégique</option>
          <option value="Conférence / média">Conférence / média</option>
          <option value="Enseignement / collaboration académique">Enseignement / collaboration académique</option>
          <option value="Autre">Autre</option>
        </select>
      </div>

      <div class="field">
        <label class="field__label" for="message">Message <span class="field__req" aria-hidden="true">*</span></label>
        <textarea id="message" name="message" required></textarea>
        <span class="field__hint">Contexte, calendrier, et ce qu’un bon résultat signifierait.</span>
      </div>

      <button class="btn btn--primary" type="submit">Envoyer le message</button>
    </form>
  </div>

  <div>
    <h2>Les sujets qui reviennent</h2>
    <div class="deflist">
      <div class="deflist__row">
        <p class="deflist__term">Direction &amp; leadership</p>
        <div class="deflist__desc"><p>Postes de direction régionaux et internationaux en
        transformation RH, technologie RH et direction d’activité.</p></div>
      </div>
      <div class="deflist__row">
        <p class="deflist__term">Conseil</p>
        <div class="deflist__desc"><p>Modèle opérationnel cible, choix de solution, diagnostic
        de programme et gouvernance des transformations complexes.</p></div>
      </div>
      <div class="deflist__row">
        <p class="deflist__term">Conférences &amp; médias</p>
        <div class="deflist__desc"><p>Keynotes, masterclasses, tables rondes, interviews et
        prises de parole sur l’IA, les compétences et le futur du travail.</p></div>
      </div>
      <div class="deflist__row">
        <p class="deflist__term">Enseignement</p>
        <div class="deflist__desc"><p>Masters, executive education, conception de cours et
        collaboration académique.</p></div>
      </div>
    </div>

    <h2>Ailleurs</h2>
    <div class="measure">
      <ul>
        <li><a href="{{ site.profile.linkedin }}" rel="noopener">LinkedIn</a>, le moyen le plus
        simple d’engager une conversation professionnelle.</li>
        <li><a href="/fr/media-kit/">Media kit</a>, biographies, photographies et positionnement
        pour organisateurs et journalistes.</li>
      </ul>
      <p>Basé à Casablanca. Actif sur la zone MEA et en Europe.</p>
    </div>
  </div>
</div>
