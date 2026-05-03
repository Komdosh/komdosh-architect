---
name: dependency-rule-planner
description: Define dependency direction, allowed coupling, forbidden shortcuts, shared-kernel constraints, layering rules, and service collaboration guardrails for maintainable architecture.
---

# Dependency Rule Planner

## Purpose

Prevent structural erosion.
Service and component boundaries need dependency rules so implementation does not silently collapse the architecture.

## Required Inputs

Require:

- structural units
- responsibilities
- collaborations
- external systems or platform dependencies when relevant

## Dependency Rules

Define:

- allowed dependency directions
- forbidden direct dependencies
- allowed shared libraries or shared kernels
- rules for shared data access
- rules for cross-boundary calls
- rules for event consumption and publication
- rules for adapters and external providers
- rules for operational tooling and admin access
- migration or legacy coexistence constraints

## Coupling Risks

Watch for:

- shared database coupling
- cyclic service calls
- chatty synchronous collaboration
- hidden write ownership through read models
- reused domain objects across boundaries
- platform dependency leaking into domain components
- external provider concepts replacing internal domain language

## Output

Return:

| Rule | Applies to | Allowed | Forbidden | Rationale |
|------|------------|---------|-----------|-----------|

Then list:

- coupling risks
- dependency exceptions
- enforcement suggestions for later implementation planning
- open dependency questions
