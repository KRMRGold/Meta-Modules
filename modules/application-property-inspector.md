---
name: application-property-inspector
type: specialized
version: "0.1.1"
related: [pafc, existing-knowledge-and-emerging-technologies, intent-and-clarity, testing-and-verification]
purpose: Guide an AI assistant in inspecting an existing application, identifying appropriate editable properties, designing a property schema, and implementing an integrated inspector suited to the application's architecture.
use_when: The user wants to add an inspector, developer panel, live configuration editor, theme editor, or structured interface for inspecting and changing selected application properties.
---

# Application Property Inspector

## Purpose

Help an AI assistant add a structured property-inspection and editing interface to an existing application. The result should feel native to the application, expose meaningful controls for its actual architecture, and modify real application settings or state through supported interfaces.

The goal is not simply to draw a panel full of inputs. The assistant must discover what is safe and useful to expose, understand where each value lives, define how it is represented, connect edits to the application, and verify that the changes have the intended effect.

This is an implementation method for adapting an inspector to an existing application. It is **not** a requirement to build a universal inspector framework or reusable cross-application library.

## 1. Understand the Intended Inspector

First establish what the user wants to inspect or change. Possible scopes include:

- **Appearance:** colors, fonts, spacing, borders, opacity, themes, and visual effects.
- **Layout:** panel sizes, positions, visibility, docking, split ratios, and responsive behavior.
- **Behavior:** feature toggles, interaction modes, shortcuts, defaults, and workflow options.
- **Configuration:** application preferences, workspace settings, project settings, and environment-specific options.
- **Content or domain properties:** properties of selected objects, nodes, tracks, layers, documents, or other application entities.
- **Diagnostics:** read-only status, counters, timing, and other useful runtime information.

These are discovery categories, not a required menu structure. Use the application's concepts and the user's intended workflow to choose useful groupings.

Determine whether the inspector should be a permanent dock, contextual side panel, settings page, floating window, developer-only panel, or another form. Prefer an existing application convention when one exists. Do not impose a Godot-like dock merely because Godot's Inspector is the reference.

If the user has not specified the scope, inspect the application and recommend a useful first slice rather than designing an all-encompassing control surface.

## 2. Inspect the Existing Application Before Designing

Read the relevant source, configuration, architecture notes, and existing UI patterns before proposing implementation details.

Identify:

- The language, framework, UI toolkit, runtime, and application architecture.
- Existing settings, theme systems, configuration files, state stores, object models, and serialization.
- How values are currently read, changed, validated, persisted, reset, and loaded.
- Existing component libraries or inspector/property-editor capabilities that could be reused.
- The natural place for the inspector in the current navigation, panel, window, and interaction model.
- Whether properties belong to the whole application, a workspace/project, a selected object, or a temporary runtime session.

Follow **Prior-Art-First Collaboration**. Search for established capabilities in the app's current stack before building custom controls. For example, a framework may already provide a settings binding system, property editor, form generator, theme tokens, or reactive state mechanism. Reuse or adapt a suitable solution when that is simpler and maintainable.

Do not infer the architecture from a framework name alone. Inspect the actual code and existing conventions.

## 3. Discover Properties: Propose Broadly, Expose Deliberately

Use source inspection and application structure to identify candidate properties. Look for:

- Existing configuration fields and settings objects.
- Theme tokens and design-system variables.
- Layout values and component properties that already support runtime updates.
- State belonging to selected domain objects.
- Repeated hard-coded values that appear to represent intended customization points.
- Existing commands or APIs that safely change application behavior.

Automatic discovery is useful for generating candidates, not for granting edit permissions. The assistant should explain why a property is a good candidate and identify its source and likely effects. The user or application maintainer decides which candidates become editable.

Use an explicit allowlist or equivalent registration mechanism for properties the inspector may modify. Do not expose every discovered variable, field, environment value, or object member automatically.

### Classify each candidate

Distinguish at least these categories:

1. **Configuration:** intended to be changed and potentially persisted.
2. **Runtime state:** currently changeable during execution but not necessarily persisted.
3. **Theme/design token:** a shared visual value that may affect many parts of the application.
4. **Read-only diagnostic:** useful to inspect but not modify.
5. **Implementation detail:** internal value that should remain hidden unless there is a specific, justified use.
6. **Immutable constant:** a value whose fixed nature is part of the implementation contract.

Do not label a value a constant merely because it is declared with a language-level constant keyword, and do not assume every hard-coded value should become a setting. Determine its actual role and intended mutability.

Never silently turn an immutable implementation invariant into a user-editable setting. If a hard-coded value appears to be a useful customization point, propose a deliberate refactor into configuration and explain the scope of its effects.

### Choose the right exposure boundary

Prefer, in order:

- Existing public settings or supported application APIs.
- Existing state-management or model update mechanisms.
- A small adapter around the existing source of truth.
- A deliberate refactor when no safe extension point exists.

Avoid direct mutation of private internals, arbitrary object traversal, reflection-based write access, or fragile selectors when the application provides a better interface.

## 4. Define a Property Schema

Before building the UI, define a compact, explicit description of each approved property. The schema should be appropriate to the application; it does not need to become a universal standard.

A useful property descriptor can include:

| Field | Purpose |
|---|---|
| `id` | Stable identifier used by the inspector and adapter. |
| `label` | Human-readable control label. |
| `description` | What the value affects, including scope or side effects. |
| `group` | Inspector section or category. |
| `type` | Data/control type, such as boolean, number, string, color, choice, vector, or structured value. |
| `default` | Reset or initial value, when meaningful. |
| `current` | Current value, supplied by the application rather than duplicated as stale inspector state. |
| `constraints` | Bounds, steps, allowed values, patterns, or other validation rules. |
| `scope` | Application, workspace, project, selected object, or runtime session. |
| `persistence` | Whether and where edits are saved. |
| `access` | Editable, read-only, or conditionally editable. |
| `apply` | Whether changes apply immediately, on confirmation, or after restart. |

Include only fields that have a real purpose. A property schema should describe the actual application's capabilities, not force every property into an elaborate generic model.

### Map types to appropriate controls

Examples include:

- Boolean → toggle or checkbox.
- Bounded number → slider, numeric input, or both.
- Unbounded or high-precision number → numeric input.
- String → text input, multiline editor, or specialized editor.
- Enumerated values → select or segmented control.
- Color → color picker with the application's supported color representation.
- Vector or dimensions → grouped numeric fields or a suitable vector editor.
- File, path, or resource reference → application-appropriate picker or validated reference control.
- Structured domain object → a contextual nested editor, not a generic text field unless that is genuinely useful.
- Diagnostic value → read-only display.

Use constraints that reflect the application domain. Do not invent arbitrary min/max values merely to make a slider convenient. Preserve units, precision, color spaces, coordinate systems, and serialization formats.

## 5. Design the Integration

Choose the smallest integration that respects the application's existing architecture.

### Direct integration

Use when the inspector and application share a runtime and can safely use the existing state/configuration interfaces. The inspector subscribes to the source of truth and dispatches supported updates.

### Adapter

Use when the inspector UI should remain separate from application-specific storage or state. Define a narrow adapter that can:

- Read a property's current value.
- Validate a proposed value.
- Apply an approved change.
- Reset to a known default when supported.
- Persist or discard changes according to the property's scope.
- Report errors and unavailable properties.

This is often the best boundary when the application has several settings sources or when the UI toolkit should not know about application internals.

### External inspector

Use only when a separate process, window, or tool is genuinely useful. The application must expose an intentional interface through an API, local IPC, message channel, or another suitable transport. Define connection lifecycle, message validation, authorization, failure handling, and version compatibility.

A separate inspector cannot safely edit an application merely by existing beside it. The application must provide a supported way to observe and apply changes.

### Keep the layers clear

A typical arrangement is:

`Application source of truth ↔ Property adapter/schema ↔ Inspector UI`

The UI renders descriptors and presents controls. The adapter owns application-specific reads, validation, writes, and persistence. The application's existing state/configuration mechanism remains authoritative.

Do not create a second settings database or duplicate state unless the application has a deliberate draft/preview workflow that requires it.

## 6. Make Editing Predictable

Define behavior for the full edit lifecycle:

1. Read the current value from the authoritative source.
2. Display the correct control and constraints.
3. Receive a proposed edit.
4. Validate it before applying.
5. Apply it through the supported application interface.
6. Reflect the resulting authoritative value in the inspector.
7. Persist it only when the property's policy requires persistence.
8. Report validation, save, or runtime errors clearly.

Consider the following where relevant:

- Live preview versus explicit Apply/Cancel.
- Reset to default and reset to inherited value.
- Undo/redo or revert.
- Dirty-state indication for unsaved changes.
- Presets or theme variants.
- External changes while the inspector is open.
- Disabled or unavailable controls when their owning context does not exist.
- Dependencies between properties and conditional visibility.
- Restart-required changes.
- Multi-selection and mixed values when editing domain objects.

Do not add every feature by default. Choose the smallest behavior set that makes edits understandable and recoverable.

Avoid feedback loops where inspector updates trigger application changes that are mistaken for new user edits. Keep subscription and update direction explicit.

## 7. Preserve Safety and Application Integrity

An inspector can become a powerful control surface. Limit it deliberately.

- Expose only approved properties; use an explicit allowlist.
- Never expose credentials, tokens, private keys, secrets, or sensitive personal data as ordinary editable properties.
- Do not provide arbitrary code execution, unrestricted file access, shell commands, or unrestricted object mutation through generic property controls.
- Validate values at the application boundary, not only in the UI.
- Enforce permissions and role restrictions in the application or adapter; hiding a control is not authorization.
- Treat imported configuration, external messages, and persisted values as untrusted input.
- Preserve invariants and reject invalid combinations of settings.
- Make broad-impact changes clear before applying them.
- Keep diagnostic and destructive operations separate from ordinary appearance or preference controls.
- Avoid exposing internal state whose modification could corrupt documents, projects, or application data.

For an inspector intended only for development, ensure it is disabled or inaccessible in production builds unless production use is explicitly intended and safely designed.

## 8. Verify the Inspector Against the Real Application

Derive checks from the approved properties and their expected behavior.

At minimum, verify as applicable:

- Every displayed property maps to the intended source of truth.
- Initial values match the application.
- Each control represents the correct type, units, constraints, and allowed values.
- Valid edits change the intended application behavior or appearance.
- Invalid edits are rejected or safely normalized.
- Read-only properties cannot be changed through the UI or adapter.
- Persistence works across restart or reload when promised.
- Reset and revert behavior restore the correct value.
- External changes are reflected without stale or conflicting UI state.
- Missing context, unavailable properties, and adapter failures are handled clearly.
- The inspector fits the application's layout, navigation, accessibility, and interaction conventions.
- Existing application behavior remains intact when the inspector is closed or disabled.

Test the adapter and schema independently where useful, then test representative end-to-end edits in the actual application runtime. Do not claim a property is editable merely because its control renders. Confirm that changing it reaches the real source of truth and produces the expected result.

Record which properties and behaviors were tested, what passed, and what remains unverified. Follow **Testing and Verification** for evidence and acceptance reporting.

## 9. Implementation Sequence

Use this adaptable sequence:

1. **Understand:** establish the inspector's intended purpose, users, scope, and UI form.
2. **Inspect:** read the application architecture and find existing settings, state, themes, and property-editing capabilities.
3. **Research:** check the framework and relevant libraries for reusable inspector or binding functionality.
4. **Discover:** identify candidate properties and classify them by role, scope, and mutability.
5. **Propose:** present a concise property inventory, explaining likely effects and any risky or ambiguous candidates.
6. **Approve:** establish the explicit set of properties that may be edited. Resolve meaningful architecture or behavior choices with the user.
7. **Specify:** define the property descriptors, constraints, source of truth, persistence policy, and adapter contract.
8. **Integrate:** build the inspector using the application's established UI patterns and the smallest suitable adapter.
9. **Verify:** test actual reads, writes, validation, persistence, failure handling, and existing behavior.
10. **Document:** update the application's canonical design or maintenance record with the accepted architecture, exposed properties, limitations, and test evidence.

For a small, low-risk inspector, combine steps and keep documentation lightweight. Do not turn the sequence into paperwork or delay a useful prototype with unnecessary abstraction.

## 10. Future Direction: Reusable Inspector Component

A standalone, cross-application inspector library is a possible future direction, not a prerequisite for using this module.

If multiple applications eventually need the same capability, compare their actual implementations and identify stable shared contracts before extracting a library. Potential shared pieces include property descriptors, generated controls, validation, grouping, and adapter interfaces. Framework-specific rendering and application-specific access should remain replaceable.

Do not build this reusable component merely because the first application needs an inspector. First validate the method against real applications and learn which parts are genuinely common.

### Related application research: SMH-Tree

[Interactive AI observability and intervention](https://github.com/KRMRGold/SMH-Tree/blob/main/Distributed-Cognitive-Architecture.md#713-interactive-ai-observability-and-intervention) is a candidate application of the inspector method to AI execution state. Explore read-only trace fields alongside deliberately editable run configuration, typed descriptors, validated adapters, scoped overrides and branch-safe changes. Historical execution records remain immutable; edits create new configurations or runs rather than rewriting provenance. The [learning roadmap](https://github.com/KRMRGold/Meta-Modules/blob/main/roadmaps/SMH-Tree-Cloud-AI-Roadmap.md) maintains the prior-art catalog. This cross-reference is not a requirement to implement a universal inspector or adopt AI-specific dependencies.

## Success Criteria

An implementation is successful when:

- The inspector serves a clear application purpose and fits its UI conventions.
- The exposed properties are deliberately selected and correctly classified.
- Every editable property has a known source of truth and supported update path.
- The schema accurately describes types, constraints, scope, and persistence.
- Changes are validated and produce the intended application behavior.
- Read-only, sensitive, and internal properties remain protected.
- The inspector does not introduce unnecessary parallel state or architecture.
- Relevant behavior has been tested in the actual application, with remaining gaps reported honestly.
