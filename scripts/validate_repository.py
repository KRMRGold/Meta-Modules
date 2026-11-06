#!/usr/bin/env python3
"""Validate metadata, optional filename-version consistency, and local Markdown links."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

import yaml

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_TYPES = {"foundational", "specialized", "specialized-workflow", "reference-design"}
REQUIRED_FIELDS = {"name", "type", "version", "purpose", "use_when"}
LINK_RE = re.compile(r"!??\[[^\]]*\]\(([^)]+)\)")
SEMVER_RE = re.compile(r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)\Z")
VERSIONED_FILENAME_RE = re.compile(r"-v(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)\.md\Z")


def markdown_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.md") if not any(part in {".git", ".venv"} for part in p.parts))


def read_front_matter(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, "missing YAML front matter"
    end = text.find("\n---", 4)
    if end < 0:
        return None, "unterminated YAML front matter"
    try:
        data = yaml.safe_load(text[4:end])
    except yaml.YAMLError as exc:
        return None, f"invalid YAML front matter: {exc}"
    if not isinstance(data, dict):
        return None, "front matter must be a YAML mapping"
    return data, None


def validate_repository(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    md_files = markdown_files(root)
    metadata_files = [
        p for p in md_files
        if p != root / "README.md"
        and any(p.is_relative_to(root / folder) for folder in ("modules", "workflows", "architecture"))
    ]
    if not metadata_files:
        errors.append("No metadata-bearing module/workflow/architecture files found.")
    for path in metadata_files:
        data, error = read_front_matter(path)
        rel = path.relative_to(root).as_posix()
        if error:
            errors.append(f"{rel}: {error}")
            continue
        missing = sorted(REQUIRED_FIELDS - data.keys())
        if missing:
            errors.append(f"{rel}: missing required fields: {', '.join(missing)}")
        if data.get("type") not in ALLOWED_TYPES:
            errors.append(f"{rel}: unsupported type {data.get('type')!r}; allowed: {', '.join(sorted(ALLOWED_TYPES))}")
        for key in REQUIRED_FIELDS:
            if key in data and (data[key] is None or not str(data[key]).strip()):
                errors.append(f"{rel}: field {key!r} must not be empty")
        version = data.get("version")
        if version is not None and not SEMVER_RE.fullmatch(str(version)):
            errors.append(f"{rel}: version {version!r} must use MAJOR.MINOR.PATCH SemVer")
        filename_version = VERSIONED_FILENAME_RE.search(path.name)
        if filename_version and version is not None:
            filename_semver = ".".join(filename_version.groups())
            if filename_semver != str(version):
                errors.append(f"{rel}: filename version {filename_semver!r} does not match front matter version {version!r}")

    for path in md_files:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(root).as_posix()
        for match in LINK_RE.finditer(text):
            target = match.group(1).strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "tel:")):
                continue
            target = target.split("#", 1)[0].split("?", 1)[0].strip("<>")
            if not target:
                continue
            target_path = (path.parent / unquote(target)).resolve()
            if not target_path.exists():
                errors.append(f"{rel}: broken local link {match.group(1)!r}")
    return errors


def main() -> int:
    errors = validate_repository()
    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
