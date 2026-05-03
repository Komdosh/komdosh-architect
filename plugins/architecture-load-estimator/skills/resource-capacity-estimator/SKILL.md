---
name: resource-capacity-estimator
description: Estimate resource pressure across CPU, memory, network, IO, workers, threads, connections, queues, caches, and external dependencies without pretending to benchmark.
---

# Resource Capacity Estimator

## Purpose

Translate load into resource pressure.
This helps architects see where capacity assumptions matter and what should be measured later.

## Required Inputs

Require:

- traffic or data-volume estimates
- service/component design or processing flows
- latency, payload, or processing assumptions when available

## Resource Categories

Consider:

- CPU-bound processing
- memory footprint and working set
- disk or storage IO
- network bandwidth and egress
- connection pools
- worker/thread pools
- queue consumers and batch workers
- cache footprint and hit-rate assumptions
- external API rate limits
- database or storage pressure at a high level
- observability/logging overhead

## Output

Return:

| Area | Load driver | Capacity pressure | Estimate/range | Confidence | Decision impact |
|------|-------------|-------------------|----------------|------------|-----------------|

Then list:

- resource pressure hotspots
- external dependency pressure
- scale-out or queue-worker assumptions
- metrics that must be measured in test or production
