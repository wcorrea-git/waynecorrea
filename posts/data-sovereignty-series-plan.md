---
title: Data Sovereignty Series Plan
author: Wayne Correa
date: 2026-04-24
updated: 2026-04-24
draft: true
slug: data-sovereignty-series-plan
description: Internal planning document for the data sovereignty LinkedIn post series.
excerpt: Planning document covering the positioning, thesis, and post structure for the data sovereignty series.
tags:
  - datasovereignty
  - planning
---

# Data Sovereignty Blog Series Plan

## Working Topic

I built a sandbox application for an AI product management class, but the real story was what the project exposed about data sovereignty.

The class assignment was to use AI tools to design, build, and deploy a working application with a frontend and backend. Instead of building a generic productivity app, I used the project to explore a problem I already cared about from work: how to reason about data sovereignty, especially the difference between proving where data is at rest and proving where it moves in transit.

`GeoGuard` is part of the setup, not the main subject. It should appear as a sandbox tool I built to test ideas around geo-boundaries, network flows, telemetry, and evidence. The blog series itself is about the bigger problem: why data sovereignty becomes much harder once you move from storage and region selection to path, transit, jurisdiction, and proof.

## Series Positioning

### Series umbrella

Data residency is a storage answer, not a network answer.

### Technical backbone

Endpoint geography and path geography are different problems.

### Editorial tone and proof standard

Compliance claims only matter if they are grounded in technical evidence.

## Core Thesis

We got good at talking about where workloads live. We are still weak at proving where traffic went.

Choosing the right cloud region can help with residency, but it does not fully answer:

- what path traffic took
- which jurisdictions it traversed
- which intermediate control points handled it
- whether the evidence is strong enough to defend to an auditor, customer, or regulator

The sandbox project matters because trying to build even a rough tool around these questions immediately exposes the gap between architecture intent and evidence-backed proof.

## Role Of GeoGuard In The Story

GeoGuard should be referenced as:

- a class project
- a sandbox experiment
- a way to pressure-test assumptions
- a lab instrument for exploring telemetry and geo-boundary evidence

GeoGuard should not be framed as:

- a finished product
- a production-ready compliance platform
- the center of the narrative
- the point of the series

Useful recurring phrasing:

- I built a sandbox app to test the assumption.
- The app was not the point; the problem it exposed was.
- Building the tool forced me to ask what network evidence can actually prove.
- The exercise made the sovereignty gap more concrete than any slide deck or policy document.

## Why This Series Works

- It starts with a personal and credible hook.
- It uses the AI class project as an entry point without becoming a build diary.
- It lets me demonstrate technical range without sounding like I am pitching a startup.
- It connects product thinking, AI-assisted building, network architecture, and sovereignty policy.
- It gives room for both strategic and deeply technical posts.

## Research Direction

The series should keep returning to these questions:

- Why is region selection often treated as sufficient proof?
- What can common network telemetry actually prove about geography?
- Where do endpoint location and path location diverge?
- How much of sovereignty is architecture intent versus verifiable evidence?
- What role can network providers play in improving sovereign path control?
- What still remains unprovable or ambiguous even with better controls?

## Important Technical Angle: FlexAlgo And Sovereign Path Classes

A network provider that uses Segment Routing and FlexAlgo on its backbone can help, but only as part of the answer.

What it can help with:

- defining path classes such as EU-only, Canada-only, Brazil-first, or non-US-when-possible
- constraining traffic to nodes and links that fit a geography or policy domain
- making sovereign routing intent more operational than cloud region choice alone
- keeping failover inside the same policy domain when the topology allows it

What it does not solve by itself:

- proving the full end-to-end path everywhere
- proving what happened inside hyperscaler backbones
- proving what happened outside the provider-controlled segment
- replacing the need for telemetry, correlation, and evidence

This is a useful recurring distinction for the series:

- FlexAlgo-style provider fabric helps with intent
- telemetry and correlation help with proof

That distinction reinforces the larger thesis that architecture claims and evidence claims are not the same thing.

## Planned Series Structure

## Post 1: The Class Project Was The Setup, Not The Story

### Objective

Introduce the AI product management class assignment, why I chose this topic, and how building a sandbox app opened a much larger question about data sovereignty.

### Key points

- The assignment required a working app built with AI tools.
- I deliberately chose a problem that overlaps with my real work interests.
- I started with a simple idea: can I build something that analyzes network-flow-style data against geo boundaries?
- Very quickly, the project stopped being about the app and became about the limits of common sovereignty assumptions.

### Purpose in the series

Establishes credibility, creates a personal hook, and opens the deeper argument without overselling GeoGuard.

## Post 2: Data Residency Is Not The Same Thing As Data In Transit

### Objective

Challenge the common assumption that picking the right region is enough.

### Key points

- Residency questions are usually framed around storage and deployment location.
- Sovereignty questions increasingly include transit, jurisdiction, and control.
- A workload can be deployed in the right region and still rely on network paths that are hard to explain or defend.
- The language enterprises use is often stronger than the evidence they actually have.

### Purpose in the series

This is the main umbrella argument and likely the broadest audience post.

## Post 3: Endpoint Geography Versus Path Geography

### Objective

Explain the technical distinction between where a service is located and where traffic actually travels.

### Key points

- Endpoint compliance and transit compliance are different.
- Flow logs often prove only one segment of a path.
- NAT, proxies, load balancers, CDNs, anycast, private backbones, and interconnects complicate path claims.
- Modeling allowed locations is relatively straightforward; proving path stayed in-zone is much harder.

### Purpose in the series

This is the main technical backbone of the series and likely the strongest differentiation piece.

## Post 4: Can A Sovereign Backbone Help?

### Objective

Explore whether a network provider using Segment Routing and FlexAlgo can materially improve the sovereignty problem.

### Key points

- Why hyperscaler networking is optimized for performance and resilience, not customer-controlled sovereign path policy.
- How a provider-controlled backbone could expose sovereign path classes.
- Why that helps with intent and operational control.
- Why intent is still not proof.
- Why observability and evidence are still required even when path policy improves.

### Purpose in the series

Adds architectural depth and a practical “what can be done now” angle.

## Post 5: Architecture Claims Need Evidence

### Objective

Close the series on the difference between design intent, dashboards, and defensible proof.

### Key points

- Compliance narratives often outrun the underlying telemetry.
- Missing telemetry is not proof of compliance.
- Good evidence requires multiple sources and careful correlation.
- Auditors, customers, and regulators increasingly ask for proof, not just design diagrams.
- My sandbox project was useful because it made those proof gaps impossible to ignore.

### Purpose in the series

Sets the tone of rigor and keeps the series from turning into marketing or vague commentary.

## Writing Guidelines For The Series

- Use GeoGuard briefly and strategically, mostly in intros, transitions, and lessons learned.
- Keep the spotlight on the sovereignty problem, not the app.
- Prefer concrete examples over abstract compliance language.
- Distinguish clearly between intent, inference, and proof.
- Avoid pretending hard path questions are already solved.
- Use a thoughtful practitioner tone rather than a founder pitch tone.

## Potential One-Sentence Series Description

This series starts with a sandbox app I built for an AI product management class and uses that project as a lens for a much bigger question: how do we prove where data traveled, not just where it was stored?

## Recommended Next Step

When starting fresh in the posts folder, use this document as the source of truth and expand each planned post into:

- audience
- working title
- opening hook
- core argument
- 3 to 5 supporting sections
- examples from the GeoGuard sandbox only where they sharpen the larger point
