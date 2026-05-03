---
name: data-protection-privacy-planner
description: Define sensitive data classification, minimization, masking, encryption posture, tokenization, retention, deletion, privacy, residency, export, sharing, and exposure rules at architecture level.
---

# Data Protection Privacy Planner

## Purpose

Define how sensitive data is protected through its lifecycle.
Data protection should be tied to business use, privacy expectations, and exposure risk.

## Required Inputs

Require:

- data design or data inventory
- security context inventory
- compliance or privacy constraints when available

## Protection Concerns

Define:

- data classification and sensitivity levels
- collection and minimization rules
- masking, redaction, tokenization, encryption, or hashing posture at architecture level
- data residency and cross-border movement assumptions
- retention, deletion, archival, and legal hold expectations
- export, reporting, analytics, and support access exposure
- logs, traces, events, backups, and files that may carry sensitive data
- external provider data sharing and contracts
- user privacy rights and operational handling

## Output

Return:

| Data | Sensitivity | Protection rule | Exposure path | Retention/deletion | Owner |
|------|-------------|-----------------|---------------|--------------------|-------|

Then list:

- data minimization rules
- sensitive exposure points
- retention and deletion expectations
- privacy and residency assumptions
- open data-protection questions
