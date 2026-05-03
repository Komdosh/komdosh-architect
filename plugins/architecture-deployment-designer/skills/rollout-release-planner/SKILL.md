---
name: rollout-release-planner
description: Define rollout, rollback, canary, blue-green, feature flag, migration, schema compatibility, deployment ordering, release gates, and support strategy at architecture level.
---

# Rollout Release Planner

## Purpose

Design how changes reach production safely.
Release strategy must cover rollback, compatibility, migrations, and operational ownership before CI/CD implementation.

## Required Inputs

Require:

- runtime topology
- API/integration contracts when available
- data migration or stateful dependency context when available

## Rollout Concerns

Define:

- release strategy: rolling, canary, blue-green, dark launch, or phased rollout
- rollback strategy and rollback limits
- deployment ordering across services, workers, consumers, and stateful dependencies
- feature flag and configuration rollout expectations
- database migration compatibility rules
- API/event/schema compatibility during rollout
- operational gates, health checks, and smoke validation
- user-visible impact and support readiness
- emergency fix path
- release owner and approval boundary

## Output

Return:

| Change area | Rollout strategy | Compatibility rule | Rollback path | Gate/metric | Owner |
|-------------|------------------|--------------------|---------------|-------------|-------|

Then list:

- deployment ordering
- migration safety rules
- rollback limits
- release validation checks
- open rollout questions
