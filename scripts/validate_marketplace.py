#!/usr/bin/env python3
"""Validate marketplace metadata, plugin manifests, and skill references."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE_PATH = ROOT / ".agents/plugins/marketplace.json"
SKILL_REF_RE = re.compile(r"\$([a-z0-9-]+):([a-z0-9-]+)")
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
FRONTMATTER_NAME_RE = re.compile(r"(?m)^name:\s*([A-Za-z0-9_-]+)\s*$")
FRONTMATTER_DESCRIPTION_RE = re.compile(r"(?m)^description:\s*(.+?)\s*$")


def load_json(path: Path, errors: list[str]) -> Any:
    try:
        return json.loads(path.read_text())
    except Exception as exc:  # pragma: no cover - exact parser message is enough.
        errors.append(f"{path.relative_to(ROOT)} is not valid JSON: {exc}")
        return None


def require_mapping(value: Any, label: str, errors: list[str]) -> dict[str, Any]:
    if not isinstance(value, dict):
        errors.append(f"{label} must be a JSON object")
        return {}
    return value


def parse_skill_frontmatter(
    skill_path: Path, errors: list[str]
) -> tuple[str | None, str | None]:
    text = skill_path.read_text()
    frontmatter_match = FRONTMATTER_RE.search(text)
    if not frontmatter_match:
        errors.append(f"{skill_path.relative_to(ROOT)} is missing YAML frontmatter")
        return None, None

    frontmatter = frontmatter_match.group(1)
    name_match = FRONTMATTER_NAME_RE.search(frontmatter)
    description_match = FRONTMATTER_DESCRIPTION_RE.search(frontmatter)

    if not name_match:
        errors.append(f"{skill_path.relative_to(ROOT)} frontmatter is missing name")
    if not description_match:
        errors.append(f"{skill_path.relative_to(ROOT)} frontmatter is missing description")

    name = name_match.group(1) if name_match else None
    description = description_match.group(1).strip() if description_match else None
    return name, description


def collect_plugin_skills(plugin_name: str, plugin_dir: Path, errors: list[str]) -> set[str]:
    skill_files = sorted((plugin_dir / "skills").glob("*/SKILL.md"))
    if not skill_files:
        errors.append(f"{plugin_name} has no skills under {plugin_dir.relative_to(ROOT)}/skills")
        return set()

    names: set[str] = set()
    for skill_path in skill_files:
        name, _description = parse_skill_frontmatter(skill_path, errors)
        if not name:
            continue
        if name in names:
            errors.append(f"{plugin_name} has duplicate skill name {name}")
        names.add(name)

        agents_yaml = skill_path.parent / "agents/openai.yaml"
        if not agents_yaml.exists():
            errors.append(f"{skill_path.parent.relative_to(ROOT)} is missing agents/openai.yaml")

    return names


def validate_marketplace(errors: list[str]) -> tuple[list[str], set[str]]:
    marketplace = require_mapping(load_json(MARKETPLACE_PATH, errors), "marketplace", errors)
    plugin_entries = marketplace.get("plugins")
    if not isinstance(plugin_entries, list):
        errors.append(".agents/plugins/marketplace.json must contain a plugins array")
        return [], set()

    plugin_names: list[str] = []
    known_skill_refs: set[str] = set()
    seen_plugin_names: set[str] = set()

    for index, entry in enumerate(plugin_entries):
        entry = require_mapping(entry, f"marketplace plugin #{index}", errors)
        name = entry.get("name")
        if not isinstance(name, str) or not name:
            errors.append(f"marketplace plugin #{index} is missing name")
            continue
        if name in seen_plugin_names:
            errors.append(f"marketplace has duplicate plugin name {name}")
        seen_plugin_names.add(name)
        plugin_names.append(name)

        source = require_mapping(entry.get("source"), f"{name}.source", errors)
        if source.get("source") != "local":
            errors.append(f"{name}.source.source must be local")
        source_path = source.get("path")
        if not isinstance(source_path, str) or not source_path.startswith("./plugins/"):
            errors.append(f"{name}.source.path must point at ./plugins/<name>")
            continue

        plugin_dir = (ROOT / source_path).resolve()
        try:
            plugin_dir.relative_to(ROOT)
        except ValueError:
            errors.append(f"{name}.source.path escapes the repository")
            continue
        if not plugin_dir.is_dir():
            errors.append(f"{name}.source.path does not exist: {source_path}")
            continue

        manifest_path = plugin_dir / ".codex-plugin/plugin.json"
        manifest = require_mapping(load_json(manifest_path, errors), f"{name} manifest", errors)
        if manifest.get("name") != name:
            errors.append(f"{manifest_path.relative_to(ROOT)} name must match marketplace entry {name}")
        if not manifest.get("description"):
            errors.append(f"{manifest_path.relative_to(ROOT)} is missing description")
        interface = require_mapping(manifest.get("interface"), f"{name}.interface", errors)
        if not interface.get("displayName"):
            errors.append(f"{manifest_path.relative_to(ROOT)} interface.displayName is missing")
        if not interface.get("shortDescription"):
            errors.append(f"{manifest_path.relative_to(ROOT)} interface.shortDescription is missing")

        for skill_name in collect_plugin_skills(name, plugin_dir, errors):
            known_skill_refs.add(f"{name}:{skill_name}")

    manifest_plugin_dirs = {
        path.parent.parent.name
        for path in (ROOT / "plugins").glob("*/.codex-plugin/plugin.json")
    }
    missing_from_marketplace = sorted(manifest_plugin_dirs.difference(seen_plugin_names))
    for name in missing_from_marketplace:
        errors.append(f"plugins/{name} has a manifest but is missing from marketplace.json")

    return plugin_names, known_skill_refs


def validate_skill_references(known_skill_refs: set[str], errors: list[str]) -> None:
    checked_suffixes = {".md", ".json", ".yaml", ".yml"}
    files = [ROOT / "README.md"]
    files.extend(
        path
        for path in (ROOT / "plugins").rglob("*")
        if path.is_file() and path.suffix in checked_suffixes
    )

    for path in sorted(set(files)):
        text = path.read_text(errors="ignore")
        for plugin_name, skill_name in SKILL_REF_RE.findall(text):
            ref = f"{plugin_name}:{skill_name}"
            if ref not in known_skill_refs:
                errors.append(f"{path.relative_to(ROOT)} references unknown skill ${ref}")


def validate_readme_catalog(plugin_names: list[str], errors: list[str]) -> None:
    readme = (ROOT / "README.md").read_text()
    for plugin_name in plugin_names:
        if f"plugins/{plugin_name}" not in readme:
            errors.append(f"README.md does not link to plugins/{plugin_name}")
        if f'[plugins."{plugin_name}@komdosh-architect"]' not in readme:
            errors.append(f"README.md is missing enable snippet for {plugin_name}")


def main() -> int:
    errors: list[str] = []
    plugin_names, known_skill_refs = validate_marketplace(errors)
    validate_skill_references(known_skill_refs, errors)
    validate_readme_catalog(plugin_names, errors)

    if errors:
        print("Marketplace validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Marketplace validation passed: {len(plugin_names)} plugins, {len(known_skill_refs)} skills.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
