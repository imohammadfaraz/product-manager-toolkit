#!/usr/bin/env python3
"""Validate example-based evaluation fixtures for the newly published Skills."""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "evals" / "lifecycle-ai-skills.json"
SKILLS_DIR = ROOT / "skills"
ERRORS: list[str] = []

def main() -> int:
    try:
        payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read lifecycle Skill fixtures: {exc}")
        return 1
    cases = payload.get("cases")
    if payload.get("schema_version") != "1.0" or not isinstance(cases, list):
        print("ERROR: invalid schema_version or cases list")
        return 1
    seen: set[str] = set()
    by_skill: dict[str, int] = {}
    for i, case in enumerate(cases):
        if not isinstance(case, dict):
            ERRORS.append(f"cases[{i}] must be an object")
            continue
        for field in ("skill", "case_id", "prompt", "expected_behaviors", "must_not"):
            if field not in case:
                ERRORS.append(f"cases[{i}] missing {field}")
        cid = case.get("case_id", "")
        if cid in seen:
            ERRORS.append(f"duplicate case_id: {cid}")
        seen.add(cid)
        skill = case.get("skill", "")
        by_skill[skill] = by_skill.get(skill, 0) + 1
        if not isinstance(case.get("prompt"), str) or not case["prompt"].strip():
            ERRORS.append(f"cases[{i}] prompt must be non-empty")
        for field in ("expected_behaviors", "must_not"):
            v = case.get(field)
            if not isinstance(v, list) or not v or not all(isinstance(x, str) and x.strip() for x in v):
                ERRORS.append(f"cases[{i}] {field} must be a non-empty list of strings")
    skill_ids = {p.parent.name for p in SKILLS_DIR.rglob("SKILL.md")}
    new_ids = set(by_skill)
    for sid in sorted(new_ids):
        if by_skill[sid] < 2:
            ERRORS.append(f"{sid} needs at least 2 cases")
        if not any(p.parent.name == sid for p in SKILLS_DIR.rglob("SKILL.md")):
            ERRORS.append(f"fixture references missing Skill: {sid}")
    if len(new_ids) != 122:
        ERRORS.append(f"expected 122 Skills in this fixture file, found {len(new_ids)}")
    if ERRORS:
        print("Lifecycle Skill fixture validation failed:")
        for e in ERRORS:
            print(f"- {e}")
        return 1
    print(f"Validated {len(cases)} evaluation fixtures across {len(new_ids)} Skills.")
    print("Note: this validates fixture structure only; it does not run or score model responses.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
