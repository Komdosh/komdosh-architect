---
name: read-model-projection-planner
description: Plan read models, projections, search indexes, reporting views, analytics datasets, cache responsibilities, freshness targets, rebuildability, and derived-data ownership.
---

# Read Model Projection Planner

## Purpose

Separate authoritative writes from read concerns.
Read models can improve usability and performance, but they must not blur source-of-truth ownership.

## Required Inputs

Require:

- functional use cases or query needs
- data ownership or boundaries
- known reporting, search, analytics, or operational needs

## Projection Types

Consider:

- user-facing read model
- search index
- operational dashboard
- reporting dataset
- analytics event stream or fact table candidate
- cache
- export view
- support or audit view

## Projection Analysis

For each derived view, identify:

- consumer
- business question answered
- source data owners
- freshness target
- rebuildability
- deletion and privacy propagation
- failure or lag impact
- whether stale data is acceptable
- owner of projection logic

## Output

Return:

| Projection/read model | Consumer | Sources | Freshness | Rebuildable | Stale-data risk |
|-----------------------|----------|---------|-----------|-------------|-----------------|

Then list:

- projection candidates
- search/reporting/analytics candidates
- cache rules
- derived-data ownership assumptions
