# Skill example-based evaluations

`skill-cases.json` contains two behavior-oriented cases for each of the ten editorially reviewed Skills. Each case includes a realistic prompt, expected behaviors, and failure patterns to avoid.

## How to evaluate

1. Run the prompt against the named Skill in the model/runtime where it will be used.
2. Score every `expected_behaviors` item as pass or fail.
3. Mark each `must_not` item as triggered or not triggered.
4. Record the model/runtime, date, reviewer, output, score, and rationale in an evaluation report.
5. Revise the Skill when a failure reveals ambiguous instructions, then rerun the affected cases.

The repository CI validates fixture structure and coverage only. It does not invoke a model or claim that generated answers passed. For dependable release decisions, execute these fixtures against the intended runtime and review outputs with a human rubric.
