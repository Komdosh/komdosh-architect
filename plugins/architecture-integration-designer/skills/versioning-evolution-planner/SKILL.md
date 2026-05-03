---
name: versioning-evolution-planner
description: Define API and integration versioning, compatibility, deprecation, sunset, migration, consumer communication, support, and future extension policy.
---

# Versioning Evolution Planner

## Purpose

Plan how contracts evolve.
Interfaces are durable promises; future development, maintenance, and support depend on explicit evolution rules.

## Required Inputs

Require:

- integration surfaces
- consumer groups
- API/event/batch contract strategy

## Evolution Policy

Define:

- versioning model
- additive change rules
- breaking change criteria
- deprecation policy
- sunset policy
- consumer migration expectations
- compatibility testing responsibility
- documentation and changelog responsibility
- old-version support window
- telemetry needed to know who uses a contract
- exception path for urgent security or compliance changes

## Breaking Change Examples

Treat these as breaking unless explicitly scoped:

- removing fields, events, endpoints, or files
- renaming fields or changing meaning
- making optional fields required
- narrowing enum/state values
- changing error semantics
- changing ordering, retry, or idempotency semantics
- reducing rate limits or retention without migration support

## Output

Return:

| Surface | Versioning model | Additive rule | Breaking-change rule | Deprecation window | Owner |
|---------|------------------|---------------|----------------------|--------------------|-------|

Then list:

- compatibility rules
- deprecation and sunset policy
- consumer migration plan
- support and documentation duties
- open lifecycle questions
