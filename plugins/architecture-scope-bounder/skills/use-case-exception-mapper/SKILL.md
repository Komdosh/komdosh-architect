---
name: use-case-exception-mapper
description: Capture high-level use cases, alternate paths, exception paths, boundary events, and top-level information flows without detailed implementation design.
---

# Use Case Exception Mapper

## Purpose

Describe the top-level behavior that makes the boundary meaningful.
Use cases should explain why actors and external systems interact with the system of interest.

## Required Inputs

Require:

- system of interest
- actor list or known roles
- external system list when integrations matter

## Use Case Coverage

Capture:

- primary happy-path use cases
- alternate legitimate paths
- exception paths and failure recovery
- manual intervention paths
- cancellation, reversal, retry, timeout, and compensation paths
- permission-denied and policy-denied paths
- stale, missing, duplicate, invalid, or conflicting data paths
- external provider unavailable or inconsistent paths
- audit, support, and investigation paths

## Use Case Style

Keep use cases high-level:

- name the actor and goal
- state preconditions and trigger
- state the system response
- state resulting state or boundary event
- avoid detailed UI, API, or database design

## Output

Return:

| ID | Use case | Primary actor | Trigger | System response | Boundary event/result |
|----|----------|---------------|---------|-----------------|-----------------------|

Then return:

- alternate paths
- exception paths
- boundary events and information flows
- architecture implications without detailed solution choices
