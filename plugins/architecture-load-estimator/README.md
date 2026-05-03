# Architecture Load Estimator

Architecture Load Estimator is a Codex plugin for concise, decision-useful load estimation in software architecture work.
It comes after requirements, scope, domain, service, and data responsibilities are clear enough to discuss workload and capacity.

## Scope Fit

Use this plugin when the requested outcome is:

- expected users, workload, and peak scenarios
- request, command, event, job, batch, and external-call rates
- throughput, concurrency, fan-out, queue, and backlog estimates
- data volume, storage growth, logs, events, and bandwidth estimates
- latency budget and SLO pressure
- CPU, memory, network, IO, connection, and worker capacity pressure
- bottleneck and saturation risk
- optimization options and architecture decision implications
- validation metrics for load tests, benchmarks, or production observability

This plugin provides estimates for architecture decisions, not benchmark proof.
It should be concise, clear, and explicit about formulas, assumptions, confidence, and what must be measured later.

## Human-Readable Output

Prefer readability over professional complexity.
Outputs should be compact, self-contained, and easy to scan.

- put the main idea or decision first
- use plain words before specialist terms
- highlight only important decisions, risks, assumptions, open questions, and next steps
- keep details close to the point they explain
- avoid long paragraphs and decorative wording
- explain necessary technical terms in place

## Skill Grouping

- `$architecture-load-estimator:architecture-load-estimator`: orchestrates the full load-estimation pass.
- `$architecture-load-estimator:workload-scenario-profiler`: defines user, business, peak, burst, and background workload scenarios.
- `$architecture-load-estimator:traffic-concurrency-estimator`: estimates request rates, throughput, fan-out, concurrency, queue depth, and latency pressure.
- `$architecture-load-estimator:data-volume-growth-estimator`: estimates records, payloads, events, logs, storage, retention, and bandwidth growth.
- `$architecture-load-estimator:resource-capacity-estimator`: frames CPU, memory, network, IO, worker, connection, and external dependency capacity.
- `$architecture-load-estimator:bottleneck-saturation-analyzer`: identifies likely bottlenecks, saturation points, and nonlinear load risks.
- `$architecture-load-estimator:optimization-decision-advisor`: links metrics to optimization and architecture decisions.
- `$architecture-load-estimator:load-decision-brief`: produces the concise decision-ready summary.
- `$architecture-load-estimator:load-diagrammer`: creates load path, hotspot, or capacity diagrams.
- `$architecture-load-estimator:load-review-gate`: reviews estimates for usefulness, clarity, and decision readiness.

Use the namespaced skill form above in Codex prompts.
The short skill names are directory names, not the guaranteed runtime invocation names.

## Quality Bar

A good output is short, numeric, assumption-aware, and useful for a real architecture decision.
It should help an architect see where load matters, what is likely safe, what is risky, what can be optimized, and what must be measured.

Reject or revise a load estimate when it:

- gives precise numbers without assumptions or formulas
- hides peak factors, burst behavior, fan-out, or background jobs
- only estimates requests and ignores storage, events, queues, external dependencies, and resource pressure
- omits confidence level or validation plan
- cannot explain what architecture decision the metric supports
- confuses benchmark results with estimates
- is too verbose to use in an architecture discussion

## Required Output Shape

The main output should be a load-estimation brief with:

- decision context
- workload assumptions
- key metrics summary
- formulas and confidence
- traffic, throughput, concurrency, and fan-out
- data volume, storage growth, retention, and bandwidth
- latency, SLO, queue, and backlog pressure
- resource and external dependency pressure
- bottlenecks and saturation risks
- optimization levers and decision implications
- validation and observability metrics
- concise final recommendation
