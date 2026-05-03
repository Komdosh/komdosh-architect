---
name: secrets-keys-lifecycle-planner
description: Define secrets, keys, certificates, credentials, tokens, service accounts, storage, access ownership, rotation, revocation, break-glass, and incident response expectations.
---

# Secrets Keys Lifecycle Planner

## Purpose

Define how sensitive credentials are created, stored, used, rotated, and revoked.
Secrets and keys are operational security boundaries, not implementation details.

## Required Inputs

Require:

- identity and integration context
- deployment or operations context when available
- external provider or machine access context when available

## Lifecycle Concerns

Define:

- secret, key, certificate, credential, and token categories
- owner and allowed consumers
- storage and access posture at architecture level
- rotation and revocation expectation
- expiration, renewal, and certificate lifecycle assumptions
- service account and workload credential rules
- break-glass access and emergency rotation path
- leak detection and incident response expectations
- audit evidence for secret access and change

## Output

Return:

| Credential | Used by | Owner | Storage/access rule | Rotation/revocation | Risk |
|------------|---------|-------|---------------------|---------------------|------|

Then list:

- high-risk secrets and keys
- rotation and revocation rules
- break-glass expectations
- incident response needs
- open credential-lifecycle questions
