# Timing Tool Contract

This document defines the stable contract for the lightweight timing helper (`scripts/estimate_timing.py`). It specifies what the tool consumes, what it produces, and what it explicitly does not do.

## Inputs

The timing helper consumes:

1. **Script text** — The spoken script, sectioned by slide or logical segment.
2. **Section labels** — Identifiers for each section (e.g., "Slide 1 — Title", "Section A: Introduction").
3. **Optional: Slide count** — Total number of slides, for sanity-checking.
4. **Optional: Target duration** — Total talk budget in minutes (e.g., 20, 30, 45).
5. **Optional: Pace profile** — One of:
   - `default` — 130 WPM, standard complexity weighting.
   - `dense` — 110 WPM, heavier penalty for technical terms.
   - `fast` — 150 WPM, lighter penalty.

## Outputs

For each section, the tool produces:

1. **Word count** — Number of spoken words.
2. **Estimated duration** — In seconds and minutes.
3. **Complexity flag** — Whether the section was flagged as dense (affects pacing).

For the entire script, the tool produces:

1. **Total estimated duration** — Sum of section durations.
2. **Budget comparison** — If a target duration was provided, whether the script is over, under, or on target.
3. **Overrun flags** — Sections most likely to exceed their fair-share time budget.
4. **Suggested cut candidates** — Sections that could be compressed or dropped if time is short.

## Strict Non-Goals

The timing helper **must not**:

1. **Analyze speech audio.** No ASR, no filler-word detection, no pace measurement from recordings.
2. **Require a GUI or visualization.** Output is plain text or JSON.
3. **Automatically rewrite the script.** It estimates and recommends; it does not edit.
4. **Use machine learning.** The model is deterministic and explainable.
5. **Become a hard dependency.** The Skill can fall back to the 120–150 WPM heuristic if the script is unavailable.

## Invocation Rules

- The Skill should invoke `estimate_timing.py` when a structured script exists and a target duration is known.
- The Skill may run the tool in heuristic-only mode when:
  - The script is not yet sectioned.
  - The target duration is unknown.
  - The script cannot be run (e.g., Python is not available).
- The output is advisory. The user decides what to cut.
