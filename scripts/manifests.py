#!/usr/bin/env python3
"""Keep the Claude Code and Codex manifests of this marketplace in step.

  manifests.py check [ROOT]                 report drift between the two marketplaces, plugin manifests,
                                            CHANGELOG.md, LICENSE and SKILL.md files; exit 1 on any problem
  manifests.py bump PLUGIN VERSION [ROOT]   set VERSION in both plugin.json files of PLUGIN

Standard library only, so it runs in CI and on a bare python3.
"""

import argparse
import json
import re
import sys
from pathlib import Path

CLAUDE_MARKETPLACE = ".claude-plugin/marketplace.json"
CODEX_MARKETPLACE = ".agents/plugins/marketplace.json"
CLAUDE_MANIFEST = ".claude-plugin/plugin.json"
CODEX_MANIFEST = ".codex-plugin/plugin.json"
CODEX_INTERFACE = ("displayName", "shortDescription", "longDescription", "developerName", "category", "capabilities")
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$")
KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DEFAULT_ROOT = Path(__file__).resolve().parent.parent


def load_json(root, rel, errors):
    try:
        return json.loads((root / rel).read_text())
    except FileNotFoundError:
        errors.append(f"{rel}: file is missing")
    except json.JSONDecodeError as exc:
        errors.append(f"{rel}: invalid JSON ({exc})")
    return None


def plugin_paths(marketplace, rel, errors):
    """Map plugin name -> relative path ("plugins/x") for every entry of a marketplace file."""
    paths = {}
    for entry in marketplace.get("plugins", []):
        source = entry.get("source")
        if isinstance(source, dict):
            source = source.get("path") if source.get("source") == "local" else None
        if not isinstance(source, str) or not source.startswith("./"):
            errors.append(f"{rel}: plugin {entry.get('name')!r} needs a local source starting with ./")
            continue
        paths[entry.get("name")] = source[2:].rstrip("/")
    return paths


def unquote(value):
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
        return value[1:-1]
    return value


def read_frontmatter(path):
    """Return the keys of a SKILL.md YAML frontmatter, or None when there is none.

    Covers what skills use: plain and quoted scalars, folded or literal blocks (joined with
    spaces) and one level of nested mapping such as `metadata: {author: ...}`.
    """
    lines = path.read_text().splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    try:
        end = lines.index("---", 1)
    except ValueError:
        return None
    fields, key, block = {}, None, False
    for line in lines[1:end]:
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        nested = re.match(r"^\s+([A-Za-z0-9_-]+):\s*(.*)$", line)
        if match:
            key, value = match.groups()
            block = value in (">", ">-", "|", "|-")
            fields[key] = "" if block else unquote(value)
        elif key and nested and not block and (fields[key] == "" or isinstance(fields[key], dict)):
            fields[key] = fields[key] or {}
            fields[key][nested.group(1)] = unquote(nested.group(2))
        elif key and line.startswith((" ", "\t")) and isinstance(fields[key], str):
            fields[key] = (fields[key] + " " + line.strip()).strip()
    return fields


def check_skills(root, plugin_dir, license_id, author, license_text, errors):
    """Each skill names the plugin's license and author and carries LICENSE.txt, so a copied folder keeps both."""
    skills_dir = root / plugin_dir / "skills"
    count = 0
    for skill in sorted(p for p in skills_dir.iterdir() if p.is_dir()) if skills_dir.is_dir() else []:
        rel = f"{plugin_dir}/skills/{skill.name}/SKILL.md"
        if not (skill / "SKILL.md").is_file():
            errors.append(f"{rel}: file is missing")
            continue
        count += 1
        fields = read_frontmatter(skill / "SKILL.md")
        if fields is None:
            errors.append(f"{rel}: no YAML frontmatter between --- lines")
            continue
        name, description = fields.get("name", ""), fields.get("description", "")
        if name != skill.name:
            errors.append(f"{rel}: name {name!r} differs from the folder name {skill.name!r}")
        if not KEBAB.match(name) or len(name) > 64:
            errors.append(f"{rel}: name {name!r} must be kebab-case, at most 64 characters")
        if not isinstance(description, str) or not description or len(description) > 1024:
            errors.append(f"{rel}: description must be 1-1024 characters, has {len(description)}")
        if fields.get("license") != license_id:
            errors.append(f"{rel}: license {fields.get('license')!r} must be the plugin license {license_id!r}")
        metadata = fields.get("metadata") if isinstance(fields.get("metadata"), dict) else {}
        if metadata.get("author") != author:
            errors.append(f"{rel}: metadata.author {metadata.get('author')!r} must be the plugin author {author!r}")
        license_copy = skill / "LICENSE.txt"
        if not license_copy.is_file():
            errors.append(f"{plugin_dir}/skills/{skill.name}/LICENSE.txt: file is missing, copy LICENSE here")
        elif license_text is not None and license_copy.read_text() != license_text:
            errors.append(f"{plugin_dir}/skills/{skill.name}/LICENSE.txt: differs from LICENSE")
    return count


def check_plugin(root, name, plugin_dir, changelog, license_text, errors):
    if not (root / plugin_dir).is_dir():
        errors.append(f"{plugin_dir}: plugin folder is missing")
        return 0
    if Path(plugin_dir).name != name:
        errors.append(f"{plugin_dir}: folder name differs from plugin name {name!r}")
    versions, licenses, authors = {}, {}, {}
    for manifest in (CLAUDE_MANIFEST, CODEX_MANIFEST):
        rel = f"{plugin_dir}/{manifest}"
        data = load_json(root, rel, errors)
        if data is None:
            continue
        if data.get("name") != name:
            errors.append(f"{rel}: name {data.get('name')!r} differs from the marketplace entry {name!r}")
        if not SEMVER.match(str(data.get("version", ""))):
            errors.append(f"{rel}: version {data.get('version')!r} is not semver")
        versions[rel] = data.get("version")
        if not data.get("description"):
            errors.append(f"{rel}: description is empty")
        if not (data.get("author") or {}).get("name"):
            errors.append(f"{rel}: author.name is empty")
        authors[rel] = (data.get("author") or {}).get("name")
        if not data.get("license"):
            errors.append(f"{rel}: license is empty")
        licenses[rel] = data.get("license")
        if manifest == CODEX_MANIFEST:
            if data.get("skills") not in ("./skills/", "./skills"):
                errors.append(f"{rel}: skills must be \"./skills/\"")
            interface = data.get("interface") or {}
            for field in CODEX_INTERFACE:
                if not interface.get(field):
                    errors.append(f"{rel}: interface.{field} is empty")
            if len(interface.get("shortDescription", "")) > 30:
                errors.append(f"{rel}: interface.shortDescription is longer than 30 characters")
    for field, values in (("version", versions), ("license", licenses), ("author.name", authors)):
        if len(set(values.values())) > 1:
            errors.append(f"{plugin_dir}: {field} differs between manifests: {values}")
    version = next(iter(versions.values()), None)
    if version and not re.search(rf"^## .*\b{re.escape(version)}\b", changelog, re.MULTILINE):
        errors.append(f"CHANGELOG.md: no '## {version}' heading for plugin {name!r}")
    license_id = next(iter(licenses.values()), None)
    author = next(iter(authors.values()), None)
    return check_skills(root, plugin_dir, license_id, author, license_text, errors)


def check(root):
    errors = []
    claude = load_json(root, CLAUDE_MARKETPLACE, errors)
    codex = load_json(root, CODEX_MARKETPLACE, errors)
    if claude is None or codex is None:
        return errors, 0, 0
    if claude.get("name") != codex.get("name"):
        errors.append(f"marketplace name differs: {claude.get('name')!r} in {CLAUDE_MARKETPLACE}, "
                      f"{codex.get('name')!r} in {CODEX_MARKETPLACE}")
    claude_paths = plugin_paths(claude, CLAUDE_MARKETPLACE, errors)
    codex_paths = plugin_paths(codex, CODEX_MARKETPLACE, errors)
    for name in sorted(claude_paths.keys() - codex_paths.keys()):
        errors.append(f"{CODEX_MARKETPLACE}: plugin {name!r} is missing (listed in {CLAUDE_MARKETPLACE})")
    for name in sorted(codex_paths.keys() - claude_paths.keys()):
        errors.append(f"{CLAUDE_MARKETPLACE}: plugin {name!r} is missing (listed in {CODEX_MARKETPLACE})")
    changelog = (root / "CHANGELOG.md").read_text() if (root / "CHANGELOG.md").is_file() else ""
    license_text = (root / "LICENSE").read_text() if (root / "LICENSE").is_file() else None
    if license_text is None:
        errors.append("LICENSE: file is missing")
    plugins = skills = 0
    for name in sorted(claude_paths.keys() & codex_paths.keys()):
        if claude_paths[name] != codex_paths[name]:
            errors.append(f"plugin {name!r}: path differs between marketplaces: "
                          f"{claude_paths[name]!r} vs {codex_paths[name]!r}")
            continue
        plugins += 1
        skills += check_plugin(root, name, claude_paths[name], changelog, license_text, errors)
    return errors, plugins, skills


def bump(root, plugin, version):
    if not SEMVER.match(version):
        return [f"version {version!r} is not semver"]
    errors = []
    marketplace = load_json(root, CLAUDE_MARKETPLACE, errors)
    if marketplace is None:
        return errors
    plugin_dir = plugin_paths(marketplace, CLAUDE_MARKETPLACE, errors).get(plugin)
    if plugin_dir is None:
        return errors + [f"{CLAUDE_MARKETPLACE}: no plugin {plugin!r}"]
    for manifest in (CLAUDE_MANIFEST, CODEX_MANIFEST):
        path = root / plugin_dir / manifest
        # Replace the first "version" value in place to keep the file's formatting.
        text = re.sub(r'("version"\s*:\s*")[^"]*(")', rf"\g<1>{version}\g<2>", path.read_text(), count=1)
        if json.loads(text).get("version") != version:
            return errors + [f"{plugin_dir}/{manifest}: top-level version not found"]
        path.write_text(text)
        print(f"{plugin_dir}/{manifest}: version {version}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    check_cmd = sub.add_parser("check")
    check_cmd.add_argument("root", nargs="?", type=Path, default=DEFAULT_ROOT)
    bump_cmd = sub.add_parser("bump")
    bump_cmd.add_argument("plugin")
    bump_cmd.add_argument("version")
    bump_cmd.add_argument("root", nargs="?", type=Path, default=DEFAULT_ROOT)
    args = parser.parse_args()

    if args.command == "check":
        errors, plugins, skills = check(args.root)
        if not errors:
            print(f"ok: {plugins} plugin(s), {skills} skill(s), manifests in step")
    else:
        errors = bump(args.root, args.plugin, args.version)
    for error in errors:
        print(f"error: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
