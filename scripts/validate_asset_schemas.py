#!/usr/bin/env python3
"""Validate JSON Schema definitions and their canonical example fixtures."""
from __future__ import annotations
import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError:
    print("ERROR: jsonschema is required. Install it with: python -m pip install jsonschema")
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"
FIXTURES = {
    "skill.schema.json": ["examples/skill-metadata.example.json"],
    "agent.schema.json": ["examples/agent.example.json"],
    "workflow.schema.json": ["examples/workflow.example.json"],
    "integration.schema.json": ["examples/integration.example.json"],
}
ERRORS: list[str] = []

def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        ERRORS.append(f"{path.relative_to(ROOT)}: cannot read valid JSON: {exc}")
        return None

def main() -> int:
    for schema_name, fixture_paths in FIXTURES.items():
        schema_path = SCHEMA_DIR / schema_name
        schema = load_json(schema_path)
        if schema is None:
            continue
        try:
            Draft202012Validator.check_schema(schema)
        except Exception as exc:
            ERRORS.append(f"{schema_path.relative_to(ROOT)}: invalid JSON Schema: {exc}")
            continue
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        for fixture_name in fixture_paths:
            fixture_path = SCHEMA_DIR / fixture_name
            instance = load_json(fixture_path)
            if instance is None:
                continue
            issues = sorted(validator.iter_errors(instance), key=lambda error: list(map(str, error.absolute_path)))
            for issue in issues:
                location = ".".join(str(part) for part in issue.absolute_path) or "$"
                ERRORS.append(f"{fixture_path.relative_to(ROOT)}:{location}: {issue.message}")
            if not issues:
                print(f"PASS {fixture_path.relative_to(ROOT)} against {schema_name}")
    # Validate every published specialist-agent definition, not only the canonical fixture.
    agent_schema = load_json(SCHEMA_DIR / "agent.schema.json")
    agents_dir = ROOT / "agents"
    agent_files = sorted(agents_dir.glob("*/agent.json")) if agents_dir.exists() else []
    if agent_schema is not None:
        agent_validator = Draft202012Validator(agent_schema, format_checker=FormatChecker())
        for agent_path in agent_files:
            instance = load_json(agent_path)
            if instance is None:
                continue
            issues = sorted(agent_validator.iter_errors(instance), key=lambda error: list(map(str, error.absolute_path)))
            for issue in issues:
                location = ".".join(str(part) for part in issue.absolute_path) or "$"
                ERRORS.append(f"{agent_path.relative_to(ROOT)}:{location}: {issue.message}")
            if not issues:
                print(f"PASS {agent_path.relative_to(ROOT)} against agent.schema.json")
    # Validate every integration definition in the registry tree.
    integration_schema = load_json(SCHEMA_DIR / "integration.schema.json")
    integrations_dir = ROOT / "integrations"
    integration_files = sorted(integrations_dir.glob("**/integration.json")) if integrations_dir.exists() else []
    if integration_schema is not None:
        integration_validator = Draft202012Validator(integration_schema, format_checker=FormatChecker())
        for integration_path in integration_files:
            instance = load_json(integration_path)
            if instance is None:
                continue
            issues = sorted(integration_validator.iter_errors(instance), key=lambda error: list(map(str, error.absolute_path)))
            for issue in issues:
                location = ".".join(str(part) for part in issue.absolute_path) or "$"
                ERRORS.append(f"{integration_path.relative_to(ROOT)}:{location}: {issue.message}")
            if not issues:
                print(f"PASS {integration_path.relative_to(ROOT)} against integration.schema.json")
    if ERRORS:
        print("\nAsset schema validation failed:")
        for error in ERRORS:
            print(f"- {error}")
        return 1
    print(f"Validated {len(FIXTURES)} schemas, {sum(map(len, FIXTURES.values()))} example fixtures, and {len(agent_files)} agent definitions, and {len(integration_files)} integration definitions.")
    print("Structural validation is not runtime compatibility or security certification.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
