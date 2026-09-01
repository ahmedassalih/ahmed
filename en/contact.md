---
layout: page
permalink: /en/contact/
lang: en
translation_key: contact
title: Contact
seo_title: "Contact Ahmed Assalih | Advisory, speaking and teaching"
eyebrow: Contact
heading: Start a conversation
lead: >-
  Open to selected strategic assignments, speaking and academic collaborations across EMEA.
description: >-
  Contact Ahmed Assalih about strategic transformation and advisory, speaking and media, or
  teaching and academic collaboration.
wide: true
breadcrumbs:
  - label: Home
    url: /en/
---

<div class="stack stack--2">
  <div>
    <div class="measure">
      <p>If you would like to discuss a transformation challenge, a speaking engagement or an
      academic collaboration, you can write to me here. Messages come straight to me, and a
      little context about your situation and timing helps me give you a useful answer.</p>
    </div>

    <form class="form" action="{{ site.forms.contact_action }}" method="POST">
      <input type="hidden" name="_language" value="en">
      <input type="hidden" name="_source_page" value="{{ page.url }}">
      <input type="hidden" name="_subject" value="ahmedassalih.com: new message (EN)">

      <div class="field">
        <label class="field__label" for="name">Name <span class="field__req" aria-hidden="true">*</span></label>
        <input type="text" id="name" name="name" autocomplete="name" required>
      </div>

      <div class="field">
        <label class="field__label" for="email">Professional email <span class="field__req" aria-hidden="true">*</span></label>
        <input type="email" id="email" name="email" autocomplete="email" required>
      </div>

      <div class="field">
        <label class="field__label" for="organisation">Organisation</label>
        <input type="text" id="organisation" name="organisation" autocomplete="organization">
      </div>

      <div class="field">
        <label class="field__label" for="reason">Reason for contact <span class="field__req" aria-hidden="true">*</span></label>
        <select id="reason" name="reason" required>
          <option value="Strategic advisory / transformation">Strategic advisory / transformation</option>
          <option value="Speaking / media">Speaking / media</option>
          <option value="Teaching / academic collaboration">Teaching / academic collaboration</option>
          <option value="Other">Other</option>
        </select>
      </div>

      <div class="field">
        <label class="field__label" for="message">Message <span class="field__req" aria-hidden="true">*</span></label>
        <textarea id="message" name="message" required></textarea>
        <span class="field__hint">Context, timing and what a good outcome would look like.</span>
      </div>

      <button class="btn btn--primary" type="submit">Send message</button>
    </form>
  </div>

  <div>
    <h2>What people write about</h2>
    <div class="deflist">
      <div class="deflist__row">
        <p class="deflist__term">Advisory</p>
        <div class="deflist__desc"><p>Target operating model, technology selection, programme
        diagnostics and governance for complex transformations.</p></div>
      </div>
      <div class="deflist__row">
        <p class="deflist__term">Speaking &amp; media</p>
        <div class="deflist__desc"><p>Keynotes, masterclasses, round tables, interviews and
        commentary on AI, skills and the future of work.</p></div>
      </div>
      <div class="deflist__row">
        <p class="deflist__term">Teaching</p>
        <div class="deflist__desc"><p>Master's programmes, executive education, course design
        and academic collaboration.</p></div>
      </div>
    </div>

    <h2>Elsewhere</h2>
    <div class="measure">
      <ul>
        <li><a href="{{ site.profile.linkedin }}" rel="noopener">LinkedIn</a>, the simplest
        place to open a professional conversation.</li>
        <li><a href="/en/media-kit/">Media kit</a>, bios, photography and speaker positioning
        for organisers and journalists.</li>
      </ul>
      <p>Based in Casablanca. Working across MEA and Europe.</p>
    </div>
  </div>
</div>
