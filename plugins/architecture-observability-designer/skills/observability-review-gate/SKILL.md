---
name: observability-review-gate
description: Review observability architecture for user-visible health, SLIs, SLOs, useful signals, logs, traces, correlation, dashboards, alerts, diagnostics, incident support, telemetry governance, diagram consistency, readability, and stage discipline.
---

# Observability Review Gate

## Purpose

Review observability design before implementation, SRE, platform, security, or support work.
Find missing health signals, noisy alerts, weak diagnostics, unclear ownership, and premature vendor/tool detail.

## Required Inputs

Require:

- observability-architecture brief or exact diff
- service, data, load, integration, deployment, security, or diagrams when available

If only an observability brief is provided, review internal coherence and state that source alignment was not verified.

## SIGNAL Review

Use `SIGNAL`:

| Check | Question |
|-------|----------|
| `S` SLO health | Are critical journeys, user-visible health, SLIs, SLOs, and error budgets clear? |
| `I` Instrumented meaning | Does every signal support a decision, alert, dashboard, diagnosis, compliance need, or support workflow? |
| `G` Guided diagnosis | Are logs, traces, correlation, errors, and diagnostic fields enough to investigate failures? |
| `N` Noise control | Are alerts actionable, owned, severity-based, and protected from alert fatigue? |
| `A` Accountability | Are telemetry owners, runbooks, escalation, support handoff, and incident responsibilities defined? |
| `L` Lifecycle | Are retention, privacy, access, cost, cardinality, and telemetry cleanup rules defined? |

Also check:

- async, event, job, batch, external-provider, and callback flows have correlation expectations
- business, product, security, and operational signals are considered when relevant
- diagrams match written signal ownership and flow
- vendor/tool implementation details are deferred when architecture decisions are still the goal

## Readability Check

Treat readability as part of review quality:

- main ideas and decisions are visible first
- wording is plain and compact
- details support nearby points instead of hiding them
- only important decisions, risks, assumptions, open questions, and next steps are highlighted
- necessary technical terms are explained in place

Mark as Major when professional complexity, long prose, or scattered details make the document hard to use.

## Blockers

Treat these as blockers:

- critical user journey has no health signal or SLI
- SLO or alert is defined without owner, action, or user-impact rationale
- important API, event, job, batch, or external dependency cannot be correlated during investigation
- logs or telemetry can leak sensitive data without a protection rule
- dashboards show internals but not user-visible health or support impact
- alert strategy lacks severity, escalation, ownership, or noise control
- incident support lacks runbook inputs, recovery validation, or support handoff data
- telemetry retention, access, privacy, cost, or ownership is missing
- diagrams contradict written signal flow, ownership, or alert path
- output jumps to vendors, collectors, agents, SDKs, dashboard JSON, alert-rule syntax, Terraform, Kubernetes, or code instrumentation before architecture decisions are sound

## Output

Return either:

```text
SIGNAL: pass
Observability readiness: pass
```

or:

```text
SIGNAL: needs changes
- Blocker/Major/Minor: <issue and fix>
```

When the user asks to improve the observability design, provide the corrected section or full revised observability-architecture brief.
