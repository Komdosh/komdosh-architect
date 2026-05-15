# Architecture Diagrammer Examples

These examples prove the plugin contract on a small source-backed architecture text.
Use them when changing skill instructions, export rules, or review-gate criteria.

## Files

- [source-backed-order-flow.md](source-backed-order-flow.md) - authoritative source text and boundary inventory.
- [expected-order-flow.mmd](expected-order-flow.mmd) - expected Mermaid output.
- [expected-order-flow.drawio](expected-order-flow.drawio) - expected DrawIO output.
- [expected-order-flow.excalidraw](expected-order-flow.excalidraw) - expected Excalidraw output.
- [expected-review-gate.md](expected-review-gate.md) - expected review-gate result for the three artifacts.

The examples intentionally stay small: actor, gateway, owning service, authoritative store, event backbone, and downstream projection.
The DrawIO and Excalidraw examples also keep visible gaps between connected blocks so edge labels are readable instead of squeezed into the line. In the Excalidraw example, block labels are bound text inside rectangle elements, not loose sibling text blocks.
