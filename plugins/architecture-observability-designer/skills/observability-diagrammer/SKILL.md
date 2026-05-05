---
name: observability-diagrammer
description: Create architecture-level observability context, signal-flow, trace-correlation, dashboard, alert, incident, and telemetry-governance diagrams from source-backed observability decisions.
---

# Observability Diagrammer

## Purpose

Visualize observability decisions.
Diagrams should show what emits signals, where they are correlated, who consumes them, and how they support diagnosis.

## Required Inputs

Require:

- observability context inventory
- SLI/SLO, telemetry, logging, tracing, dashboard, alert, or incident decisions
- requested format when the user needs Mermaid, DrawIO, or another output

If observability inputs are missing, route back to `$architecture-observability-designer:observability-designer`.

## Diagram Types

Use an observability context diagram when the goal is:

- systems, owners, signal consumers, and critical journeys

Use a signal-flow diagram when the goal is:

- logs, metrics, traces, events, dashboards, alerts, and support tools

Use a trace-correlation diagram when the goal is:

- request, event, job, callback, and external-system causality

Use an alert or incident diagram when the goal is:

- trigger, owner, escalation, runbook, recovery validation, and support handoff

Use a governance diagram when the goal is:

- retention, access, privacy, and cost boundaries for telemetry

## Diagram Rules

- Label signals with purpose, not vendor/tool names.
- Show user-visible health before internal signals when both matter.
- Show owners and consumers when they affect action.
- Show async and external-system correlation gaps explicitly.
- Mark sensitive telemetry, retention, or access boundaries when relevant.
- Do not show collectors, agents, dashboard JSON, alert-rule syntax, SDKs, or storage backend implementation unless explicitly requested.

## Output

Return:

- diagram purpose
- observability context, signal-flow, trace-correlation, alert, incident, or governance diagram
- source-assumption note
- diagram limitations for later implementation or SRE workflow
