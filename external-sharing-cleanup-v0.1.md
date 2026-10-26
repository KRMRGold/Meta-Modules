---
name: external-sharing-cleanup
type: specialized-workflow
version: "0.1"
purpose: Prepare a file or document to be shared with someone who lacks the author's private, project-specific, or conversational context.
use_when: The user wants to share, publish, hand off, submit, or provide a file to an outside reader and asks to remove irrelevant personal details, internal references, or context that the recipient does not need.
---

# External-Sharing Cleanup

## Core Principle

Make the material understandable and useful to its intended recipient without exposing unnecessary personal information, internal context, or unrelated project details.

Clean the artifact, not its purpose. Preserve the substance, intent, technical correctness, and useful context needed to understand or use it.

## 1. Identify the Sharing Context

Before editing, infer or establish the likely recipient and purpose from the request.

- If the intended audience or purpose would materially change what should be removed, ask one concise clarifying question.
- Otherwise, proceed using a reasonable general-audience assumption and state it briefly when helpful.
- Do not turn a simple cleanup into a long questionnaire.

## 2. Remove or Generalize Unnecessary Context

Inspect the entire artifact for information that is irrelevant to the recipient or reveals context they do not need, including:

- Personal names, identifying details, private anecdotes, or personal circumstances unrelated to the artifact's purpose.
- References to the author's other projects, repositories, internal tools, private workflows, or separate conversations.
- Internal nicknames, shorthand, unresolved notes, private file paths, local machine details, and comments meant only for the author.
- Statements such as "as discussed earlier," "see my other project," or "use the usual setup" when the recipient cannot access that context.
- Duplicated, obsolete, accidental, or distracting material.
- Private links, credentials, tokens, secrets, or other sensitive data. Never reproduce exposed secrets in the cleaned version; remove them and flag that a secret may need rotation if it appears genuine.

Prefer deleting irrelevant material or replacing it with a neutral description over adding explanations of private context.

## 3. Preserve What the Recipient Needs

Do not remove information merely because it is specific. Retain details that are necessary to interpret, evaluate, implement, or safely use the material.

- Keep essential definitions, assumptions, requirements, constraints, examples, citations, attribution, licensing, and safety information.
- Replace unexplained internal references with self-contained descriptions when the underlying information is available and relevant.
- If a necessary reference points to material the recipient cannot access, include a concise explanation or identify the missing dependency.
- Preserve uncertainty and caveats. Do not invent missing context to make the artifact appear complete.
- Keep the original voice and formatting where practical unless the user requests a different style.

## 4. Use Minimal, Traceable Changes

- Prefer the smallest changes that make the artifact suitable for its intended audience.
- Do not rewrite sound content merely to make it feel more polished.
- Do not alter technical meaning, factual claims, authorship, attribution, or legal notices as part of routine cleanup.
- If a detail may be private but its importance is unclear, generalize it or flag it for the user rather than silently deleting something consequential.
- If the user asks for cleanup only, do not add new features, arguments, sections, or design ideas.

## 5. Check the Result

Before presenting the cleaned artifact, verify:

1. It can be understood without access to unrelated projects or prior conversations.
2. Internal references, private shorthand, and irrelevant personal details have been removed or explained.
3. Essential context, dependencies, constraints, attribution, and safety information remain.
4. No unsupported facts or invented explanations were introduced.
5. The content still serves its original purpose.

When useful, provide a brief change summary that identifies categories of material removed or generalized. Do not repeat sensitive details in the summary.

## 6. Default Output

- If the user supplied a file and asks for a cleaned version, return the cleaned artifact or create the requested cleaned copy when file tools are available and the user has authorized that action.
- Keep the original intact unless the user explicitly asks to replace it.
- If direct file editing is not requested or appropriate, provide the revised content for the user to copy.
- If no specific audience is given and the content is otherwise suitable, optimize for a competent reader with no prior context about the author or their projects.

**Success criterion:** A new reader can understand and use the material for its intended purpose without receiving irrelevant personal or project context.
