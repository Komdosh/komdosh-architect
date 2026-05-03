---
name: data-contract-designer
description: Frame data contract ownership, producer and consumer responsibilities, compatibility, versioning, schema evolution, quality expectations, and consumer impact without final schemas.
---

# Data Contract Designer

## Purpose

Define who owns shared data contracts and how they can evolve.
Data contracts are architecture responsibilities before they are schemas.

## Required Inputs

Require:

- data flows or data boundaries
- producers and consumers
- known external systems or analytics/reporting needs

## Contract Framing

For each contract, identify:

- producer owner
- consumer groups
- business meaning
- authoritative versus derived status
- compatibility expectation
- versioning expectation
- quality expectations such as completeness, timeliness, validity, deduplication, ordering, or nullability at a high level
- privacy and deletion obligations
- change notification responsibility
- consumer breakage risk

## Output

Return:

| Contract | Producer | Consumers | Meaning | Compatibility | Quality expectation | Risk |
|----------|----------|-----------|---------|---------------|---------------------|------|

Then list:

- producer responsibilities
- consumer responsibilities
- versioning assumptions
- deferred schema decisions
- open contract questions
