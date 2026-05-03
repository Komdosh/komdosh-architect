# Architecture Diagrammer Marketplace

Codex marketplace for the Architecture Diagrammer plugin.

## Install

```bash
codex plugin marketplace add https://github.com/Komdosh/architecture-diagrammer.git
```

The marketplace name is `local-architecture-tools`, and it exposes the `architecture-diagrammer` plugin.

To enable the plugin explicitly in `~/.codex/config.toml`:

```toml
[plugins."architecture-diagrammer@local-architecture-tools"]
enabled = true
```

Restart Codex after adding or updating the marketplace so the plugin skills are loaded into the session context.

## Plugin

The plugin package lives at [plugins/architecture-diagrammer](plugins/architecture-diagrammer).
