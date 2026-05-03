---
name: runtime-topology-designer
description: Define deployment units, runtime processes, stateless/stateful boundaries, compute/runtime choices, worker/job placement, control-plane dependencies, and topology responsibilities at architecture level.
---

# Runtime Topology Designer

## Purpose

Define what runs as deployable runtime units.
The topology should make ownership, scaling, isolation, and operational behavior clear without becoming platform manifests.

## Required Inputs

Require:

- deployment context inventory
- service/component design
- load or SLO context when available

## Topology Concerns

Define:

- deployment units and their purpose
- stateless services versus stateful components
- API, worker, scheduler, consumer, admin, and background-job separation
- runtime/process isolation needs
- compute/runtime expectation at architecture level
- dependency direction between runtime units
- startup, readiness, liveness, and graceful shutdown expectations
- co-location or separation rationale
- horizontal versus vertical scaling expectation
- operational owner and support boundary

## Output

Return:

| Deployment unit | Runtime role | State | Scaling model | Key dependencies | Owner |
|-----------------|--------------|-------|---------------|------------------|-------|

Then list:

- topology decisions
- units that must be isolated
- units that can scale independently
- operational control points
- deferred platform implementation decisions
