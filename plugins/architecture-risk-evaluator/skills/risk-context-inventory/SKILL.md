---
name: risk-context-inventory
description: Identify architecture source context, evaluation boundary, decisions, assumptions, constraints, stakeholders, delivery context, coverage gaps, and risk categories to evaluate.
---

# Risk Context Inventory

## Purpose

Define what the risk evaluation covers.
Risk work is useful only when the source context, scope, and gaps are visible.

## Required Inputs

Require at least one of:

- architecture brief or design proposal
- stage outputs from requirements, scope, service, data, integration, deployment, security, or observability
- decision-context brief or ADR context
- implementation readiness question

## Inventory Coverage

Consider:

- architecture scope and stage
- source documents and missing sources
- decisions already made
- assumptions and open questions
- business, product, compliance, timeline, budget, team, and support constraints
- known external systems and dependencies
- validation already done
- risk categories to include or exclude

## Output

Return:

| Area | Source | Known? | Risk relevance | Coverage gap |
|------|--------|--------|----------------|--------------|

Then list:

- evaluation boundary
- trusted sources
- missing context
- risk categories in scope
- confidence limits
