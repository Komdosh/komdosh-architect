---
name: bottleneck-saturation-analyzer
description: Identify likely bottlenecks, saturation points, nonlinear load risks, queue buildup, dependency limits, data hotspots, and failure amplification paths.
---

# Bottleneck Saturation Analyzer

## Purpose

Find where the architecture is likely to bend first.
Bottleneck analysis should help prioritize optimization and validation work.

## Required Inputs

Require:

- traffic, data, or resource estimates
- service/component or data design when available

## Bottleneck Signals

Look for:

- high fan-out synchronous paths
- shared source-of-truth hotspots
- queue arrival rate near service rate
- external dependency rate limits
- batch jobs overlapping peak traffic
- large payload or file flows
- high-cardinality query or search patterns
- lock/serialization or single-writer assumptions
- cache-miss amplification
- retry storms and failure amplification
- logging/audit volume amplification
- noisy tenant or hot partition risk

## Output

Return:

| Bottleneck | Trigger | Saturation signal | Impact | Mitigation option | Validation metric |
|------------|---------|-------------------|--------|-------------------|-------------------|

Then list:

- top 3 saturation risks
- risks that need architectural change
- risks that need measurement first
- assumptions that could invalidate the estimate
