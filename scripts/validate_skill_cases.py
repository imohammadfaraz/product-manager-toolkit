#!/usr/bin/env python3
"""Validate example-based Skill evaluation fixtures without external dependencies."""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "evals" / "skill-cases.json"
REQUIRED_REVIEWED = {
    "metrics-analytics-designer", "ux-reviewer", "problem-definition-expert",
    "ab-testing-expert", "monetization-strategist", "gtm-planner",
    "risk-and-edge-case-analyzer", "prd-generator",
    "competitive-analysis-expert", "product-strategy-builder",
}
errors: list[str] = []

def main() -> int:
    try:
        payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read evaluation fixtures: {exc}")
        return 1
    if payload.get("schema_version") != "1.0":
        errors.append("schema_version must be 1.0")
    cases = payload.get("cases")
    if not isinstance(cases, list):
        errors.append("cases must be a list")
        cases = []
    seen_ids: set[str] = set()
    by_skill: dict[str, int] = {}
    for i, case in enumerate(cases):
        prefix = f"cases[{i}]"
        if not isinstance(case, dict):
            errors.append(f"{prefix} must be an object")
            continue
        for field in ("skill", "case_id", "prompt", "expected_behaviors", "must_not"):
            if field not in case:
                errors.append(f"{prefix} missing {field}")
        cid = case.get("case_id", "")
        if cid in seen_ids:
            errors.append(f"duplicate case_id: {cid}")
        seen_ids.add(cid)
        skill = case.get("skill", "")
        by_skill[skill] = by_skill.get(skill, 0) + 1
        if not isinstance(case.get("prompt"), str) or not case["prompt"].strip():
            errors.append(f"{prefix} prompt must be non-empty text")
        for field in ("expected_behaviors", "must_not"):
            value = case.get(field)
            if not isinstance(value, list) or not value or not all(isinstance(x, str) and x.strip() for x in value):
                errors.append(f"{prefix} {field} must be a non-empty list of non-empty strings")
    for skill in sorted(REQUIRED_REVIEWED):
        if by_skill.get(skill, 0) < 2:
            errors.append(f"{skill} needs at least 2 evaluation cases")
    unexpected = set(by_skill) - REQUIRED_REVIEWED
    if unexpected:
        errors.append("unexpected Skill IDs: " + ", ".join(sorted(unexpected)))
    if errors:
        print("Skill evaluation fixture validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Validated {len(cases)} evaluation cases across {len(by_skill)} reviewed Skills.")
    print("Note: fixture validation does not execute or score model responses.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
