---
name: authorization-policy-designer
description: Define authorization architecture, permission model, roles, scopes, policy ownership, tenant isolation, delegated access, admin/operator privilege, support access, and decision/audit points.
---

# Authorization Policy Designer

## Purpose

Define what each identity is allowed to do.
Authorization should protect data, tenants, operations, and privileged paths without freezing implementation policy too early.

## Required Inputs

Require:

- identity model
- actors, roles, and tenant context
- data and service ownership when available

## Authorization Concerns

Define:

- permission model: roles, scopes, claims, attributes, ownership, or policy decision style at architecture level
- policy owner and source of truth
- tenant, organization, workspace, account, or resource boundary
- admin, operator, support, and break-glass privilege
- delegated access and service-to-service authorization
- read/write/export/delete authorization differences
- policy decision point and enforcement point at architecture level
- denial behavior and audit needs
- migration and compatibility risks for permissions

## Output

Return:

| Action/resource | Actor | Permission rule | Enforcement point | Audit need | Risk |
|-----------------|-------|-----------------|-------------------|------------|------|

Then list:

- permission model decision
- tenant isolation rules
- privileged access rules
- policy ownership
- open authorization questions
