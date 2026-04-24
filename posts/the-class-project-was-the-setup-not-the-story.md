---
title: The Class Project Was The Setup, Not The Story
author: Wayne Correa
date: 2026-04-24
updated: 2026-04-24
draft: true
slug: the-class-project-was-the-setup-not-the-story
description: A LinkedIn-ready draft about how an AI class project opened a larger question about data sovereignty and proof.
excerpt: I built a sandbox app for an AI product management class, but the more interesting outcome was not the app. It was the gap the exercise exposed between where data is stored and what we can actually prove about where it traveled.
tags:
  - datasovereignty
  - cloudnetworking
  - linkedin
---

I built a sandbox app for an AI product management class, but the more interesting outcome was not the app.

It was the gap the exercise exposed.

The assignment was straightforward: use AI tools to design, build, and deploy a working application with a frontend and backend.

I could have picked a generic workflow problem or a lightweight productivity use case. Instead, I chose a question that overlaps with the kind of infrastructure and compliance problems I already care about:

How do you reason about data sovereignty in a way that goes beyond a region label on a dashboard?

That question turned into a sandbox project I called GeoGuard.

But GeoGuard is not really the story.

The story is what happened when I tried to build even a rough tool around geo-boundaries, network flows, and compliance evidence.

Very quickly, I ran into a distinction that I think many teams still blur together:

Data residency is about where data is stored.

Data sovereignty is increasingly about whether you can defend where data moved, which jurisdictions it traversed, and what technical evidence supports that claim.

That sounds obvious when you say it out loud.

In practice, it is still common to hear strong statements like:

- "The workload is in-region."
- "The data stays in-country."
- "We selected the compliant cloud region."

Those statements may be directionally useful, but they are not always evidence-backed answers.

Building the sandbox app forced me to ask better questions:

- What does ordinary telemetry actually prove?
- What does it only suggest?
- Where do endpoint location and path location diverge?
- What would I need to show an auditor, customer, or regulator if they asked for more than an architecture diagram?

That was the real value of the class project.

It turned an abstract concern into a concrete engineering and product problem.

Once I started modeling traffic, control points, and geo-boundaries, the problem became much less theoretical. It became easier to see how quickly the gap opens between architecture intent and defensible proof.

You can make a good-faith design decision to keep a workload in a given geography.

You can even document that intent clearly.

But proving what happened in transit is a different standard entirely.

And that is where the topic gets interesting.

For me, the class project was useful because it created a forcing function.

Instead of debating the problem in the abstract, I had to translate it into a working system:

- What evidence would I ingest?
- How would I classify geographic policy boundaries?
- What kinds of claims could the system make responsibly?
- Where would the uncertainty remain?

That last question matters.

One of the fastest ways to lose credibility in compliance-heavy topics is to overstate what the data can prove.

The sandbox was helpful precisely because it made those limits impossible to ignore.

It also reinforced something I think applies broadly to AI-assisted building:

AI can help you ship faster, but it also removes excuses.

Once the cost of building a rough tool drops, you can pressure-test your assumptions much earlier. You find out faster whether your idea survives contact with real data, real edge cases, and real proof standards.

That is what happened here.

I started with a class assignment and a sandbox app.

I ended up with a much larger question:

Why are we still so much better at talking about where workloads live than proving where traffic went?

That is the thread I want to pull on in this series.

GeoGuard will show up as a lab instrument, not as the hero of the story. The point is not that I built an app. The point is that building it exposed how much harder sovereignty becomes once you move from storage to transit, from architecture to evidence, and from intent to proof.

If you work in cloud, networking, security, or compliance, I think this gap is only going to matter more.

The next post will start with the most important distinction in the whole conversation:

Data residency is not the same thing as data in transit.
