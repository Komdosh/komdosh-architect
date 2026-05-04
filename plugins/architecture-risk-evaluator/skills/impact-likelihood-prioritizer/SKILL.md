---
name: impact-likelihood-prioritizer
description: Prioritize architecture risks by likelihood, impact, urgency, confidence, blast radius, reversibility, detectability, and decision deadline.
---

# Impact Likelihood Prioritizer

## Purpose

Rank risks so the architect knows what matters now.
Prioritization should make tradeoffs explicit and avoid treating every risk as urgent.

## Required Inputs

Require:

- risk catalog
- source context or risk evidence

## Ranking Factors

Score or label:

- likelihood
- impact
- urgency
- confidence
- blast radius
- reversibility
- detectability
- cost of delay
- decision deadline
- affected users, teams, systems, or data

Use simple labels such as `High`, `Medium`, `Low`, and explain important rankings.

## Output

Return:

| Risk | Likelihood | Impact | Urgency | Confidence | Priority | Why |
|------|------------|--------|---------|------------|----------|-----|

Then list:

- top risks
- low-priority risks to monitor
- risks needing more evidence
- risks with high blast radius
- risks that are reversible enough to defer
