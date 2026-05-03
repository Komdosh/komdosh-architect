# Architecture Security Designer

Architecture Security Designer is a Codex plugin for security-stage software architecture.
It comes after enough product, scope, service, data, integration, and deployment context exists to design security boundaries and controls.

## Scope Fit

Use this plugin when the requested outcome is:

- trust boundaries and threat surfaces
- user, service, admin, operator, and external-system access
- authentication and identity architecture
- authorization policy and permission model
- tenant isolation and data exposure rules
- sensitive data classification and protection
- privacy, retention, deletion, and compliance expectations
- abuse cases and misuse paths
- secrets, keys, certificates, tokens, and session lifecycle
- API, event, webhook, batch, and admin security controls
- audit, security observability, incident support, and evidence needs
- security context, trust-boundary, data-exposure, and abuse-flow diagrams

This plugin designs security architecture.
It should not jump into library choices, framework configuration, policy code, Terraform, Kubernetes security settings, or a full formal threat model unless a later workflow asks for that detail.

## Human-Readable Output

Prefer readability over professional complexity.
Outputs should be compact, self-contained, and easy to scan.

- put the main idea or decision first
- use plain words before specialist terms
- highlight only important decisions, risks, assumptions, open questions, and next steps
- keep details close to the point they explain
- avoid long paragraphs and decorative wording
- explain necessary technical terms in place

## Skill Grouping

- `$architecture-security-designer:architecture-security-designer`: orchestrates the full security-design pass.
- `$architecture-security-designer:security-context-inventory`: identifies assets, actors, trust assumptions, data sensitivity, and security constraints.
- `$architecture-security-designer:trust-boundary-mapper`: maps trust zones, boundary crossings, threat surfaces, and control points.
- `$architecture-security-designer:identity-access-modeler`: defines identity types, authentication posture, sessions, tokens, and access entry points.
- `$architecture-security-designer:authorization-policy-designer`: defines permission model, role boundaries, policy ownership, tenant isolation, and admin access.
- `$architecture-security-designer:data-protection-privacy-planner`: defines sensitive data classification, protection, retention, deletion, privacy, and exposure rules.
- `$architecture-security-designer:threat-abuse-case-modeler`: identifies architecture-level abuse cases, misuse paths, and required mitigations.
- `$architecture-security-designer:api-integration-security-planner`: defines security controls for APIs, events, webhooks, batch, files, and external systems.
- `$architecture-security-designer:secrets-keys-lifecycle-planner`: defines secrets, keys, certificates, credentials, rotation, storage, and break-glass rules.
- `$architecture-security-designer:audit-compliance-observability-planner`: defines audit events, security logs, monitoring, compliance evidence, and incident support.
- `$architecture-security-designer:security-diagrammer`: creates security context, trust-boundary, access, data-exposure, and abuse-flow diagrams.
- `$architecture-security-designer:security-review-gate`: reviews security design for readiness and stage discipline.

Use the namespaced skill form above in Codex prompts.
The short skill names are directory names, not the guaranteed runtime invocation names.

## Quality Bar

A good output is clear, risk-aware, and actionable for architects.
It should explain what must be protected, who can access it, where trust changes, how misuse is prevented or detected, and what security work must happen next.

Reject or revise a security design when it:

- treats security as a checklist after architecture decisions are done
- hides trust boundaries, threat surfaces, or privileged access
- leaves authentication, authorization, tenant isolation, or data exposure vague
- ignores abuse cases, admin/operator misuse, external providers, or machine actors
- misses audit, security logs, incident support, or compliance evidence
- proposes controls without explaining which risk they reduce
- jumps directly to implementation libraries, framework settings, or formal threat-model detail before architecture decisions are clear

## Required Output Shape

The main output should be a security-architecture brief with:

- security design purpose and source context
- assets, actors, trust assumptions, and sensitive data
- trust boundaries and threat surfaces
- identity, authentication, sessions, tokens, and access entry points
- authorization, permissions, tenant isolation, and admin/operator model
- data protection, privacy, retention, deletion, and exposure rules
- abuse cases, misuse paths, and architecture mitigations
- API, integration, event, webhook, batch, and external-system controls
- secrets, keys, certificates, credential, and token lifecycle
- audit, compliance, security observability, incident support, and evidence expectations
- security diagrams
- risks, alternatives, assumptions, and open questions
- handoff checklist for detailed threat model, implementation, AppSec review, and operations
