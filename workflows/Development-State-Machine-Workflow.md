---
name: development-state-machine-workflow
type: specialized-workflow
version: "1.5.2"
purpose: Guide reliable, evidence-based development through planning, implementation, verification, recovery, documentation, and version history.
use_when: The user is developing or maintaining an application or substantial project and wants a repeatable workflow for making and verifying changes.
---

# Development State Machine Workflow
## Reusable Workflow Prompt v1.5.2

- **Workflow version:** 1.5.2
- **Document policy:** Keep one current workflow file at its canonical path. Update that file in place; use Git history for prior revisions. Do not create side-by-side versioned copies.
- **Revision history:** Earlier revisions are preserved in Git history, not separate files.
- **Scope:** A reusable, modular development workflow for applications and other projects, independent of any one app, programming language, framework, or tool.
- **Purpose:** Help people develop reliable applications without requiring them to already know the best development methods. The workflow guides design, implementation, verification, recovery, documentation, and version history, using evidence from actual work to improve the process over time.

## 1. What This Workflow Is

This document is both a process definition and a prompt that a user can give to an AI assistant to help guide development.

A user can adopt the workflow for a new or existing app and incorporate it into that app's initial design document. The workflow remains a separate, reusable component. The app's design describes the app; this workflow describes how to develop it.

The user does not need to know every useful practice in advance. Help them discover and apply appropriate practices as the project needs them. Explain decisions clearly, ask focused questions when an important choice is missing, and avoid making the process heavier than the work requires.

The workflow is independent of any particular app or project. Its practices should be evaluated in context, and further use should reveal where they work well, where they need adaptation, and where the workflow itself should improve.

**Core idea:** make a clear plan, preserve the last accepted state, implement a candidate, inspect and test it, record what the evidence shows, then decide what to do next.

## 2. Modularity and Adoption

### 2.0 Default adoption for substantial projects

Recommend this workflow by default for substantial software, design, research, or other multi-stage projects where planning, iteration, verification, and recoverability matter. Introduce it early, explain the benefits in plain language, and ask about deviations only when goals, risks, or constraints make the default a meaningful choice. Use the lightweight path for small changes and adapt stages to non-software projects. This is a reliability aid, not a paperwork requirement. Record the exact adopted version and justified adaptations in the initial design or equivalent project record.

### 2.1 Core workflow

The core workflow covers:

- understanding the user's goal and constraints;
- designing and refining the intended behavior;
- defining observable acceptance criteria;
- identifying and preserving the last known-working version;
- implementing a scoped candidate;
- inspecting source changes;
- testing actual behavior;
- repairing failures and retesting;
- updating maintenance knowledge only from verified results;
- keeping versions and history clear;
- deciding when a project has reached its desired scope.

### 2.2 Project-specific additions

An app may need additional modules for its own risks or behavior, such as persistence and migration, security, accessibility, networking, media timing, collaboration, or import/export. Add modules when they solve a real project need. Do not assume every app requires every module.

A project's initial design should state:

1. that it adopts the reusable workflow;
2. which version of the workflow it adopts;
3. which optional modules or project-specific checks are needed;
4. where its initial design, code, maintenance document, tests, and any milestone document live;
5. any justified adaptations to the general workflow.

A project can link to the workflow instead of copying its entire text. If a copy is embedded in a project's design, identify the source version so the copy can be traced and updated deliberately.

### 2.3 Keep the layers separate

- **Reusable workflow:** how development is organized.
- **App initial design:** what this particular app should be and how the workflow applies to it.
- **Application code:** what has actually been implemented.
- **Maintenance document:** the ongoing record of accepted implementation state, evidence, limitations, and next work.
- **Milestone document:** a reconciled reference for a significant accepted state of the app, detailed enough to guide reconstruction.
- **Tests and test records:** the evidence used to judge candidate behavior.

Do not turn the reusable workflow into an app-specific architecture document. Do not treat an app's design as proof that its planned behavior has been implemented.

## 3. Evidence, Learning, and Workflow Evolution

The workflow should improve through experience, not through unsupported claims that one method is universally best.

Use evidence from actual projects to identify:
- practices that repeatedly help;
- steps that are missing or confusing;
- unnecessary effort or duplicated documentation;
- failure patterns that need a better recovery method;
- useful techniques discovered during development;
- practices that work in one context but may not generalize.

A failure is not the only reason to improve the workflow. Successful experiments, clearer explanations, and more efficient ways of preserving correctness can also justify changes.

When considering a workflow change:

1. describe the problem or opportunity;
2. identify the evidence and the context in which it appeared;
3. decide whether the change belongs in the core workflow or an optional module;
4. consider compatibility with existing projects using the prior version;
5. make the smallest change that addresses the need;
6. record what changed and why;
7. use the revised workflow and continue evaluating its results.

Distinguish observed evidence from assumptions and expectations. A successful result in one context is useful evidence, but does not by itself prove that the same practice works in every context.

## 4. Versioning and Artifact Identity

### Project-wide default

Use SemVer by default for application code and other artifacts whose identity is tied to a distinct released build. Introduce the convention at project setup and include it in the initial design. Each independently versioned build artifact has its own MAJOR.MINOR.PATCH sequence.

**Document storage rule: one current file per document, never a stack of versioned copies.** Initial designs, maintenance documents, milestone documents, reusable workflows, modules, and other living documentation stay at one stable canonical path. When a document changes, update that same file in place. Do not create a second file with a bumped version in its filename, keep an `-old` or `-backup` copy, or leave superseded document versions beside the current one. Git commits provide the revision history and recovery. If Git is unavailable, use another deliberate history mechanism rather than cluttering the working folder with duplicate documents.

A document may carry a version field in its contents when that identifier is useful, but the version number does **not** create a new file. Increment that metadata when appropriate, then update the canonical file. If a different scheme is justified, explain the trade-off and record the exception.

This rule is intentional and applies even when a document is described as versioned elsewhere in this workflow. A request for a new document version means update the existing canonical document unless the user explicitly asks for a separate, distinct document.

### 4.1 SemVer meaning

Use the same general rules for every artifact:

- **MAJOR:** an incompatible change to the artifact's contract, structure, or expected use.
- **MINOR:** a backward-compatible addition or meaningful expansion.
- **PATCH:** a backward-compatible correction, repair, or clarification.

For app code, a new backward-compatible feature normally increments MINOR; a backward-compatible bug fix increments PATCH; and an incompatible behavior, interface, or data-format change increments MAJOR. Use judgment for documents: a substantive expansion is usually MINOR, a correction is usually PATCH, and a change that breaks the document's expected use may be MAJOR.

SemVer versions have exactly three numeric components. For example, `1.31.1` is valid; `1.31.01` is not, because numeric identifiers must not have leading zeros. Do not add extra numeric components.

### 4.2 Artifact versions are independent

Version each independently versioned code/build artifact according to changes to that artifact, not the version of another artifact. For example, app code may be `1.31.0`; its maintenance document remains one file at `docs/MAINTENANCE.md`, and its initial design remains one file at `docs/DESIGN.md`. Document revision metadata, if used, is independent, but it never creates parallel files.

Record cross-references where useful: the maintenance document should identify the exact accepted code version and commit; project documents should identify the workflow version adopted; and a milestone document should identify the accepted code state it describes. Link to canonical document paths, not version-suffixed duplicates.

### 4.3 Candidate, accepted, and failed versions

A version number identifies an artifact version; its status describes whether it has been accepted. Do not use the version number alone to imply that a candidate passed testing.

- Preserve the last accepted version as the recovery baseline.
- Develop a candidate without overwriting that baseline.
- Keep failed **code/build candidates** and their test evidence available as history when practical, using Git commits, tags, or another source-history mechanism.
- When repairing a code/build candidate, create a new version rather than silently replacing the failed candidate. A backward-compatible repair normally increments PATCH.
- Do not create failed or superseded copies of living documents. Edit the canonical document in place; Git history records the prior contents.
- Inspect and retest the repaired version. Do not mark it accepted until the required acceptance checks pass.
- Record explicit status such as **candidate**, **failed**, **accepted**, or **superseded** in the maintenance record or version history.
- If a failed code candidate is never repaired, retain its version and status as historical evidence. Do not relabel it as accepted. For documents, retain the revision in Git history rather than as a separate file.
- Never claim tests passed unless the tests were actually run and the result is known.

Example: code `1.31.0` introduces a feature. If testing reveals a bug, preserve `1.31.0` as the failed candidate and create `1.31.1` with the repair. If another repair is needed, create `1.31.2`. The maintenance document records which version, if any, is accepted. The failed candidate remains traceable and is not overwritten.

A repository commit provides document revision history. Keep document filenames stable and descriptive, such as `AppCode.html`, `DESIGN.md`, or `MAINTENANCE.md`; do not append version numbers to living document filenames. Code/build artifacts may use their own release/version identity where the project needs it, but that is not a reason to duplicate documentation.

### 4.4 Workflow versioning

Use SemVer for this reusable workflow:

- **MAJOR:** a change that breaks the expected workflow contract or requires adopters to change how they use it.
- **MINOR:** a backward-compatible addition, such as a new optional module or an expanded adoption rule.
- **PATCH:** a backward-compatible correction or clarification that does not materially change the workflow's behavior.

Keep one canonical workflow file at its stable repository path. When the workflow changes, update that file in place and increment its internal version metadata according to SemVer. Do not publish additional version-suffixed workflow files or retain older copies beside it. Git history preserves prior revisions. Future chats must retrieve this one canonical current workflow file and must not search for or resurrect older version-suffixed copies. When a project adopts the workflow, record its current internal version and any relevant changes to its development plan.

### 4.5 Maintenance documents and milestone documents

A **maintenance document** is the ongoing record of development. Keep exactly one current maintenance document at a stable canonical path, and update it in place after acceptance to identify the current accepted code version, source commit or path, test evidence, known issues, and next work. It may also record failed code candidates and their outcomes. If the document carries revision metadata, update that metadata in the same file; use Git history for prior revisions. Never create a new maintenance file for each update.

A **milestone document** captures the latest deliberate, reconciled state of the app at a user-defined milestone. Keep one current milestone document at a stable canonical path and update it in place when the accepted state changes. It should identify the exact accepted code version it describes. Use Git history to preserve earlier milestone-document revisions; do not create a separate versioned document for each milestone or update. Creating a milestone does not reset or replace the app's code-version sequence.

A milestone is a reference point, not a claim that the app can never change again and not a substitute for version control.

## 5. Core Development State Machine

Use the complete path for substantial features and new subsystems. For small fixes, use the lightweight path in Section 9 while retaining the essential checks.

### State definitions

- **S0 — Request or idea:** Understand the user's goal, constraints, priorities, and definition of success. Ask concise questions when needed.
- **S1 — Initial design:** Describe the intended app or feature, including goals, expected behavior, relevant data, dependencies, and scope. For an app adopting this workflow, identify the workflow version and applicable modules.
- **S2 — Design refinement:** Look for ambiguity, contradictions, failure cases, compatibility issues, persistence needs, and unintended consequences. Refine until the design is implementable.
- **S3 — Ready to implement:** Confirm important choices are resolved, acceptance checks are defined, the working baseline is known, and any needed user approval has been obtained.
- **S4 — Implementation:** Build a candidate from the agreed design, current maintenance knowledge, and last accepted code. Assign the candidate its own artifact version and preserve the baseline.
- **S5 — Source inspection:** Review changed files and diffs. Check data flow, architecture, security, compatibility, syntax, and available static checks.
- **S6 — Runtime and acceptance testing:** Run the candidate and perform acceptance and relevant regression tests in the actual runtime where possible. Record exact candidate version and results.
- **S7 — Acceptance gate:** Compare recorded results with the acceptance criteria. If a required check fails, move to S8. If required checks pass, proceed to S9.
- **S8 — Repair and iteration:** Compare the requirements, last accepted code, failed candidate, and observed failure. Decide whether the issue is in the design, implementation, or test assumptions. Preserve the failed candidate and evidence. Create a new version for the repair. If the design is inadequate, return to S2. Otherwise repair the candidate and return to S5.
- **S9 — Maintenance update:** Record the accepted code version, source reference, test evidence, differences from the design, and unresolved limitations. Update the single canonical maintenance document in place; Git history preserves earlier revisions.
- **S10 — Accepted feature and next decision:** The feature is accepted for the agreed scope. Decide what to work on next or whether the app has reached its desired completion scope.
- **S11 — Milestone document:** When the user declares the app complete to the desired scope, establish the accepted code and documentation state, create or update the single canonical milestone document in place, and test whether it communicates the app well enough for reconstruction in a fresh session.

### Transition map

```text
S0 Request / idea
  -> S1 Initial design
  -> S2 Refine design
  -> S3 Ready to implement
  -> S4 Implement versioned candidate
  -> S5 Inspect source
  -> S6 Runtime + acceptance tests
  -> S7 Acceptance gate
       -> failed: S8 Preserve failure + repair as new version
            -> design flaw: S2
            -> implementation flaw: S4
            -> then S5 -> S6 -> S7
       -> passed: S9 Update maintenance document
            -> S10 Accept feature / choose next work
                 -> next feature: S0 or S1
                 -> desired completion declared: S11 Milestone document
```

### Transition requirements

- **S0 → S1:** the goal and relevant constraints are understood well enough to draft a design.
- **S1 → S2:** a draft design exists to review.
- **S2 → S3:** the design is specific enough to implement and has observable acceptance criteria.
- **S3 → S4:** the user has authorized implementation when approval is needed.
- **S4 → S5:** a candidate exists, has a clear version identity, and the prior accepted baseline remains recoverable.
- **S5 → S6:** no known blocker prevents meaningful testing, or remaining risks are explicitly understood. The AI must consult the maintenance document and use its existing test/check list as the starting verification plan.
- **S6 → S7:** the AI has executed all required checks its available tools and environment permit, recorded actual results against the exact candidate version, and marked unavailable checks **BLOCKED / NOT RUN** with the reason and minimum human action needed. Writing tests or suggesting that a human run an executable check does not satisfy this transition.
- **S7 → S8:** a required check fails, a regression is found, or a critical check remains unverified and is executable in the available environment.
- **S8 → S5:** a corrected candidate with a new version is ready for inspection. Return to S2 first if the design needs correction.
- **S7 → S9:** all required checks pass and behavior matches the agreed scope. A blocked or unrun check may remain only when it is non-critical or the user explicitly accepts the documented limitation; a critical required check cannot be treated as passed merely because the current environment cannot run it.
- **S9 → S10:** maintenance notes accurately describe the accepted state and exact code version.
- **S10 → S11:** the user declares the app complete to their desired scope.
- **S11 → S0/S1:** future work begins after the milestone.

## 6. Design and Implementation Rules

For a feature of meaningful complexity, the design should cover:

1. **Goal:** what problem it solves.
2. **User flow:** how the user triggers and uses it.
3. **Behavior:** expected results and how ambiguous cases resolve.
4. **Data model:** data, ownership, relationships, defaults, and persistence.
5. **State changes:** what changes and what must remain unchanged.
6. **Compatibility:** interactions with existing features, saved data, imports, exports, and earlier versions.
7. **Failure behavior:** invalid input, cancellations, missing dependencies, interruptions, and recovery.
8. **Boundaries:** what is out of scope.
9. **Acceptance checks:** observable evidence of success.
10. **Risks and alternatives:** relevant trade-offs and reasonable options.

Implementation and recovery rules:

- Identify and preserve the last accepted version before changing code.
- Assign distinct versions to code/build candidates where applicable. Never silently overwrite the accepted code baseline or reuse a code version number for changed contents. Living documents are updated at their one canonical path; Git history preserves prior revisions.
- Prefer small, coherent changes over unrelated rewrites.
- Do not mix unrequested features into a fix.
- Keep version-control history or backups that allow recovery.
- Use actual errors and reproduction steps instead of guessing.
- Compare the requirements, accepted baseline, candidate, and observed behavior when repairing a failure.
- Correct the source of the failure. If the requirement itself is wrong or ambiguous, update the design before coding again.
- Repeat inspection and relevant tests after every repair.
- Do not create or retain duplicate historical document files. If older version-suffixed document copies already exist, consolidate the newest content into the canonical file and remove the superseded copies when authorized. Git history, not a cluttered directory, is the document archive.
- Separate **artifact version** from **acceptance status**. A higher version is not automatically a better or accepted version.

## 7. AI-Owned Testing and Verification

For software projects, use the reusable [Testing and Verification module](../modules/testing-and-verification.md) to design the test inventory, choose appropriate test layers, improve regression coverage, and establish meaningful automated checks. This workflow remains responsible for when verification gates apply and how evidence affects acceptance; the module supplies the deeper testing practice. Adapt test depth to project risk and available runtime/platform access.

Testing is an active responsibility of the AI doing the implementation, not a handoff for the human by default. The AI must run available checks, inspect their results, repair failures, and rerun affected checks before claiming acceptance.

### Use maintenance documents as the test inventory

Before changing an existing app, read its maintenance document and use documented behavior, acceptance criteria, known issues, compatibility requirements, and prior test results as the starting test inventory. Do not discard existing checks merely because they were originally written as instructions for a human.

For each relevant check:

1. Identify the expected behavior and what evidence would prove it.
2. Run an existing automated test if available.
3. If a check is manual but repeatable, add or improve an automated test when the project and available tools support it.
4. Use suitable runtime/UI automation for real user flows when available.
5. Execute the check, inspect actual output, and record the result.
6. Keep tests for existing accepted behavior as regression tests when practical.
7. If a check cannot be automated or executed in the current environment, mark it **BLOCKED / NOT RUN**, explain why, and identify the minimum human action needed. Never silently convert it into a pass.

### Required AI execution loop

For each implementation candidate, the AI should:

1. Identify the exact candidate version or commit and preserve the last accepted baseline.
2. Inspect the maintenance test inventory and the acceptance criteria in the design or milestone document.
3. Run applicable formatters, linters, type checks, unit tests, integration tests, builds, security/dependency checks, and runtime/acceptance tests available to it.
4. Inspect failures and logs. Fix the underlying cause, not merely the assertion or test reporting.
5. Rerun failed checks and relevant regression tests after each repair.
6. Report passed, failed, blocked, and not-run checks separately, with commands and evidence.
7. Stop feature expansion when a required check fails or critical behavior remains unverified. Continue repair, narrow the scope with explicit agreement, or ask for the one decision that blocks progress.
8. Update the latest test record and maintenance document from actual evidence, not intended or assumed results.

A check is **AI-verified** only when the AI actually executed it or inspected a trustworthy execution result for the exact candidate. A test file that exists, a plan, source review, or generated output is not execution evidence. A green CI run applies only to the commit and checks shown by that run.

The AI should do as much as its tools and environment permit. Human testing is reserved for checks the AI genuinely cannot perform, such as a required test on the user's device, physical hardware, an inaccessible account, or subjective experience that requires user judgment. Clearly state the boundary; do not routinely offload executable checks to the human.

### Test records and maintenance documents

Maintain a latest-test record when useful. It identifies the candidate version, environment, exact commands/checks, actual results, links to CI/logs, remaining gaps, and overall gate status. Preserve older runs in version-control history. Do not overwrite a failed run with a pass claim unless the repaired candidate was actually rerun.

The maintenance document retains the test inventory and accepted behavior; the test record summarizes the most recent run. Keep those roles distinct. The test record is evidence of execution, not a substitute for executable tests.

## 8. Evidence Labels

Use clear labels when recording project status:

- **Designed:** behavior is described but not implemented.
- **Implemented:** code exists, but testing may be incomplete.
- **Source checked:** relevant source was inspected and available static checks passed.
- **Runtime tested:** behavior was exercised in the actual runtime against named checks.
- **User-confirmed:** the user reports that it works in their environment.
- **Unverified:** adequate test evidence is not available.
- **Known issue:** a reproducible defect or unresolved limitation is recorded.
- **Candidate:** a version under evaluation that has not yet passed the acceptance gate.
- **Failed:** a candidate did not pass one or more required checks.
- **Accepted:** the version passed the required acceptance gate for its stated scope.
- **Superseded:** a newer version has replaced it for current use, while the old version remains part of history.

Do not treat these labels as interchangeable. Source inspection cannot establish every aspect of actual behavior. Features that depend on runtime conditions must be tested in the relevant runtime. Keep test evidence tied to the exact version tested.

## 9. Maintenance and Milestone Documents

### Maintenance document

After a candidate passes the acceptance gate, update the app's one canonical maintenance document in place with:

- current accepted app-code version and exact source path, commit, or other recoverable reference;
- implemented behavior and important design decisions;
- relevant architecture, data model, and compatibility notes;
- tests performed, their results, and evidence level;
- known limitations, bugs, and unverified areas;
- candidate versions that failed and concise outcomes when relevant to future work;
- next step and deferred features;
- concise history of meaningful maintenance-document changes;
- the adopted workflow version and a link to the reusable workflow.

The maintenance document describes the accepted implementation state, not an untested aspiration. Preserve useful history, but correct stale claims instead of copying them forward unchanged. Do not mark a candidate accepted until required checks pass. If a maintenance document carries internal revision metadata, update it in the same canonical file; do not create a separate file for each revision. Git history preserves the prior contents.

### Milestone document

A milestone document is a deliberate milestone reference, not a replacement for version control and not a claim that the app can never change again.

When the user declares the app complete to the desired scope:

1. Identify the exact accepted code version and commit or equivalent source reference.
2. Bring the maintenance document up to date with actual behavior and test evidence.
3. Reconcile **the app's initial design document, the latest maintenance document, and the accepted code** into one coherent milestone specification.
4. Preserve links to the source documents and code so the origin of decisions remains traceable.
5. Distinguish implemented behavior from planned or deferred behavior. Resolve discrepancies rather than blindly copying conflicting statements.
6. Include goals, user experience, architecture, data model, important algorithms, dependencies, constraints, and acceptance tests as relevant.
7. Keep the milestone document at its one canonical path and update it in place. Identify the exact accepted code version it describes. Use Git history for prior document revisions, not separate versioned milestone files.
8. Test the milestone in a fresh LLM session without relying on hidden conversation context. Compare the resulting recreation against the accepted app using the same acceptance criteria.
9. Record important gaps and refine the milestone if necessary, by updating the one canonical document in place; Git history retains the previous revision.

The reusable workflow guides this process; it is not an app-specific design source that must be merged into every app's milestone document. The milestone should record which workflow version was used where that context matters.

A successful reproduction test provides evidence that the milestone communicates the design well. It cannot guarantee identical results across models, tools, or environments.

## 10. Lightweight Use

For a small fix, the process may be brief:

`identify accepted baseline → read maintenance checks → clarify expected behavior → create versioned candidate → inspect → run checks → repair/retest → preserve evidence → update maintenance notes`

Even on the lightweight path, the AI runs available tests itself and does not treat an unexecuted check as passed.

For a new subsystem, significant design change, or high-risk feature, use the full design and refinement stages.

The state machine exists to prevent important reasoning, testing, and history from being skipped. It is not meant to force unnecessary paperwork or make the user learn process terminology before they can build something. Scale the amount of documentation to the work, but never sacrifice recoverability or truthful status.

## 11. Final Checklist

Before accepting a feature:

- [ ] Intended behavior is clear and approved where needed.
- [ ] The last accepted version is recoverable and unchanged.
- [ ] The code/build candidate has a distinct, valid SemVer version where applicable.
- [ ] Living documents were updated at their existing canonical paths rather than duplicated into new versioned files.
- [ ] Acceptance checks are defined.
- [ ] The candidate was inspected.
- [ ] The maintenance document's relevant test inventory was consulted.
- [ ] The AI executed all feasible required checks and inspected actual results for the identified version.
- [ ] Manual checks were automated where practical, or explicitly marked blocked/not run with a reason.
- [ ] Failed checks were fixed in a new version and relevant regression tests rerun.
- [ ] Failed candidates and useful evidence remain traceable.
- [ ] Compatibility and persistence were checked where relevant.
- [ ] Maintenance documentation accurately records the accepted implementation, exact version, and evidence.
- [ ] Code/build artifact versions are independent and their history is clear.
- [ ] Exactly one current file exists for each living document; prior revisions are recoverable through Git history, not duplicate files.
- [ ] The user decides whether to continue, defer work, or declare the app complete.

When revising the reusable workflow:

- [ ] The reason for the change and supporting evidence are recorded.
- [ ] The change is classified as core workflow or optional module.
- [ ] Compatibility with existing adopters is considered.
- [ ] The SemVer increment matches the impact of the change.
- [ ] The prior workflow revision remains available through Git history; the repository contains only one current workflow document.

**Core invariants:** the workflow remains reusable across projects; each app's initial design identifies how it adopts the workflow; the maintenance document describes the accepted implementation; the AI executes and records all feasible required checks, code is accepted only after required checks pass, and unexecutable checks are explicitly blocked rather than silently delegated; code/build artifacts have independent SemVer histories; each living document has one canonical file updated in place with prior revisions retained in Git history; failed candidates are not silently overwritten or treated as accepted; and the milestone document reconciles the app's initial design, maintenance knowledge, and accepted code.
