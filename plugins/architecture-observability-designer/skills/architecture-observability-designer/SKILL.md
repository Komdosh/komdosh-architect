---
name: architecture-observability-designer
description: Design observability architecture from service, data, load, integration, deployment, and security context, covering user-visible health, SLIs, SLOs, logs, metrics, traces, correlation, dashboards, alerts, error taxonomy, diagnostics, incidents, support, telemetry ownership, retention, diagrams, assumptions, and handoff readiness.
---

# Architecture Observability Designer

## Purpose

Design how the system explains its behavior in production.
The result must help a system designer define what is measured, logged, traced, alerted, diagnosed, retained, and owned before implementation-specific telemetry work starts.

Use this skill when the user asks for observability architecture, SLIs, SLOs, logs, metrics, traces, correlation IDs, dashboards, alerts, diagnostic context, incident investigation, runbooks, telemetry retention, or observability diagrams.

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

Treat observability architecture as a first-class design stage:

- observability must support real diagnosis, not only collect raw telemetry
- define user-visible health before internal metrics
- connect every signal to a decision, alert, dashboard, investigation, compliance need, or support workflow
- cover logs, metrics, traces, events, business signals, security signals, and diagnostic context together
- make correlation across APIs, events, jobs, external systems, and async flows explicit
- define owners, retention, privacy, access, and cost guardrails for telemetry
- prepare inputs for later implementation, SRE, platform, security, and support workflows

## Required Inputs

Load the minimum needed context:

- requirements and user journeys when available
- service, data, load, integration, deployment, and security decisions when available
- existing SLOs, incident history, production constraints, or support needs when available
- privacy, compliance, retention, cost, and access constraints for telemetry when available

If observability context is unknown, infer conservative assumptions and label them.
Ask when user-visible health, operational ownership, compliance, privacy, or incident support needs would materially change the design.

## Skill Flow

1. Use `$architecture-observability-designer:observability-context-inventory` to identify journeys, components, dependencies, failure modes, and support needs.
2. Use `$architecture-observability-designer:sli-slo-health-designer` to define user-visible health, SLIs, SLOs, error budgets, and availability signals.
3. Use `$architecture-observability-designer:telemetry-signal-planner` to define metrics, events, business signals, security signals, and ownership.
4. Use `$architecture-observability-designer:logging-diagnostics-planner` to define logs, diagnostic context, sensitive-data rules, and support usefulness.
5. Use `$architecture-observability-designer:tracing-correlation-planner` to define tracing, correlation IDs, causality, async flows, and cross-boundary visibility.
6. Use `$architecture-observability-designer:error-taxonomy-diagnostics-designer` to define error categories, failure classification, user impact, and diagnostic expectations.
7. Use `$architecture-observability-designer:dashboard-alert-planner` to define dashboards, alerts, severity, escalation, and noise control.
8. Use `$architecture-observability-designer:incident-runbook-support-planner` to define incident workflows, runbook inputs, investigation data, and support handoff.
9. Use `$architecture-observability-designer:telemetry-governance-retention-planner` to define ownership, retention, privacy, access, cost, and compliance.
10. Use `$architecture-observability-designer:observability-diagrammer` when diagrams clarify signal flow or diagnosis.
11. Use `$architecture-observability-designer:observability-review-gate` before final delivery.

## Output Contract

Return a self-contained observability-architecture brief with this structure unless the user asks for another format:

1. Observability design purpose
2. Source context
3. User journeys, components, dependencies, and failure modes
4. User-visible health, SLIs, SLOs, and error-budget expectations
5. Logs, metrics, traces, events, business signals, and security signals
6. Correlation, causality, async-flow, and cross-boundary visibility
7. Error taxonomy and diagnostic context
8. Dashboards, alerts, severity, escalation, and noise control
9. Incident investigation, runbook inputs, and support handoff
10. Telemetry ownership, retention, privacy, access, and cost guardrails
11. Observability diagrams
12. Observability risks and alternatives
13. Assumptions
14. Open questions
15. Handoff checklist for implementation, SRE, platform, security, and support

## Observability Design Discipline

Do not jump directly to tool implementation:

- do not choose observability vendors, collectors, agents, dashboards, storage backends, alert engines, or tracing SDKs unless context requires them
- do not write instrumentation code, logging configuration, alert rules, Terraform, Kubernetes monitors, or dashboard JSON
- do not define alerts without owner, severity, user impact, threshold rationale, and action
- do not collect sensitive data in telemetry without a protection, retention, and access rule
- do not add metrics that nobody uses to decide, alert, diagnose, or improve the system
- do not treat internal uptime as the same thing as user-visible health

You may state observability-level architecture decisions:

- this journey needs an availability SLI measured at the API boundary because users care about completion
- this async flow needs correlation from command to event to worker outcome
- this external provider dependency needs latency, error, quota, and degradation signals
- this security-sensitive action needs audit and anomaly signals, not only application logs
- this dashboard should show user impact first and dependency details second

## Stop Conditions

Stop and ask when:

- user-visible health or critical journeys are unknown and cannot be inferred
- support ownership, escalation, or incident response expectations are central but unclear
- privacy, compliance, or retention constraints for telemetry are central and unknown
- the user asks for dashboard or instrumentation implementation while observability goals and ownership are unresolved
