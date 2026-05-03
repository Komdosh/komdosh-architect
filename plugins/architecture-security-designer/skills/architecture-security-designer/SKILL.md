---
name: architecture-security-designer
description: Design security architecture from requirements, scope, domain, service, data, load, integration, and deployment context, covering assets, actors, trust boundaries, identity, authorization, data protection, privacy, abuse cases, API and integration controls, secrets, audit, compliance, observability, diagrams, assumptions, and handoff readiness.
---

# Architecture Security Designer

## Purpose

Design how the system protects users, data, operations, and integrations.
The result must help a system designer define trust boundaries, access model, data protection, abuse resistance, auditability, and security support before implementation-specific security work starts.

Use this skill when the user asks for security architecture, trust boundaries, authentication, authorization, tenant isolation, privacy, abuse cases, audit, compliance, secrets, key lifecycle, security controls, or security diagrams.

## Human Readability Rule

Every output must be easy for humans to read:

- start each section with the main idea or decision in plain words
- keep the document compact and remove decorative explanation
- use short sections, tables, and bullets for scanning
- prefer clear words over professional-sounding complexity
- keep details near the point they explain
- highlight only important decisions, risks, assumptions, open questions, and handoff steps
- explain necessary technical terms in place

## Core Rule

Treat security architecture as a first-class design stage:

- security is hard and expensive to retrofit after API, data, integration, and deployment decisions are fixed
- identify assets, actors, trust boundaries, privileged paths, and sensitive data before choosing controls
- define identity and authorization at the architecture level before implementation roles or policies
- make tenant isolation, data exposure, audit, compliance, and support expectations explicit
- include human users, admins, operators, services, jobs, external systems, and attackers in the model
- connect every control to a risk, misuse path, or compliance need
- prepare inputs for later threat modeling, implementation, AppSec review, platform hardening, and operations workflows

## Required Inputs

Load the minimum needed context:

- product goals and requirements when available
- scope, actors, roles, and external-system landscape when available
- domain, service, data, integration, load, and deployment decisions when available
- compliance, privacy, data residency, legal, security, support, and audit constraints when available
- existing security model or production constraints when the design must align with a current system

If security context is unknown, infer conservative assumptions and label them.
Ask when compliance, privacy, tenant isolation, privileged access, or sensitive data uncertainty would make the security design misleading.

## Skill Flow

1. Use `$architecture-security-designer:security-context-inventory` to identify assets, actors, data sensitivity, trust assumptions, and constraints.
2. Use `$architecture-security-designer:trust-boundary-mapper` to map trust zones, boundary crossings, threat surfaces, and control points.
3. Use `$architecture-security-designer:identity-access-modeler` to define identity types, authentication, sessions, tokens, and access entry points.
4. Use `$architecture-security-designer:authorization-policy-designer` to define permission model, tenant isolation, policy ownership, and admin access.
5. Use `$architecture-security-designer:data-protection-privacy-planner` to define sensitive data protection, privacy, retention, deletion, and exposure rules.
6. Use `$architecture-security-designer:threat-abuse-case-modeler` to identify architecture-level abuse cases, misuse paths, and mitigations.
7. Use `$architecture-security-designer:api-integration-security-planner` to define controls for APIs, events, webhooks, batch, files, and external systems.
8. Use `$architecture-security-designer:secrets-keys-lifecycle-planner` to define secrets, keys, certificates, credentials, rotation, and break-glass rules.
9. Use `$architecture-security-designer:audit-compliance-observability-planner` to define audit events, security logs, compliance evidence, monitoring, and incident support.
10. Use `$architecture-security-designer:security-diagrammer` when diagrams clarify security boundaries or flows.
11. Use `$architecture-security-designer:security-review-gate` before final delivery.

## Output Contract

Return a self-contained security-architecture brief with this structure unless the user asks for another format:

1. Security design purpose
2. Source context
3. Assets, actors, trust assumptions, and sensitive data
4. Trust boundaries and threat surfaces
5. Identity, authentication, sessions, tokens, and access entry points
6. Authorization, permissions, tenant isolation, and admin/operator model
7. Data protection, privacy, retention, deletion, and exposure rules
8. Abuse cases, misuse paths, and architecture mitigations
9. API, integration, event, webhook, batch, and external-system controls
10. Secrets, keys, certificates, credentials, and token lifecycle
11. Audit, compliance, security observability, incident support, and evidence expectations
12. Security diagrams
13. Security risks and alternatives
14. Assumptions
15. Open questions
16. Handoff checklist for detailed threat model, implementation, AppSec review, and operations

## Security Design Discipline

Do not jump directly to implementation:

- do not choose security libraries, IAM products, frameworks, policy engines, cloud services, or cryptographic primitives unless context requires them
- do not write framework configuration, Terraform, Kubernetes policies, or code-level authorization rules
- do not produce a full formal threat-model report unless the user asks for that stage
- do not hide unresolved compliance, privacy, tenant isolation, admin access, or data exposure decisions
- do not prescribe encryption, tokens, roles, or audit logs without tying them to a risk or requirement
- do not treat authentication as enough when authorization, data exposure, and audit also matter

You may state security-level architecture decisions:

- this API crosses a public trust boundary and needs explicit rate limits, audit, and abuse controls
- this admin action must use separate privileged access and produce immutable audit events
- this tenant boundary must be enforced at every read and write path
- this integration needs workload identity and scoped credentials instead of shared static secrets
- this sensitive data should be tokenized or minimized before it leaves the owning boundary

## Stop Conditions

Stop and ask when:

- regulated data, privacy, legal, financial, medical, or safety risk is central and unknown
- tenant isolation or privileged access expectations are unclear
- identity provider, actor model, or external trust relationship is unknown and cannot be safely inferred
- the user asks for implementation security controls while architecture-level risks and boundaries are unresolved
