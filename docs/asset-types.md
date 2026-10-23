# Asset Types

- **Skill:** focused task capability with instructions and an output contract.
- **Agent:** specialist role or runtime configuration that may use tools or coordinate capabilities.
- **Workflow:** ordered steps, inputs, handoffs, and decisions. Documentation alone does not automate execution.
- **Toolkit:** curated capabilities for a broader job to be done.
- **Command:** named entry point for a compatible runtime.
- **Prompt:** reusable instruction for manual use.
- **Template:** reusable artifact structure.
- **Integration:** platform-specific adapter or tool connection.
- **Evaluation:** test cases, fixtures, expected outputs, and scoring rubrics.

## Definition schemas

JSON Schema Draft 2020-12 contracts are maintained in [schemas/README.md](../schemas/README.md). They cover Skill metadata, full Agent definitions, full Workflow definitions, and Integration definitions. A schema is a validation contract, not proof that the described asset is published, executable, compatible, or secure.
