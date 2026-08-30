# Security and Architecture Risk

## Security architecture

- Inventory assets and sensitivity; human, service, operator, support, job, and external identities; privileged paths; and trust-boundary crossings.
- Define authentication and credential/session flow, then authorization by resource, action, scope, tenant, policy owner, and audit point. Include delegated and break-glass access when relevant.
- Minimize sensitive data and define encryption posture, key ownership, masking or tokenization, sharing, export, retention, deletion, residency, and privacy obligations.
- Model credible abuse and misuse: privilege escalation, fraudulent workflows, automation abuse, data exfiltration, denial paths, confused-deputy behavior, and privileged insider misuse.
- Secure public, partner, internal, admin, event, webhook, batch, and provider interfaces according to their exposure and data.
- Define secrets, keys, certificates, service accounts, and tokens through creation, storage, distribution, access, rotation, revocation, expiry, incident response, and recovery.
- Identify required audit events, tamper resistance where warranted, compliance evidence, anomaly signals, investigation context, retention, and evidence ownership.

Map each material control to a requirement, threat, trust crossing, or compliance obligation. Avoid generic control inventories and product choices that do not change a decision.

## Risk and readiness

- State a risk as a condition and consequence, backed by evidence. Do not turn missing evidence into a claim of failure.
- Prioritize by likelihood, impact, urgency, blast radius, reversibility, detectability, and confidence only to the depth needed for a decision.
- For material risks, name the mitigation, validation signal or spike, owner, deadline or trigger, fallback, residual risk, and revisit condition.
- Treat assumptions as risks when their failure would invalidate a boundary, capacity estimate, control, rollout, or business outcome.
- Record accepted risk only with an explicit decision owner and consequence. “Known” is not the same as accepted.
- Give one readiness result: `Go`, `Conditional go`, or `No-go`, followed by the exact blockers or conditions.

Do not claim security, compliance, or production readiness when essential evidence or ownership is absent.
