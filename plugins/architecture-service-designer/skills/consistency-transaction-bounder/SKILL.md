---
name: consistency-transaction-bounder
description: Identify transaction boundaries, consistency expectations, idempotency-sensitive paths, retries, compensation, process ownership, and distributed consistency risks for service design.
---

# Consistency Transaction Bounder

## Purpose

Clarify where consistency must be strong and where process-level or eventual consistency is acceptable.
This prevents service decomposition from breaking business invariants.

## Required Inputs

Require:

- service/component responsibilities
- rules, invariants, and lifecycles
- collaborations or use cases

## Boundary Analysis

Identify:

- invariants requiring same-boundary enforcement
- commands that must be atomic
- state transitions owned by one component
- cross-boundary workflows requiring process ownership
- eventual-consistency candidates
- idempotency-sensitive commands or callbacks
- retry, timeout, and compensation expectations
- duplicate, stale, missing, or out-of-order event risks
- manual recovery or support intervention needs

## Output

Return:

| Scenario | Consistency need | Boundary owner | Pattern expectation | Risk | Later decision |
|----------|------------------|----------------|---------------------|------|----------------|

Then list:

- same-boundary invariants
- process-managed workflows
- eventual consistency assumptions
- idempotency requirements
- unresolved consistency tradeoffs
