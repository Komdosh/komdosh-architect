---
name: optimization-decision-advisor
description: Connect load metrics to architecture decisions, optimization levers, tradeoffs, cost impact, validation priority, and when not to optimize yet.
---

# Optimization Decision Advisor

## Purpose

Turn estimates into architecture decisions.
The output should help decide what to optimize now, what to defer, and what to validate.

## Required Inputs

Require:

- key load estimates
- bottleneck or resource-pressure notes
- architecture decision context

## Optimization Levers

Consider:

- reduce fan-out
- introduce async processing or queues
- split read/write paths
- add read models, projections, or caches
- batch or coalesce writes
- rate limit or shed load
- isolate tenants or noisy workloads
- move heavy jobs off peak paths
- precompute or materialize expensive reads
- reduce payload size
- tune retention or logging volume
- add idempotency and retry controls
- change component boundary only when metrics justify it

## Decision Rules

- Optimize only when a metric creates real risk or cost.
- Prefer simple design when estimated load is low and uncertainty is high.
- Recommend measurement when the decision depends on unknown service time or resource usage.
- State tradeoffs: latency, consistency, complexity, cost, operability, and correctness.

## Output

Return:

| Decision area | Metric signal | Recommendation | Tradeoff | Validate with |
|---------------|---------------|----------------|----------|---------------|

Then list:

- optimize now
- defer until measured
- avoid over-engineering
- architecture changes justified by load
