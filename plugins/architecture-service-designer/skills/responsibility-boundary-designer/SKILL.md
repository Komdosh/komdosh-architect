---
name: responsibility-boundary-designer
description: Assign responsibilities, ownership, source-of-truth boundaries, lifecycle authority, operational ownership, and explicit non-responsibilities for service or component candidates.
---

# Responsibility Boundary Designer

## Purpose

Make each structural unit accountable.
Boundaries are useful only when responsibilities and non-responsibilities are explicit.

## Required Inputs

Require:

- service/component candidates
- domain concepts or capabilities
- known ownership or lifecycle facts

## Responsibility Analysis

For each structural unit, identify:

- owned domain responsibilities
- explicitly not-owned responsibilities
- source-of-truth state
- lifecycle authority
- rules and invariants enforced
- commands accepted
- events published
- queries served
- operational and support ownership
- data visibility and privacy concerns
- failure ownership

## Boundary Rules

- Avoid shared ownership of the same authoritative state.
- Keep read models, caches, and projections distinct from authoritative ownership.
- Do not assign external-system-owned facts to internal services as sources of truth.
- Make cross-boundary mutations explicit.
- State when a component is a module inside a deployable system rather than a separate service.

## Output

Return:

| Unit | Owns | Does not own | Source of truth | Lifecycle authority | Operational owner |
|------|------|--------------|-----------------|---------------------|-------------------|

Then list:

- ownership conflicts
- source-of-truth assumptions
- unclear responsibilities
- boundary risks
