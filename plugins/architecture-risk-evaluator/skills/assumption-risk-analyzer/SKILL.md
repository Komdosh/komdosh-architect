---
name: assumption-risk-analyzer
description: Identify architecture assumptions that can fail, their impact, confidence, validation signal, owner, decision dependency, and fallback path.
---

# Assumption Risk Analyzer

## Purpose

Find assumptions that could break the architecture.
Assumptions are risks when the design depends on them and they are not proven.

## Required Inputs

Require:

- risk context inventory
- architecture brief or assumptions list

## Assumption Checks

Analyze:

- product and user behavior assumptions
- load, traffic, latency, storage, and growth assumptions
- external system behavior
- data quality and ownership assumptions
- security, compliance, privacy, and tenant assumptions
- platform, deployment, reliability, and operations assumptions
- team capability, timeline, and delivery assumptions
- assumptions inherited from ADRs or prior decisions

## Output

Return:

| Assumption | Design depends on it? | Failure impact | Confidence | Validation signal | Owner |
|------------|------------------------|----------------|------------|-------------------|-------|

Then list:

- assumptions to validate first
- assumptions safe to accept for now
- assumptions needing business or stakeholder input
- fallback paths
- open assumption questions
