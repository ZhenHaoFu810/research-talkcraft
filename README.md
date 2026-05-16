# Research Talkcraft

A script-first rehearsal Skill for research presentations. It reads existing slides and supporting materials, then produces a structured Presentation Rehearsal Pack containing a grounded script, critique, revision, Q&A preparation, and timing guidance.

Research Talkcraft does not generate, rewrite, or redesign slides. It optimizes the spoken narrative around fixed presentation materials.

---

## Overview

Research presentations often suffer from a gap between finished materials and effective oral delivery. Slide decks may be polished, but the spoken narrative remains uncalibrated for audience, time constraints, and likely challenges. Research Talkcraft closes this gap by transforming existing materials into a rehearsal-ready output pack.

The Skill operates in two modes:

- **`slides-only`**: For self-contained decks where slide text is sufficient for script generation.
- **`slides+context`**: For sparse decks where additional materials (paper drafts, abstracts, notes, reviewer comments) provide necessary grounding. This mode also enables contradiction detection between slides and supporting materials.

---

## Core Capabilities

- **Slide-by-slide script generation**: Produces spoken narrative that explains slide content rather than reading bullets verbatim.
- **Audience-aware critique**: Evaluates scripts against three personas — Confused Listener, Domain Expert, and Skeptical Reviewer — using a stable rubric (groundedness, clarity, audience fit, timing).
- **Revised script generation**: Produces an improved script incorporating critique feedback.
- **Likely Q&A preparation**: Anticipates audience questions and provides structured answer guidance.
- **Timing control**: Estimates per-section delivery time, flags overrun risks, and identifies cut-for-time candidates. Includes a deterministic helper script (`scripts/estimate_timing.py`) with configurable WPM profiles and complexity modifiers.
- **Contradiction detection**: Identifies factual inconsistencies between slide content and supporting materials.

---

## Output: Presentation Rehearsal Pack

Each run produces a standardized pack with eight sections:

1. **Presentation Brief** — Talk purpose, audience profile, core narrative arc, communication risks, recommended tone, operating mode, and uncertainty flags.
2. **Slide-by-Slide Script** — Spoken narrative per slide with transition cues and approximate timing.
3. **Confusion and Challenge Points** — Structured list of likely audience friction points with mitigation strategies.
4. **Critique Summary** — Scored evaluation across groundedness, clarity, audience fit, and timing dimensions.
5. **Revised Script** — Improved version incorporating critique recommendations.
6. **Likely Q&A** — Anticipated questions with strong answer guidance.
7. **Time-Control Guidance** — Per-section timing, overrun risks, and compression strategies.
8. **Rehearsal Checklist** — Verifiable items to confirm before delivery.

---

## Installation

```bash
npx skills add <your-github-username>/research-talkcraft
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

## Usage Examples

- "I have a 20-minute seminar deck. Help me rehearse."
- "Critique this talk script for a mixed CS/economics audience."
- "My slides are sparse — I have a paper draft too. Build a rehearsal pack."
- "I'm defending next week. Prepare likely Q&A and timing traps."
- "Turn these bullet points into spoken Chinese for a lab meeting."

---

## Design Principles

- **Script-first, not slide-first**: The Skill optimizes spoken narrative around fixed materials. It does not generate, rewrite, or redesign slides.
- **User-visible mode selection**: The `slides-only` and `slides+context` modes are always surfaced to the user, not chosen silently by the agent.
- **Single-agent default**: The core workflow is deterministic and single-agent. Multi-agent rehearsal is an optional extension, not the default.
- **Grounded generation**: All script claims must trace back to provided materials. The Skill flags rather than invents when content is insufficient.
- **Time-bounded realism**: Scripts are calibrated to actual delivery duration, with explicit guidance for compression under pressure.

---

## Package Contents

### Core

| File | Purpose |
|------|---------|
| `SKILL.md` | Main workflow definition. Defines operating modes (`slides-only` / `slides+context`), the 7-step core workflow, input handling rules, and guardrails. |
| `references/script-output-template.md` | Template for the 8-section Presentation Rehearsal Pack. Specifies required content for each section. |

### Playbooks & Personas

| File | Purpose |
|------|---------|
| `references/scenario-playbooks.md` | Calibrations for common presentation settings (seminar, conference, lab meeting, defense, mixed-background update). |
| `references/audience-personas.md` | Three audience archetypes (Confused Listener, Domain Expert, Skeptical Reviewer) used during critique and Q&A generation. |
| `references/qna-playbook.md` | Categories of common research presentation questions with guidance on what strong answers contain. |

### Critique & Revision

| File | Purpose |
|------|---------|
| `references/critique-rubric.md` | Eight-dimension scoring rubric for evaluating draft scripts (groundedness, clarity, audience fit, timing, etc.). |
| `references/revision-patterns.md` | Catalog of common weak-script → strong-script transformations with before/after guidance. |

### Exemplars

| File | Purpose |
|------|---------|
| `references/exemplars.md` | Index pointing to domain-specific and occasion-specific exemplar files. |
| `references/exemplars/*.md` | Concrete weak vs. improved script examples across domains (CS/ML, finance/econ, neuroscience, social science) and occasions (seminar, defense, group meeting, mixed-background). |

### Optional Extensions

| File | Purpose |
|------|---------|
| `references/multi-agent-rehearsal-contract.md` | Contract for the optional `v1A` multi-agent intensification mode. |
| `references/multi-agent-workflow.md` | Step-by-step workflow for multi-agent rehearsal. |
| `references/multi-agent-personas.md` | Persona definitions for multi-agent simulation. |
| `references/overlay-contract.md` | Contract for discipline-specific overlay layers (`v1B`). |
| `references/overlays/*.md` | Domain-specific calibrations (finance, CS group meeting, defense-heavy). |
| `references/contradiction-contract.md` | Contract for contradiction detection between slides and supporting materials (`v2A`). |
| `references/contradiction-taxonomy.md` | Taxonomy of contradiction types. |
| `references/contradiction-reconciliation-rules.md` | Rules for resolving detected contradictions. |
| `references/exemplar-contract.md` | Contract governing the exemplar layer (`v3A`). |
| `references/timing-tool-contract.md` | Contract for the deterministic timing helper (`v4A`). |
| `references/timing-model.md` | WPM profiles and complexity modifiers for timing estimation. |
| `references/non-english-support-contract.md` | Scope contract for Chinese academic presentation support (`v5A`). |

### Scripts & Validation

| File | Purpose |
|------|---------|
| `scripts/estimate_timing.py` | Deterministic timing estimator with configurable WPM profiles and complexity modifiers. |
| `references/capability-matrix.md` | Unified inventory of 29 capabilities across 8 modules. |
| `references/benchmark-set.md` | 25 benchmark cases with scenario mappings and yield ratings. |
| `references/distilled-assets-index.md` | Indexed list of all 29 reference files. |
| `STOP_LINE.md` | Explicit scope boundary and non-goals. |

---

## Validation

- **25 benchmark cases** mapped across real and synthetic scenarios, including high-yield and low-yield cases, discipline overlays, contradiction detection, timing pressure, and Chinese-language support.
- **Capability matrix** documenting 29 capabilities across 8 modules, with source version, default status, applicable scenarios, and known boundaries.
- **Stop line** documenting explicit non-goals to prevent scope creep.

Key documents: [Capability Matrix](research-talkcraft/references/capability-matrix.md) | [Benchmark Set](research-talkcraft/references/benchmark-set.md) | [Stop Line](research-talkcraft/STOP_LINE.md)

---

## License

MIT
