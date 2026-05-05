# Architecture Observability Designer

Architecture Observability Designer is a Codex plugin for observability-stage software architecture.
It comes after enough service, data, load, integration, deployment, and security context exists to decide what the system must make visible.

## Scope Fit

Use this plugin when the requested outcome is:

- user-visible health, SLIs, SLOs, and error-budget expectations
- logs, metrics, traces, events, and correlation IDs
- dashboards, alerting, escalation, and on-call signals
- diagnostic context for failures and customer support
- error taxonomy and failure classification
- business, product, security, and operational signals
- incident investigation and runbook inputs
- telemetry ownership, retention, privacy, and cost guardrails
- observability boundaries across services, APIs, integrations, jobs, and infrastructure
- observability context, signal-flow, dashboard, alert, trace, and incident diagrams

This plugin designs observability architecture.
It should not jump into vendor dashboards, agents, collectors, instrumentation code, OpenTelemetry setup, logback config, Terraform, Kubernetes monitors, or alert-rule implementation unless a later workflow asks for that detail.

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

- `$architecture-observability-designer:observability-designer`: orchestrates the full observability-design pass.
- `$architecture-observability-designer:context-inventory`: identifies journeys, components, dependencies, failure modes, and support needs.
- `$architecture-observability-designer:sli-slo-health-designer`: defines user-visible health, SLIs, SLOs, error budgets, and availability signals.
- `$architecture-observability-designer:telemetry-signal-planner`: defines metrics, events, business signals, security signals, and ownership.
- `$architecture-observability-designer:logging-diagnostics-planner`: defines logs, diagnostic context, sensitive-data rules, and support usefulness.
- `$architecture-observability-designer:tracing-correlation-planner`: defines tracing, correlation IDs, causality, async flows, and cross-boundary visibility.
- `$architecture-observability-designer:dashboard-alert-planner`: defines dashboards, alerts, severity, escalation, and noise control.
- `$architecture-observability-designer:error-diagnostics-designer`: defines error categories, failure classification, user impact, and diagnostic expectations.
- `$architecture-observability-designer:incident-support-planner`: defines incident workflows, runbook inputs, investigation data, and support handoff.
- `$architecture-observability-designer:telemetry-retention-planner`: defines telemetry ownership, retention, privacy, access, cost, and compliance.
- `$architecture-observability-designer:observability-diagrammer`: creates observability context, signal-flow, tracing, dashboard, alert, and incident diagrams.
- `$architecture-observability-designer:observability-review-gate`: reviews observability design for readiness and stage discipline.

Use the namespaced skill form above in Codex prompts.
Directory names are source layout only; runtime skill names come from `SKILL.md` frontmatter.

## Quality Bar

A good output is clear, compact, and useful during production incidents.
It should explain what is measured, why it matters, who owns it, what should alert, and how engineers diagnose the issue.

Reject or revise an observability design when it:

- treats observability as logging everything
- lacks user-visible health, SLIs, SLOs, or clear support signals
- defines metrics without owner, decision value, threshold, or action
- omits correlation across APIs, events, jobs, external systems, and async flows
- misses sensitive-data, retention, access, or telemetry-cost constraints
- creates alerts without severity, owner, escalation, or noise control
- jumps directly to vendor dashboards, collectors, agents, or code instrumentation before architecture decisions are clear

## Required Output Shape

The main output should be an observability-architecture brief with:

- observability design purpose and source context
- user journeys, components, dependencies, and failure modes
- user-visible health, SLIs, SLOs, and error-budget expectations
- logs, metrics, traces, events, business signals, and security signals
- correlation, causality, async-flow, and cross-boundary visibility
- error taxonomy and diagnostic context
- dashboards, alerts, severity, escalation, and noise control
- incident investigation, runbook inputs, and support handoff
- telemetry ownership, retention, privacy, access, and cost guardrails
- observability diagrams
- risks, alternatives, assumptions, and open questions
- handoff checklist for implementation, SRE, platform, security, and support
