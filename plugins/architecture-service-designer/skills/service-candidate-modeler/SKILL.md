---
name: service-candidate-modeler
description: Identify service, component, module, and deployability candidates from domain capabilities, lifecycles, ownership, quality attributes, and operational constraints.
---

# Service Candidate Modeler

## Purpose

Find reasonable structural units without over-splitting.
Candidates are proposals to evaluate, not final microservice declarations.

## Required Inputs

Require at least one of:

- domain model
- capability map
- scope-boundary brief
- requirements and known external systems

## Candidate Signals

Consider a separate service, component, or module when there is:

- distinct domain responsibility
- clear source-of-truth ownership
- separate lifecycle authority
- different scaling or availability needs
- different security or compliance boundary
- distinct operational ownership or support model
- high change-rate difference
- external integration boundary needing isolation
- policy/rule area that should evolve independently

Prefer one module or component when:

- concepts share one transaction boundary
- ownership is the same
- operational independence is not needed
- splitting would create chatty calls
- the team cannot support distributed operations

## Output

Return:

| Candidate | Type | Responsibility | Why separate or together | Source evidence | Risk |
|-----------|------|----------------|--------------------------|-----------------|------|

Then list:

- candidates to merge
- candidates to split later
- deployability assumptions
- open decomposition questions
