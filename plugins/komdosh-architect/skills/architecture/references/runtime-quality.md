# Load, Deployment, and Observability

## Load and capacity

- Define named workload scenarios with normal, peak, burst, growth, degraded, and recovery conditions as relevant.
- Show formulas, units, ranges, and assumptions for traffic, concurrency, throughput, payload size, storage growth, retention, and background work. Avoid false precision.
- Identify saturation points across compute, memory, pools, queues, databases, caches, storage, networks, and external quotas.
- Tie scaling units and capacity headroom to observable signals. Recommend an optimization only when a scenario or bottleneck justifies it.

## Deployment and reliability

- Define deployment units, processes and jobs, stateless/stateful boundaries, environment and promotion strategy, region or zone placement, and state locality.
- Show ingress, egress, public/private and trust zones, service connectivity, DNS/TLS responsibility, and external-provider access where they affect design.
- Place stateful dependencies with ownership, availability, backup, restore, retention, locality, and operational responsibility.
- Specify scaling signals and limits, quotas, worker concurrency, queue backlogs, external limits, and cost guardrails.
- Cover rollout, rollback, compatibility and migration order, feature control, release gates, and support during change.
- Derive availability, degradation, failover, backup/restore, RPO, RTO, and disaster-recovery testing from requirements. Name the recovery owner.
- Keep configuration separate from secrets; state ownership, delivery, rotation, revocation, and restart/reload behavior when relevant. Produce manifests or infrastructure code only when requested.

## Observability and incident support

- Start from critical user journeys, service responsibilities, dependencies, and failure modes.
- Define SLIs and SLOs in terms of user-visible success, latency, correctness, freshness, availability, or durability. State the measurement window and error-budget consequence where useful.
- Assign the minimum useful logs, metrics, traces, events, and correlation identifiers to each failure mode. Avoid secrets and unnecessary personal data.
- Use an actionable error taxonomy: stable category/code, safe message, retryability, correlation, owner, and diagnostic context.
- Alerts need a symptom, threshold or anomaly condition, severity, owner, response, runbook, and noise control. Dashboards should support a concrete operational question.
- Ensure incidents can be detected, scoped, diagnosed, mitigated, recovered, and learned from. Define telemetry retention, access, cost, and privacy constraints.

Do not promise a quality level that the topology, capacity, telemetry, or recovery design cannot prove.
