# Cloud Robotics Experimentation

Version: 0.1.0 | 25 November 2026 | Exploratory proposal

> Historical collaborative concept. SMH-Tree is the primary personal cloud-learning project; Spacefruit is not a dependency.

## Purpose
Explore a collaborative ML and evaluation pipeline for a farming robot, learning Google Cloud, MLOps and applied AI while producing credible portfolio evidence. Longer term, explore reusable experimentation infrastructure.

## Existing foundations
- [Spacefruit](https://github.com/kingQueue/spacefruit_robot): C++17, FreeRTOS POSIX/Linux development runtime, simulated moisture readings, mission workflows and tests. Its README says NASA cFS is not currently in the source tree.
- [PartsMapper](https://github.com/kingQueue/partsmapper): local manual parts and wiring workspace, reusable components and JSON exports; no active agent or cloud integration documented.
- [Chess the Infinity](https://github.com/KRMRGold/Chess-The-Infinity): branching game-state exploration, reported inspiration for PartsMapper.
- [SMH-Tree](https://github.com/KRMRGold/SMH-Tree): nonlinear context, orchestration and alternative paths; integration optional.

## First experiment
Predict simulated soil moisture or classify simulated plant conditions. Define target, dataset, train/test split and metrics before training. Compare a small supervised model against a simple baseline. Keep outputs offline and simulation-only; no physical actuator integration. Synthetic results do not establish real-world performance.

## Architecture
Simulation → versioned dataset → training → evaluation → model registry → experiment review.

| Technology | Purpose |
|---|---|
| Cloud Storage | Versioned datasets and artifacts |
| Vertex AI custom training | Repeatable training jobs |
| Vertex AI Experiments / Pipelines | Track and automate runs |
| Model Registry | Candidate model versions |
| BigQuery (optional) | Analyze results at scale |
| Cloud Run (optional) | Review interface or API |
| IAM / Cloud Logging | Access and failure investigation |

## Interface concept
Branch baseline experiments into alternative datasets, models or simulation configurations. Retain parent, configuration, dataset/model versions, metrics and human notes. Compare alternatives without overwriting results. Evaluate existing trackers before building a custom interface.

## Evaluation
Compare against persistence or rule-based baselines; use MAE/RMSE for regression or precision, recall and F1 for classification. Separate training and test scenarios, record seeds, dependencies and provenance. Track failures, runtime, latency and cost; report negative results. Use least-privilege access and keep credentials outside repositories. Start locally; verify cloud pricing and eligibility.

## Roadmap
1. Define useful prediction task, available data and evaluation criteria.
2. Export data, train baseline and candidate locally, reproduce evaluation with tests.
3. Learn IAM, storage, containers and Vertex AI; reproduce a bounded experiment and record costs.
4. Automate validation, training, evaluation and artifact tracking.
5. If useful, build branching navigation and comparison around real needs.
6. Publish a case study with architecture, reproducible instructions, measured results and individual contributions.

## Collaboration and career
Possible division, subject to agreement: robotics collaborator defines domain requirements, scenarios and validation; other collaborator focuses on cloud ML, orchestration and interactive review. Both contribute to architecture, testing and documentation. Relevant careers: forward deployed engineering, applied AI, creative technology, prototyping and MLOps. Claims must reflect actual contributions, independent debugging and trade-offs.

## Open decisions
Available simulation data and useful prediction targets; budget, eligibility and collaboration structure; repository location and existing experiment tools.

## Resources
- [Custom training](https://codelabs.developers.google.com/vertex_custom_training_prediction)
- [Custom training pipelines](https://codelabs.developers.google.com/vertex-pipelines-custom-model)
- [ML pipelines introduction](https://codelabs.developers.google.com/vertex-pipelines-intro)
- [MLOps architecture](https://docs.cloud.google.com/architecture/blueprints/genai-mlops-blueprint)

## Provenance
AI-curated from the November 2026 discussion and retrieved Spacefruit and PartsMapper READMEs. Full source trees not audited; resource links carried forward without fresh verification. Architecture, roles and milestones are proposals, not commitments or completed work. Meta-Modules README was subsequently retrieved under KRMRGold. This is reference material, not an active instruction module.
