---
name: "Future Workflow System: Architecture & Metadata Notes"
type: "reference-design"
version: "0.1"
purpose: "Record the current assessment of the Meta-Modules architecture, propose future improvements, and explain metadata concepts relevant to Meta-Modules and DVA."
use_when: "Consult when reviewing or evolving the instruction-system architecture, module metadata, discovery behavior, or the relationship between Meta-Modules and DVA."
---

# Future Workflow System: Architecture & Metadata Notes

**Status:** Reference and design direction, not an implementation specification  
**Version:** 0.1  
**Purpose:** Preserve the current assessment of the Meta-Modules instruction system, identify useful future improvements, and explain metadata in a way that can inform both this repository and DVA.

## Executive Summary

The current modular instruction system is a sound starting point. Its current foundation consists of four foundational modules:

- **Intent & Clarity:** understand the user's goal and resolve meaningful ambiguity.
- **Prior-Art-First Collaboration (PAFC):** investigate established solutions before inventing.
- **Discovery & Exploration:** reveal useful possibilities the user may not know to ask about.
- **Capability & Agency:** help users accomplish more through AI while retaining control, finding leverage, and making sustained progress.

The next step is to test the current system against real tasks and improve it based on observed failures. Consider additional foundational modules only when testing or recurring needs demonstrate a genuine gap.

The most promising future improvement is lightweight, consistent metadata for reusable modules. Metadata can help the assistant or a retrieval mechanism identify what a file is for without reading every file in full. However, metadata only works when something actually reads and uses it. Adding YAML to a Markdown file does not, by itself, make ChatGPT or DVA automatically discover or activate that file.

## 1. Current Architecture Assessment

The repository already has several strong choices:

- **A small global foundation:** a few complementary principles guide general collaboration.
- **Separate specialized workflows:** detailed procedures can remain in their own files and only be used when relevant.
- **Repository-first discovery:** the current repository contents are the source of truth, rather than a manually maintained list that can become stale.
- **Progressive disclosure:** discover candidate files first, read the relevant instructions, and load supporting material only when needed.
- **Human-readable and versionable:** Markdown and Git make the system inspectable, editable, and reversible.
- **Proportionate behavior:** the assistant should not turn every task into a ceremony or load every module indiscriminately.

### Current recommendation

Keep the current four-module foundation and the broader modular architecture. Do not build an automated module index, custom retrieval engine, or larger instruction framework until actual use demonstrates that manual discovery is failing often enough to justify the extra complexity.

The architecture is a good starting point, not yet a proven system. Test behavior in real conversations before adding more rules.

## 2. What to Test

Use a small set of recurring test cases to check whether the instructions improve behavior:

| Situation | Desired behavior |
|---|---|
| A proposed build may duplicate an existing tool or standard | Investigate established options before recommending custom work |
| A request has an ambiguity that could change the result | Ask one focused question or state a reasonable assumption |
| The user does not know what tools or methods exist | Surface a small number of relevant, useful possibilities |
| A specialized workflow already exists but the user does not know its name | Discover and apply it when appropriate |
| A simple question needs a simple answer | Answer directly without unnecessary process |
| A creative idea differs from conventional approaches | Explore alternatives without taking over the idea |
| A source, file, or capability cannot be accessed | State the limitation instead of claiming it was checked |
| The assistant is corrected | Adapt without defending the earlier interpretation |

Judge the results, not whether the assistant mentions the modules. The goal is better assistance, not visible compliance theater.

Record repeated failures and identify whether each one calls for:
1. Clarifying an existing principle.
2. Improving a specialized workflow.
3. Improving metadata or discovery.
4. Adding a genuinely new module.
5. No permanent change because the issue was one-off.

## 3. Metadata: The Core Idea

**Metadata is structured information about an item, rather than the main content of that item.**

For an instruction file, the content is the full guidance. Its metadata might say:

- What the module is called.
- What it does.
- When it is relevant.
- What kind of item it is.
- Which other modules it depends on, if any.

Example:

```yaml
---
name: intent-and-clarity
type: foundational
purpose: Understand the user's goal and resolve meaningful ambiguity.
use_when: A request has competing interpretations or important missing information.
---
```

The Markdown body below the metadata contains the detailed instructions.

This is called **YAML front matter** when the metadata appears at the top of a Markdown file between `---` delimiters. YAML is just a human-readable data format. The delimiters and field names are conventions; a program or workflow must parse and interpret them for them to have machine behavior.

Metadata is not magic. It becomes useful when a system uses it to make a decision.

## 4. How Metadata Helps Discover Modules

A module-discovery system can work in stages:

1. **Discover the available files.** Obtain the current file listing from the repository or workspace.
2. **Read lightweight metadata.** Learn each candidate's name, purpose, type, and likely trigger conditions.
3. **Select likely candidates.** Compare the current task with each module's purpose and use cases.
4. **Read the full instructions.** Load the body of only the selected module or modules.
5. **Follow relevant references.** Load additional reference material only if the selected workflow needs it.
6. **Apply and verify.** Follow the instructions, then be honest about what was actually accessed or done.

This is an example of **progressive disclosure**: reveal enough information to choose the next layer, rather than loading everything at once.

Official examples of this approach exist in agent-skill systems:
- OpenAI, *Build skills*: https://learn.chatgpt.com/docs/build-skills
- OpenAI API, *Skills*: https://developers.openai.com/api/docs/guides/tools-skills
- Anthropic, *Agent Skills overview*: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Open Agent Skills specification: https://agentskills.io/specification

These systems use metadata such as a skill's name and description to help identify when its full instructions should be loaded. Their exact runtime behavior depends on the host application.

### Important distinction for this repository

The current Meta-Modules README tells the assistant to inspect the repository and read relevant files. That is a **discovery policy**, not a guaranteed automatic metadata loader.

If a ChatGPT conversation only receives the README pointer, metadata in other files does not magically appear in the model's context. The assistant or a tool must retrieve the files, inspect their metadata, and decide what to read. If the repository cannot be accessed, the intended discovery process cannot be fully executed.

Metadata can make discovery more efficient and precise, but it cannot replace repository access or a mechanism that reads it.

### Recommended type vocabulary

The `type` field should describe an item's role in the instruction system, not merely its subject. Use the following small, controlled vocabulary:

| Type | Definition | Typical use |
|---|---|---|
| `foundational` | Broad collaboration principles that apply across many tasks. | General guidance used throughout collaboration. |
| `specialized` | A focused method or capability for a particular kind of interaction or problem. It can be adaptive rather than a fixed sequence of stages. | A technique selected when its particular approach is useful. |
| `specialized-workflow` | A repeatable, procedural approach with stages or steps for carrying a task through. | A task-specific process that guides execution and verification. |
| `reference-design` | Explanatory or proposal-oriented material about architecture, concepts, or potential future designs. It is not automatically an instruction to execute. | Consultation when reviewing or evolving a system. |

The key distinction between `specialized` and `specialized-workflow` is **method versus process**. A specialized method guides *how to approach* a kind of problem and may adapt fluidly to the conversation. A specialized workflow describes *how to carry* a kind of task through a repeatable sequence. Guided Inquiry is a method; Development State Machine and External Sharing Cleanup are workflows.

Use these values consistently across files. Define a new type only when an item's role cannot be represented accurately by the existing vocabulary, and update both this document and the README before using it. If classification is uncertain, inspect the file's purpose and body; do not infer its type from its filename alone.

Types guide discovery and interpretation. They do not automatically load, activate, or execute a file.

## 5. A Practical Metadata Schema for Instruction Files

Do not introduce every possible field at once. Start with a small set that answers the most important discovery questions.

| Field | Purpose | Recommendation |
|---|---|---|
| `name` | Stable, human-readable identifier | Use a clear name; keep it distinct from the filename if needed |
| `type` | Distinguishes a foundational principle, task workflow, project context, or reference | Useful because not every file is an instruction module |
| `purpose` | Summarizes what the item helps accomplish | Required for discoverability |
| `use_when` | Explains situations where the item is relevant | High value for selecting modules |
| `version` | Identifies a revision of the module's own content | Optional if Git history already meets the need |
| `related` | Points to complementary material | Add only when it improves navigation |
| `depends_on` | Identifies required prerequisite instructions | Use sparingly; avoid creating a complicated dependency graph |

For an initial experiment, `name`, `type`, `purpose`, and `use_when` are likely enough. You can later decide whether metadata belongs in YAML front matter, a separate manifest, or a DVA-like structured data layer.

### What makes good discovery metadata?

A useful description should explain both **what the item does** and **when to use it**. A vague description such as "helps with projects" gives little basis for selection. A stronger description identifies the task, the benefit, and the circumstances that should trigger consideration.

Keep descriptions concise and discriminative. If several modules all claim to help with everything, metadata will not help choose among them.

Metadata should describe the module's role, not duplicate its entire body.

## 6. How This Relates to DVA

DVA has a related but broader problem. It is not only about finding instruction files. It is about letting people capture content naturally, attach meaning and relationships without disrupting writing, and later navigate or reorganize that material.

The key principle is:

**Syntax is an input shortcut, not the data model.**

A user may type a marker, press a shortcut, select text, or use a context action. Those interactions can create or modify structured metadata behind the scenes. The chosen syntax should not have to become the permanent representation of the information.

For example, the user writes:

```text
Alex discovered the station's hidden control system.
```

The underlying workspace could store the prose as content, and separately store structured information such as:

```json
{
  "content": "Alex discovered the station's hidden control system.",
  "tags": ["station", "discovery"],
  "relationships": [
    {
      "type": "discovered",
      "target": "hidden-control-system"
    }
  ]
}
```

This is illustrative, not a prescribed DVA schema. Real relationships would benefit from stable IDs and validation rather than relying only on display names.

The user should not have to manually write that JSON. It represents the structured information created by the interface or an input shortcut.

### Distinguish content, metadata, and relationships

- **Content:** the prose, notes, or other material the user is creating.
- **Metadata:** properties describing an item, such as its type, status, author, date, tags, or version.
- **Relationships:** explicit links between items, including a relationship type when the distinction matters.
- **Presentation:** how the same underlying information is displayed, filtered, arranged, or visualized.
- **Input syntax:** a shortcut for creating or editing content, metadata, or relationships.

Tags answer roughly **"What is this about or what kind of thing is it?"** Relationships answer **"How is this connected to that other thing?"** A graph, list, panel, or mind-palace view can present the same underlying data in different ways without owning a separate copy of the meaning.

### Why this matters

If visible markers are the only place meaning exists, changing syntax, themes, or views can become difficult. If meaning is represented as structured data, the interface can offer different ways to create, inspect, search, and edit it.

For DVA, inline marks can remain useful as a fast input method, while the application translates those marks into structured state. Mark definitions and their appearance can be global settings, while themes may have global, workspace, or pane scope. The presentation should not determine the identity of the underlying data.

Similarly, a saved state or snapshot can have its own metadata, such as a name, tags, or flags, without changing the snapshot's content. Metadata about a version should describe that version, not silently alter it.

## 7. Similarity Between DVA and Meta-Modules, and Where They Differ

Both systems need to separate **what an item is** from **how a person or system discovers and interacts with it**.

| Concern | Meta-Modules | DVA |
|---|---|---|
| Main item | Instruction, workflow, context, or reference file | Note, panel, file, snapshot, or other workspace object |
| Metadata helps answer | What is this module for, and when might it apply? | What is this item, what properties does it have, and how can it be found or organized? |
| Selection mechanism | Assistant or retrieval tool chooses relevant files | User actions, queries, filters, workspace logic, or AI may locate relevant objects |
| Full content | Instructions and supporting documentation | User-authored prose or other content |
| Relationships | References and dependencies between modules | Typed connections between workspace objects |
| Primary concern | Choosing relevant guidance without loading everything | Capturing and navigating information without forcing a rigid workflow |

The shared lesson is not that DVA should use YAML front matter everywhere. It is that both systems benefit from separating structured meaning from the content and interface used to create or display it.

A Markdown file's metadata is one useful representation. It is not the only possible representation, and it should not be confused with the underlying concept of metadata itself.

## 8. Recommended Next Steps

### For Meta-Modules

1. Continue using the current four foundational modules.
2. Test them against real tasks and note recurring failures.
3. Add concise metadata to modules when module selection becomes difficult.
4. Start with `name`, `type`, `purpose`, and `use_when`; avoid an elaborate schema at first.
5. Keep specialized methods and specialized workflows distinct in metadata, while selecting either only when relevant. Their instruction files must be present and inspected before applying their specific guidance. Weather Pattern, Guided Inquiry, and Refinement are specialized methods; Development State Machine and External Sharing Cleanup are specialized workflows.
6. Consider automated discovery only when manual repository inspection is demonstrably insufficient.

### For DVA

1. Define the core object types and what each represents.
2. Decide which information belongs to content, metadata, relationships, or presentation.
3. Let users create structured meaning through convenient interactions without requiring them to learn the underlying data format.
4. Give objects stable identities where relationships must survive renaming or rearrangement.
5. Keep search and navigation able to use content, tags, relationships, versions, and references as appropriate.
6. Treat visible marks as an interface convention that can be changed, not as the only source of truth.
7. Prototype the simplest data model that supports the desired interactions before building a broad metadata framework.

These are design directions, not a demand to implement every item immediately.

## 9. Final Recommendation

Keep the current instruction architecture and learn from its use. Metadata is a promising next improvement, but it should solve a demonstrated discovery problem rather than become a goal in itself.

For both systems, keep this distinction clear:

- **The data model** defines what information exists and how it relates.
- **Metadata** describes and classifies items.
- **The interface or syntax** lets people create and change that information.
- **The discovery mechanism** decides what to show or load for a particular task.

Those layers can cooperate without being the same thing. Keeping them separate allows the system to evolve without forcing users to adopt a new writing style, reorganize everything, or understand every implementation detail.

---

*This document records design guidance and a proposed direction. It does not change the existing module format, introduce a mandatory metadata schema, or prescribe a final DVA data model.*
