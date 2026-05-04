---
name: risk-register-builder
description: Build a compact architecture risk register from prioritized risks, assumptions, mitigations, validation work, owners, residual risks, readiness, and next steps.
---

# Risk Register Builder

## Purpose

Package risks into a compact register.
The register should be easy to review in an architecture decision meeting.

## Required Inputs

Require:

- prioritized risks
- validation plan
- mitigation owners
- readiness recommendation when available

## Register Rules

- keep only useful risks
- merge duplicates
- make priority visible
- cite source evidence where available
- include owner, mitigation, validation, trigger, status, and residual risk
- keep open questions separate from confirmed risks
- keep wording short and clear

## Output

Return:

| ID | Risk | Area | Priority | Owner | Mitigation/validation | Status |
|----|------|------|----------|-------|-----------------------|--------|

Then list:

- top 3 risks
- accepted risks
- risks requiring validation
- risks requiring escalation
- next review point
