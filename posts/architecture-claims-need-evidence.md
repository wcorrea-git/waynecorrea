---
title: Architecture Claims Need Evidence
author: Wayne Correa
date: 2026-04-24
updated: 2026-04-24
draft: true
slug: architecture-claims-need-evidence
description: A LinkedIn-ready draft on why compliance narratives need observable, correlated evidence rather than design intent alone.
excerpt: Compliance discussions often begin with architecture diagrams and policy statements. The harder question is whether the evidence behind those claims is strong enough to stand up to scrutiny.
tags:
  - compliance
  - telemetry
  - linkedin
---

Architecture diagrams are useful.

They are not evidence.

That may be the simplest summary of how I now think about data sovereignty and compliance-heavy infrastructure claims.

Most teams begin where they should begin: with design.

They choose regions carefully.

They document controls.

They define approved architectures.

They try to reduce unnecessary exposure.

All of that matters.

But the moment a team moves from "this is how we designed it" to "this is what definitely happened," the standard changes.

That second statement requires evidence.

And in many organizations, that is where the story gets weaker than the slide deck.

This is not because teams are careless or dishonest.

It is because architecture intent is easier to communicate than evidence quality.

Design documents are clean.

Operational reality is not.

Telemetry is partial.

Networks cross control domains.

Provider abstractions hide useful detail.

Different logs describe different parts of the same event.

And the evidence chain is often only obvious once someone asks a very specific question.

For example:

- Can you prove this traffic did not traverse an unapproved jurisdiction?
- Can you show which controls governed failover behavior?
- Can you demonstrate what happened during a specific time window?
- Can you distinguish observed facts from provider assertions and from your own inferences?

Those are harder questions than "Which region did you deploy in?"

They are also increasingly the questions that matter.

This is why I think a more disciplined sovereignty conversation needs three separate buckets:

- intent
- inference
- proof

Intent is what the architecture was designed to do.

Inference is what you reasonably conclude from partial evidence, provider documentation, and known controls.

Proof is what you can defend directly with strong, relevant, time-bound evidence.

The problem is that many organizations collapse all three into one sentence.

That is where confidence gets inflated.

And inflated confidence is dangerous in compliance contexts, because it tends to survive until the moment someone asks for the underlying evidence.

Then the real answer becomes more qualified:

- "We believe the path stayed in-zone based on the architecture."
- "We have some telemetry for portions of the route."
- "We rely on provider controls for part of the assurance."
- "We cannot directly observe every segment."

Those may still be reasonable positions.

But they are not the same as full proof.

I think teams gain credibility when they say that plainly.

A mature compliance posture is not about sounding absolute.

It is about being precise about what is known, what is inferred, and what is not currently observable.

This is also where better evidence practices start to matter more than prettier compliance narratives.

Good evidence usually requires correlation across multiple sources.

No single dashboard is likely to tell the full story.

No single log format is likely to settle the question.

You often need to combine:

- architecture intent
- provider control statements
- flow telemetry
- event timing
- boundary classification
- operational context for reroutes and failovers

And even then, there may still be ambiguity.

That ambiguity should be documented, not hidden.

One of the most useful outcomes of my GeoGuard sandbox was that it made this painfully obvious. The app was never the point. The point was that trying to build a system around geo-boundary evidence forces a more honest answer to a simple question:

How much can we really prove?

That is the question I think more infrastructure teams need to ask before they make strong sovereignty claims.

Because in the end, architecture is only the beginning of the story.

The part that holds up under scrutiny is the evidence behind it.

If you work in cloud, networking, security, or compliance, I think this is where the conversation is heading. The teams that stand out will not just be the ones with stronger architectures. They will be the ones that can explain, clearly and responsibly, the difference between design intent and defensible proof.
