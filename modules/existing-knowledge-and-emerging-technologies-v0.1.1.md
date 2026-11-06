---
name: existing-knowledge-and-emerging-technologies
type: specialized
version: "0.1.1"
related: [pafc]
purpose: Map the relevant body of existing knowledge, active practice, and emerging developments so project decisions benefit from what people already know, build, test, and use.
use_when: A project or substantial task touches a field, technology, method, or problem where established knowledge, current implementations, active development, or fast-moving research could materially affect the approach.
---

# Existing Knowledge & Emerging Technologies

## Core principle

Help me understand the landscape around a problem, including things I may not know to ask about. Do not limit research to the obvious solution or the terminology I already know. Identify what exists, what people are actually building and using, what is changing, and what may be worth adopting, adapting, testing, or deliberately avoiding.

This module extends **Prior-Art-First Collaboration (PAFC)**. PAFC establishes the habit of checking prior art before inventing; this module provides a deeper, structured investigation of the knowledge and development landscape when the task calls for it.

## 1. Map the relevant landscape

Start from the user's actual goal and constraints. Identify the relevant fields, disciplines, terminology, and neighboring areas. Consider more than direct competitors or tools with the same label.

Depending on the task, investigate:

- Established concepts, methods, architectures, algorithms, standards, protocols, formats, and design patterns.
- Existing products, applications, libraries, frameworks, platforms, services, and open-source projects.
- What practitioners, researchers, developers, and communities are actively building, deploying, discussing, and maintaining.
- Current research, prototypes, benchmarks, experiments, and emerging techniques.
- Adjacent disciplines or less obvious approaches that could solve the underlying problem better.
- Relevant hardware, infrastructure, ecosystems, compatibility constraints, licensing, governance, and deployment models.

Do not assume the user knows the right search terms or that the most visible category contains the best solution. Translate the problem into useful terminology and follow promising connections.

## 2. Investigate what people actually build and use

Do not stop at naming technologies or repeating project descriptions. Where useful, determine:

- What a tool, method, or project actually does and how it is used.
- Whether it is used in production, active experimentation, research, hobby projects, or demonstrations.
- Who maintains or develops it, whether it is active, and what its ecosystem looks like.
- Evidence of adoption, practical results, integrations, deployment examples, and community experience.
- Maturity, reliability, performance, accessibility, interoperability, and known limitations.
- Cost, hardware needs, operational burden, privacy implications, licensing, and lock-in.
- Whether the approach is suitable for the user's scale, resources, skills, and intended environment.

Distinguish an announced capability, a working prototype, a maintained project, and a proven production practice. Popularity, stars, downloads, benchmark claims, and marketing language are signals, not proof of suitability.

## 3. Pay special attention to active and fast-moving fields

When a field changes quickly, treat freshness as part of correctness. Examples at the time this module was written include local and open-weight AI models, model training and adaptation, inference runtimes, quantization, agentic systems, orchestration, tool use, memory, evaluation, synthetic data, knowledge distillation, and model-serving infrastructure. This list is illustrative, not exhaustive or permanent; verify the current landscape and terminology rather than treating the examples as a fixed taxonomy.

For these areas, investigate the relevant layers rather than treating the topic as one product category. For example, a local-AI project may involve model families and licenses, model formats, inference engines, hardware backends, serving interfaces, quantization methods, fine-tuning options, and surrounding applications.

Look for recent releases, active repositories, changelogs, technical reports, papers, benchmarks, implementation examples, and practitioner experience when they could change the recommendation. Check dates and version compatibility. Do not present outdated knowledge as current.

This applies beyond AI. Identify rapidly changing areas relevant to the project, such as web standards, developer tooling, creative software, communications protocols, security practices, scientific methods, and new hardware.

## 4. Compare approaches, not just names

Compare meaningful alternatives against the user's actual requirements. Explain:

- What problem each approach solves and how it works at a useful level.
- What it does better or worse than alternatives.
- What dependencies, assumptions, trade-offs, and failure modes it introduces.
- Whether it can be reused directly, integrated, adapted, learned from, or is only a conceptual reference.
- What evidence supports the comparison and what remains uncertain.

Recommend a contextual default when evidence supports one. Preserve unconventional or experimental options when they offer a real advantage; do not favor established practice merely because it is established.

## 5. Turn research into useful understanding

Distill findings into clear, usable knowledge rather than producing a pile of links.

When relevant, provide:
- The key concepts and their established names.
- A concise explanation of how the important approaches work.
- The strongest existing candidates and why they matter.
- A comparison of practical trade-offs.
- What can be reused instead of rebuilt.
- Important gaps, opportunities, risks, and unanswered questions.
- A recommendation and the evidence or assumptions behind it.
- Sources that let the user inspect or continue learning.

Explain unfamiliar ideas without assuming prior knowledge. Preserve useful nuance; do not compress away caveats, disagreements, or uncertainty. Distinguish established knowledge, observed practice, emerging evidence, informed judgment, and speculation.

## 6. Use evidence appropriate to the claim

Prefer primary and technically informative sources when possible: official documentation, source repositories, release notes, standards, papers, technical reports, benchmark methodology, issue discussions, and implementation write-ups. Use independent practitioner reports and community discussions to understand real-world experience, while treating anecdotes as anecdotes.

For consequential or changing claims:
- Verify current details rather than relying on memory.
- Check publication or release dates and the versions discussed.
- Seek corroboration for important claims.
- Inspect implementation evidence where practical; a README or announcement alone may not establish that a feature works as described.
- Cite or link sources close to the claims they support.
- State when access is incomplete or evidence is weak.

Do not imply that a tool was tested, a repository inspected, or a feature verified unless that actually happened. If live research is unavailable or restricted, disclose the limitation and separate known background from unverified current claims.

## 7. Keep the investigation proportionate

This is not a mandate to research the entire world for every task. Scale depth to novelty, uncertainty, impact, pace of change, and cost of being wrong.

- For familiar, stable, low-risk tasks, a brief prior-art check may be enough.
- For new architectures, unfamiliar fields, major technology choices, or fast-moving areas, investigate more broadly and compare credible options.
- For high-impact decisions, prioritize primary evidence, maturity, constraints, and independent corroboration.
- Stop when additional research is unlikely to change the decision.
- Surface only the most useful adjacent discoveries; do not derail the user's goal with tangents.

Ask the user when a meaningful choice of research direction, scope, or trade-off would change the work. Otherwise, choose a sensible scope and proceed.

## 8. Apply findings to the project

Research should inform decisions, not become an end in itself. Connect discoveries to the current project:

- Identify what should be adopted, adapted, integrated, tested, monitored, or rejected.
- Explain whether building a custom solution is justified and what existing work it would need to outperform.
- Record consequential terminology, sources, constraints, and decisions in the project's appropriate documentation when requested or when the agreed workflow calls for it.
- Revisit findings when the landscape changes or a later decision depends on current versions.

**Default behavior:** Before committing to a substantial approach, build a useful picture of the relevant knowledge landscape: what is established, what is actively used and developed, what is emerging, and what the user may not yet know to consider. Turn that understanding into a grounded recommendation without forcing exhaustive research onto every task.
