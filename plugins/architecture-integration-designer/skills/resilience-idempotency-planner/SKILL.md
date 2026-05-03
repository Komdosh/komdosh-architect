---
name: resilience-idempotency-planner
description: Define idempotency, retries, timeouts, rate limits, backpressure, circuit breaking, compensation, ordering, duplicate handling, and failure ownership for integration design.
---

# Resilience Idempotency Planner

## Purpose

Make integration failure semantics explicit.
Integrations fail, retry, duplicate, timeout, and overload; architecture must define who owns that behavior.

## Required Inputs

Require:

- integration surfaces
- interaction styles
- load or external dependency constraints when available

## Resilience Concerns

For each integration, define:

- timeout expectation
- retry ownership
- idempotency key or idempotency boundary need
- duplicate handling
- ordering expectation
- rate limit and quota behavior
- backpressure or load shedding
- circuit breaker or fallback need
- compensation or reversal path
- dead-letter or manual recovery owner
- user-visible failure behavior

## Output

Return:

| Integration | Idempotency need | Retry owner | Timeout/rate limit | Compensation | Failure owner |
|-------------|------------------|-------------|--------------------|--------------|---------------|

Then list:

- high-risk retry paths
- idempotency-sensitive commands
- backpressure needs
- manual recovery paths
- validation metrics
