# Contributing

Thanks for improving Product Manager Toolkit.

## Core principles

- Keep each Skill focused on a distinct user job and output.
- Prefer evidence-backed, decision-useful work over generic frameworks.
- Preserve source references and distinguish facts, interpretations, assumptions, unknowns, conflicts, and proposals.
- Never silently invent product rules, thresholds, policies, defaults, metrics, permissions, or expected behavior.
- Do not claim browsing, execution, testing, validation, or approvals unless they actually happened.
- Keep portable product methods separate from vendor-specific setup in `integrations/`.
- Use synthetic examples and avoid unnecessary sensitive data.
- Check source attribution and licensing before adding third-party material.

## Required Skill metadata

Every `skills/**/SKILL.md` file must start with YAML frontmatter containing:

- `name`: stable kebab-case ID matching the containing directory.
- `display_name`: reader-facing title.
- `description`: concise statement of the job and outcome.
- `category`: matching the top-level category directory.
- `asset_type`: `skill`.
- `version`: semantic version, initially `1.0.0`.
- `status`: `active`, `draft`, or `deprecated`.
- `portability`: `portable` or `migrated-source-preserved`.
- `review_status`: honest state of editorial and portability review.
- `tags`: short list of discoverability terms.
- `source`: required for migrated material.

See [docs/skill-standard.md](docs/skill-standard.md) for the canonical section structure and review rules.

## Required body sections

Portable, toolkit-authored Skills must include Purpose, When to use, Inputs, Process, Expected outputs, Quality checklist, Guardrails, and Definition of done.

Migrated Skills must use the same standardized top-level wrapper sections, retain the source instructions under Detailed operating instructions, preserve source attribution, and remain marked as needing content review until platform-specific wording and conflicting instructions have been assessed.

## Before submitting

1. Run `python scripts/validate_skills.py`.
2. Check for an existing Skill with the same or overlapping job before adding another.
3. Update `catalog/skills.yaml`, the README, and relevant workflows.
4. Add a worked example and evaluation cases for important behavior.
5. Verify internal links, source URLs, and licensing.
6. Describe known limitations and review status honestly.

The validation script checks structure and repository consistency. A passing structural check does not by itself prove a Skill is factually correct, safe, useful, or portable.
