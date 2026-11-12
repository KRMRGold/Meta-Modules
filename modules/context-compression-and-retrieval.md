---
name: context-compression-and-retrieval
type: specialized
version: "0.1.0"
related: [context-continuity, intent-and-clarity]
purpose: Reduce the active context needed for long conversations and multi-document projects while preserving authoritative source material, provenance, and the ability to recover detail.
use_when: A conversation, project, or task has accumulated enough history or documentation that loading everything is inefficient, continuity is at risk, or relevant information must be selected from multiple sources.
---

# Context Compression & Retrieval

## Purpose

Keep the active context small without making the underlying knowledge smaller, less reliable, or harder to recover.

Use compression to create a useful working representation, not to replace canonical source material. Combine a compact state summary with carefully selected original messages, document excerpts, decisions, and evidence. Retrieve more detail when the task requires it.

This module adapts useful ideas from Codex conversation compaction: generate a compact continuation state, retain selected original high-value inputs, restore canonical instructions, and keep the replacement context within a deliberate budget. Codex's native encrypted compaction item is model-managed and opaque; this module defines a portable, human-readable approach rather than claiming to reproduce that internal representation.

## 1. Two distinct compression problems

Choose the policy that matches the material. They may be used together, but must not be conflated.

### Conversation compaction

Reduce a long interaction to a continuation checkpoint that lets a later turn or fresh session resume the work.

Preserve:
- the user's objective and latest explicit request;
- user-stated constraints, preferences, and decisions that still apply;
- accepted state, exact artifact versions, commits, and paths;
- what changed, what was actually verified, and the evidence;
- unresolved questions, blockers, known failures, and next steps;
- source references needed to recover detail;
- selected original user messages or tool results when paraphrasing could change meaning.

Do not preserve every turn by default. Do not discard a critical original instruction merely because a later summary seems to cover it. Keep exact errors, commands, identifiers, test results, and acceptance evidence when they matter to continuation.

### Document and project compression

Reduce the amount of project documentation that must be loaded for a task.

Use a small project map or context index to describe:
- the project's purpose and current accepted state;
- canonical documents and the authority each one holds;
- topic-to-document routing (where architecture, decisions, tests, maintenance, and requirements live);
- important dependencies and known conflicts;
- source revisions used to produce the index.

Create topic summaries only where they reduce repeated retrieval. Prefer one compact index with topic sections over a separate summary file for every source document. For one-off tasks, generate a temporary task-specific context packet instead of adding permanent documentation.

## 2. Compression is not deletion

- Keep canonical source documents intact unless the user separately requests edits.
- Treat summaries, indexes, and checkpoints as derived material, never as a replacement for source documents.
- Preserve a route from every consequential summary claim to its source file and relevant heading, section, line range, or record identifier.
- Preserve exact wording for requirements, constraints, errors, commands, identifiers, and user decisions when paraphrase could alter their meaning.
- Do not silently discard unresolved disagreement, uncertainty, caveats, or negative evidence.
- Never convert a proposal into an accepted decision or an implemented feature into a verified one.
- Do not claim that a summary preserves hidden reasoning. Record outcomes, evidence, decisions, and concise rationales, not private chain-of-thought.

If the source material cannot be recovered, label the affected information as unavailable or unverified. Do not invent a replacement.

## 3. Establish source authority before summarizing

Before compressing multiple documents:

1. Inventory the relevant files from the current repository state; do not rely on a remembered or stale file list.
2. Classify each source by role, such as requirements, design, decisions, implementation/maintenance, test evidence, workflow, or historical record.
3. Identify which source is authoritative for each kind of fact. Authority is subject-specific; one file does not necessarily outrank every other file.
4. Check current repository state and revisions for documents that may have changed.
5. Detect contradictions, stale statements, duplicate sources of truth, and claims that lack evidence.
6. Preserve unresolved conflicts explicitly. Do not average conflicting claims into a synthetic answer.

Typical software-project distinctions:
- Design/specification: intended behavior and constraints.
- Maintenance: accepted implementation state and known limitations.
- Decisions: choices and reasons that resolve design ambiguity.
- Test record/CI: evidence for a particular candidate and environment.
- Git history: provenance and prior revisions, not a substitute for the current document.

Use the project's own documented authority rules when they exist.

## 4. Hierarchical context selection

Use the shallowest level that can answer the task, and expand only when needed.

1. **Project overview:** purpose, current state, constraints, and links to canonical sources.
2. **Topic summary:** a concise map for the relevant area, such as backend, UI, architecture, persistence, testing, or release.
3. **Document section:** the specific headings, decisions, requirements, or test cases needed.
4. **Original source:** the complete document, code, commit, test output, or conversation record when detail or verification requires it.

Do not load every level automatically. A task packet can combine a project overview, one or two topic summaries, and selected source excerpts.

For each selected source, record enough provenance to identify what was read:
- repository and path;
- branch/ref or commit when available;
- Git blob SHA or another stable revision identifier when available;
- relevant heading or section;
- retrieval date only when useful and available.

A source path without a checked revision is a weaker freshness signal. State that limitation.

## 5. Build a task-specific context packet

Select context by relevance to the current task, not by document size or recency alone.

A useful packet contains:

1. **Objective:** what the user is trying to accomplish now.
2. **Applicable constraints:** user decisions, project invariants, tool and environment limits.
3. **Current accepted state:** exact version/commit and implemented behavior.
4. **Relevant design:** requirements and expected behavior for this task.
5. **Decisions:** accepted choices and their reasons.
6. **Evidence:** exact checks, commands, results, and evidence level.
7. **Open issues:** blockers, known failures, uncertainty, and deferred work.
8. **Source map:** references to the original material behind important claims.
9. **Omissions:** important sources not loaded and why they were omitted.
10. **Freshness:** whether source revisions were checked and whether derived summaries are current.

Keep the packet concise, but do not omit a fact whose absence could cause an incorrect or unsafe action. If the packet cannot establish a critical fact, retrieve the source or pause for clarification.

## 6. Conversation compaction procedure

When a conversation becomes too large to use reliably:

1. Identify the active objective and the latest user request.
2. Separate durable decisions and constraints from temporary discussion, discarded ideas, and superseded plans.
3. Capture the current artifact state and distinguish discussed, designed, implemented, source-checked, runtime-tested, user-confirmed, accepted, and unverified work.
4. Preserve exact evidence and identifiers needed to continue.
5. Retain selected original user messages and important tool outputs where exact wording or structured data matters.
6. Produce a compact continuation checkpoint with unresolved issues and the next actionable step.
7. Restore or reference canonical instructions independently of the summary; do not assume a compressed conversation still contains every applicable instruction.
8. Check that the checkpoint does not contradict the retained source material.
9. Continue from the checkpoint while keeping original history available for retrieval where the platform permits.

If the compaction attempt fails or produces an incomplete checkpoint, keep the original context and retry or retrieve the missing sources. Do not proceed as though the checkpoint were complete.

## 7. Freshness, invalidation, and regeneration

A derived summary is current only relative to the source revisions from which it was produced.

- Record source revision identifiers when available. Prefer Git commit/blob SHAs over dates alone.
- When a source changes, mark summaries that depend on it stale.
- If dependency relationships are unknown, treat the affected summary as freshness-unknown rather than assuming it is current.
- Regenerate affected sections from canonical sources, not by repeatedly summarizing an older summary.
- Preserve unchanged topic summaries when their source dependencies are unchanged.
- Do not update a derived summary merely to make its timestamp look recent.
- If the source repository cannot be checked, disclose that freshness could not be verified.

A simple manifest may map each summary section to its source paths and revisions. Avoid building an elaborate dependency database unless project scale justifies it.

## 8. Budget and prioritization

Allocate the available context budget deliberately. Do not use a fixed percentage split as a universal rule; the right allocation depends on the task and model.

Prioritize:
1. system and applicable canonical instructions;
2. the user's current objective and constraints;
3. accepted project state and invariants;
4. task-relevant requirements and decisions;
5. evidence, failures, and unresolved issues;
6. selected recent interaction and source excerpts;
7. background information that is useful but not necessary.

Keep enough capacity for the actual task, tool results, and unexpected findings. If the budget is tight, narrow retrieval to the task before truncating high-priority context. Record important omissions.

Do not optimize token count at the expense of correctness, source traceability, or the ability to resume.

## 9. Conflict and uncertainty handling

When summaries and sources disagree:
- prefer the current authoritative source for the specific fact;
- verify current implementation or test evidence before claiming behavior;
- preserve the disagreement if authority cannot resolve it;
- mark stale or unsupported summary claims for regeneration;
- disclose conflicts that could change implementation or acceptance.

Use explicit evidence labels from the project's workflow where available. A green test result applies only to the candidate and environment actually tested.

## 10. Lightweight use

For a small task:

`identify objective → find authoritative source → retrieve relevant section → work`

For a multi-document task:

`inventory → classify authority → select relevant sources → build packet → work → verify claims against sources`

For a long-running conversation:

`capture objective/state/decisions/evidence → retain critical originals → restore canonical instructions → continue`

Do not create a permanent context index for a one-time task. Create or refresh one only when repeated retrieval cost or continuity risk justifies maintaining it.

## 11. Success criteria

- The active context is materially smaller than loading all available history and documents.
- Important user intent, constraints, accepted state, decisions, and evidence survive compression.
- Consequential summary claims are traceable to current sources.
- Stale summaries and conflicting sources are identified rather than silently trusted.
- Detail can be retrieved from original sources when needed.
- The user is not asked to repeat information that can be recovered.
- Compression reduces friction without creating a second, competing source of truth.
