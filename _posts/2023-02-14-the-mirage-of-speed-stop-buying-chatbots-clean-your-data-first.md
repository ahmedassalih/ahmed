---
layout: post
title: "The Mirage of Speed: Stop Buying Chatbots, Clean Your Data First"
date: 2023-02-14 09:00:00 +0100
categories: architecture
lang: en
description: "I audited a major bank in Dubai yesterday. They wanted Generative AI. They needed a data sanitation strategy."
image: /assets/images/the-mirage-of-speed-stop-buying-chatbots-clean-your-data-first.jpeg
---

I was in a boardroom in Dubai yesterday. The energy was palpable. The CHRO was excited, showing me a demo of a "Revolutionary HR Copilot" that promised to answer any employee question instantly. "It's like magic," he told me.

I asked one simple, architectural question: **"Which database does it query to find the vacation balance?"**

Silence.
Then the CTO leaned in and spoke the truth: "Well, we have three different SAP instances, a legacy Oracle system for the acquisition we made last year, and a local Excel file for the Egypt office."

**The Verdict**

If you deploy this bot today, it will not be intelligent. It will be a liar. It will tell an employee they have 20 days off when they actually have 5. Why? Because AI is not a magic wand that fixes broken infrastructure. It is a magnifier.

If your data is messy, AI will just generate mess faster.

**The Architectural Reality**

We often confuse "User Interface" with "Intelligence". A chatbot is just a UI. The intelligence lives in the data layer. Before you spend a single dollar on LLMs (Large Language Models), you need to invest in your API strategy and your Data Ontology.

1.  **Map your sources:** Where does the truth live?
2.  **Clean the swamp:** You cannot build a skyscraper on quicksand.
3.  **Governance:** Who owns the data when the AI hallucinates?

As an engineer, my rule is simple: **No AI without API.** Before you buy the magic, build the plumbing.
