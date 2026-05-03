---
name: data-boundary-modeler
description: Identify data boundary candidates, write model responsibilities, read model responsibilities, reference data, duplicated data, derived data, and data clustering implications.
---

# Data Boundary Modeler

## Purpose

Shape data boundaries before physical schemas.
Data boundaries should follow ownership, lifecycle, invariants, and collaboration needs.

## Required Inputs

Require:

- authoritative data ownership or domain concepts
- service/component candidates when available

## Data Boundary Types

Consider:

- authoritative write model
- read model
- projection
- cache
- search index
- analytics view
- audit/history log
- external reference data
- replicated or duplicated data
- operational reporting data

## Boundary Analysis

For each boundary, identify:

- owner
- purpose
- data subjects included
- data subjects excluded
- lifecycle authority
- consistency need
- freshness expectation
- privacy classification
- likely consumers
- reasons to merge or split

## Output

Return:

| Boundary | Type | Owner | Includes | Excludes | Freshness | Consumers |
|----------|------|-------|----------|----------|-----------|-----------|

Then list:

- write model responsibilities
- read model responsibilities
- reference data rules
- boundary risks and open questions
