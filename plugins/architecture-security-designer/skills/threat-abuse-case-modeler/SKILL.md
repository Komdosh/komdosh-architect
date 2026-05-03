---
name: threat-abuse-case-modeler
description: Identify architecture-level abuse cases, misuse paths, attacker goals, privileged misuse, fraud, automation abuse, data exfiltration, denial paths, and required mitigations without producing a full formal threat model unless asked.
---

# Threat Abuse Case Modeler

## Purpose

Identify the ways the system can be misused.
This is an architecture-level abuse pass, not a full formal threat-model report unless the user asks for that stage.

## Required Inputs

Require:

- security context inventory
- trust boundary map
- identity, authorization, data, or integration context when available

## Abuse Concerns

Consider:

- external attacker goals
- malicious or compromised user behavior
- admin, operator, or support misuse
- service credential compromise
- tenant boundary bypass
- data exfiltration or overexposure
- automation, scraping, spam, fraud, and quota abuse
- webhook, event, callback, and batch replay or spoofing
- denial of service or resource exhaustion
- audit evasion and evidence tampering

## Output

Return:

| Abuse case | Actor | Target | Path | Impact | Required mitigation |
|------------|-------|--------|------|--------|---------------------|

Then list:

- highest-risk misuse paths
- controls that must exist in architecture
- detection and audit needs
- assumptions to verify in formal threat modeling
- open abuse-case questions
