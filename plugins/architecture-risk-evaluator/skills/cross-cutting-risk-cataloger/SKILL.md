---
name: cross-cutting-risk-cataloger
description: Catalog architecture risks across product, technical, data, integration, security, deployment, operations, observability, delivery, decision, support, and maintainability areas.
---

# Cross-Cutting Risk Cataloger

## Purpose

Find risks across architecture areas.
Good risk evaluation avoids focusing only on technology and missing product, data, operations, or delivery failure modes.

## Required Inputs

Require:

- risk context inventory
- architecture brief or stage outputs
- decision context when available

## Risk Areas

Catalog risks in:

- product fit and user workflow
- domain model and scope
- service boundaries and coupling
- data ownership, quality, lifecycle, migration, and privacy
- load, performance, scale, and capacity
- API, event, webhook, batch, and external integrations
- security, authorization, tenant isolation, and abuse
- deployment, reliability, recovery, and rollout
- observability, support, and incident response
- delivery, team capability, timeline, and maintainability
- ADR alignment and decision drift

## Output

Return:

| Risk | Area | Evidence | Impact | Trigger | Initial action |
|------|------|----------|--------|---------|----------------|

Then list:

- risks by area
- missing evidence
- risks caused by decisions
- risks caused by open questions
- duplicate or related risks to merge
