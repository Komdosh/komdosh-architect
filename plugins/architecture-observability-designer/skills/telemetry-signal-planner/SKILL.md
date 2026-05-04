---
name: telemetry-signal-planner
description: Define decision-useful metrics, events, business signals, product signals, security signals, operational signals, ownership, aggregation, cardinality risks, and signal purpose.
---

# Telemetry Signal Planner

## Purpose

Define which signals are worth collecting.
A signal should support a decision, alert, dashboard, diagnosis, compliance need, or product improvement.

## Required Inputs

Require:

- observability context inventory
- SLI/SLO decisions when available
- service, load, security, or business context when available

## Signal Concerns

Define:

- technical metrics: traffic, errors, latency, saturation, queue depth, job outcomes, dependency health
- business and product signals
- security and abuse signals
- operational events and lifecycle events
- ownership and audience
- aggregation level and cardinality risk
- thresholds or review expectations
- signals that should not be collected because they add noise or risk

## Output

Return:

| Signal | Type | Purpose | Owner | Decision/action | Risk |
|--------|------|---------|-------|-----------------|------|

Then list:

- essential signals
- signals tied to SLOs
- business/security signals
- high-cardinality or high-cost risks
- open signal questions
