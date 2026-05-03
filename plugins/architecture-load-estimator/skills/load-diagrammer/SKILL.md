---
name: load-diagrammer
description: Create concise load path, hotspot, queue, and capacity diagrams from source-backed load estimates without pretending they are benchmark proof.
---

# Load Diagrammer

## Purpose

Visualize where load enters, fans out, queues, accumulates, or saturates.
Diagrams should clarify decisions, not decorate estimates.

## Required Inputs

Require:

- load estimates or workload scenarios
- architecture components or flows
- bottleneck notes when available
- requested format when the user needs Mermaid, DrawIO, or another output

If estimates are missing, route back to `$architecture-load-estimator:architecture-load-estimator`.

## Diagram Types

Use a load path diagram when the goal is:

- user action to service/component flow
- fan-out and external dependency rates
- key RPS or job rates

Use a hotspot diagram when the goal is:

- likely bottlenecks
- shared resource pressure
- saturation points

Use a queue/backlog diagram when the goal is:

- async arrival and service rates
- drain time
- retry and failure amplification

## Diagram Rules

- Show only decision-relevant metrics.
- Label estimates with units.
- Mark assumptions and low-confidence numbers.
- Do not present estimates as measured benchmarks.
- Keep diagrams compact and readable.

## Output

Return:

- diagram purpose
- load path, hotspot, or queue diagram
- assumption note
- validation metrics needed
