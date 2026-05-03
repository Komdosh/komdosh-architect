---
name: concept-relationship-modeler
description: Identify core domain concepts, relationships, concept types, ownership candidates, source-of-truth candidates, cardinality hints, and domain risks without creating implementation schemas.
---

# Concept Relationship Modeler

## Purpose

Model the important business concepts and how they relate.
The result should help later architecture steps reason about ownership and decomposition without becoming a database model.

## Required Inputs

Require:

- domain glossary or product/domain context
- bounded scope or system of interest

## Concept Types

Classify concepts at architecture level:

- entity: has continuity and identity over time
- value: describes something and is replaceable
- policy: decides eligibility, permissions, rules, pricing, routing, or behavior
- event: business fact that happened
- command: request for business change
- actor: human or system participant
- external concept: owned outside the system of interest
- read concern: derived view or lookup need

## Relationship Analysis

For each concept, identify:

- responsibility
- lifecycle ownership
- source-of-truth candidate
- relationship to other concepts
- cardinality hints when useful
- dependency on external systems
- business criticality
- ambiguity or instability

## Output

Return:

| Concept | Type | Responsibility | Source-of-truth candidate | Key relationships | Risk |
|---------|------|----------------|---------------------------|-------------------|------|

Then list:

- relationship notes
- ownership candidates
- concepts that should stay outside the boundary
- unstable concepts that block service decomposition
