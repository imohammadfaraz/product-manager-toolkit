#!/usr/bin/env python3
"""Validate Product Manager Toolkit Skill structure and repository references.

Uses only the Python standard library. Structural validation is not a substitute
for editorial review or Skill evaluation.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
REQUIRED_META = {
    "name", "display_name", "description", "category", "asset_type",
    "version", "status", "portability", "review_status", "tags",
}
PORTABLE_SECTIONS = [
    "Purpose", "When to use", "Inputs", "Process", "Expected outputs",
    "Quality checklist", "Guardrails", "Definition of done",
]
MIGRATED_SECTIONS = [
    "Purpose", "When to use", "Inputs", "Expected outputs",
    "Quality and safety contract", "Detailed operating instructions",
]
ERRORS: list[str] = []
WARNINGS: list[str] = []

def fail(message: str) -> None:
    ERRORS.append(message)

def parse_frontmatter(path: Path, content: str) -> tuple[dict[str, str], str]:
    if not content.startswith("---\n"):
        fail(f"{path.relative_to(ROOT)}: frontmatter must start at line 1")
        return {}, content
    end = content.find("\n---\n", 4)
    if end < 0:
        fail(f"{path.relative_to(ROOT)}: frontmatter closing delimiter is missing")
        return {}, content
    raw = content[4:end]
    data: dict[str, str] = {}
    for line_no, line in enumerate(raw.splitlines(), 2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith(" ") or ":" not in line:
            fail(f"{path.relative_to(ROOT)}:{line_no}: unsupported frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if key in data:
            fail(f"{path.relative_to(ROOT)}:{line_no}: duplicate metadata key '{key}'")
        data[key] = value
    return data, content[end + 5:]

def headings(body: str) -> set[str]:
    return {m.group(1).strip() for m in re.finditer(r"^##\s+(.+?)\s*$", body, re.M)}

def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] == '"':
        return value[1:-1].replace('\\\\', '\\').replace('\\"', '"')
    return value

def check_local_links(path: Path, content: str) -> None:
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
        target = target.strip().split("#", 1)[0]
        if not target or target.startswith(("https://", "http://", "mailto:", "tel:")):
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            fail(f"{path.relative_to(ROOT)}: broken local link: {target}")

def main() -> int:
    skill_files = sorted(SKILLS_DIR.rglob("SKILL.md"))
    if not skill_files:
        fail("No skills/**/SKILL.md files found")
    seen_names: dict[str, Path] = {}
    seen_descriptions: dict[str, Path] = {}
    paths: set[str] = set()

    for path in skill_files:
        relative = path.relative_to(ROOT).as_posix()
        content = path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(path, content)
        missing = REQUIRED_META - set(meta)
        if missing:
            fail(f"{relative}: missing metadata: {', '.join(sorted(missing))}")
        name = unquote(meta.get("name", ""))
        category = unquote(meta.get("category", ""))
        description = unquote(meta.get("description", ""))
        portability = unquote(meta.get("portability", ""))
        review_status = unquote(meta.get("review_status", ""))
        if name:
            if name in seen_names:
                fail(f"{relative}: duplicate Skill ID '{name}' also used by {seen_names[name].relative_to(ROOT)}")
            seen_names[name] = path
            if path.parent.name != name:
                fail(f"{relative}: directory name must match metadata name '{name}'")
        if category and path.parent.parent.name != category:
            fail(f"{relative}: category '{category}' does not match directory '{path.parent.parent.name}'")
        if unquote(meta.get("asset_type", "")) != "skill":
            fail(f"{relative}: asset_type must be 'skill'")
        if unquote(meta.get("status", "")) not in {"active", "draft", "deprecated"}:
            fail(f"{relative}: invalid status")
        if not re.fullmatch(r"\d+\.\d+\.\d+", unquote(meta.get("version", ""))):
            fail(f"{relative}: version must use semantic version format, e.g. 1.0.0")
        if portability not in {"portable", "migrated-source-preserved"}:
            fail(f"{relative}: invalid portability value '{portability}'")
        if review_status not in {"standardized", "standardized-wrapper-content-review-needed", "content-reviewed", "deprecated"}:
            fail(f"{relative}: invalid review_status '{review_status}'")
        if portability == "migrated-source-preserved" and "source:" not in content.split("\n---\n", 1)[0]:
            fail(f"{relative}: migrated Skill requires a source URL")
        if portability == "migrated-source-preserved" and review_status != "standardized-wrapper-content-review-needed":
            WARNINGS.append(f"{relative}: migrated content should remain flagged until portability review is complete")
        if description:
            normalized = re.sub(r"[^a-z0-9]+", " ", description.lower()).strip()
            if normalized in seen_descriptions:
                WARNINGS.append(f"{relative}: description duplicates {seen_descriptions[normalized].relative_to(ROOT)}")
            else:
                seen_descriptions[normalized] = path
        required_sections = MIGRATED_SECTIONS if portability == "migrated-source-preserved" else PORTABLE_SECTIONS
        present = headings(body)
        missing_sections = [section for section in required_sections if section not in present]
        if missing_sections:
            fail(f"{relative}: missing required sections: {', '.join(missing_sections)}")
        if "---\nname:" in body:
            fail(f"{relative}: nested frontmatter found in body")
        paths.add(relative)
        check_local_links(path, content)

    catalog = ROOT / "catalog" / "skills.yaml"
    if not catalog.exists():
        fail("catalog/skills.yaml is missing")
    else:
        catalog_content = catalog.read_text(encoding="utf-8")
        catalog_paths = re.findall(r"^\s+path:\s*(skills/[^\s]+/SKILL\.md)\s*$", catalog_content, re.M)
        if len(catalog_paths) != len(set(catalog_paths)):
            fail("catalog/skills.yaml contains duplicate paths")
        for p in sorted(paths - set(catalog_paths)):
            fail(f"Skill missing from catalog: {p}")
        for p in sorted(set(catalog_paths) - paths):
            fail(f"Catalog points to missing Skill: {p}")
        for p in catalog_paths:
            if not (ROOT / p).exists():
                fail(f"Catalog points to missing file: {p}")

    for markdown in [ROOT / "README.md", ROOT / "CONTRIBUTING.md"]:
        if markdown.exists():
            check_local_links(markdown, markdown.read_text(encoding="utf-8"))

    print(f"Checked {len(skill_files)} Skills.")
    for warning in WARNINGS:
        print(f"WARNING: {warning}")
    if ERRORS:
        for error in ERRORS:
            print(f"ERROR: {error}")
        print(f"Validation failed with {len(ERRORS)} error(s) and {len(WARNINGS)} warning(s).")
        return 1
    print(f"Validation passed with {len(WARNINGS)} warning(s).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
