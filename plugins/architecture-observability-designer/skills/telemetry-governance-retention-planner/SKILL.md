---
name: telemetry-governance-retention-planner
description: Define telemetry ownership, access, retention, privacy, sensitive-data handling, compliance, cost guardrails, cardinality limits, quality review, and lifecycle expectations.
---

# Telemetry Governance Retention Planner

## Purpose

Make telemetry safe and sustainable.
Observability data has cost, privacy, access, and lifecycle risks that must be designed explicitly.

## Required Inputs

Require:

- telemetry signal plan
- logging/tracing context
- privacy, security, compliance, or cost constraints when available

## Governance Concerns

Define:

- telemetry ownership and stewardship
- access control and audience
- retention by signal type
- sensitive-data handling and redaction expectations
- privacy and compliance constraints
- cardinality, volume, and cost guardrails
- sampling or aggregation posture at architecture level
- quality review and stale telemetry cleanup
- data export, legal hold, and incident evidence expectations when relevant

## Output

Return:

| Telemetry class | Owner | Access | Retention | Privacy/cost rule | Review need |
|-----------------|-------|--------|-----------|-------------------|-------------|

Then list:

- retention rules
- access and privacy rules
- cost/cardinality guardrails
- compliance evidence needs
- open governance questions
