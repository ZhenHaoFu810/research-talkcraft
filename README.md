# Research Talkcraft

A Skill for rehearsing research presentations. It reads your slides and supporting materials, then produces a spoken script, critique, revised version, likely Q&A, and timing guidance.

It does not generate, rewrite, or redesign slides. It works with the materials you already have.

---

## What It Does

Research Talkcraft turns existing presentation materials into a rehearsal-ready output pack. You provide your slides, optionally with a paper draft, abstract, or notes; it returns a complete **Presentation Rehearsal Pack** that you can use to prepare for a talk.

The Skill runs in two modes:

- **`slides-only`** — for self-contained decks where slide text is sufficient.
- **`slides+context`** — for sparse decks where additional materials (paper drafts, abstracts, notes, reviewer comments) provide stronger grounding. This mode also checks for contradictions between slides and supporting materials.

### Core Capabilities

- **Script writing** — generates a slide-by-slide spoken narrative that explains rather than reads bullets.
- **Critique** — evaluates the script against three personas: Confused Listener, Domain Expert, and Skeptical Reviewer.
- **Revision** — rewrites the script based on the critique feedback.
- **Q&A preparation** — anticipates likely questions and drafts answer guidance.
- **Timing** — estimates per-section duration, flags overrun risks, and suggests compression targets. Includes a deterministic helper script (`scripts/estimate_timing.py`) with configurable WPM profiles.
- **Contradiction detection** — spots factual inconsistencies between slide content and supporting materials.

### The Rehearsal Pack

The output has eight sections:

1. **Brief** — audience profile, narrative arc, communication risks, tone guidance.
2. **Script** — spoken narrative per slide, with transition cues and approximate timing.
3. **Friction Points** — likely audience confusion spots and how to handle them.
4. **Critique Summary** — scored evaluation across groundedness, clarity, audience fit, and timing.
5. **Revised Script** — improved version incorporating the critique.
6. **Likely Q&A** — anticipated questions with strong answer guidance.
7. **Timing** — per-section duration, overrun risks, and compression strategies.
8. **Checklist** — items to verify before presenting.

---

## Installation

```bash
npx skills add ZhenHaoFu810/research-talkcraft
```

Or install manually by copying `research-talkcraft/` into your agent's skills directory:

```bash
# Claude Code
mkdir -p ~/.claude/skills/
cp -r research-talkcraft ~/.claude/skills/

# Project-local
mkdir -p .claude/skills/
cp -r research-talkcraft .claude/skills/
```

---

## Usage

The Skill triggers when you mention rehearsing, scripting, or critiquing a research presentation. Examples:

- "I have a 20-minute seminar deck. Help me rehearse."
- "Critique this talk script for a mixed CS/economics audience."
- "My slides are sparse — I have a paper draft too. Build a rehearsal pack."
- "I'm defending next week. Prep me for likely Q&A and timing traps."
- "Turn these bullets into spoken Chinese for a lab meeting."

---

## Design Principles

- **Script-first, not slide-first.** Optimize the spoken narrative around fixed materials. Do not redesign slides.
- **Modes are user-visible.** `slides-only` and `slides+context` are always surfaced to the user, never chosen silently by the agent.
- **Single-agent by default.** The core workflow is deterministic and single-agent. Multi-agent rehearsal is an optional add-on.
- **Grounded, not invented.** Every claim traces back to the provided materials. When content is thin, the Skill flags it rather than filling gaps.
- **Time-bounded.** A 35-minute script for a 20-minute slot is a failed script. Compression guidance is built in.

---

## Package Contents

### Core

- **`SKILL.md`** — Main workflow definition: operating modes, the 7-step core workflow, input handling rules, and guardrails.
- **`references/script-output-template.md`** — Template for the 8-section Presentation Rehearsal Pack.

### Playbooks & Personas

- **`references/scenario-playbooks.md`** — Calibrations for common presentation settings (seminar, conference, lab meeting, defense, mixed-background update).
- **`references/audience-personas.md`** — Three archetypes used during critique and Q&A: Confused Listener, Domain Expert, Skeptical Reviewer.
- **`references/qna-playbook.md`** — Common question categories and what strong answers look like.

### Critique & Revision

- **`references/critique-rubric.md`** — Eight-dimension scoring rubric (groundedness, clarity, audience fit, timing, etc.).
- **`references/revision-patterns.md`** — Weak-script to strong-script transformations with before/after guidance.

### Exemplars

- **`references/exemplars.md`** — Index of domain-specific and occasion-specific exemplar files.
- **`references/exemplars/*.md`** — Weak vs. improved script examples across domains (CS/ML, finance/econ, neuroscience, social science) and occasions (seminar, defense, group meeting, mixed-background).

### Optional Extensions

- **`references/multi-agent-rehearsal-contract.md`** — Optional multi-agent intensification mode.
- **`references/multi-agent-workflow.md`** — Step-by-step multi-agent rehearsal workflow.
- **`references/multi-agent-personas.md`** — Persona definitions for multi-agent simulation.
- **`references/overlay-contract.md`** — Discipline-specific overlay layer definitions.
- **`references/overlays/*.md`** — Domain-specific calibrations (finance, CS group meeting, defense-heavy).
- **`references/contradiction-contract.md`** — Contradiction detection rules.
- **`references/contradiction-taxonomy.md`** — Taxonomy of contradiction types.
- **`references/contradiction-reconciliation-rules.md`** — Rules for resolving contradictions.
- **`references/exemplar-contract.md`** — Exemplar layer governance.
- **`references/timing-tool-contract.md`** — Deterministic timing helper configuration.
- **`references/timing-model.md`** — WPM profiles and complexity modifiers.
- **`references/non-english-support-contract.md`** — Chinese academic presentation support scope.

### Scripts & Validation

- **`scripts/estimate_timing.py`** — Deterministic timing estimator with configurable WPM profiles.
- **`references/capability-matrix.md`** — Inventory of 29 capabilities across 8 modules.
- **`references/benchmark-set.md`** — 25 benchmark cases with scenario mappings.
- **`references/distilled-assets-index.md`** — Indexed list of all reference files.
- **`STOP_LINE.md`** — Explicit scope boundary and non-goals.

---

## Validation

The project was validated with 25 benchmark cases covering real and synthetic scenarios, including discipline overlays, contradiction detection, timing pressure, and Chinese-language support. A capability matrix documents 29 capabilities across 8 modules, and a stop line records explicit non-goals to prevent scope creep.

Key documents: [Capability Matrix](research-talkcraft/references/capability-matrix.md) | [Benchmark Set](research-talkcraft/references/benchmark-set.md) | [Stop Line](research-talkcraft/STOP_LINE.md)

---

## License

MIT