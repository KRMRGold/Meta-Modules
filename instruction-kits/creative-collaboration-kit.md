---
name: Creative Collaboration Kit
type: reference-design
version: "0.1.0"
purpose: Model-agnostic creative collaboration in Blender and Godot.
use_when: Exploring AI-assisted games, 3D projects, visual guidance or reusable creative tooling.
status: exploratory
---

# Creative Collaboration Kit

Concept proposal • 25 November 2026 • Exploratory / not implemented

A model-agnostic environment for making games and 3D projects with Blender, Godot and AI, while preserving human creative direction. Curated with AI as a living reference for future experimentation.

## 1. From instructions to capabilities

Instruction modules are useful for communicating principles, but their application depends on a model discovering and following them. A creative kit should instead make the relevant context, tools and constraints available at the point of action. It should work even without a model remembering to load Meta-Modules.

The proposed kit begins as a reusable project template and tool configuration, not a new standalone application. Over time, demonstrated gaps may justify native editor extensions, a shared context service or integration into SMH Tree. Documentation remains useful, but is not the enforcement mechanism.

## 2. The creative feedback loop

Express intent → inspect current state → propose a targeted change → preview or execute → inspect results → accept, undo or refine.

- Spatial guidance: rough geometry, blockouts, object placement and camera framing.
- Visual guidance: select an object, annotate a viewport, sketch a silhouette or provide a reference.
- Numerical guidance: editable properties, sliders and procedural controls.
- Behavioral guidance: playtest a mechanic and identify what feels wrong.
- Preservation: explicitly identify what must not change, including unrelated assets and approved design decisions.

## 3. Architecture and authority

The human directs the project. A model interprets intent and proposes operations. Tool adapters expose scene data and controlled editing through Blender and Godot. A shared context layer records decisions, references and accepted state. The editor remains authoritative for live scene state; the project files remain authoritative for saved state.

Use stable object identifiers, scoped edits, state revisions, previews and recoverable checkpoints. Reject stale or out-of-scope operations where feasible. Do not rely on a prompt alone to protect locked elements. Start with local, least-privilege access and explicit approval for destructive operations.

## 4. Existing tools to investigate

- [Blender MCP](https://github.com/ahujasid/blender-mcp)
- [Godot MCP](https://github.com/Coding-Solo/godot-mcp)
- [Blender Python API](https://docs.blender.org/api/current/)
- [Godot EditorPlugin](https://docs.godotengine.org/en/stable/classes/class_editorplugin.html)
- [glTF asset interchange](https://www.khronos.org/gltf/)
- [Ollama local model runtime](https://ollama.com/)
- [PureRef visual reference organization](https://www.pureref.com/)

These are starting points, not a tested compatibility matrix. Investigate current maintenance, licensing, viewport access, selection grounding, tool permissions and local model support before adoption. Geometry Nodes and Godot exported properties offer native parameter editing.

## 5. Persistent project context

Suggested template: AGENTS.md as a short discovery entry point; design/ for creative direction, constraints and decisions; references/ for visual assets; blender/ and godot/ for native projects; evaluation/ for repeatable tasks and results. Keep one canonical record per concern and use Git history rather than version-suffixed copies.

A future context service could expose the active selection, relevant constraints, asset metadata and recent decisions through MCP resources or tools. Automatic context retrieval should be scoped to the task rather than injecting every document into every prompt. Model-specific adapters should remain replaceable.

## 6. Initial experiment

Make a small playable 3D environment with a character, lighting, animation, interactable objects and one mechanic. Choose a local MCP-capable client and verify read-only inspection first. Then test one reversible Blender edit, export an asset to Godot, and test one targeted scene or gameplay change. Record failures before building custom infrastructure.

Acceptance: a model can identify the selected object, make a requested change, preserve unrelated state, show the result and allow recovery. A human should be able to continue editing normally in either editor.

## 7. Evaluation and development path

- Instruction accuracy: requested changes actually occur.
- Preservation: unrelated elements and locked properties remain unchanged.
- Visual fidelity: human review against references and stated constraints.
- Technical validity: assets import, scenes load and mechanics function.
- Correction efficiency: interventions, time and failed attempts per task.
- Resource efficiency: latency, token usage and compute requirements.

Use fixed starting scenes and repeatable tasks to compare models and tool configurations. Record model versions, tool versions, inputs and outcomes. Keep subjective aesthetic judgments separate from deterministic checks. Local evaluation comes first; Google Cloud / Vertex AI evaluation is an optional later portfolio direction, subject to cost and approval.

## 8. Relationship to existing projects

SMH Tree could eventually manage branching creative exploration, project context, tool routing and model switching. The reusable inspector concept could expose editable properties and constraints across applications. Meta-Modules remains a source of collaboration principles, not a required runtime dependency. Keep the kit independently useful before deciding whether to merge it into another project.

## 9. Roadmap

1. Establish the project template and test existing MCP integrations.
2. Build the small game and collect real collaboration friction.
3. Add the smallest missing capability: selection grounding, annotation, property editing or context retrieval.
4. Benchmark the improvement against the original workflow.
5. Package proven components as reusable adapters or editor plugins.
6. Consider specialized models or training only when measured failures justify it.

## 10. Open decisions and limitations

The kit name, packaging, client, game concept and eventual SMH Tree integration are provisional. No tools have been installed or tested for this proposal. Adopt a lightweight development workflow, semantic versioning and verification criteria when implementation begins.

**Core principle:** make the game first; let the collaboration infrastructure emerge from the problems encountered while making it.
