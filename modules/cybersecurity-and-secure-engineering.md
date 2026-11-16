---
name: cybersecurity-and-secure-engineering
type: specialized
version: "0.1.0"
related: [code-review-and-change-assurance, sandboxing-and-safe-execution, testing-and-verification, tool-use-consent]
purpose: Apply explicit, risk-based cybersecurity practices to software architecture, implementation, operations, dependencies, data handling, and incident response.
use_when: Designing, building, reviewing, deploying, or maintaining software that stores data, accepts input, communicates over a network, runs code, integrates services, manages identity, or exposes user-controlled functionality.
---

# Cybersecurity and Secure Engineering

## Purpose and boundaries

Treat security as a property of the whole system and its lifecycle, not as a final scan or a single feature. Identify what must be protected, who or what could affect it, the paths through which impact could occur, and the controls that reduce the risk.

This module is the broad security-engineering guide:

- Use **Sandboxing and Safe Execution** for execution isolation, command permissions, and containment.
- Use **Code Review and Change Assurance** for structured review of candidate changes and findings.
- Use **Testing and Verification** for test design, execution, and evidence.
- Use **Tool Use and Consent Boundaries** for user authorization and tool-use restrictions.

Do not duplicate those procedures here. This module identifies the security concerns that the architecture, implementation, review, and tests must address.

Security is risk-based. Do not claim a system is secure because it uses encryption, passes a scanner, runs in a container, or has no known findings. State the scope, controls, evidence, assumptions, and remaining risks.

## 1. Establish the security context

Before proposing controls, establish:

1. **Assets:** data, credentials, accounts, source code, model context, services, devices, availability, and user trust that need protection.
2. **Actors:** legitimate users, administrators, services, agents, dependencies, external providers, and untrusted or compromised actors.
3. **Trust boundaries:** where data, identity, authority, or execution crosses between users, processes, machines, tenants, providers, or privilege levels.
4. **Entry points:** user interfaces, APIs, imports, files, URLs, IPC, plugins, model outputs, webhooks, update channels, and administrative functions.
5. **Security objectives:** confidentiality, integrity, availability, authenticity, accountability, privacy, and recoverability as applicable.
6. **Consequences:** what unauthorized access, modification, disclosure, disruption, or misuse would mean.
7. **Constraints:** platform, deployment model, offline/online operation, user capabilities, regulatory obligations, and realistic maintenance capacity.

Do not assume an application is low-risk because it is local-first, single-user, experimental, or not publicly deployed. Local software can still expose data through plugins, dependencies, child processes, network listeners, logs, backups, or a compromised account.

## 2. Threat modelling and attack-surface analysis

For meaningful features or architectural changes, perform a proportionate threat model before implementation.

- Draw or describe the important components, data flows, trust boundaries, and privileged operations.
- Identify what an attacker or compromised component could control.
- Consider misuse and failure scenarios, not only intended user flows.
- Examine threats involving unauthorized access, privilege escalation, data disclosure or tampering, injection, insecure deserialization, path traversal, request forgery, denial of service, dependency compromise, supply-chain tampering, and unsafe update mechanisms where relevant.
- Consider insider mistakes, accidental exposure, malicious or malformed files, prompt-injected content, compromised model/tool output, and confused-deputy behavior in agentic systems.
- Prioritize threats by likelihood, impact, exposure, and existing mitigations. Do not present speculative scenarios as confirmed vulnerabilities.

A lightweight threat record should capture assets, trust boundaries, important threats, controls, assumptions, and unresolved risks. Scale detail to the consequences of failure; avoid producing a ceremonial threat-model document for trivial changes.

## 3. Identity, authentication, and authorization

Treat identity and permission as separate questions:

- **Authentication:** who or what is making the request?
- **Authorization:** is that identity allowed to perform this exact action on this exact resource in this context?

Apply these principles:

- Deny by default when access is not explicitly granted.
- Enforce authorization on the trusted server or service boundary, not only in the user interface.
- Check ownership and scope for every resource access; do not rely on an ID being difficult to guess.
- Apply least privilege to users, services, agents, plugins, API tokens, and background processes.
- Separate ordinary use from administrative and destructive operations.
- Use secure session handling, expiration, revocation, and reauthentication where appropriate.
- Avoid shared, hard-coded, default, or long-lived credentials.
- Protect against privilege escalation, insecure direct object references, confused-deputy behavior, and cross-tenant or cross-project data leakage.
- Record important permission decisions without logging credentials or unnecessary personal data.

For local applications, validate local IPC and loopback API boundaries. A service bound to localhost is not automatically private from every local process or browser-origin attack. Use appropriate authentication, origin protections, and narrowly scoped interfaces.

## 4. Input, output, and data-flow security

Treat all data crossing a trust boundary as untrusted until validated for its intended use. This includes user input, imported documents, filenames, environment variables, network responses, database content, model output, plugin output, and inter-agent messages.

- Validate types, structure, size, encoding, allowed values, and semantic constraints at the receiving boundary.
- Prefer allowlists and strict schemas over fragile denylist filtering.
- Use parameterized database queries and safe APIs rather than constructing executable query strings.
- Apply context-appropriate output encoding when rendering HTML, shell arguments, SQL, URLs, logs, or other interpreted formats.
- Avoid evaluating generated code, expressions, templates, or serialized objects unless the behavior is necessary, reviewed, and constrained.
- Defend against path traversal, unsafe archive extraction, symbolic-link escapes, unsafe file uploads, and unexpected file types.
- Limit request sizes, recursion, parsing depth, decompression, concurrency, and execution time to reduce resource-exhaustion risks.
- Validate model- or agent-generated structured output before it can trigger state changes or privileged actions.
- Keep data provenance where it matters: distinguish user-provided facts, imported material, model-generated suggestions, and verified system state.

Sanitization is context-specific. Do not treat one generic cleaning function as a universal defense.

## 5. Secrets, cryptography, and sensitive data

### Secrets

- Never commit credentials, tokens, private keys, recovery codes, or production secrets to source control.
- Keep secrets out of prompts, model context, renderer code, logs, crash reports, screenshots, test fixtures, and generated documentation.
- Prefer operating-system secret stores or an established secret manager over custom encryption schemes.
- Scope credentials to the minimum permissions and lifetime needed; support rotation and revocation.
- Do not expose a secret to an agent, plugin, child process, or remote provider merely because it may be useful.
- If a secret may have been exposed, treat it as compromised: stop further disclosure, revoke or rotate it, and investigate where it was used.

### Cryptography

- Use established, maintained cryptographic libraries and protocols.
- Do not invent algorithms, key derivation, random-number generation, or encryption formats.
- Use authenticated encryption and appropriate key management when encryption at rest is required.
- Protect data in transit with correctly configured modern transport security when traffic leaves a trusted local boundary.
- Understand what encryption does not protect: unlocked devices, compromised processes, exposed keys, metadata, or data already decrypted for use.
- Document key ownership, storage, rotation, backup, recovery, and failure behavior.

### Data minimization and privacy

- Collect and retain only data needed for a defined purpose.
- Separate data by user, project, workspace, conversation, and other relevant scope.
- Apply access filtering before retrieval, context compilation, export, or remote transmission.
- Make external data flows visible and require the appropriate explicit authorization.
- Define retention, deletion, backup, export, and recovery behavior.
- Avoid placing sensitive data in diagnostics or telemetry by default.
- Use synthetic or minimized data for tests and examples.

## 6. Application and platform security

Inspect the actual platform and architecture rather than applying web-only assumptions to every application.

Where relevant, review:

- Browser and desktop boundaries: content security policy, context isolation, sandbox settings, preload/IPC exposure, navigation restrictions, permission prompts, and safe handling of external links.
- Backend services: bind addresses, authentication, authorization, request limits, error handling, and service lifecycle.
- Databases: file permissions, encryption needs, query safety, migrations, backup integrity, and scope enforcement.
- Filesystem access: allowed roots, canonical path checks, symlink behavior, atomic writes, temporary files, and safe cleanup.
- Network access: outbound destinations, DNS and redirect behavior, TLS validation, SSRF exposure, and unexpected listeners.
- APIs: authentication, per-resource authorization, schema validation, rate limits, replay/idempotency, and safe error responses.
- Browser-facing features: origin checks, CSRF defenses where cookie-based authentication applies, XSS prevention, secure cookies, and clickjacking protections where relevant.
- Updates and packaging: artifact provenance, signatures where available, update-channel integrity, dependency pinning, and rollback/recovery.
- Plugins and integrations: permission scope, data disclosure, execution authority, and isolation between extensions.

Do not copy a checklist blindly. Mark controls not applicable with a brief reason when the system boundary makes them irrelevant.

## 7. Dependencies and software supply chain

Treat dependencies, build tools, CI actions, package registries, generated artifacts, and update channels as part of the system's attack surface.

- Prefer maintained dependencies with clear provenance and a reason for inclusion.
- Pin or lock versions where reproducibility and supply-chain risk justify it.
- Review new dependencies, transitive impact, install scripts, native binaries, and license/maintenance status.
- Monitor known vulnerabilities using suitable ecosystem tools; verify whether findings affect the versions and features actually used.
- Update vulnerable dependencies deliberately and test compatibility.
- Pin CI actions or otherwise control their update process where practical.
- Give CI jobs only the permissions they need; avoid exposing write tokens or secrets to untrusted pull-request code.
- Protect release artifacts and signing credentials.
- Generate a software bill of materials when the project's risk, distribution, or operational requirements justify it.
- Treat build output as untrusted until the build and provenance checks are complete.

A clean dependency scan is evidence about the databases and packages checked at that time; it is not a guarantee that dependencies are safe.

## 8. Secure development and verification

Integrate security into design, implementation, review, testing, and release rather than treating it as a final gate.

For security-relevant changes:

1. Identify assets, trust boundaries, and plausible threats.
2. Define the security properties and negative cases that must hold.
3. Implement controls at the authoritative boundary.
4. Review the diff and affected call paths.
5. Test both allowed and denied behavior, including malformed input, wrong scope, missing credentials, expired or revoked access, and failure paths as relevant.
6. Run suitable static analysis, dependency checks, secret scanning, and dynamic testing when available and proportionate.
7. Inspect the exact candidate's CI evidence and record checks that could not be run.
8. Reassess residual risk before acceptance.

Do not use scanners as a substitute for architecture review or tests. Do not weaken checks, suppress findings, or label a vulnerability fixed without verifying the correction and relevant regression behavior.

For web applications and services, use the OWASP Application Security Verification Standard (ASVS) as a source of concrete technical requirements when appropriate. For secure development lifecycle practices, consult the NIST Secure Software Development Framework (SSDF). Use the current stable or published versions and identify the exact version when citing a requirement; do not silently treat a draft as a final standard.

## 9. Vulnerability handling and incident response

When a possible vulnerability or security incident is found:

1. Preserve the evidence and identify the affected versions, assets, and trust boundaries.
2. Distinguish confirmed impact from plausible exposure and unknowns.
3. Contain ongoing exposure using the least disruptive safe action.
4. Revoke or rotate exposed credentials and tokens when applicable.
5. Assess affected data, users, systems, dependencies, and downstream projects.
6. Prioritize remediation by severity and exploitability, not by cosmetic convenience.
7. Add regression tests or controls that prevent recurrence where practical.
8. Record the fix, affected versions, verification evidence, and remaining risk.
9. Communicate material impact clearly to the responsible owner and affected parties through appropriate channels.

Do not erase logs or overwrite the only evidence while investigating. Do not publish sensitive exploit details, credentials, or private user data in an issue, chat, or public report.

## 10. Findings, exceptions, and security claims

For each meaningful finding, record:

- affected component and version/commit;
- threat or violated security property;
- severity and rationale;
- evidence and reproduction conditions at a safe, non-destructive level;
- impact and exposure;
- recommended mitigation;
- owner or next action;
- disposition and verification result.

Use explicit statuses such as **CONFIRMED**, **POTENTIAL**, **NOT REPRODUCED**, **MITIGATED**, **ACCEPTED RISK**, and **UNRESOLVED**. Do not turn absence of evidence into evidence of absence.

Any exception to a security control should identify the reason, affected scope, compensating control, owner, and review point. A convenience exception must not silently become a permanent default.

Avoid blanket claims such as "fully secure", "unhackable", or "no vulnerabilities". State exactly what was assessed and what remains outside the assessment.

## 11. Practical security review checklist

Use only the checks relevant to the system and feature:

- [ ] Assets, actors, entry points, and trust boundaries are identified.
- [ ] Important threats and abuse cases were considered.
- [ ] Authentication is distinct from authorization.
- [ ] Access is enforced at trusted boundaries and scoped to the requested resource.
- [ ] Untrusted inputs and generated outputs are validated for their use.
- [ ] Secrets and sensitive data are not exposed to unnecessary components or services.
- [ ] Cryptography and key management use established implementations.
- [ ] Data storage, export, backup, deletion, and remote transmission respect privacy and scope.
- [ ] Network, filesystem, process, IPC, and plugin boundaries are appropriate.
- [ ] Dependencies, build actions, and update channels have reasonable provenance controls.
- [ ] Security-relevant negative cases and regressions are tested.
- [ ] Review findings and scanner results have been triaged rather than blindly accepted.
- [ ] Residual risks, exceptions, and unverified controls are recorded.
- [ ] Incident and recovery actions are understood for the system's risk level.

## References

- OWASP Application Security Verification Standard (ASVS): https://asvs.owasp.org/
- OWASP ASVS source and releases: https://github.com/OWASP/ASVS
- NIST SP 800-218, Secure Software Development Framework (SSDF): https://csrc.nist.gov/pubs/sp/800/218/final
- NIST SSDF project and published updates: https://csrc.nist.gov/Projects/ssdf

These references are starting points, not a claim that every requirement applies to every project. Verify the current edition before using version-specific requirement identifiers.
