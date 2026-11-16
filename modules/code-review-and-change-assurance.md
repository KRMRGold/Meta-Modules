---
name: code-review-and-change-assurance
type: specialized
version: "0.1.0"
related: [testing-and-verification, Development-State-Machine-Workflow, sandboxing-and-safe-execution]
purpose: Review proposed software changes systematically for correctness, maintainability, security, scope control, and evidence quality before acceptance.
use_when: A code change, pull request, generated patch, agent-produced implementation, or meaningful configuration change needs review beyond confirming that tests pass.
---

# Code Review and Change Assurance

## Purpose

Use this module to assess whether a proposed change is appropriate, understandable, and safe to accept. Code review complements testing: tests provide evidence about selected behavior, while review examines the change's design, assumptions, boundaries, and risks—including important cases tests may not cover.

Review depth should match the change's risk. A tiny isolated correction does not need a ceremonial review; changes involving security, permissions, persistence, data migration, networking, external inputs, or execution boundaries deserve closer scrutiny.

## 1. Establish the Review Scope

Before reviewing:

1. Identify the requested behavior and its acceptance criteria.
2. Identify the exact candidate commit, diff, or changed files.
3. Establish the last accepted baseline and distinguish requested changes from unrelated pre-existing work.
4. Read relevant design, maintenance, and interface contracts.
5. Identify affected components, data flows, dependencies, permissions, and trust boundaries.
6. Determine whether the review is self-review, a separate reviewer, or an automated analysis.

Do not claim to have reviewed files or a diff that were not actually available. If the diff is incomplete, say what was and was not inspected.

## 2. Review the Change, Not Just the Happy Path

Inspect the changed code and the surrounding context needed to understand it. Consider the following where relevant:

- **Correctness:** Does the implementation satisfy the requested behavior and acceptance criteria?
- **Scope:** Are changes limited to the task? Are unrelated refactors, dependencies, generated files, or configuration changes justified?
- **Data flow:** Where does input originate, how is it validated, transformed, stored, and exposed?
- **State and persistence:** Are state transitions, serialization, migrations, recovery, and compatibility handled?
- **Failure behavior:** What happens with invalid input, missing resources, partial completion, timeouts, retries, cancellation, and unavailable dependencies?
- **Security:** Are authentication, authorization, trust boundaries, secrets, injection risks, path handling, and unsafe defaults addressed?
- **Permissions:** Does each component or agent receive only the access required for its task? Can untrusted content influence privileged actions?
- **Dependencies and supply chain:** Are new packages, scripts, binaries, and external services necessary and reasonably trustworthy?
- **Maintainability:** Is the solution understandable, consistent with project conventions, and no more complex than needed?
- **Observability:** Can important failures be diagnosed without leaking secrets or sensitive data?
- **Tests:** Do tests verify meaningful observable behavior, edge cases, and failure paths? Could they pass while the implementation is still wrong?

Follow relevant data and control flow across file boundaries. A review limited to changed lines can miss assumptions or side effects in their callers and dependencies.

## 3. Distinguish Review from Testing

- A passing test suite does not establish that the change is well-designed, secure, or complete.
- Source inspection does not establish runtime behavior.
- Static-analysis output is evidence about the checks it actually performs, not a general approval.
- A reviewer must not describe an unexecuted test as passed.
- A test author should not weaken or remove meaningful assertions merely to make a candidate pass.

Use [Testing and Verification](testing-and-verification.md) for test strategy and execution evidence. Use [Sandboxing and Safe Execution](sandboxing-and-safe-execution.md) when code or tools will be executed and their permissions or isolation matter.

## 4. Independence and Reviewer Roles

For consequential changes, prefer a reviewer that did not author the implementation. An independent reviewer should receive the requirements, relevant design, baseline, and candidate diff—not merely the implementer's claim that the work is complete.

When a separate reviewer is unavailable:

1. Perform an explicit self-review after implementation rather than relying on the reasoning used while writing the code.
2. Re-read the acceptance criteria and inspect the diff from the baseline.
3. Use automated static analysis and tests where available.
4. Label the result **self-reviewed**, not independently reviewed.
5. State remaining blind spots, especially where the reviewer shares the implementer's assumptions or context.

Multiple agents or model instances are not automatically independent. Independence is weakened when reviewers share the same incomplete specification, are given the same leading summary, or simply endorse an implementer's conclusion. Ask reviewers to identify concrete evidence and counterexamples.

## 5. Findings and Disposition

Report actionable findings with:

- **Severity:** critical, high, medium, low, or informational.
- **Location:** file and relevant function or line range where available.
- **Evidence:** the observed code, behavior, or missing control that supports the finding.
- **Impact:** what could happen and under what conditions.
- **Recommendation:** the smallest reasonable correction or a reasoned alternative.

Do not inflate speculative concerns into confirmed vulnerabilities. Separate confirmed defects from plausible risks and questions requiring runtime evidence.

Resolve or explicitly disposition findings before acceptance:

- Critical/high findings that affect safety, security, data integrity, or core correctness block acceptance until fixed or explicitly scoped out through an informed decision.
- Medium/low findings may be fixed, deferred, or accepted with a brief rationale according to project risk.
- Informational observations do not block acceptance by themselves.

A review with no findings means no issues were identified within the review's scope; it is not proof that no defects exist.

## 6. Review Completion Record

For meaningful changes, record a compact result alongside the development or pull-request record:

- candidate commit/version and review scope;
- reviewer identity or role and whether review was independent or self-review;
- files/diff inspected and checks consulted;
- findings with severity and disposition;
- unresolved risks and unreviewed areas;
- overall status: **PASS**, **CHANGES REQUIRED**, or **BLOCKED**.

Do not mark a change accepted solely because a review was completed. Acceptance still depends on the project's criteria and the required verification gates in its development workflow.
