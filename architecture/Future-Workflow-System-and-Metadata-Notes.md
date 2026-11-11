


---
name: "Future Workflow System: Architecture & Metadata Notes"
type: "reference-design"
version: "0.2.0"
purpose: "Document the Meta-Modules architecture, the accepted design for linked guidance distribution and assisted migration, and metadata concepts relevant to Meta-Modules and DVA."
use_when: "Consult when reviewing or evolving the instruction-system architecture, guidance adoption and migration, module metadata, discovery behavior, or the relationship between Meta-Modules and DVA."
---

# Future Workflow System: Architecture & Metadata

**Status:** Architecture reference; the Workflow Distribution & Migration design in Section 6 is accepted, while implementation details remain proposals until separately authorized.  
**Version:** 0.2.0  
**Purpose:** Preserve the current assessment of the Meta-Modules instruction system, identify useful future improvements, and explain metadata in a way that can inform both this repository and DVA.

## Executive Summary

The current modular instruction system is a sound starting point. Its current foundation consists of four foundational modules:

- **Intent & Clarity:** understand the user's goal and resolve meaningful ambiguity.
- **Prior-Art-First Collaboration (PAFC):** investigate established solutions before inventing.
- **Discovery & Exploration:** reveal useful possibilities the user may not know to ask about.
- **Capability & Agency:** help users accomplish more through AI while retaining control, finding leverage, and making sustained progress.

The current modular instruction system remains the canonical source for reusable guidance. Its next architectural step is a linked adoption model for projects, covering both workflows and reusable modules. Meta-Modules owns canonical guidance; projects record which revisions they have adopted and retain control over when updates become effective.

The accepted direction is linked references with assisted updates, not copied workflow distributions or automatic migration. A project can inspect the current canonical source while continuing to use its last reviewed revision until it accepts an update. Metadata supports discovery and impact analysis, but it does not load files, activate instructions, or make changes by itself.

## 1. Current Architecture Assessment

The repository already has several strong choices:

- **A small global foundation:** a few complementary principles guide general collaboration.
- **Separate specialized methods and workflows:** focused techniques and detailed procedures can remain in their own files and be used only when relevant.
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

These systems use metadata such as a skill's name and description to help identify when its full instructions should be loaded. Their exact runtime behavior depends on the host application. The links above are illustrative references captured for this design discussion, not permanent dependencies or a guarantee that the linked documentation remains current; verify current documentation before relying on product-specific details.

### Important distinction for this repository

The current Meta-Modules README tells the assistant to inspect the repository and read relevant files. That is a **discovery policy**, not a guaranteed automatic metadata loader.

If a ChatGPT conversation only receives the README pointer, metadata in other files does not magically appear in the model's context. The assistant or a tool must retrieve the files, inspect their metadata, and decide what to read. If the repository cannot be accessed, the intended discovery process cannot be fully executed.

Metadata can make discovery more efficient and precise, but it cannot replace repository access or a mechanism that reads it.

### Type vocabulary authority

The canonical `type` vocabulary and its definitions live in the [Meta-Modules README, Section 3](../README.md#3-metadata-first-module-discovery). Keep the table in one place to prevent competing definitions. This reference document uses that vocabulary but does not independently redefine it.

The distinction is **method versus process**: a specialized method guides how to approach a kind of problem and may adapt fluidly; a specialized workflow describes how to carry a task through a repeatable sequence. Guided Inquiry is a method; Development State Machine and External Sharing Cleanup are workflows.

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
| `related` | Points to complementary material | Add only when it improves navigation; it is a non-binding discovery hint, not a dependency or activation graph |
| `depends_on` | Identifies required prerequisite instructions | Use sparingly; avoid creating a complicated dependency graph |

For an initial experiment, `name`, `type`, `purpose`, and `use_when` are likely enough. Add `related` when it materially improves navigation. Reserve `depends_on` for genuine prerequisites, not merely modules that can be combined. A `related` link does not require automatic or transitive loading; inspect and select each candidate based on the current task. Treat `related` as an optional, curated subset of the relationships explained in the module's prose. The prose is authoritative; `related` exists only to improve discovery and must not introduce a dependency, requirement, or relationship that the prose does not establish. You can later decide whether metadata belongs in YAML front matter, a separate manifest, or a DVA-like structured data layer.

### What makes good discovery metadata?

A useful description should explain both **what the item does** and **when to use it**. A vague description such as "helps with projects" gives little basis for selection. A stronger description identifies the task, the benefit, and the circumstances that should trigger consideration.

Keep descriptions concise and discriminative. If several modules all claim to help with everything, metadata will not help choose among them.

Metadata should describe the module's role, not duplicate its entire body.

## 6. Workflow Distribution & Migration System

### 6.1 Accepted architectural decisions

The following design decisions have been accepted:

- **Distribution:** linked references. Meta-Modules remains the single canonical source; adopting projects do not maintain routine copies of reusable guidance.
- **Updates:** assisted. The system detects and explains changes and prepares project-specific recommendations. It does not silently modify project records or project behavior.
- **Scope:** both workflows and reusable modules. They share one adoption and update model while retaining their existing metadata types and distinct purposes.

The governing principle is:

**Meta-Modules owns the guidance. Projects own their adoption decisions and implementation context.**

This separates three concerns:

1. **Canonical guidance:** the authoritative instructions and their history in Meta-Modules.
2. **Adoption:** which guidance source and revision a project has accepted, and how it handles future changes.
3. **Project application:** how the guidance is interpreted in the context of that project's goals, constraints, and existing decisions.

A project may discover and use a module for an individual task without formally adopting it. Adoption records are for guidance that is part of the project's ongoing working conventions, not a mandatory inventory of every module ever consulted.

### 6.2 Linked references and revision identity

An adoption identifies a guidance source using, at minimum:

- canonical repository;
- repository-relative file path;
- guidance type;
- human-readable version from the source metadata, when present;
- exact Git commit SHA identifying the revision reviewed or adopted.

The repository path and exact commit together identify the actual content. A version string is useful for humans but is not a substitute for a commit SHA. File paths are case-sensitive.

Projects should link to canonical files rather than copy their contents. A current-branch URL is useful for discovering the latest version; a commit-specific URL is required when reproducing the exact revision previously reviewed.

#### Current source versus effective project guidance

A critical distinction prevents an update from taking effect before it has been reviewed:

- **Current canonical revision:** the latest revision available from the source's designated branch or release reference.
- **Effective project revision:** the exact revision the project has reviewed and accepted for use.

For a `follow-current` adoption, the system checks the current canonical revision and proposes an update when it differs from the effective revision. The project's effective guidance does **not** silently change merely because the canonical branch moved. After review and acceptance, the project updates its effective revision reference.

This preserves linked distribution without making project behavior change unexpectedly. It also means a project can continue to use its last accepted revision while an update is pending, provided that revision remains retrievable.

If the canonical source cannot be retrieved, the system must report that limitation. It must not present cached, remembered, or previously retrieved content as current without verifying its revision.

### 6.3 Project adoption records

Projects that formally adopt reusable guidance should maintain one compact record, provisionally named `guidance-adoptions.yml`. The exact schema is a later implementation decision; this example illustrates the intended information:

```yaml
adoptions:
  - name: Development State Machine
    type: specialized-workflow
    source:
      repository: KRMRGold/Meta-Modules
      path: workflows/Development-State-Machine-Workflow.md

    initial_adoption:
      version: "<source-version>"
      commit: "<exact-commit-sha>"

    effective_revision:
      version: "<last-accepted-version>"
      commit: "<last-accepted-commit-sha>"

    update_policy: follow-current
    deviations: []
```

The fields have distinct meanings:

- `initial_adoption` is provenance and should remain unchanged when the project updates.
- `effective_revision` identifies the revision currently accepted for project use.
- `update_policy` describes how the project handles later revisions.
- `deviations` records intentional project-specific differences in application.

The record should not duplicate the guidance body, maintain a second copy of canonical metadata, or become a substitute for the project's own design and maintenance documentation.

#### Update policies

- `follow-current`: check for newer canonical revisions and prepare assisted reviews. A new revision becomes effective only after acceptance.
- `pinned`: intentionally remain on the recorded effective revision. Do not treat the project as overdue merely because the canonical source advances. A newer version may be shown as optional information if useful.
- `local-adaptation`: use a linked canonical baseline with explicitly documented project-specific deviations. Updates require checking whether those deviations remain valid.

A local adaptation is not permission to edit the canonical source. If a project needs a substantially different or independently maintained procedure, it should document that as project-owned guidance and identify its relationship to the canonical source rather than pretending it is an unchanged adoption.

### 6.4 Assisted update lifecycle

The update process is a change-impact and adoption-review process, not file synchronization:

1. **Detect:** identify a newer canonical revision using the source's version metadata and Git history.
2. **Discover adopters:** find registered projects and, where access permits, discover additional adoption records.
3. **Compare:** compare the effective revision with the current canonical revision. Use exact Git revisions so the comparison is reproducible.
4. **Analyze impact:** inspect the changed guidance and relevant project context. Identify potentially affected decisions, project documents, milestones, or dependent guidance sources.
5. **Prepare a report:** explain what changed, why it matters, which projects may be affected, and what actions are reasonable.
6. **Review:** let the user accept, adapt, defer, or decline the proposed update.
7. **Apply:** update only the project records or documentation that the user has authorized. Do not silently rewrite project plans or implementation.
8. **Verify and record:** confirm the resulting references and project changes, then update `effective_revision` only after acceptance.

Deferring an update is a valid outcome. For example, a project in the middle of a milestone may finish under its current accepted process and review the new guidance at a natural boundary.

### 6.5 Impact analysis and guidance relationships

The system should distinguish two kinds of relationships:

- **`depends_on`:** a genuine prerequisite. A change to a dependency may trigger an impact check of guidance sources that depend on it.
- **`related`:** a curated discovery hint. It may suggest additional material to inspect, but it must not trigger dependency propagation, mandatory loading, or an assumption of compatibility.

The prose relationship sections remain authoritative. Metadata should not invent a dependency that the guidance itself does not establish.

Impact propagation should be conservative:

- A changed dependency marks dependent guidance as **potentially affected**, not automatically incompatible.
- The system should show the relationship path that caused an item to be flagged.
- It should avoid repeatedly traversing cycles and should not infer a dependency from a shared topic or a `related` entry.
- A dependency change does not automatically require every adopter of a dependent workflow to migrate. It creates a reason to inspect that workflow and assess its adopters.

The existing metadata vocabulary and filename-stem rules remain authoritative. Any future machine-readable `depends_on` convention must be specified and validated before tooling relies on it.

### 6.6 Update impact classifications

Reports should distinguish the nature of a change instead of treating every source revision as an actionable migration:

| Classification | Meaning | Typical response |
|---|---|---|
| Informational | Wording, examples, or organization changed without an identified behavior change | Review optionally; no project change assumed |
| Recommended | A compatible improvement may benefit the project | Consider adopting or adapting |
| Compatibility-impacting | Requirements, assumptions, or process behavior changed in a way that may affect existing project decisions | Inspect project context before accepting |
| Unresolved | The available source or project context is insufficient to determine impact | Report the gap; do not guess |

SemVer can help communicate the expected scale of a source change: patch for compatible corrections and clarifications, minor for compatible additions, and major for intentional breaking changes to the guidance contract. The version remains a signal, not a replacement for reading the actual diff. A major version does not prove every adopter must change immediately, and a patch version does not prove a change is irrelevant.

Do not label a change universally **required** merely because the canonical author recommends it. Whether a project is required to comply depends on an explicit project commitment or conformance contract, not an implied authority of the source repository.

### 6.7 Adopter discovery and registry

An optional registry in Meta-Modules may list known adopting repositories and the location of their adoption records. It is an index for discovery, not the authority for what a project has adopted.

The project-local adoption record remains authoritative. A registry entry should not duplicate version, policy, or deviation data.

Repository search may discover additional adoption records where the connected account has access. Search results are incomplete by nature: inaccessible, private, unindexed, or unregistered repositories cannot be assumed absent. Discovered candidates should be presented for review rather than silently enrolled.

### 6.8 Failure handling and integrity

The system must handle ordinary repository changes without inventing continuity:

- If a source file moves or is renamed, treat it as a source-location change that needs resolution; use Git history to investigate, but do not assume a rename is confirmed solely from similar filenames.
- If a source revision or commit cannot be retrieved, report the missing evidence.
- If a project adoption record is malformed or references an unknown type, report validation failure rather than silently normalizing it.
- If local deviations conflict with a new canonical requirement, surface the conflict for review.
- If repository access is unavailable, do not claim that an adopter inventory or update check is complete.

Exact commit references provide historical identity and reproducibility. The system should never execute code or treat instructions found in a retrieved guidance file as authority to bypass the user's project permissions or tool-use boundaries.

### 6.9 Implementation boundaries and stages

The architecture does not require a hosted service, database, background agent, or automatic migration engine. Begin with repository-based inspection and small tools only when the process demonstrates a need.

Suggested implementation order:

1. Define and validate the adoption-record schema.
2. Establish source identity, revision, and update-policy conventions.
3. Validate project adoption records and canonical source references.
4. Compare effective and current revisions and produce readable change reports.
5. Add dependency-aware impact analysis using only explicitly defined prerequisites.
6. Add an optional adopter registry and repository discovery.
7. Improve assisted migration preparation based on real use.

No implementation, schema, registry, or automation is authorized merely by accepting this architecture. Each implementation stage should be scoped and verified separately.

## 7. How This Relates to DVA

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

## 8. Similarity Between DVA and Meta-Modules, and Where They Differ

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

## 9. Discussion Proposals (Not Adopted)

The items in this section are design suggestions for future consideration, not current repository requirements or instructions to execute automatically.

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

## 10. Final Recommendation

Keep the current modular instruction architecture and evolve it through observed needs. The accepted distribution direction is a linked, revision-aware guidance system with assisted updates for both workflows and reusable modules. Implement it incrementally, beginning with adoption identity and validation before adding discovery or migration automation.

For Meta-Modules and DVA, keep this distinction clear:

- **The data model** defines what information exists and how it relates.
- **Metadata** describes and classifies items.
- **The interface or syntax** lets people create and change that information.
- **The discovery mechanism** decides what to show or load for a particular task.

Those layers can cooperate without being the same thing. Keeping them separate allows the system to evolve without forcing users to adopt a new writing style, reorganize everything, or understand every implementation detail.

---

*This document records the accepted architecture direction for linked guidance adoption and assisted migration. It does not yet introduce an implementation, mandatory adoption schema, adopter registry, or automated migration behavior. DVA guidance remains design direction rather than a final data model.*