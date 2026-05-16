# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This repository contains the finished `research-talkcraft` Skill package plus its archived development and validation documents.

## Current Repository Layout

- **`research-talkcraft/`** — The Skill package itself. This directory should contain only core Skill files needed for use and maintenance:
  - `SKILL.md`
  - `references/`
  - `scripts/`
- **`docs/overview/`** — Product route, master status, and Chinese project summary
- **`docs/task-cards/`** — Archived development task cards
- **`docs/round-history/`** — Per-round logs and handoff documents
- **`docs/validation/`** — Benchmark set, capability matrix, validation notes, sample materials, and test cases
- **`docs/policies/`** — Policy documents such as the stop line

## Key Documents

- **`docs/overview/research_talkcraft_product_route.md`** — Primary product route and boundary document
- **`docs/overview/research_talkcraft_master_status.md`** — Current lifecycle status and closure state
- **`docs/overview/research_talkcraft_功能与阶段总览.md`** — Chinese summary of implemented functionality and maturity
- **`docs/validation/capability-matrix.md`** — Unified capability inventory
- **`docs/validation/benchmark-set.md`** — Unified benchmark directory

## Core Skill Package Structure

The maintained Skill package rooted at `research-talkcraft/` should look like:

```
research-talkcraft/
├── SKILL.md                              # Core workflow, modes, and boundaries
├── references/
│   ├── scenario-playbooks.md             # General research presentation scenarios
│   ├── audience-personas.md              # Confused Listener, Domain Expert, Skeptical Reviewer
│   ├── critique-rubric.md                # Scoring dimensions (groundedness, clarity, audience fit, etc.)
│   ├── revision-patterns.md              # Weak → strong script transformations
│   ├── script-output-template.md         # Standard Presentation Rehearsal Pack structure
│   ├── qna-playbook.md                   # Research Q&A categories and strong answer guidance
│   └── exemplars.md                      # Weak script / improved script / critique examples
└── scripts/                              # Optional; only for lightweight deterministic helpers
```

## Core Design Commitments

These are non-negotiable constraints from the product route:

1. **Script-first, not slide-first.** The Skill optimizes the spoken narrative around fixed materials. It does not generate, rewrite, or redesign slides.
2. **Two operating modes.** `slides-only` (deck + context) and `slides+context` (deck + paper/draft/notes). The mode must be user-visible and user-controllable.
3. **Single-agent default.** The `v0` workflow is deterministic and single-agent. Multi-agent rehearsal is an optional future extension, not the default.
4. **Presentation Rehearsal Pack output.** The final output is a structured pack, not a raw script. Required sections: Presentation Brief, Slide-by-Slide Script, Confusion/Challenge Points, Critique Summary, Revised Script, Likely Q&A, Time-Control Guidance, Rehearsal Checklist.
5. **General research scope.** `v0` targets general research presentations (seminars, conferences, thesis defenses, lab meetings), not a single discipline.

## Build / Test / Lint

There is no full software build pipeline in this repository. The only executable helper currently maintained in the Skill package is the lightweight timing script under `research-talkcraft/scripts/`.

## Development Workflow

When working here:

1. Read `docs/overview/research_talkcraft_master_status.md` first to understand the current closed state.
2. Read `docs/overview/research_talkcraft_product_route.md` for the product boundary and design commitments.
3. Treat `research-talkcraft/` as the clean Skill package. Do not put development logs, task cards, or project-management docs back into that directory.
4. Put any future non-core documents into `docs/` under the appropriate category.
5. Keep the package compact. Do not add large raw datasets, training pipelines, OCR/video assets, or heavy multi-agent orchestration into the core Skill directory unless the product scope is explicitly reopened.
