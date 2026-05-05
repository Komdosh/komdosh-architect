---
name: audit-compliance-planner
description: Define security audit events, compliance evidence, security logs, metrics, traces, alerts, anomaly signals, incident support, investigation data, retention, and evidence ownership.
---

# Audit Compliance Observability Planner

## Purpose

Make security behavior visible and reviewable.
Security architecture is incomplete if incidents, misuse, compliance evidence, and privileged actions cannot be investigated.

## Required Inputs

Require:

- security context inventory
- identity, authorization, data, and abuse-case context when available
- compliance or operational constraints when available

## Coverage

Define:

- audit events for login, access, admin actions, data export, deletion, policy change, and credential change
- immutable or tamper-resistant evidence expectations at architecture level
- security logs, metrics, traces, alerts, and anomaly signals
- compliance evidence and reporting needs
- retention and privacy rules for audit data
- incident investigation data and support workflows
- alert ownership and escalation path
- audit access control and evidence protection
- gaps that require later AppSec, legal, or compliance review

## Output

Return:

| Signal/evidence | Purpose | Trigger | Retention/protection | Owner | Risk |
|-----------------|---------|---------|----------------------|-------|------|

Then list:

- required audit events
- security monitoring signals
- compliance evidence needs
- incident support expectations
- open audit/compliance questions
