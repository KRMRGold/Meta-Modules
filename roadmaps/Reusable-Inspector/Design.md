---
name: reusable-inspector-design
type: reference-design
version: "0.1.0"
purpose: Preserve the exploratory architecture of a reusable cross-application customization environment.
use_when: Designing, evaluating or prototyping the reusable inspector application.
status: exploratory
---

# Reusable Inspector — Application Design

## 1. Purpose

Make application customization accessible to ordinary users without requiring knowledge of source code, APIs, internal identifiers or modding. An integration creator exposes meaningful application properties; an everyday user adjusts them through understandable controls. Game mod configuration is a useful analogy: the technical discovery and integration work should not become the user's burden.

The product is a standalone customization host and an embeddable inspector, not primarily a debugger. It should work across creative tools, games with supported mod interfaces, editors and other applications. Applications remain authoritative over their own state.

This is a living project design, not an active instruction module or an implementation claim. The existing [Application Property Inspector module](../../modules/application-property-inspector.md) remains the method for adding an inspector to an individual application. This project explores reusable infrastructure across applications.

## 2. Confirmed decisions

| Area | Decision |
|---|---|
| Delivery | Standalone host and embeddable inspector sharing a core |
| Connection | Native and external integrations; prefer native when it offers better supported access |
| Discovery | API-driven and AI-assisted |
| Registration | Automatic registration within explicit policy, not automatic write permission |
| Organization | Hybrid contextual, hierarchical, category and search views over one registry |
| Scope | Unified multi-application registry with namespaces |
| Semantic identity | Explicit mappings; similar names do not establish equivalence |
| Storage | Host-side registry/profiles plus optional application-side metadata |
| Changes | Live by default, staged batches/transactions where useful |
| Integration unit | Required declarative manifest and optional executable adapter |
| Distribution | Bundled and independently installable integrations |
| Execution | Isolated adapter processes by default |
| Compatibility | Semantic version ranges and runtime capability negotiation |
| Primary UX | Both general settings manager and contextual inspector |
| Initial exposure | Adaptive, with useful defaults and access to authorized supported properties |

The following detailed contracts, subsystem boundaries and milestones are proposals unless explicitly covered by these decisions.

## 3. Users and experience

Integration creators discover properties, establish supported access, provide constraints and metadata, and define approved write boundaries. Customization designers may improve labels, grouping, presets and composite controls. Everyday users browse, search, edit, reset and save settings without understanding the integration.

The settings manager covers application/project-wide preferences. The contextual inspector follows selected objects, tracks, layers, nodes or components. Both use the same property definitions, instances, editors, validation, profiles and history. A property can appear in multiple views without duplicating its state.

Progressive disclosure: basic, advanced, expert and hidden are proposed presentation levels, not authorization levels. Users should be able to search, pin and reorganize authorized controls. Explain unavailable, read-only, pending, restart-required and mixed-value states. Prefer controls that communicate their effect without requiring a manual. Support keyboard navigation, accessible labels, units and precision.

## 4. Architecture

```text
Settings manager | Contextual inspector | Embedded UI | Optional AI/MCP client
                             |
Customization layer: exposure, presentation, context resolution,
composite controls, presets, profiles, views
                             |
Shared core: registry, property engine, discovery, policy,
editor resolution, validation, change history
                             |
Connection layer: sessions, capabilities, permissions,
revisions, events, transactions, health
                             |
Native integrations | External adapters | Declarative connectors
                             |
Application-owned state and supported APIs
```

The core is independent of transport and application-specific rendering. UI clients share the core; adapters translate supported operations, not UI implementation. Application state and accepted values remain authoritative. Host caches must be revalidated on reconnect.

## 5. Property and context model

Separate property definitions from instances: object.transform.location describes a property; object:Cube identifies an instance. Use application namespaces and stable identifiers, context ownership, explicit relationships, provenance, schema revisions and value revisions. Model relationships as a graph with multiple navigable views, not a single rigid tree.

A descriptor includes type, constraints, units, precision, default/reset semantics, scope, persistence, access, supported operations, dependencies and provenance. Contexts may represent application, project, scene, document, track, object, component or session. A context resolver translates selection and ownership into shared queries; multi-selection shows common properties and mixed values where supported.

Semantic mappings are explicit, versioned and validated; AI may suggest mappings but cannot assume equivalence. Preserve coordinate systems, color spaces and units. Distinguish state properties from actions such as export/render/playback; actions have separate contracts and permissions.

## 6. Discovery, registration and exposure

Pipeline: observe → normalize → validate → registration policy → register → exposure evaluation → presentation → monitor.

Sources include declared metadata, supported APIs, AI-assisted source/schema analysis, user definitions and imports. Retain provenance and evidence. Session discoveries, persistent discoveries and integration definitions are distinct. Disappearing instances become unavailable.

AI may register verified candidates under policy. Uncertain candidates remain reviewable or read-only. Discovery and registration never grant write permission. Explicit approved access boundaries protect immutable invariants, secrets and sensitive state. Do not use arbitrary memory mutation, private reflection writes or unsupported internal access as a generic fallback.

The exposure engine combines deterministic rules with optional AI suggestions using context, type, constraints, descriptions, dependencies, integration hints and user preferences. It determines visibility, grouping, labels, explanations and appropriate controls. Keep technical registration separate from user-facing customization descriptors. Adaptive exposure must not silently remove user-pinned controls or change permissions; offer stable defaults and explain meaningful changes. AI is optional for ordinary editing.

Example:
```yaml
property:
  id: game.camera.fov
  type: number
  constraints: {min: 60, max: 120, step: 1}
  unit: degrees
customization:
  label: Field of view
  description: Controls how much of the world is visible.
  editor: slider
  group: Camera
  exposure: basic
```
Illustrative bounds only; actual constraints come from the application.

## 7. Customization model

Separate technical descriptors, property instances, context descriptors, customization descriptors, composite settings, presets, profiles and views.

Composite settings map one understandable control to multiple properties, e.g. a graphics-quality selector applying validated resolution and distance settings. Presets are reusable collections of values; profiles capture user choices and target mappings; views arrange controls without changing values. Define explicit mappings and mixed/custom states when underlying values diverge. AI may propose composite controls or intent-driven changes, but preview scope and validate before applying broad changes.

Profiles may support visual, performance, accessibility, creative and mod configurations. Store schema/application compatibility and mapping provenance; import as untrusted data. Preview missing, incompatible and conflicting values. Never promise portability merely because property names match.

Editor resolution maps descriptor types to host-owned controls (toggle, number, slider, choice, color, vector, resource picker, structured editor). Prefer declarative editor extensions; defer executable UI extensions until a constrained environment is justified.

## 8. Changes and persistence

Read authoritative values, validate proposed edits, apply via supported API, reflect accepted values and report errors. The app may normalize, clamp or reject values. Live edits are default for ordinary settings; staged changes support interdependent settings. Distinguish true atomic transactions from best-effort batches and do not promise rollback when unsupported.

Track revisions to reject stale writes; propagate external changes without feedback loops. Keep pending values distinct from committed values. Undo/history records user-initiated edits and attempts restoration only when supported and safe; do not imply reversal of arbitrary application side effects. Support reset, persistence scope, reconnect, unavailable contexts and explicit conflict handling.

Application owns values, native definitions and authoritative constraints. Host owns profiles, layouts, mappings, discovery records and caches. Optional app metadata supplements the registry; no competing source of truth.

## 9. Integration packages and SDK

A manifest is mandatory; executable adapter is optional. Manifest-only packages can use generic connectors. Packages declare identity, version, compatible app/contract versions, connection modes, capabilities, dependencies, permissions, contexts and properties. Requests for permission do not grant permission.

Loader: locate → parse without executing → validate → resolve compatibility/dependencies → establish trust and grants → launch → handshake → register → monitor. Failed initialization removes partial registrations; integrations can be stopped/restarted independently.

Bundled and installed packages share contracts. Separate installed package identity from running session identity. Default isolated process per integration runtime is a proposal; multi-session support must be explicit, with separate state and grants. Exact process granularity remains open.

SDK layers:
- Contract SDK: language-independent schemas, identifiers, protocol, capabilities, errors and manifests.
- Runtime SDK: lifecycle, connection, property/discovery/action providers, events and health helpers.
- Host SDK: embedding, registry, profiles, permissions, editor registration and loading.

Proposed provider interfaces: IntegrationLifecycle, ConnectionProvider, PropertyProvider (describe/get/set/validate), DiscoveryProvider (discover/explain), ActionProvider, EditorProvider and HealthProvider. Host context exposes narrow granted services, not unrestricted host internals. Start with one reference implementation; language and UI stack remain open.

## 10. Protocol and compatibility

Transport-independent contract; JSON-RPC 2.0 over stdio or local socket is a candidate, not a final selection. Separate logical control operations (lifecycle, discovery, read/write, validation, permissions, health, transactions) from events (value/context/schema updates). Initially they may share transport. Define message/session IDs, request correlation, timeouts, cancellation and bounded payloads.

Errors include unsupported, permission_denied, not_found, stale_revision, validation_failed, application_unavailable, adapter_failure and timeout.

Preflight checks package, contract, protocol, application version, runtime and dependencies. Negotiate actual capabilities at runtime. Read-only if no write; polling/manual refresh if no subscriptions; staged batches with explicit limits if no transactions; declared definitions if no discovery. Capability is not permission. Version package, SDK contract, protocol and property schema independently; document migration and breaking changes.

## 11. Security and reliability

Process isolation is not a complete sandbox. Enforce least privilege with OS-supported controls where available; mediate sensitive operations and restrict filesystem, network and process access. Separate bundled, independently installed and experimental/AI-generated trust policies. Validate all external messages and imports at boundaries. Exclude credentials and sensitive personal data from ordinary controls; avoid arbitrary code execution and unrestricted object mutation. Require deliberate authorization for write access, broad-impact actions and security-sensitive changes. AI-generated adapters need review and isolated testing before trusted use.

Keep integration failures local; enforce resource/time limits, disconnect recovery, health reporting and graceful degradation. Do not allow historical AI traces or other immutable records to be rewritten through generic controls.

## 12. Prior art and research catalog

These are discussion-derived research candidates, not freshly audited dependencies. Verify current licenses, APIs, maintenance and fit before adoption.

| Reference | Study focus |
|---|---|
| [Godot Inspector](https://docs.godotengine.org/en/stable/tutorials/editor/inspector_dock.html) | Contextual typed editing and extensibility |
| [Tweakpane](https://tweakpane.github.io/docs/) | Generated parameter controls and bindings |
| [Blender Python API](https://docs.blender.org/api/current/) | Real application property/context integration |
| [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/) | Remote inspection, events and protocol boundaries |
| [JSON-RPC](https://www.jsonrpc.org/specification) | Transport-neutral request/response contract |
| [Language Server Protocol](https://microsoft.github.io/language-server-protocol/) | Client/server separation and capability negotiation |
| [VS Code extensions](https://code.visualstudio.com/api) | Manifests, contributions and activation |
| [OpenAPI](https://spec.openapis.org/oas/latest.html) | Machine-readable API description |
| [MCP](https://modelcontextprotocol.io/) | Tool/resource discovery and optional AI clients |
| [WebExtensions](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions) | Permission and package boundaries |

Additional candidates from discussion: Gua, AIRI and Pact plugin capability proposals; exact projects/versions need verification. Compare existing property-grid libraries, schema-driven forms and settings managers before implementing controls. Reuse stable contracts where appropriate; do not combine every reference into a mandatory stack.

## 13. Proposed development roadmap

1. Validate the individual-app inspector method against real applications and identify shared needs.
2. Build a minimal vertical slice: simulated or controlled app, typed registry, one supported adapter, basic controls, authoritative reads/writes and validation.
3. Add a second real application with different contexts; demonstrate standalone and embedded reuse before generalizing SDK contracts.
4. Add context resolution, live events, revision conflicts, profiles and adaptive deterministic exposure.
5. Add package loading, capability negotiation, isolation and conformance tests.
6. Explore AI-assisted discovery, composite controls and cross-application workspaces after the deterministic baseline works.

Keep the first prototype small; no requirement for AI, cloud, marketplace or universal compatibility. Select stack, initial applications and deployment targets after prior-art comparison. A possible candidate is SMH-Tree for editable run configuration and read-only observable execution records; historical records remain immutable. No dependency or implementation commitment.

Recommended development workflow: [Development State Machine Workflow](../../workflows/Development-State-Machine-Workflow.md), current version at design drafting 1.10.0; adoption to be confirmed at implementation setup. Pair with [Testing and Verification](../../modules/testing-and-verification.md). Use independent SemVer for code/build artifacts and one canonical design document updated in place.

## 14. Acceptance and verification plan

Test descriptor validation, stable identities, namespaces, explicit mappings, editor selection, deterministic exposure, permissions, invalid writes, authoritative values, persistence/reset, external changes, stale revisions, unavailable contexts, mixed values, transaction limitations, disconnect/recovery, package compatibility, isolation and resource limits. Integration conformance tests cover lifecycle, capabilities, read/write, events, failure and shutdown. Conformance is not proof of trust or compatibility with every app.

End-to-end acceptance: an ordinary user can find and understand a meaningful setting, change the real application, see the accepted result, recover from errors and save/reload a supported profile without knowing internals. Test both UI modes against actual application runtimes. Measure task completion, time, errors and discoverability with representative users; no arbitrary success threshold adopted yet.

All implementation checks: NOT RUN — design only; no app or test harness exists in this project folder.

## 15. Open decisions and continuation

Next design target: user-created cross-application customization workspaces. Explore workspace composition, profile portability/migration, no-code customization authoring, user-controlled adaptive exposure and layout stability. Also resolve first prototype applications, stack, transport, adapter process granularity, permission UX, semantic mapping format, package trust/distribution, persistence and undo boundaries. Decide which features are genuinely shared before expanding the core.

Current state: exploratory architecture; confirmed decisions recorded in section 2, proposals elsewhere. No accepted code baseline, implementation or runtime evidence. Resume by reading this file and the existing inspector module, comparing prior art, and choosing a minimal prototype or continuing workspace design.

## Provenance

AI-curated living design from collaborative architecture discussion, 26 November 2026. Repository README, inspector module and roadmap structure were retrieved during drafting. Prior-art links are research starting points, not a fresh audit. No separate repository was created.
