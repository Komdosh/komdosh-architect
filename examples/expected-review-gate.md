# Expected Review Gate Output

Source: [source-backed-order-flow.md](source-backed-order-flow.md)

```text
SCHEMA: pass
Architecture fit: pass
Presentation: pass
Format validity: pass
```

## Checks

- Scope: one confirmed order-submission flow, no deferred or optional capabilities.
- Components: actor, public gateway, owning service, authoritative PostgreSQL store, event backbone, and downstream projection are all source-backed.
- Hierarchy: Search Projection is shown as downstream read model, not authoritative state.
- Edges: command, write, publish, and consume relationships are directional and labeled.
- Medium: Mermaid, DrawIO, and Excalidraw artifacts each carry the same source-backed meaning.
- Alignment: left-to-right flow follows caller, gateway, service, event, projection; store write is attached to the owning service.
- Format validity: Mermaid syntax is simple, DrawIO XML parses with source/target edge cells, and Excalidraw JSON parses with bound arrows.
