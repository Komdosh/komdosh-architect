---
name: lifecycle-retention-privacy-planner
description: Define data lifecycle, retention, deletion, privacy, residency, PII classification, consent, audit, history, and legal hold expectations for data architecture.
---

# Lifecycle Retention Privacy Planner

## Purpose

Make data lifecycle and privacy constraints visible before storage design.
These requirements often change ownership, flow, projection, and retention decisions.

## Required Inputs

Require:

- data subjects or data boundaries
- known domain, regulatory, privacy, or audit context

If sensitive data is likely but requirements are missing, label the gap as a high-risk open question.

## Coverage

For each data subject, consider:

- creation and update lifecycle
- retention period
- deletion or anonymization requirement
- privacy classification
- PII, sensitive, confidential, public, or operational classification
- consent and purpose limitation
- regional residency or transfer limits
- audit and history requirements
- legal hold or dispute needs
- propagation to read models, logs, exports, analytics, and backups
- support visibility and access controls

## Output

Return:

| Data subject | Classification | Retention | Deletion/anonymization | Audit/history | Propagation concern |
|--------------|----------------|-----------|------------------------|---------------|---------------------|

Then list:

- high-risk privacy gaps
- deletion propagation needs
- audit/history ownership
- residency or compliance questions
