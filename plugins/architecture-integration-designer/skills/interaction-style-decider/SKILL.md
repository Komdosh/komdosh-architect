---
name: interaction-style-decider
description: Choose sync, async, event, command, query, webhook, callback, batch, file, or manual integration style based on ownership, latency, consistency, load, resilience, and support needs.
---

# Interaction Style Decider

## Purpose

Choose the right interaction style for each integration.
The default should not be synchronous calls everywhere.

## Required Inputs

Require:

- integration surfaces or use cases
- service/data ownership
- load or quality constraints when available

## Decision Factors

Consider:

- consumer expectations
- authoritative owner
- latency sensitivity
- consistency need
- failure isolation
- retry and duplicate tolerance
- ordering requirement
- load and fan-out
- human versus machine workflow
- external provider behavior
- support and observability needs

## Style Guidance

- Use synchronous request/response when the caller needs an immediate answer and the dependency is reliable enough.
- Use events for business facts that multiple consumers may react to.
- Use commands for requested changes owned by another component.
- Use webhooks or callbacks when an external system pushes state changes.
- Use batch/file exchange for large volumes, legacy integration, or scheduled reconciliation.
- Use manual operations only when human judgment or exception handling is inherent.

## Output

Return:

| Integration | Recommended style | Why | Tradeoff | Failure mode |
|-------------|-------------------|-----|----------|--------------|

Then list:

- synchronous dependencies to watch
- async/event candidates
- batch/file candidates
- manual fallback paths
- open interaction-style questions
