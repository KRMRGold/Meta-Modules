Remaining Open Items
2.1 DSM §4.4 — "must not search for or resurrect older version-suffixed files" is still slightly ambiguous about pinned retrieval
The revised §4.4 now says:

"A deliberate historical pin must be explicit and identify the relevant Git commit SHA or tag; retrieve that historical revision from Git only when the pin or a historical question requires it. Future chats must retrieve the canonical current workflow by default and must not search for or resurrect older version-suffixed files."

This is much better than the prior version, but "must not search for or resurrect older version-suffixed files" could still be read by a literal-minded reader as forbidding the Git retrieval described in the immediately preceding sentence. The two clauses are compatible if "files" means working-tree files, but the contrast between "retrieve from Git" and "must not search for… files" would benefit from an explicit reconciliation.

Proposed refinement: Add one clause: "…must not search for or resurrect older version-suffixed working-tree files; retrieving a pinned revision from Git history by SHA or tag is the sanctioned exception."

Source: workflows/Development-State-Machine-Workflow.md §4.4.

2.2 README §1 "First-response contract" — "Discovery & Exploration applies the same recommendation-first, clarify-only-when-needed approach"
Previous review flagged this as ambiguous (does "that approach" mean recommendation-first or clarify-only-when-needed?). The rewrite now says "applies the same recommendation-first, clarify-only-when-needed approach to uncovering relevant possibilities" — which is clearer but now bundles two principles as one compound noun phrase, and reads as if Discovery & Exploration applies both. It does apply both, but they are conceptually distinct (recommendation-first is Intent & Clarity's opening move; clarify-only-when-needed is its restraint principle). Minor.

Proposed refinement: Optional — could split: "applies Intent & Clarity's recommendation-first opening and clarify-only-when-needed restraint to uncovering…" Not urgent.

Source: README.md §1.

2.3 Testing and Verification related is narrow
testing-and-verification.md related: [development-state-machine-workflow] — only one entry. But its prose says "Use this module alongside the project's development workflow" and the module is referenced by DSM §7. Given the new "prose is authoritative, related is a curated subset" rule, a single-entry related is defensible, but the prose relationship is reciprocal (DSM links to Testing; Testing links to DSM only via related and the intro). This is fine but inconsistent with the pattern used by Refinement (6 entries) and Weather Pattern (4 entries).

Observation, not a defect. Worth confirming the asymmetry is intentional rather than an oversight.

2.4 existing-knowledge-and-emerging-technologies related: [pafc] is asymmetric
PAFC's related is [existing-knowledge-and-emerging-technologies] and PAFC's prose says "continue with Existing Knowledge & Emerging Technologies." Existing Knowledge's related is [pafc] and its prose says "This module extends PAFC." Reciprocity is present. But Existing Knowledge's prose does not have a "Relationship to other modules" section — it only has the "extends PAFC" line in the Core principle. Given that PAFC now has a dedicated relationship paragraph and Existing Knowledge does not, the pattern is inconsistent.

Proposed refinement: Optional — add a short "Relationship to other modules" section to Existing Knowledge (PAFC as the lightweight default; Discovery for surfacing adjacent fields; Intent & Clarity for goal-checking). Or state that the "extends PAFC" line is sufficient and the section is not required for a specialized module. Either is fine; the current state is a mild inconsistency, not an error.

Source: modules/existing-knowledge-and-emerging-technologies.md; modules/pafc.md.

2.5 DSM §2.0 now covers non-software "candidate" but §6's "Implementation and recovery rules" still reads software-centric
§6 says "Identify and preserve the last accepted version before changing code," "Assign distinct versions to code/build candidates," "Do not mix unrequested features into a fix," and "Use actual errors and reproduction steps." These are all fine for software, and §2.0 now says to adapt stages to non-software projects. But the rules in §6 are not marked as software-specific, so a non-software adopter might read them as mandatory. §2.0's adaptation clause is one sentence; §6 is nine bullets.

Proposed refinement: One sentence at the top of §6: "These rules are written for software; adapt the version/candidate vocabulary to the non-software deliverable type identified in §2.0 (versioned candidate vs. living document)."

Source: workflows/Development-State-Machine-Workflow.md §6.

2.6 Consistency of related syntax across modules
Spot-checking:

related: [intent-and-clarity, development-state-machine-workflow, capability-and-agency] — Context Continuity

related: [existing-knowledge-and-emerging-technologies] — PAFC

related: [intent-and-clarity, discovery-and-exploration, weather-pattern, guided-inquiry, pafc, capability-and-agency] — Refinement

related: [intent-and-clarity, weather-pattern, refinement] — Guided Inquiry

related: [intent-and-clarity, discovery-and-exploration, guided-inquiry, refinement] — Weather Pattern

related: [development-state-machine-workflow] — Testing and Verification

related: [intent-and-clarity, tool-use-consent, refinement] — External Sharing Cleanup

related: [intent-and-clarity] — Intent & Clarity

related: [pafc] — Existing Knowledge

related: [context-continuity] — (implied by Intent & Clarity's related)

No related — Bratty Support, Capability & Agency, Discovery & Exploration, Tool Use and Consent

Bratty Support, Capability & Agency, Discovery & Exploration, and Tool Use and Consent all have prose relationship sections (or explicit delegation paragraphs) but no related front matter. Under the "curated subset" rule this is allowed, but it's inconsistent: Capability & Agency's "Relationship to other modules" lists 4 modules, all reasonable related candidates; Tool Use and Consent has no "Relationship" section but is cross-referenced by 6 other modules; Bratty Support is cross-referenced by README §2 and Capability & Agency.

Proposed refinement: Either (a) add related to the four modules that currently lack it (at minimum Tool Use and Consent, which is the most cross-referenced module in the repo), or (b) state in README §3 that related is optional and its absence is not a discovery gap. The current state is legal under the rule but looks like an oversight to a reader who checks all front matter.

Source: README §3; front matter of bratty-support.md, capability-and-agency.md, discovery-and-exploration.md, tool-use-consent.md.

2.7 DSM §11 Final Checklist — two overlapping bullets remain
Previous review (M5) noted §11's checklist overlaps §7's execution loop. The new §11 bullets:

"Required checks and actual results for the identified candidate are recorded as PASS, FAIL, BLOCKED, or NOT RUN."

"Manual checks were automated where practical, or explicitly marked blocked/not run with a reason."

These two are adjacent and partially redundant — the first says "recorded as PASS/FAIL/BLOCKED/NOT RUN"; the second says "marked blocked/not run with a reason." The first is the state-recording requirement; the second is the automation-attempt requirement. They can be merged or the second can be clarified to focus on "automation was attempted before marking blocked."

Proposed refinement: Merge: "Required checks and actual results are recorded as PASS, FAIL, BLOCKED, or NOT RUN; for any BLOCKED/NOT RUN, automation was attempted where practical and the blocker and minimum human action are stated."

Source: workflows/Development-State-Machine-Workflow.md §11.

2.8 Architecture §4's external links — "captured for this design discussion"
The added caveat is good: "The links above are illustrative references captured for this design discussion, not permanent dependencies or a guarantee that the linked documentation remains current." But this is a reference-design document whose snapshot date is 2026-11-06; the links point to product documentation that may not have existed or may have changed by that date. The caveat correctly disclaims currency. No action needed, but worth noting that the examples themselves are illustrative of a pattern, and the pattern (metadata-driven progressive disclosure) is stable even if the specific URLs are not. The document does not claim otherwise. Confirming this is adequately handled.

No change needed. Flagging for completeness.

2.9 Snapshot inventory vs. source index
The consolidated reference's inventory says "16 source documents total." The source index lists 16 (1 README + 12 modules + 2 workflows + 1 architecture). The "Additional source index" section begins at item 9, which is correct (items 1–8 are listed in the first index). Reconciles.

No issue.

2.10 Tool Use and Consent related absence (subset of 2.6)
tool-use-consent.md has no related field but is the most cross-referenced module in the repository (referenced by README §1, §5, §7; by Capability & Agency; by Discovery; by PAFC; by External Sharing Cleanup; by Bratty Support). If any module should have related for discovery, it is this one. Under the "prose is authoritative" rule, its lack of a "Relationship to other modules" section is also notable.

Proposed refinement: Add a short "Relationship to other modules" section (it is the hard boundary; other modules defer to it) and consider a minimal related: [intent-and-clarity, discovery-and-exploration, capability-and-agency, external-sharing-cleanup]. Or state explicitly that Tool Use and Consent is intentionally relationship-light because it is a hard boundary that other modules must defer to, not a discovery target.

Source: modules/tool-use-consent.md.

3. Minor / Editorial (carryover and new)
M1. README §1 "Defaults for substantial projects" paragraph is long (one paragraph covering living-document rule, SemVer, workflow adoption, provenance, current-canonical default, independent versions, scaling, context continuity, and software pairing). It is readable but dense. A bullet list would improve scannability. Optional.

M2. DSM §4.3's new research-report example is good, but it sits inside the paragraph that begins "A repository commit provides document revision history. Keep document filenames stable…" — the transition from code example to document example to living-document filename rule is three topics in one paragraph. Consider splitting.

M3. context-continuity.md "Relationship to other modules" says "These relationships guide discovery; they do not require automatic activation." Good, consistent with README §3's related rule.

M4. intent-and-clarity.md related: [context-continuity] is one entry; its prose "Context gaps" section points to Context Continuity. Consistent.

M5. Architecture §5 table row for related now says "Add only when it improves navigation; it is a non-binding discovery hint, not a dependency or activation graph" — good. The row for depends_on says "Use sparingly; avoid creating a complicated dependency graph." Since no module currently uses depends_on, and the new README §3/§4 rule treats prose as authoritative, depends_on is effectively unused. Consider whether it should be removed from the schema or kept as a future option. (Minor — keeping it costs nothing.)

4. Proposed Refinements vs. Adopted Rules
Adopted (present in this snapshot): all "Resolved" items in §1, the precedence list, the related-as-subset rule, the non-software candidate clarification, the External Sharing Cleanup cross-reference in Tool Use and Consent, the architecture body/front-matter version alignment.

Proposed (not adopted, from this review): §2.1 (Git retrieval wording), §2.2 (First-response contract split — optional), §2.3 (Testing related asymmetry — observation), §2.4 (Existing Knowledge relationship section — optional), §2.5 (§6 software-specific note), §2.6 / §2.10 (related consistency; Tool Use and Consent relationship section), §2.7 (§11 bullet merge).

No source files modified. This is review-only.
