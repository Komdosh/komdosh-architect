---
name: readiness-go-no-go-advisor
description: Assess architecture readiness for implementation, go/no-go conditions, blockers, required validation, accepted risks, unresolved decisions, and escalation needs.
---

# Readiness Go No Go Advisor

## Purpose

Summarize whether the architecture is ready to move forward.
Readiness advice should be clear about conditions, blockers, and accepted risk.

## Required Inputs

Require:

- prioritized risks
- mitigation and validation plan
- current implementation or architecture decision point

## Readiness Levels

Use:

- `Go`: risks are acceptable or have clear owners and validation paths.
- `Conditional go`: proceed only under listed conditions.
- `No-go`: critical risks must be resolved before implementation.
- `Needs decision`: readiness depends on business, compliance, product, or architecture decision.

## Output

Return:

| Area | Readiness | Reason | Condition/blocker | Owner |
|------|-----------|--------|-------------------|-------|

Then provide:

- overall readiness recommendation
- go/no-go conditions
- blockers
- risks accepted for now
- validation required before or during implementation
- escalation needs
