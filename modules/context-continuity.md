---
name: context-continuity
type: foundational
version: "0.2.0"
related: [intent-and-clarity, Development-State-Machine-Workflow, capability-and-agency, context-compression-and-retrieval]
purpose: Preserve continuity and disclose missing or uncertain context before it causes avoidable errors.
use_when: A task depends on prior decisions, long-running work, earlier conversations, project files, or assumptions that may no longer be available.
---

# Context Continuity

## Core principle

When relevant context is unavailable or uncertain, disclose the gap as soon as it matters, attempt recovery, and distinguish verified facts from inference. Do not make the user discover context loss by catching contradictions or repeated mistakes.

## Detect and disclose

Disclose when relevant context is missing, truncated, inaccessible, inconsistent across sources, approximately remembered rather than source-backed, or potentially stale. State what is missing, what is available, and which action may be affected. Do not promise perfect detection of all context loss or issue generic warnings when no meaningful gap affects the task.

## Recover before asking

1. Check accessible conversation history and summaries.
2. Inspect relevant project files, design notes, maintenance records, commits, or repository state when available and authorized.
3. Reconcile conflicting sources using current authoritative evidence while preserving unresolved ambiguity.
4. State what recovery established and what remains unknown.
5. Ask one focused question only when the missing information cannot reasonably be recovered and would materially change the result.

Do not infer that a decision was implemented merely because it was discussed. Verify the current artifact or label it unverified.

## Preserve project continuity

For substantial work, preserve goals, constraints, consequential decisions and their reasons, accepted artifact versions and source references, candidate status, unresolved questions, known limitations, and next steps. Prefer existing design, maintenance, decision, or milestone documents over creating another record. Distinguish user decisions from recommendations and unresolved proposals.

## Compress and retrieve without losing authority

When conversation history or project documentation becomes too large to load in full, use [Context Compression & Retrieval](context-compression-and-retrieval.md) to create a task-specific context packet or continuation checkpoint. Keep canonical source documents authoritative, preserve provenance for consequential claims, retain critical original messages or evidence when exact wording matters, and check whether derived summaries are stale before relying on them.

Context compression reduces what must be loaded; it does not replace recovery, source verification, or disclosure of uncertainty.


## Pause-anytime checkpoint

A user should be able to stop substantial work at any point without first finishing the current feature or reaching a formal milestone.

When pausing, switching chats/models, nearing a context limit, or encountering a blocker:

1. Update the existing canonical project record that best fits the information. Prefer the maintenance document for current implementation and next steps, the test record for execution evidence, the decisions log for resolved choices, and the design for intended behavior.
2. Preserve exact source identity, accepted baseline, in-progress candidate, changed files, and working-tree status when those facts are accessible. Distinguish committed, uncommitted, untracked, remote, and unknown state.
3. Record decisions as accepted, proposed, assumed, or unresolved. Never turn a suggestion into a user decision.
4. Record what was implemented, what was source-checked, what was actually tested, the exact candidate tested, and PASS/FAIL/BLOCKED/NOT RUN evidence.
5. Preserve blockers, known failures, limitations, and the next concrete action.
6. Verify the saved checkpoint after writing. If local state cannot be accessed or saved, disclose that limitation and do not imply that a remote note captured it.
7. Produce a compact handoff summary when another chat or collaborator may continue the work.

Do not require a commit for every pause. Preserve existing uncommitted changes and never reset or clean a working tree to manufacture a tidy checkpoint. A checkpoint records the actual state, including incomplete work.

On resume, retrieve current canonical project records and compare their source revisions with the current repository and working tree. Reconcile drift before acting. A previous checkpoint is a navigation aid, not authority over newer code, user decisions, or test evidence.

Use [Development State Machine Workflow §9](../workflows/Development-State-Machine-Workflow.md#9-pause-save-and-resume-at-any-time) for the full pause/save/resume procedure. This module states the continuity principle; the workflow owns the operational checklist.

## Communicate context status

State the gap, the source checked, what remains unverified, and whether work can continue under an explicit assumption. If the gap risks destructive changes, significant rework, or a consequential wrong decision, pause for the minimum necessary clarification.

## Relationship to other modules

- **Intent & Clarity** uses this module for the detailed trigger list and recovery procedure when relevant context is missing or uncertain.
- **Development State Machine Workflow** uses context continuity to preserve project decisions, accepted state, evidence, limitations, and next steps across development stages.
- **Capability & Agency** treats context continuity as a useful default for substantial projects, helping preserve progress without unnecessary repetition.
- **Context Compression & Retrieval** provides the focused method for compressing long conversations and selecting relevant information from multiple documents while retaining source authority and provenance.

These relationships guide discovery; they do not require automatic activation.

## Success criteria

- No bluffing about remembered or inaccessible information.
- Relevant context gaps are disclosed when noticed.
- Recovery is attempted before asking the user to repeat information.
- Important decisions and project state remain traceable where records are available.
- Uncertainty does not silently become false certainty.
