---
name: ci-cd-pipeline
type: specialized-workflow
version: "0.1.0"
purpose: Establish reproducible automated integration, verification, packaging and controlled delivery.
use_when: Setting up or improving automated builds, tests, releases or deployments for an application.
related: [Development-State-Machine-Workflow, testing-and-verification, cybersecurity-and-secure-engineering, docker-portable-deployment]
---

# CI/CD Pipeline

## Goal and scope

Make changes verifiable and deliverable without relying on undocumented manual steps. CI integrates and checks changes; continuous delivery produces a releasable candidate; continuous deployment automatically publishes accepted changes. Do not assume automatic production deployment is wanted. Choose provider and runner based on project needs, supported platforms, cost/quotas, trust and existing infrastructure. Respect Tool Use and Consent; do not invoke restricted services or create branches, tags, releases or pull requests without explicit authorization.

## Workflow

1. Inspect current repository, branch, build/test commands, dependency locks, existing workflows, accepted versions, target platforms and deployment requirements. Preserve user changes. Agree on triggers, acceptance gates, artifact destinations and whether delivery is manual or automatic. Start with the smallest useful pipeline.
2. Define reproducible stages: checkout exact revision; provision pinned toolchain; restore locked dependencies; lint/static checks where relevant; run unit/integration and representative smoke tests; build/package; verify artifacts. Use platform matrices only where meaningful. Keep local equivalents documented. Cache safely without treating cache hits as proof of correctness.
3. Add security and supply-chain controls appropriate to risk: least-privilege job permissions, isolated untrusted contributions, pinned trusted actions/dependencies, secret scanning, dependency/image scanning, SBOM and provenance where useful. Never expose deployment secrets to untrusted code or logs. Prefer short-lived scoped credentials where supported. Treat scanner findings according to documented policy, not blanket claims of security.
4. Produce versioned artifacts tied to commit, platform, checksums and build evidence. Build once and promote the same verified artifact where feasible. For containers, use immutable image digests and the Docker and Portable Deployment workflow; native packages and static builds are equally valid. Separate artifact creation from publication.
5. For authorized deployment, define environment configuration, approvals, staging/smoke checks, concurrency control, migrations, backups and rollback/recovery. Default to manual production approval unless automatic deployment is explicitly adopted. Do not assume rollback is safe for irreversible data migrations. Document last accepted version and recovery procedure.
6. Verify pipeline behavior: successful run, intentional failing test blocks later stages, artifact retrieval and representative execution, appropriate permissions and deployment gating. Test recovery in a safe environment when applicable. Inspect actual logs and results; distinguish configured, executed, passed, failed and unverified stages. Do not equate a green build with full application acceptance.
7. Record workflow paths, triggers, toolchain versions, supported targets, artifact locations, evidence, costs/limits, maintenance ownership and unresolved gaps. Update existing project records and canonical workflows rather than duplicating them.

## Deliverables

Provider-specific pipeline configuration, local reproduction commands, test and artifact evidence, release/deployment instructions, permissions and secret requirements, rollback plan and known limitations. CI can operate without Docker or deployment. CD can be added incrementally after CI is reliable.

## References

[GitHub Actions documentation](https://docs.github.com/actions), [GitLab CI/CD](https://docs.gitlab.com/ci/), [SLSA](https://slsa.dev/). These are starting references, not a mandated provider; verify current documentation and service terms before adoption.
