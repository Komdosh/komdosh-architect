---
name: architecture-load-estimator
description: Produce concise, decision-useful architecture load estimates across workload scenarios, traffic, throughput, concurrency, storage growth, resource pressure, bottlenecks, optimization decisions, assumptions, confidence, and validation metrics.
---

# Architecture Load Estimator

## Purpose

Estimate load so architecture decisions are grounded in numbers.
The result must be concise, clear, and useful for deciding whether the architecture is acceptable, risky, or needs optimization.

Use this skill when the user asks for load estimation, capacity planning, traffic estimates, performance sizing, scalability assumptions, peak load, storage growth, resource pressure, bottleneck analysis, or load-driven architecture decisions.

## Human Readability Rule

Every output must be easy for humans to read:

- start each section with the main idea or decision in plain words
- keep the document compact and remove decorative explanation
- use short sections, tables, and bullets for scanning
- prefer clear words over professional-sounding complexity
- keep details near the point they explain
- highlight only important decisions, risks, assumptions, open questions, and handoff steps
- explain necessary technical terms in place

## Core Rule

Provide real decision information, not fake precision:

- use ranges when exact numbers are unknown
- show formulas or reasoning for important estimates
- separate known facts, assumptions, estimates, and validation needs
- include confidence level for each important metric
- cover multiple metric categories, not only requests per second
- connect metrics to architecture decisions and optimization levers
- keep the final brief short enough for an architect to use
- do not claim benchmark certainty unless measured evidence exists

## Required Inputs

Load the minimum needed context:

- requirements, scope, domain, service, or data design when available
- expected users, tenants, devices, integrations, jobs, events, or business transactions
- peak, burst, seasonal, batch, or background workload facts when available
- SLO, latency, availability, cost, retention, or resource constraints when available
- existing production metrics, logs, benchmarks, or analytics when available

If numbers are missing, make explicit conservative assumptions and mark them as assumptions.
Ask only when a missing fact would make the estimate misleading or unsafe.

## Skill Flow

1. Use `$architecture-load-estimator:workload-scenario-profiler` to define workload scenarios and peak assumptions.
2. Use `$architecture-load-estimator:traffic-concurrency-estimator` to estimate traffic, throughput, fan-out, concurrency, queues, and latency pressure.
3. Use `$architecture-load-estimator:data-volume-growth-estimator` to estimate data volume, storage growth, retention, events, logs, and bandwidth.
4. Use `$architecture-load-estimator:resource-capacity-estimator` to frame CPU, memory, network, IO, worker, connection, and external dependency pressure.
5. Use `$architecture-load-estimator:bottleneck-saturation-analyzer` to identify likely bottlenecks and saturation risks.
6. Use `$architecture-load-estimator:optimization-decision-advisor` to connect metrics to architecture decisions and optimization options.
7. Use `$architecture-load-estimator:load-decision-brief` to produce a concise decision-ready summary.
8. Use `$architecture-load-estimator:load-diagrammer` when a load path or hotspot diagram would clarify the decision.
9. Use `$architecture-load-estimator:load-review-gate` before final delivery.

## Output Contract

Return a concise load-estimation brief with this structure unless the user asks for another format:

1. Decision context
2. Known facts
3. Assumptions
4. Key metrics summary
5. Workload scenarios
6. Traffic, throughput, concurrency, and fan-out
7. Data volume, storage growth, retention, and bandwidth
8. Latency, SLO, queue, and backlog pressure
9. Resource and external dependency pressure
10. Bottlenecks and saturation risks
11. Optimization levers
12. Architecture decision implications
13. Validation and observability plan
14. Final recommendation

## Required Metric Categories

Consider at least:

- active users, tenants, devices, or actors
- business transactions per day and at peak
- requests, commands, queries, events, jobs, and batch rates
- read/write ratio
- fan-out per user action
- external dependency calls
- concurrency using Little's Law when latency or service time is known
- payload size and bandwidth
- record count and storage growth
- logs, audit records, events, and retention
- p50/p95/p99 latency budget when relevant
- queue arrival rate, service rate, backlog, and drain time when relevant
- CPU, memory, IO, network, worker, thread, and connection pressure
- cost or resource multiplier when it affects decisions

## Stop Conditions

Stop and ask when:

- the decision cannot be stated
- every meaningful workload input is missing and assumptions would be arbitrary
- safety, financial, legal, or operational risk depends on precise measured load
- the user asks for benchmark-level confidence without measured data
