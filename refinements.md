# Meta-Modules Refinement Record

## Status

The review in this document records the refinements adopted into the current Meta-Modules system. The modular source files remain the working source of truth. This record is a concise decision log, not a second copy of the modules.

## Adopted decisions

- Tool-use restrictions, first-message disclosure, and instruction receipts have one canonical source: `modules/tool-use-consent.md`.
- Instruction precedence is explicit in `README.md`.
- Chat-specific working agreements are proportionate: inline for simple requests, persistent only when continuity and complexity justify them.
- The README is the sole authority for the metadata type vocabulary.
- `related` metadata is a non-binding discovery hint, not an activation or dependency graph.
- PAFC points to deeper existing-knowledge research; specialized methods and workflows are discoverable through repository metadata.
- Context Continuity remains a separate module, linked from Intent & Clarity.
- Bratty Support focuses on tone; general collaboration principles remain in the foundational modules.
- Fast-moving technology examples and external documentation references are explicitly treated as time-sensitive.
- Testing transitions distinguish executed checks from blocked or unrun checks.

## Document storage and version policy

Keep **one current file per document** at a stable, descriptive path. Update it in place. Do not create version-suffixed duplicates, backup copies, or parallel historical documents. Git history preserves prior revisions.

This policy applies to the README, modules, workflows, architecture notes, refinement records, consolidated references, and project documentation. Internal version metadata may be retained where useful, but it does not justify a second file. Code/build artifacts may keep their own version identities where the project requires them.

## Current source locations

- [README](README.md)
- [Modules](modules/)
- [Workflows](workflows/)
- [Architecture reference](architecture/Future-Workflow-System-and-Metadata-Notes.md)
- [Development workflow](workflows/Development-State-Machine-Workflow.md)
- [Consolidated reference](Meta-Modules-Complete-Reference.md)

## Verification principle

When changing the system, inspect the current repository tree and current canonical files. Do not assume old versioned filenames remain valid. Verify links, current content, and repository inventory after changes.
