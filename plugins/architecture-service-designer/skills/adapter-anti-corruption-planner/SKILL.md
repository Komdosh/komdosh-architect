---
name: adapter-anti-corruption-planner
description: Plan adapter boundaries, anti-corruption layers, translation responsibilities, external provider isolation, and integration ownership for service design.
---

# Adapter Anti-Corruption Planner

## Purpose

Protect the internal domain model from external system language and behavior.
Adapters and anti-corruption layers should be explicit before detailed integration design starts.

## Required Inputs

Require:

- external systems
- structural units
- domain language or concepts
- integration expectations

## Adapter Analysis

For each external boundary, identify:

- external owner
- internal owning component
- translation responsibility
- external vocabulary that must not leak inward
- data mapping or normalization responsibility
- error and retry ownership
- authentication and trust boundary
- provider replacement or multi-provider concern
- manual fallback or support concern

## Output

Return:

| External system | Internal owner | Adapter role | Translation concern | Failure concern | Anti-corruption need |
|-----------------|----------------|--------------|---------------------|-----------------|----------------------|

Then list:

- provider language risks
- adapter ownership assumptions
- integration decisions deferred to later workflow
- open external-boundary questions
