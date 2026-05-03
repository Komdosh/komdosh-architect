---
name: traffic-concurrency-estimator
description: Estimate request rates, command/query/event throughput, fan-out, external-call rates, concurrency, queue pressure, backlog, and latency budget pressure.
---

# Traffic Concurrency Estimator

## Purpose

Convert workload scenarios into traffic and concurrency numbers.
These estimates help architects reason about interaction style, scaling pressure, queues, and latency budgets.

## Required Inputs

Require:

- workload scenarios
- key user actions, commands, queries, events, or jobs
- latency or service-time assumptions when concurrency is estimated

## Estimation Rules

Use simple formulas when useful:

- `average RPS = requests per day / 86,400`
- `peak RPS = average RPS * peak factor`
- `fan-out calls = user action rate * downstream calls per action`
- `concurrency ~= arrival rate * average response time`
- `backlog growth = arrival rate - service rate`
- `drain time = backlog / spare service rate`

Use ranges when inputs are uncertain.

## Metrics To Cover

- requests per second and per minute
- commands per second
- queries per second
- event publication and consumption rates
- background job rates
- external dependency call rates
- fan-out per user action
- peak concurrency
- queue arrival and service rate
- backlog and drain time
- p95/p99 latency pressure

## Output

Return:

| Flow | Baseline | Peak | Burst | Formula | Decision impact |
|------|----------|------|-------|---------|-----------------|

Then list:

- highest fan-out flows
- concurrency-sensitive flows
- queue/backlog risks
- latency budget risks
- assumptions and validation metrics
