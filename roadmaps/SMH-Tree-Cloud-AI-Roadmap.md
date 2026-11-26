# SMH-Tree — Cloud AI Experimentation & Learning Roadmap

Version: 0.1.0 | 25 November 2026 | Exploratory proposal

## Purpose
Use SMH-Tree as the primary research environment for Google Cloud, applied AI engineering, model evaluation and MLOps. Build reusable experimentation infrastructure around genuine application problems rather than disconnected résumé tutorials. SMH-Tree is a branching AI conversation application with local model integration and ongoing memory, context and routing work. Spacefruit is not a dependency; independent collaboration remains possible.

## Proposed architecture

| Layer | Responsibility |
|---|---|
| SMH-Tree | Conversation branches, task cases, context configurations, human feedback |
| Experiment orchestration | Versioned datasets, model configurations, repeatable runs, execution adapters |
| Local execution | Python, Ollama, Qwen; optional MLflow and containers |
| Google Cloud execution | Cloud Storage artifacts, Vertex AI experiments/custom training, Cloud Run batch or service workloads |
| Evaluation | Task success, retrieval accuracy, instruction adherence, latency, tokens, cost |
| Experiment history | Compare runs, preserve lineage, inspect failures, reproduce results |

Keep ordinary local chat usable without cloud access. Cloud execution is optional.

## Research directions

| Area | Research question |
|---|---|
| Context engineering / RAG | Which retrieval strategy preserves relevant information and improves task success? |
| Memory compression | How much context can be reduced before important details are lost? |
| Model routing | When does a specialist outperform a general model accounting for latency and cost? |
| Knowledge distillation | Can a larger teacher improve a smaller local model on a defined task? |
| MCP / tool calling | How reliably are tools selected and invoked with valid arguments? |
| Instruction adherence | Do models consistently follow versioned Meta-Modules instructions? |
| Precision editing | Can requested changes be made without unrelated modifications? |
| Branching context | Does nonlinear history improve task completion or recovery? |
| Human-AI interaction | Do visual annotations or direct manipulation improve communication of intent? |

## First experiment: context retrieval
Create a small versioned dataset of synthetic conversations and tasks with known relevant facts. Compare full context, retrieval, summarization and hybrid retrieval with the same model and tasks. Hold out test cases from tuning. Record correct answers, missed facts, irrelevant retrieval, token usage, latency and cost. Use deterministic checks where possible and human review for ambiguous cases. Start locally and reproduce a selected run in Google Cloud only after the benchmark is repeatable. No performance results are claimed.

## Development and learning roadmap

| Phase | Deliverable / evidence |
|---|---|
| 1 — Local benchmark | Python evaluation runner, fixed dataset, baseline, tests, reproducible results |
| 2 — Experiment tracking | Run manifests, model/dataset versions, metrics, logs, comparable artifacts |
| 3 — Cloud foundations | Learn IAM, storage, containers and billing controls; reproduce one bounded run |
| 4 — Cloud pipeline | Automate preparation, execution and evaluation; document failures and reproducibility |
| 5 — Training | Train or distill a small model only when benchmarks identify a meaningful need; compare with unchanged baseline |
| 6 — Interface and portfolio | Optional experiment lineage and comparison interface; publish measured case studies |

## Cost, privacy and scope
Develop locally first. Verify current cloud pricing and eligibility before running jobs. Set budgets and alerts, use short-lived resources and remove unused endpoints. Alerts are not spending caps. Use synthetic or explicitly approved datasets; exclude private conversations, secrets and credentials from cloud uploads.

## Career relevance
Demonstrate applied AI, data engineering, cloud infrastructure, MLOps, automated evaluation, reproducible research and human-AI interface design. Each case study should explain the problem, architecture, personal contributions versus AI assistance, baseline, measured results, limitations and lessons learned.

## References
- [SMH-Tree](https://github.com/KRMRGold/SMH-Tree)
- [Vertex AI](https://cloud.google.com/vertex-ai)
- [Pricing](https://cloud.google.com/vertex-ai/pricing)
- [MLflow](https://mlflow.org/)

## Provenance
AI-curated proposal based on prior discussions, not a fresh source audit. Service availability and prices have not been rechecked. Meta-Modules README was subsequently retrieved under KRMRGold. No cloud jobs or implementation changes are claimed. This is reference material, not an active instruction module.
