# Lifecycle and AI Skill evaluation fixtures

`lifecycle-ai-skills.json` includes two draft behavior-oriented cases for each of the 122 newly added Skills: a normal task and an underspecified request. Each includes expected behaviors and failure patterns to avoid.

These fixtures are starting rubrics, not proof that the Skills pass. To evaluate a Skill, run each prompt against the intended model/runtime, score the expected behaviors and prohibited patterns, record the output and rationale, and revise the Skill if it fails. The validator checks coverage and structure only; it does not execute a model or score quality.
