---
name: security-review-gate
description: Review security architecture for asset clarity, trust boundaries, identity, authorization, data protection, abuse cases, API and integration controls, secrets lifecycle, audit, compliance, observability, diagram consistency, readability, and stage discipline.
---

# Security Review Gate

## Purpose

Review security design before detailed threat modeling, implementation, AppSec review, or operational hardening.
Find hidden trust assumptions, vague access rules, missing data protection, weak abuse coverage, and premature implementation details.

## Required Inputs

Require:

- security-architecture brief or exact diff
- requirements, scope, service, data, integration, deployment, or diagrams when available

If only a security brief is provided, review internal coherence and state that source alignment was not verified.

## SHIELD Review

Use `SHIELD`:

| Check | Question |
|-------|----------|
| `S` Scope/assets | Are assets, actors, sensitive data, and security goals clear? |
| `H` Human and machine identity | Are users, admins, operators, services, jobs, and external systems covered? |
| `I` Isolation and authorization | Are permissions, tenant boundaries, admin access, and policy ownership defined? |
| `E` Exposure and data protection | Are sensitive data exposure, privacy, retention, deletion, and sharing rules clear? |
| `L` Limit abuse | Are misuse paths, abuse controls, rate limits, replay protection, and detection covered? |
| `D` Detect and document | Are audit events, security logs, compliance evidence, incidents, and support ownership defined? |

Also check:

- trust boundaries and control points match diagrams
- secrets, keys, certificates, credentials, tokens, and rotation expectations are covered
- API, event, webhook, batch, file, admin, and external-provider controls are explicit
- controls are tied to risks or requirements
- implementation details are deferred when architecture decisions are still the goal

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

- critical asset, sensitive data, actor, or privileged path is missing
- trust boundary or exposed entry point is undefined
- authentication exists but authorization, tenant isolation, or data exposure is vague
- admin, operator, support, service, or external-system access is ignored
- sensitive data has no protection, retention, deletion, or exposure rule
- high-risk API, webhook, event, batch, file, or external integration has no security controls
- secrets, keys, credentials, tokens, or certificates have no owner or rotation/revocation expectation
- audit, security logs, compliance evidence, or incident support is missing
- controls are listed without the risk or requirement they address
- diagrams contradict written trust boundaries, access paths, or data exposure
- output jumps to security library, framework config, IAM resource, Terraform, Kubernetes, or code-level policy detail before architecture decisions are sound

## Output

Return either:

```text
SHIELD: pass
Security readiness: pass
```

or:

```text
SHIELD: needs changes
- Blocker/Major/Minor: <issue and fix>
```

When the user asks to improve the security design, provide the corrected section or full revised security-architecture brief.
