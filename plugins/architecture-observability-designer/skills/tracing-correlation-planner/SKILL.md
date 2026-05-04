---
name: tracing-correlation-planner
description: Define tracing, correlation IDs, causality, request-to-event-to-job visibility, async flow linking, external dependency tracking, tenant/user-safe identifiers, and diagnostic handoff.
---

# Tracing Correlation Planner

## Purpose

Design how engineers follow one user action across the system.
Tracing and correlation must cover both synchronous calls and asynchronous work.

## Required Inputs

Require:

- integration or service flow context
- observability context inventory
- logging and telemetry needs when available

## Correlation Concerns

Define:

- correlation ID and causation ID needs
- trace boundaries across APIs, services, events, jobs, queues, batches, and external systems
- parent/child flow relationships at architecture level
- tenant, account, user, and request identifiers that are safe to use
- propagation expectations through retries and callbacks
- links between logs, metrics, traces, audit events, and support tickets
- sampling or retention concerns at architecture level
- failure cases where trace continuity breaks

## Output

Return:

| Flow | Correlation need | Boundary crossed | Required identifiers | Diagnostic value | Risk |
|------|------------------|------------------|----------------------|------------------|------|

Then list:

- correlation rules
- async-flow visibility needs
- external-system trace gaps
- safe identifier rules
- open tracing questions
