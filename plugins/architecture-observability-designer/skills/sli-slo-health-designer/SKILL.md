---
name: sli-slo-health-designer
description: Define user-visible health, SLIs, SLOs, error budgets, availability, latency, correctness, freshness, durability, and critical journey success signals at architecture level.
---

# SLI SLO Health Designer

## Purpose

Define how the system knows it is healthy from the user's point of view.
Internal uptime is not enough when users care about successful outcomes.

## Required Inputs

Require:

- observability context inventory
- user journeys or business workflows
- load, latency, availability, or support expectations when available

## Health Concerns

Define:

- critical user-visible journeys
- SLIs for availability, latency, correctness, freshness, durability, and completion
- SLO targets or target ranges when known
- error-budget meaning at architecture level
- synthetic checks or boundary probes when useful
- dependency health versus product health
- degradation indicators and partial outage signals
- ownership and review cadence

## Output

Return:

| Journey/capability | User-visible health | SLI | Target/SLO | Owner | Risk |
|--------------------|---------------------|-----|------------|-------|------|

Then list:

- most important health signals
- SLO assumptions
- dependency signals that affect user health
- missing measurements
- open SLI/SLO questions
