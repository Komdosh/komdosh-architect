---
name: dashboard-alert-planner
description: Define dashboard views, alert strategy, severity, ownership, escalation, thresholds, symptoms versus causes, noise control, alert fatigue risks, and user-impact-first presentation.
---

# Dashboard Alert Planner

## Purpose

Define what humans see when the system is healthy or failing.
Dashboards should explain status; alerts should demand action only when action is needed.

## Required Inputs

Require:

- SLI/SLO decisions
- telemetry signals
- incident or support ownership when available

## Dashboard And Alert Concerns

Define:

- user-impact dashboards
- dependency and saturation dashboards
- business, security, and operational dashboards when relevant
- alert severity and ownership
- alert triggers tied to user impact, SLOs, symptoms, or urgent risks
- escalation path and response expectation
- noise control and grouping rules
- alerts that should be tickets or reviews instead
- dashboard audience: engineer, support, product, security, operations, executive

## Output

Return:

| View/alert | Audience | Trigger/content | Severity | Owner/action | Noise risk |
|------------|----------|-----------------|----------|--------------|------------|

Then list:

- must-have dashboards
- paging alerts
- non-paging review signals
- escalation expectations
- open dashboard/alert questions
