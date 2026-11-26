---
name: docker-portable-deployment
type: specialized-workflow
version: "0.2.0"
purpose: Package and distribute applications with reproducible container-based setup where appropriate.
use_when: Preparing an application for portable local use, sharing, reproducible development or deployment.
related: [Development-State-Machine-Workflow, testing-and-verification, cybersecurity-and-secure-engineering, ci-cd-pipeline]
---

# Docker and Portable Deployment

## Goal and applicability

Help a recipient run an application without manually reconstructing the developer's environment. Docker packages compatible userspace dependencies, not every host capability. Do not promise universal compatibility. Inspect the application, runtime, target operating systems, CPU architectures, GUI, GPU, hardware, networking, persistence, licensing and offline requirements. Identify whether containers are suitable; native installers, portable binaries, static web builds or a hybrid containerized backend/native frontend may be better. Verify Docker Engine/Desktop or compatible runtime availability and licensing for intended recipients. Do not assume paid services are authorized.

## Workflow

1. Inspect repository, current branch, existing packaging, dependency locks, startup commands, configuration, tests and supported targets. Preserve existing changes and follow Tool Use and Consent and the development workflow. Establish observable acceptance criteria and last accepted state.
2. Choose a minimal supported base image and pin appropriate versions/digests; use lockfiles, multi-stage builds where useful, a non-root runtime user, minimal runtime dependencies and a .dockerignore. Never bake credentials, private files or development tokens into images or build arguments. Keep build context narrow. Document update strategy for pinned dependencies.
3. Define a Dockerfile and, where multiple services or persistent configuration justify it, a Compose file. Provide explicit ports, health checks, startup dependencies, resource needs, volumes and configuration examples. Bind local-only services to loopback where appropriate; do not expose internal services or grant privileged mode, host mounts or Docker socket access by default. Keep secrets outside images and source control. Document data ownership, backup, migration and recovery.
4. Build and test for intended platforms (e.g. linux/amd64 and linux/arm64 where supported). Distinguish native tests from emulation and untested platforms. Linux containers on Windows/macOS require a compatible virtualization/runtime layer; Windows containers have separate host compatibility constraints. GPU and GUI access require explicit platform-specific validation. Do not claim cross-platform support based solely on a successful build.
5. Provide a simple recipient path: prerequisites, obtain image or source, configure, start, open/use, stop, update, backup and uninstall. Prefer a single documented startup command where feasible. For offline sharing, consider an image archive with checksum and architecture labels; for online distribution, use an authorized registry and immutable version identifiers. Do not publish without permission. Include licenses and required notices.
6. Test from a clean environment or fresh runtime state: build/pull, startup, health, representative application behavior, restart, persistence, configuration errors, shutdown and update/rollback. Test the documented recipient instructions. Record actual commands, platform, image digest, outcomes and gaps; never claim tests not run.

## Adaptive environment detection and provisioning

Offer a platform-aware bootstrapper when recipient setup would otherwise require manual dependency discovery. This is optional and independent of Docker; prefer existing installers and provisioning tools before building a custom one.

- Detect locally only necessary facts: OS/version, CPU architecture, available disk and memory, required GPU/runtime capabilities, installed dependency versions and virtualization availability. Avoid collecting identifiers, personal files or transmitting machine inventory by default.
- Compare detected facts against a versioned application requirements manifest and a verified support matrix. Distinguish supported, unsupported and unknown configurations; fail clearly rather than guessing.
- Select a compatible native package, container image or hybrid distribution using declared priorities and actual available artifacts. Use CI-produced immutable artifact identifiers, checksums and signatures where available. Never download arbitrary executable URLs supplied by untrusted input.
- Present a preflight plan listing missing prerequisites, download sizes where known, sources, licensing, network requirements, privilege needs and proposed changes. Obtain explicit approval before installation or system changes. Use trusted official installers/package managers, least privilege and normal OS authorization; never bypass security controls.
- Install only missing compatible dependencies, avoid replacing shared runtimes unnecessarily, handle restart requirements, verify versions and integrity, and test application startup. Provide dry-run, manual/offline alternatives, clear failure recovery and safe retry. Track bootstrapper-owned changes for cleanup; do not remove unrelated dependencies.
- Provide a consistent launch entry point after setup. Updates should repeat compatibility and integrity checks, preserve user data and allow recovery to a known-working version where feasible.
- For unsupported hosts, explain the limitation and available alternatives. Docker cannot provision missing physical hardware or guarantee host compatibility.

### Proposed reusable requirements manifest

The following is illustrative, not a standard or an implemented contract. Define and validate a schema before using it for automated provisioning. Each supported target must map to a verified artifact and explicit dependency constraints.

```yaml
application:
  name: example-app
  version: "0.1.0"
targets:
  - os: linux
    architecture: amd64
    distribution: docker
    artifact: example-app-linux-amd64
    requirements:
      - capability: container-runtime
  - os: windows
    architecture: amd64
    distribution: native
    artifact: example-app-windows-amd64
setup:
  require_install_consent: true
  allow_offline: true
  verify_artifact_integrity: true
```

Keep machine-readable artifact metadata and dependency rules separate from platform-specific installation adapters. CI/CD should generate or validate the release artifact inventory; the bootstrapper selects from that inventory rather than inventing packages. Consider Nix, Dev Containers, WinGet, Homebrew, Ansible, Docker Buildx and native installer/updater ecosystems as prior art; verify applicability, current terms and supported platforms before adoption.

### Additional acceptance checks

Test clean supported hosts, already-installed dependencies, missing dependencies, unsupported architectures, denied consent, offline operation where promised, interrupted downloads, integrity failures, repeated setup, startup and cleanup. Record real versus simulated environments and untested targets. A successful container build is not proof of successful recipient provisioning.

## Deliverables

Dockerfile, .dockerignore, optional Compose/config example, recipient-facing quick start, supported-platform matrix, image/version identification, test evidence and known limitations. Keep native packaging if needed. Integrate CI/CD only when useful; container packaging must remain independently usable.

## References

[Docker build best practices](https://docs.docker.com/build/building/best-practices/), [Compose](https://docs.docker.com/compose/), [multi-platform builds](https://docs.docker.com/build/building/multi-platform/). Verify current documentation for selected runtime and platform before implementation.
