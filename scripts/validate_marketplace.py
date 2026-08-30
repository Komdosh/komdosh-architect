#!/usr/bin/env python3
"""Validate this repository's marketplace, plugin, skill, and local references."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE_PATH = ROOT / ".agents/plugins/marketplace.json"
PLUGIN_NAME_RE = re.compile(r"^[A-Za-z0-9_-]+(?:\.[A-Za-z0-9_-]+)*$")
SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_RE = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$"
)
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
FRONTMATTER_NAME_RE = re.compile(r"(?m)^name:\s*([A-Za-z0-9_-]+)\s*$")
FRONTMATTER_DESCRIPTION_RE = re.compile(r"(?m)^description:\s*(.+?)\s*$")
SKILL_REF_RE = re.compile(r"\$([a-z0-9-]+):([a-z0-9-]+)")
LOCAL_MD_LINK_RE = re.compile(r"\[[^\]]+\]\((?!https?://|#)([^)]+\.md)\)")
ALLOWED_INSTALLATION = {"NOT_AVAILABLE", "AVAILABLE", "INSTALLED_BY_DEFAULT"}
ALLOWED_AUTHENTICATION = {"ON_INSTALL", "ON_USE"}


def load_json(path: Path, errors: list[str]) -> Any:
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        errors.append(f"{path.relative_to(ROOT)} is not valid JSON: {exc}")
        return None


def mapping(value: Any, label: str, errors: list[str]) -> dict[str, Any]:
    if isinstance(value, dict):
        return value
    errors.append(f"{label} must be an object")
    return {}


def require_text(container: dict[str, Any], key: str, label: str, errors: list[str]) -> str:
    value = container.get(key)
    if isinstance(value, str) and value.strip():
        return value
    errors.append(f"{label}.{key} must be a non-empty string")
    return ""


def validate_local_markdown_links(path: Path, errors: list[str]) -> None:
    text = path.read_text(errors="ignore")
    for target in LOCAL_MD_LINK_RE.findall(text):
        clean_target = target.split("#", 1)[0]
        if clean_target and not (path.parent / clean_target).resolve().is_file():
            errors.append(f"{path.relative_to(ROOT)} links to missing {target}")


def collect_skills(plugin_name: str, plugin_dir: Path, errors: list[str]) -> set[str]:
    skills_dir = plugin_dir / "skills"
    skill_files = sorted(skills_dir.glob("*/SKILL.md"))
    if not skill_files:
        errors.append(f"{plugin_name} must contain at least one skills/<name>/SKILL.md")
        return set()

    names: set[str] = set()
    for path in skill_files:
        match = FRONTMATTER_RE.search(path.read_text())
        if not match:
            errors.append(f"{path.relative_to(ROOT)} is missing YAML frontmatter")
            continue
        frontmatter = match.group(1)
        name_match = FRONTMATTER_NAME_RE.search(frontmatter)
        description_match = FRONTMATTER_DESCRIPTION_RE.search(frontmatter)
        if not name_match:
            errors.append(f"{path.relative_to(ROOT)} frontmatter is missing name")
            continue
        name = name_match.group(1)
        if not SKILL_NAME_RE.fullmatch(name):
            errors.append(f"{path.relative_to(ROOT)} has invalid skill name {name}")
        if path.parent.name != name:
            errors.append(f"{path.relative_to(ROOT)} folder must match skill name {name}")
        if name in names:
            errors.append(f"{plugin_name} has duplicate skill name {name}")
        names.add(name)
        if not description_match or not description_match.group(1).strip():
            errors.append(f"{path.relative_to(ROOT)} frontmatter is missing description")
        if not (path.parent / "agents/openai.yaml").is_file():
            errors.append(f"{path.parent.relative_to(ROOT)} is missing agents/openai.yaml")
        validate_local_markdown_links(path, errors)
        for reference in sorted((path.parent / "references").glob("*.md")):
            validate_local_markdown_links(reference, errors)
    return names


def validate_manifest(
    plugin_name: str, plugin_dir: Path, errors: list[str]
) -> set[str]:
    path = plugin_dir / ".codex-plugin/plugin.json"
    manifest = mapping(load_json(path, errors), f"{plugin_name} manifest", errors)
    if manifest.get("name") != plugin_name:
        errors.append(f"{path.relative_to(ROOT)} name must equal {plugin_name}")
    version = require_text(manifest, "version", plugin_name, errors)
    if version and not SEMVER_RE.fullmatch(version):
        errors.append(f"{path.relative_to(ROOT)} version is not strict semver: {version}")
    require_text(manifest, "description", plugin_name, errors)
    require_text(mapping(manifest.get("author"), f"{plugin_name}.author", errors), "name", f"{plugin_name}.author", errors)
    require_text(manifest, "license", plugin_name, errors)
    if manifest.get("skills") != "./skills/":
        errors.append(f"{path.relative_to(ROOT)} skills must be ./skills/")

    interface = mapping(manifest.get("interface"), f"{plugin_name}.interface", errors)
    for field in (
        "displayName",
        "shortDescription",
        "longDescription",
        "developerName",
        "category",
        "brandColor",
    ):
        require_text(interface, field, f"{plugin_name}.interface", errors)
    capabilities = interface.get("capabilities")
    if not isinstance(capabilities, list) or not capabilities or not all(
        isinstance(item, str) and item for item in capabilities
    ):
        errors.append(f"{plugin_name}.interface.capabilities must be a non-empty string array")
    prompts = interface.get("defaultPrompt")
    if not isinstance(prompts, list) or not 1 <= len(prompts) <= 3:
        errors.append(f"{plugin_name}.interface.defaultPrompt must contain 1 to 3 prompts")
    elif any(not isinstance(prompt, str) or not prompt or len(prompt) > 128 for prompt in prompts):
        errors.append(f"{plugin_name}.interface.defaultPrompt entries must be 1 to 128 characters")
    for field in ("homepage", "repository"):
        value = manifest.get(field)
        if value is not None and (not isinstance(value, str) or not value.startswith("https://")):
            errors.append(f"{path.relative_to(ROOT)} {field} must be an https URL")

    return collect_skills(plugin_name, plugin_dir, errors)


def validate_marketplace(errors: list[str]) -> tuple[list[str], set[str]]:
    marketplace = mapping(load_json(MARKETPLACE_PATH, errors), "marketplace", errors)
    require_text(marketplace, "name", "marketplace", errors)
    require_text(
        mapping(marketplace.get("interface"), "marketplace.interface", errors),
        "displayName",
        "marketplace.interface",
        errors,
    )
    entries = marketplace.get("plugins")
    if not isinstance(entries, list) or not entries:
        errors.append("marketplace.plugins must be a non-empty array")
        return [], set()

    plugin_names: list[str] = []
    known_refs: set[str] = set()
    for index, raw_entry in enumerate(entries):
        entry = mapping(raw_entry, f"marketplace plugin #{index}", errors)
        name = require_text(entry, "name", f"marketplace plugin #{index}", errors)
        if not name:
            continue
        if not PLUGIN_NAME_RE.fullmatch(name):
            errors.append(f"marketplace plugin #{index} has invalid name {name}")
        if name in plugin_names:
            errors.append(f"marketplace has duplicate plugin name {name}")
        plugin_names.append(name)

        source = mapping(entry.get("source"), f"{name}.source", errors)
        if source.get("source") != "local":
            errors.append(f"{name}.source.source must be local")
        expected_path = f"./plugins/{name}"
        if source.get("path") != expected_path:
            errors.append(f"{name}.source.path must be {expected_path}")
        plugin_dir = ROOT / "plugins" / name
        if not plugin_dir.is_dir():
            errors.append(f"{expected_path} does not exist")
            continue

        policy = mapping(entry.get("policy"), f"{name}.policy", errors)
        if policy.get("installation") not in ALLOWED_INSTALLATION:
            errors.append(f"{name}.policy.installation is invalid")
        if policy.get("authentication") not in ALLOWED_AUTHENTICATION:
            errors.append(f"{name}.policy.authentication is invalid")
        require_text(entry, "category", name, errors)

        for skill_name in validate_manifest(name, plugin_dir, errors):
            known_refs.add(f"{name}:{skill_name}")

    plugin_dirs = {
        path.name
        for path in (ROOT / "plugins").iterdir()
        if path.is_dir() and any(child.is_file() for child in path.rglob("*"))
    }
    for stale in sorted(plugin_dirs.difference(plugin_names)):
        errors.append(f"plugins/{stale} contains files but is absent from marketplace.json")
    return plugin_names, known_refs


def validate_namespaced_refs(known_refs: set[str], errors: list[str]) -> None:
    files = [ROOT / "README.md"]
    files.extend(
        path
        for path in (ROOT / "plugins").rglob("*")
        if path.is_file() and path.suffix in {".md", ".json", ".yaml", ".yml"}
    )
    for path in sorted(set(files)):
        for plugin_name, skill_name in SKILL_REF_RE.findall(path.read_text(errors="ignore")):
            ref = f"{plugin_name}:{skill_name}"
            if ref not in known_refs:
                errors.append(f"{path.relative_to(ROOT)} references unknown skill ${ref}")


def validate_readme(plugin_names: list[str], known_refs: set[str], errors: list[str]) -> None:
    readme = (ROOT / "README.md").read_text(errors="ignore")
    for name in plugin_names:
        if f"plugins/{name}" not in readme:
            errors.append(f"README.md does not link to plugins/{name}")
    for ref in known_refs:
        if f"${ref}" not in readme:
            errors.append(f"README.md does not show invocation ${ref}")


def main() -> int:
    errors: list[str] = []
    plugin_names, known_refs = validate_marketplace(errors)
    validate_namespaced_refs(known_refs, errors)
    validate_readme(plugin_names, known_refs, errors)
    if errors:
        print("Marketplace validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Marketplace validation passed: {len(plugin_names)} plugin, {len(known_refs)} skill.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
