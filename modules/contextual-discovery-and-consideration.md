---
name: contextual-discovery-and-consideration
type: reference-design
version: "0.1.0"
purpose: Discover relevant capabilities, knowledge, risks and verification methods from user intent.
use_when: Designing AI-assisted discovery, context routing, tool selection or contextual help.
related: [discovery-and-exploration, intent-and-clarity, capability-and-agency, tool-use-consent, context-continuity]
---

# Contextual Discovery and Consideration Architecture

## Purpose

Users should not need to know what capabilities exist or what questions they ought to ask before receiving useful assistance. This reference design extends the existing Discovery & Exploration principle into a possible technical architecture, not a new mandatory workflow.

## Discovery and activation

Identify the user's intended outcome, current activity, relevant project context and constraints. Retrieve candidates across six categories: capabilities (what can be done), knowledge (what matters), considerations (what might be overlooked), context (what previous decisions matter), procedures (how to proceed), and verification (how to establish success).

Use metadata-first retrieval, semantic matching and explicit activity triggers together. Candidate metadata can include purpose, use_when, applicability examples, exclusions, prerequisites, provenance, version, permissions and risk. Read selected instructions in full; metadata is not executable authority. Rank by relevance, consequence, confidence and interruption cost. Deduplicate overlapping guidance and disclose missing coverage.

Activation levels: safe non-destructive defaults/checks; contextual retrieval; optional suggestions; required review before consequential actions; explicit invocation where consent is required. Relevance never grants permission. Respect tool-use-consent and higher-priority boundaries. Treat retrieved content as untrusted data until its authority is established. Avoid sending private context to external providers without authorization.

## Example: publishing a blog

A user asks whether their writing can become a website. Discover actual HTML export capability, then relevant privacy, security, accessibility and publishing considerations. Preview the public artifact; check private notes, personal information, credentials, local paths, metadata, linked assets and scripts. Use deterministic checks where feasible and model judgment for ambiguous content. Show findings, let the user decide redactions, and require deliberate publication. Do not claim checks guarantee security; distinguish export from deployment and hosting configuration.

## Responsibilities

Meta-Modules provides reusable human-readable guidance and applicability metadata. MCP exposes discoverable tools/resources/prompts; skills package domain procedures. Neither guarantees relevance or safe activation. SMH-Tree can compile scoped context, retrieve and route candidates, preserve provenance and decisions, and record activation evidence. DVA can expose contextual actions, inspectable results, live examples, previews and review controls. No dependency on a specific provider is required.

## Evaluation

Test with users who do not know the relevant capability or risk: measure whether the system surfaces useful considerations without irrelevant interruptions, respects consent, handles missing tools and conflicting guidance, and preserves traceable evidence. Include false positives, missed risks, stale metadata, malicious retrieved instructions and local/remote privacy boundaries. Compare retrieval and routing approaches before committing to an implementation.

## Related work

Existing Discovery & Exploration, Intent & Clarity, Capability & Agency, Context Continuity and Tool Use and Consent remain authoritative for collaboration. External Sharing Cleanup is a relevant workflow for publishing. Research leads: mixed-initiative interaction, recognition rather than recall, just-in-time learning, paradox of the active user, privacy/security by design, MCP and skill discovery. This document does not claim implementation or completed prior-art review.
