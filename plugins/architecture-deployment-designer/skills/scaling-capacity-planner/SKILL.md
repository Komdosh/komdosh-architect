---
name: scaling-capacity-planner
description: Define deployment scaling units, autoscaling signals, capacity headroom, quotas, bottlenecks, worker concurrency, queue backlogs, external dependency limits, and cost guardrails.
---

# Scaling Capacity Planner

## Purpose

Translate load estimates into deployment scaling behavior.
Scaling design must be clear enough to protect bottlenecks and costs before platform rules are implemented.

## Required Inputs

Require:

- runtime topology
- load estimate or expected workload
- stateful and external dependency constraints when available

## Scaling Concerns

Define:

- independent scaling units
- horizontal versus vertical scaling posture
- autoscaling signals at architecture level
- minimum, maximum, and headroom expectations
- queue depth, backlog, and worker concurrency limits
- database, cache, queue, broker, and external provider quotas
- cold start or warmup concerns
- backpressure and load-shedding behavior
- cost guardrails and capacity tradeoffs
- validation metrics for load tests and production observability

## Output

Return:

| Unit | Scaling signal | Scale limit | Protected dependency | Cost/risk note | Metric |
|------|----------------|-------------|----------------------|----------------|--------|

Then list:

- bottlenecks that scaling can worsen
- autoscaling assumptions
- fixed-capacity dependencies
- cost guardrails
- validation metrics
