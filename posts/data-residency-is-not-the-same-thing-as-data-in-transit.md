---
title: Data Residency Is Not The Same Thing As Data In Transit
author: Wayne Correa
date: 2026-04-24
updated: 2026-04-24
draft: true
slug: data-residency-is-not-the-same-thing-as-data-in-transit
description: A LinkedIn-ready draft explaining why region selection answers a storage question, not a full sovereignty question.
excerpt: Choosing the right region is often presented as the answer to a sovereignty requirement. In reality, it is only one piece of the story because residency answers a storage question, not a network-path question.
tags:
  - datasovereignty
  - compliance
  - linkedin
---

Choosing the right cloud region is often treated like the end of the conversation.

For many teams, it is really the beginning.

When people talk about data residency, they are usually talking about where workloads are deployed, where storage sits, and which geography is associated with the service configuration.

Those are important questions.

They are just not the only questions anymore.

If the claim is "our data remains in the EU" or "customer traffic stays in-country," that statement carries a meaning that goes beyond storage.

It suggests something about transit.

It suggests something about jurisdiction.

It implies some degree of control over the path data took between endpoints.

That is where the problem starts.

Residency is mostly a storage and placement answer.

Transit is a network answer.

Those are related, but they are not interchangeable.

A workload can be deployed in the right geography and still depend on paths that are difficult to explain with confidence. Traffic can traverse intermediaries, cross provider boundaries, hit control points the customer does not manage directly, or move across backbones that are optimized for resilience and performance rather than customer-visible sovereignty controls.

None of that automatically means a provider failed.

It does mean the language we use is often stronger than the evidence we have.

That gap matters because compliance conversations are shifting.

Customers, auditors, and regulators increasingly want more than a screenshot showing a deployment region. They want to understand what assurances exist for the whole data-handling chain, including movement in transit.

And if we are honest, many organizations are still answering that newer question with an older toolset.

We know how to say:

- "The database is hosted in-region."
- "Backups are confined to approved geographies."
- "The control plane has a regional option."

We are much less consistent when the question becomes:

- "What path did traffic take?"
- "Which jurisdictions did it traverse?"
- "What evidence supports that assertion?"
- "How much of that answer is design intent versus observed proof?"

This is one reason the phrase "data sovereignty" can become muddy so fast.

Different people hear different things:

- legal teams may hear jurisdiction and access
- cloud teams may hear regional deployment
- network teams may hear path control and carrier choices
- auditors may hear documentation and evidence quality

Everyone is partly right, but the discussion breaks down when we collapse those layers into one clean sentence.

That is why I keep coming back to a simple framing:

Data residency is a storage answer.

Data in transit is a path answer.

Data sovereignty is broader than both, because it includes who had control, which legal domains applied, and whether the evidence behind the claim is strong enough to stand up under scrutiny.

The practical issue is not that teams are careless.

The practical issue is that the infrastructure stack is complicated, and many of the networks involved are not fully transparent to the customer consuming the service.

Cloud architectures abstract complexity for good reasons. That abstraction is one reason they are so powerful.

But abstraction also makes it easier to confuse a placement decision with a full proof statement.

That is where I think teams need to get more precise.

There is a meaningful difference between these two claims:

- "We configured the workload to reside in an approved geography."
- "We can prove the relevant traffic remained inside an approved geography."

The first may be true.

The second requires a much higher bar.

It requires telemetry.

It requires correlation.

It requires clarity about what portion of the path you actually control and what portion you can only infer.

That distinction is not just technical hygiene. It is credibility.

If your controls are strong, say so.

If your evidence is partial, say that too.

In sovereignty discussions, overclaiming is usually more dangerous than admitting where the limits are.

That is one of the biggest things my GeoGuard sandbox made concrete for me. Even a rough attempt to model the problem makes it obvious that storage location and transit behavior answer different questions.

The next step is understanding why.

In the next post, I will break down the technical distinction underneath this issue:

Endpoint geography and path geography are different problems.
