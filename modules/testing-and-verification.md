---
name: testing-and-verification
type: specialized
version: "0.1.2"
related: [Development-State-Machine-Workflow]
purpose: Design, implement, execute, and maintain meaningful automated tests so software changes are supported by behavioral evidence rather than assumptions.
use_when: The user is developing, debugging, reviewing, or maintaining software and needs a suitable test strategy, stronger regression protection, or reliable verification.
---

# Testing and Verification

## Purpose

Use this module alongside the project's development workflow to turn requirements and expected behavior into repeatable tests. The development workflow determines when verification gates apply; this module helps determine what to test, how to test it, and how to interpret the evidence.

The goal is confidence in important behavior, not a maximum number of tests or an arbitrary coverage percentage.

## 1. Inspect Before Choosing a Test Stack

Before adding or changing tests:

1. Inspect the repository structure, language, framework, package/build scripts, existing test files, CI workflows, and project maintenance/design documents.
2. Identify the current test runner and conventions. Reuse them when they are suitable; do not add a second framework without a concrete reason.
3. Determine which checks already run automatically and which are missing, unreliable, slow, or manual.
4. Read documented acceptance criteria, existing behavior, known bugs, and compatibility requirements to build a test inventory.
5. Choose the smallest practical set of tools that can verify the required behavior. Explain significant trade-offs before introducing a new dependency or major testing framework.

Never assume a command, framework, test, or runtime exists without checking the repository and environment.

## 2. Test at the Appropriate Layers

Use a risk-based testing pyramid. Most checks should be fast and focused, while broader tests cover the seams between components and the most important user flows.

### Unit tests

Test small units of behavior in isolation where isolation provides useful confidence. Cover:

- normal and boundary inputs;
- empty, malformed, missing, or invalid input where relevant;
- expected errors and failure handling;
- important state transitions and business rules;
- deterministic outputs and invariants.

Prefer tests of observable behavior over tests coupled to private implementation details. Use mocks or fakes at genuine external boundaries, not to mock away the behavior the test is supposed to verify.

### Integration tests

Test interactions between components that can fail at their boundaries, such as persistence, serialization, filesystem operations, databases, APIs, event handling, process communication, and configuration. Use realistic implementations where practical, with isolated test data and cleanup.

### End-to-end and runtime tests

Test the highest-value user journeys through the actual application boundary when the environment supports it. Examples include opening the app, creating or editing content, saving and reopening it, importing/exporting data, and handling a recoverable failure.

For desktop, mobile, media, networking, or hardware-dependent software, identify platform-specific behavior that ordinary unit tests cannot establish. Run suitable UI automation, smoke tests, packaging checks, or manual device checks as appropriate. Clearly label checks that cannot be executed in the current environment.

### Regression tests

When fixing a reproducible bug, add a test that fails for the faulty behavior and passes for the corrected behavior whenever feasible. Preserve tests for previously accepted behavior so new changes do not silently break it.

## 3. Derive Tests from Requirements

For each meaningful acceptance criterion or documented behavior, identify:

- the scenario and relevant starting state;
- the action or input;
- the expected observable outcome;
- the test layer that can verify it;
- the evidence produced by execution.

Include positive paths, edge cases, invalid input, failure recovery, and state/persistence behavior according to risk. Avoid tests that merely assert a mock was called when the actual result can be checked. Avoid duplicating many tests that prove the same thing while leaving important behavior untested.

Maintain a compact behavior-to-test map in the project's maintenance document or test inventory when it helps track gaps. Mark behavior without adequate evidence as untested or unverified, rather than silently treating it as covered.

## 4. Coverage and Test Quality

Use coverage reports as a diagnostic tool to find untested code, not as proof of correctness or the sole acceptance criterion.

- Prioritize critical behavior, complex logic, data integrity, security-sensitive paths, and known failure modes.
- Prefer meaningful assertions and tests that distinguish correct behavior from plausible incorrect behavior.
- Keep tests deterministic, isolated, understandable, and repeatable.
- Control time, randomness, environment variables, filesystem state, network dependencies, and shared state where these can cause flaky results.
- Do not weaken assertions, delete valuable tests, skip failures, or lower coverage thresholds merely to obtain a green run. If a test is invalid or obsolete, explain why and replace it with appropriate verification.
- Treat flaky tests as defects in the test system that need investigation, not as harmless noise.

A project does not need a unit test for every line. Test depth should reflect the consequences of failure and the confidence needed for release.

## 5. Execute the Quality Gate

For each implementation candidate, run the checks applicable to the repository, typically including some of:

1. formatting and linting;
2. static analysis and type checking;
3. unit tests;
4. integration tests;
5. production build and packaging;
6. end-to-end, UI, or runtime smoke tests;
7. dependency or security checks when relevant.

Discover exact commands from the project configuration and existing documentation. Run tests against the candidate being evaluated, inspect logs and failure details, fix root causes, and rerun failed checks plus affected regression tests. Run the broader relevant suite before acceptance.

Do not claim tests passed because test files exist, because code looks correct, because a build succeeded, or because a CI run tested a different commit. Record the candidate commit/version and the actual commands and results.

## 6. Continuous Integration

Where the repository has CI, inspect what it runs and whether it covers the required quality gate. Add or improve automated CI checks when appropriate to the project's size and hosting environment.

- Run fast, deterministic checks on proposed changes.
- Ensure failures are visible and do not silently become success.
- Keep platform-specific jobs where platform differences matter.
- Avoid making CI unnecessarily slow or fragile; separate quick required checks from heavier scheduled or release checks when sensible.
- Verify the workflow itself by inspecting the run result for the exact commit. A workflow file is not evidence that its jobs ran.

For a small project without CI, provide a reproducible local test command and consider CI once it will meaningfully reduce risk.

## 7. Evidence and Reporting

Report checks in distinct categories:

- **PASS:** actually executed or verified from trustworthy results for the exact candidate.
- **FAIL:** executed and did not meet the expected result.
- **BLOCKED:** could not be run due to a concrete environment, permission, dependency, or platform limitation.
- **NOT RUN:** not attempted; state why when relevant.

For significant work, preserve a concise test record in the maintenance document or latest-test record: candidate version/commit, environment, commands, results, relevant CI/log links, known gaps, and acceptance status. Do not present blocked, skipped, or unrun tests as passes.

A passing suite increases confidence but cannot prove that all defects are absent. State what was tested, what remains unverified, and whether the acceptance criteria were met. If a critical behavior remains unverified, follow the development workflow's acceptance gate rather than expanding features as if verification were complete.

## 8. Completion Checklist

Before describing a software change as verified, check:

- [ ] Relevant existing tests and acceptance criteria were inspected.
- [ ] New or changed behavior has meaningful tests at appropriate layers.
- [ ] Important edge cases and failure paths are covered according to risk.
- [ ] Bug fixes have regression tests where feasible.
- [ ] Relevant format, lint, type, test, build, and runtime checks were actually executed.
- [ ] Failures were investigated and repaired, with affected checks rerun.
- [ ] CI results, if applicable, correspond to the exact candidate.
- [ ] Passed, failed, blocked, and unrun checks are reported honestly.
- [ ] Remaining verification gaps are recorded and reflected in the acceptance decision.
