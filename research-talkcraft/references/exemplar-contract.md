# Exemplar Contract

This document defines what an exemplar is, what fields it must contain, and what it must not be.

## What An Exemplar Is

An exemplar is a **concrete, self-contained illustration** of a weak script segment, the critique that identifies its weakness, and an improved script segment that fixes it. Exemplars anchor the Skill's quality judgments by showing what "bad" and "better" look like in a specific context.

Exemplars are **reference material**, not training data. The Skill consults them during critique and revision to match weaknesses to transformations.

## Required Fields

Every exemplar must contain the following fields:

1. **Scenario** — The presentation setting (e.g., finance seminar, CS group meeting, thesis defense).
2. **Domain** — The academic field (e.g., economics, computer science, neuroscience).
3. **Audience** — Who is in the room and what they know.
4. **Input material type** — Slide content summary or section description.
5. **Weak script** — A realistic but flawed script segment.
6. **Critique** — Specific observations about why the weak script fails.
7. **Improved script** — A revised segment that fixes the weaknesses.
8. **Why the improvement works** — Explanation of the transformation principle.

## Optional Fields

Use these fields when relevant:

- **Overlay used** — Which v1B overlay applies (e.g., `finance-academic-talk`).
- **Contradiction present** — Whether a deck-vs-support discrepancy is involved (v2A).
- **v1A intensification relevance** — Whether multi-agent rehearsal would catch additional issues.
- **Timing issue category** — Whether the exemplar illustrates a timing problem (overrun, under-allocation).

## What An Exemplar Is Not

An exemplar **must not** be:

1. **A full dataset row.** Exemplars are narrative illustrations, not structured data entries.
2. **A long transcript dump.** Each exemplar should be short (under 300 words for scripts).
3. **A copyrighted source reproduction.** Weak and improved scripts must be original writing for this project.
4. **Domain-trivia documentation.** The lesson must generalize beyond the specific field.
5. **A complete talk.** Each exemplar covers one segment or one transformation, not an entire presentation.

## Quality Bar

A good exemplar:
- Shows a **realistic** weakness that actual speakers make.
- Provides a **specific** critique, not generic negativity.
- Produces a **materially better** script, not just stylistic tweaking.
- Teaches a **generalizable** pattern that transfers across domains.
