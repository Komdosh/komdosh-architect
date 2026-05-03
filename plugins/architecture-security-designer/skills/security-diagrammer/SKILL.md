---
name: security-diagrammer
description: Create architecture-level security context, trust-boundary, identity/access, authorization, data-exposure, API/integration security, abuse-flow, and audit diagrams from source-backed security decisions.
---

# Security Diagrammer

## Purpose

Visualize security architecture.
Diagrams should make trust, access, sensitive data, control points, and abuse paths clear without becoming implementation configuration.

## Required Inputs

Require:

- security context inventory
- trust boundary map
- identity, authorization, data, integration, or abuse-case decisions when relevant
- requested format when the user needs Mermaid, DrawIO, or another output

If security inputs are missing, route back to `$architecture-security-designer:architecture-security-designer`.

## Diagram Types

Use a security context diagram when the goal is:

- actors, assets, systems, external providers, and trust zones

Use a trust-boundary diagram when the goal is:

- boundary crossings, exposed entry points, and control points

Use an access diagram when the goal is:

- identities, authentication, authorization, tenant isolation, and privileged paths

Use a data-exposure diagram when the goal is:

- sensitive data movement, storage, logging, export, and external sharing

Use an abuse-flow diagram when the goal is:

- misuse path, detection point, and mitigation path

## Diagram Rules

- Label boundaries with trust level or exposure type.
- Label edges with security meaning, not implementation method.
- Show admins, operators, services, jobs, and external systems when they affect security.
- Mark sensitive data and privileged operations clearly.
- Keep controls tied to risk: authentication, authorization, validation, rate limit, audit, monitoring, or encryption.
- Do not show framework classes, library configuration, IAM resource names, Terraform resources, or code-level policy rules.

## Output

Return:

- diagram purpose
- security context, trust-boundary, access, data-exposure, integration-security, abuse-flow, or audit diagram
- source-assumption note
- diagram limitations for later detailed threat model or implementation design
