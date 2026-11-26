---
name: Demonstration-Based Procedural Memory
type: reference-design
version: "0.1.0"
status: exploratory
purpose: Retain demonstrated and corrected techniques as transferable, inspectable capabilities.
use_when: Designing AI-assisted creative workflows, skill libraries or persistent procedural memory.
---

# Demonstration-Based Procedural Memory (DPM)

An exploratory design, curated with AI. Companion to the [Creative Collaboration Kit](creative-collaboration-kit.md). The objective is accumulated capability independent of any particular model, initially explored in Blender and Godot but applicable to other software.

## 1. Retention model

Preserve original demonstrations separately from interpretations. Capture actions, relevant initial and final state, intermediate observations, application versions and human explanations. Prefer semantic editor operations and state differences over raw mouse coordinates. Capture only explicitly selected sessions; allow inspection, redaction and deletion.

- Episodic: what happened in a particular session.
- Semantic: intended result, preferences and inferred principles.
- Procedural: how to perform a technique.
- Corrective: mistakes, corrections and counterexamples.
- Contextual: prerequisites, scope and exceptions.
- Evaluative: test results, human judgments and reliability.

Inferences are hypotheses until confirmed. An accidental action or a single correction is not automatically a general preference. Preserve provenance so future models can reinterpret evidence without replacing it.

## 2. Capture and storage

A demonstration record should include a stable identifier, timestamps, application and adapter versions, initial state reference, ordered operations, final state reference, relevant before/after images, user annotations and provenance. Store large assets separately with content references. Use project-local storage initially, with explicit promotion to a reusable cross-project library.

Example layout:

```text
creative-memory/
  demonstrations/
    stylized-tree/
      operations.json
      before.png
      after.png
      intent.md
  skills/
    stylized-tree-shaping/
      manifest.yaml
      procedure.py
      tests/
  index.json
```

Keep source evidence distinct from generated code. Blender operators, Python scripting and undo history are potential capture foundations, but complete capture requires instrumentation and validation. Godot editor plugins are another candidate.

## 3. Executable skill representation

```yaml
skill: stylized-tree-shaping
version: 0.1.0
status: candidate
scope: Blender
source: human-demonstration
inputs:
  - tree_mesh
  - curvature
  - asymmetry
constraints:
  - preserve_root_position
  - preserve_materials
validation:
  - valid_geometry
  - human_approval
```

A skill may reference a script, native procedural graph, recorded command sequence or contextual guidance. Not every demonstration should become code. Parameterize only dimensions supported by evidence; distinguish fixed constraints from adjustable preferences. Record dependencies, compatible versions, expected effects, preconditions and rollback strategy.

## 4. Lifecycle

Observed → interpreted → candidate → validated → established → revised or retired.

Retain raw evidence; propose a technique; review inferred intent; test against different inputs and counterexamples; promote only after appropriate validation. Revised skills retain provenance and independent semantic versions. Retired skills are excluded from automatic execution. Deletion must also remove or invalidate derived indexes and artifacts where requested.

## 5. Retrieval and execution

Index skills by task, semantic intent, application, object type, prerequisites, constraints and demonstrated outcomes. Use metadata filters plus semantic retrieval where useful. Retrieve only relevant evidence and procedures. Check compatibility and scope before proposing execution; abstain when no reliable match exists.

Treat generated procedures as untrusted until reviewed and tested. Use least-privilege adapters, explicit authorization for consequential operations, previews, state revision checks and recoverable checkpoints. Never automatically execute arbitrary code merely because it was retrieved. Verify actual results and preserve unrelated state. Record corrections as new evidence rather than silently rewriting established skills.

## 6. Transfer between applications

Separate application-independent intent from application-specific implementation. For example, softer movement may imply gradual acceleration and transitions; Blender may implement this with animation curves, Godot with movement easing, and video editors with keyframe easing. Transfer is a candidate adaptation, not a guarantee of equivalence. Validate against each target environment.

## 7. Prior art to investigate

- Programming by demonstration and learning from demonstration.
- Case-based reasoning and retrieval-augmented generation.
- [Voyager](https://github.com/MineDojo/Voyager): external executable skill library.
- [OpenUSD](https://openusd.org/): composable scene state and variants.
- Event sourcing: reconstructing state from recorded events.
- [OpenTelemetry](https://opentelemetry.io/): structured operation traces.
- Continual learning: longer-term model adaptation.

These are research leads, not verified implementation choices. External procedural memory is the initial recommendation over fine-tuning because it is inspectable, revisable and portable.

## 8. Prototype and evaluation

Manually record a small Blender demonstration (e.g., shaping a stylized tree). Preserve before/after state and actions, extract a candidate parameterized procedure, validate it on another object, then retrieve it in a fresh model session. Compare against an equivalent task without retained memory.

Measure task success, preservation of unrelated state, correction count, retrieval relevance, transfer success and time/compute cost. Include incompatible inputs and failed demonstrations. Acceptance requires successful retrieval in a fresh session, a verified scoped edit and recoverability. Start with manual capture before investing in automatic instrumentation.

## 9. Relationship to existing projects

The Creative Collaboration Kit provides the initial domain and experiment. SMH Tree could orchestrate retrieval, context and model switching. The reusable inspector could expose skill parameters and constraints. Meta-Modules provides collaboration principles without being a runtime dependency. A future independent SDK or service may be justified by evidence from prototypes.

## 10. Open decisions

Capture granularity, storage format, retrieval strategy, skill validation authority, cross-project promotion, adapter design and eventual packaging remain open. No implementation or integration has been tested. Use a lightweight development workflow and observable acceptance criteria when implementation begins.
