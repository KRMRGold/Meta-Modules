---
name: Reinventing the Wheel
type: reference-design
version: "0.1.0"
purpose: Curated research into humane, malleable, expressive and AI-assisted computing.
use_when: Exploring prior art for human-computer interaction, software environments and tools for thought.
---

# Reinventing the Wheel

## Purpose

A living research collection about how people interact with computers, express ideas, discover functionality and shape their own tools. Many seemingly new ideas have substantial histories. The goal is to understand those histories, learn from working systems and their limitations, and discover opportunities rather than assume everything needs to be reinvented.

This collection is curated and summarized with AI in collaboration with the user. It is a starting point for independent exploration, including with another AI. Original sources remain authoritative. Descriptions below are preliminary research notes, not a completed literature review; links and current availability have not all been independently checked.

## Humane interaction and interface design

- Jef Raskin, [The Humane Interface](https://en.wikipedia.org/wiki/The_Humane_Interface) (2000), and Archy: habit formation, cognitive friction, modes, monotony of design and document-centered interaction. Investigate the trade-off between one method per atomic task and accessible alternative inputs.
- [Laws of UX](https://lawsofux.com/) — Jon Yablonski: interaction psychology and practical heuristics.
- Jakob Nielsen, [Ten Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/): recognition rather than recall, feedback, consistency, recovery and user control.
- John M. Carroll and Mary Beth Rosson, Paradox of the Active User (1987): users prioritize accomplishing tasks over learning software.
- Christopher Alexander et al., A Pattern Language (1977): inhabitable environments and composable spatial patterns; investigate transfer to interfaces rather than assume equivalence.
- [Material Design 3](https://m3.material.io/) and [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/): design conventions and visual systems. Distinguish documentation from an actual composition environment.

## Computing as a medium for thought

- [Dynamicland](https://dynamicland.org/) and [CDG Research Agenda (2014)](https://dynamicland.org/2014/CDG_Research_Agenda.pdf): computing as an expressive, communal and explorable medium.
- Bret Victor, [Media for Thinking the Unthinkable](https://worrydream.com/MediaForThinkingTheUnthinkable/): interactive representations for reasoning.
- Bret Victor, [Up and Down the Ladder of Abstraction](https://worrydream.com/LadderOfAbstraction/), including Tools & Implementation: move between concrete examples, properties, structure and abstraction; explore parameters and linked representations.
- [Observable](https://observablehq.com/) and [Grist](https://www.getgrist.com/): reactive computation and alternative representations of data.

## Malleable software and direct manipulation

- [Glamorous Toolkit](https://gtoolkit.com/): moldable development, contextual views and inspectors. Prioritize its practical video demonstrations.
- [Ink & Switch](https://www.inkandswitch.com/): research into local-first and malleable software.
- Smalltalk, [Squeak](https://squeak.org/), [Self](https://selflanguage.org/) and [Lively.next](https://lively-next.org/): live, inspectable and modifiable environments.
- HyperCard and [TiddlyWiki](https://tiddlywiki.com/): user-composable documents and interactive information environments.
- [Node-RED](https://nodered.org/), [Godot](https://godotengine.org/), [Penpot](https://penpot.app/), GrapesJS and Storybook: investigate visual composition, property inspection and live component examples. Distinguish their intended audiences and actual usability.

## Structured writing, publishing and inspection

- [Obsidian Properties](https://obsidian.md/help/properties) and [Bases](https://obsidian.md/help/bases), [Logseq properties](https://github.com/logseq/docs/blob/master/pages/Properties.md), [Org-mode](https://orgmode.org/org.html): human-readable structure and alternative views.
- [Quarto](https://quarto.org/docs/), [Astro Content Collections](https://docs.astro.build/en/guides/content-collections/) and Hugo: declarative publishing and metadata.
- [JSON Forms](https://jsonforms.io/docs/), [React JSON Schema Form](https://github.com/rjsf-team/react-jsonschema-form), [Decap CMS](https://decapcms.org/docs/widgets/): schema-driven property editors.
- [yaml](https://eemeli.org/yaml/) and [ruamel.yaml](https://yaml.dev/doc/ruamel.yaml/): round-trip editing candidates.

## Contextual AI and discovery

- [MCP](https://modelcontextprotocol.io/), skills and [IntelliSense](https://code.visualstudio.com/docs/editing/intellisense): capability and procedure discovery.
- Mixed-initiative interaction, just-in-time learning, cognitive apprenticeship, unknown unknowns, privacy/security by design: research leads for surfacing relevant considerations without requiring users to ask.
- [Contextual Discovery and Consideration Architecture](../modules/contextual-discovery-and-consideration.md): project-derived proposal, not independent prior art.

## Learning through play, spatial context and history

Study well-designed video games as interaction models: discovery through use, immediate feedback, reversible experimentation, consistent mechanics, spatial awareness and agency. This is not gamification or engagement optimization.

Investigate history as an explorable dimension: undo, snapshots, branching, side-by-side revisions, comparison and recombination. Git is one possible history source, not necessarily the architecture. Further leads include Emacs Dired/dired-subtree and Miller columns for contextual navigation.

## Emerging design questions (user/project interpretations)

- Can users learn an environment by pursuing intentions rather than reading manuals?
- Can documentation itself be a working, editable example?
- Can interaction be consistent while expression remains diverse? Semantic monotony, common interaction grammar and orthogonality are proposals to explore, not claims about Raskin's terminology.
- Can people move between text, structured properties, visual representations and direct manipulation without losing context?
- Can AI discover capabilities and relevant considerations while preserving consent, inspectability and user control?
- Can software be functional and aesthetically coherent without hiding its purpose behind novelty or complexity?

## Research method

For each reference, progressively record the original source, date, problem, central ideas, concrete demonstrations or working examples, strengths, limitations, criticisms, relationships and open questions. Prefer demonstrations that show actual workflows before abstract explanations. Distinguish observed behavior, author claims, AI interpretation and project proposals. Do not infer usability from a polished website or a manifesto. Preserve disagreements and unsuccessful experiments as useful evidence.

## Related projects

[DVA](https://github.com/KRMRGold/DVA), [SMH-Tree](https://github.com/KRMRGold/SMH-Tree), [F-2](https://github.com/KRMRGold/F-2-different-windows-file-explorer) and Meta-Modules are potential consumers of this research, not its boundaries. Existing project documentation remains intact.
