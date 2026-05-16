# Contradiction Reconciliation Rules

This document defines how to reconcile contradictions between the slide deck and supporting materials for each contradiction class. The rules are ordered by class and severity.

---

## Severity Levels

| Level | Definition | Mandatory Action |
|-------|-----------|-----------------|
| **High** | Credibility-risk contradiction; the speaker cannot safely state either claim without resolution. | **Escalate to user.** Refuse to state the disputed claim in the script until resolved. |
| **Medium** | Important discrepancy; the speaker should acknowledge it but can proceed with a warning. | Surface prominently in the pack. Propose a reconciliation. Let the user override. |
| **Low** | Minor version drift or non-blocking detail difference. | Note briefly in the pack. Do not interrupt the workflow. |

---

## Reconciliation Strategies

### Prefer the Deck

Use when:
- The deck is the rehearsal anchor by design.
- The supporting material contains aspirational or outdated claims.
- The discrepancy is presentational compression.

Action: Use the deck claim in the script, but note the supporting-material discrepancy in the contradiction report.

### Prefer the Supporting Material

Use when:
- The supporting material is newer and the discrepancy is clearly version drift.
- The deck contains an obvious error (typo, outdated number).
- The user explicitly states that the paper is authoritative.

Action: Use the supporting-material claim in the script, flag that the deck differs, and recommend updating the deck if possible.

### Present Both Explicitly

Use when:
- Both claims are defensible but reflect different scopes or framings.
- The audience may know both versions and will ask about the difference.

Action: Include both claims in the script with an explicit bridge: "The deck reflects our original sample through 2023; the updated paper extends through 2024."

### Warn and Ask the User

Use when:
- The discrepancy is material but the right resolution depends on the speaker's intent.
- The severity is Medium and the default reconciliation is uncertain.

Action: Surface the contradiction prominently. Propose two options. Ask the user which to use.

### Refuse to State the Disputed Claim

Use when:
- The severity is High and neither source can be trusted without verification.
- Stating either claim would expose the speaker to a credibility attack.

Action: Replace the claim with an explicit uncertainty flag: "The deck and the paper differ on [specific point]. The speaker should verify which is correct before presenting."

---

## Class-Specific Default Rules

### 1. Temporal Mismatch

| Severity | Default Reconciliation | Rationale |
|----------|----------------------|-----------|
| High | **Warn and ask.** The temporal difference changes a main result. | The speaker must know which sample period they are presenting. |
| Medium | **Present both explicitly.** Acknowledge version drift. | Common and manageable if surfaced. |
| Low | **Prefer the deck.** Note the newer date in the contradiction report. | The deck is the rehearsal anchor; the date difference is minor. |

### 2. Sample / Dataset Mismatch

| Severity | Default Reconciliation | Rationale |
|----------|----------------------|-----------|
| High | **Warn and ask.** The sample change is material to identification. | External validity depends on the correct sample. |
| Medium | **Prefer the deck.** Note the broader sample in the report. | Often presentational compression. |
| Low | **Prefer the deck.** Ignore. | Typographic or naming variation. |

### 3. Claim-Strength Mismatch

| Severity | Default Reconciliation | Rationale |
|----------|----------------------|-----------|
| High | **Refuse to state the disputed claim.** Use the weaker, defensible framing. | Overselling is more dangerous than underselling. |
| Medium | **Prefer the deck.** Note the stronger abstract language as a risk. | The deck is usually more cautious and more defensible. |
| Low | **Prefer the deck.** Ignore. | Minor wording difference. |

### 4. Method-Description Mismatch

| Severity | Default Reconciliation | Rationale |
|----------|----------------------|-----------|
| High | **Warn and ask.** The method descriptions are fundamentally different. | The speaker must know which method they used. |
| Medium | **Present both explicitly.** Use the detailed description from supporting material but note the deck simplification. | Presentational compression is acceptable if acknowledged. |
| Low | **Prefer the deck.** Ignore. | Naming variation or minor simplification. |

### 5. Result-Magnitude Mismatch

| Severity | Default Reconciliation | Rationale |
|----------|----------------------|-----------|
| High | **Refuse to state the disputed claim.** Force verification. | Numerical discrepancies are easy to spot and hard to defend. |
| Medium | **Warn and ask.** May be rounding or specification differences. | The speaker should know which number is correct. |
| Low | **Prefer the deck.** Note the alternative figure. | Minor rounding difference. |

### 6. Contribution-Framing Mismatch

| Severity | Default Reconciliation | Rationale |
|----------|----------------------|-----------|
| High | **Warn and ask.** The framings are incompatible. | The audience will be confused if the opening and closing claim different contributions. |
| Medium | **Present both explicitly.** Use the deck framing but note the broader abstract claim. | Common when abstracts are written for broader appeal. |
| Low | **Prefer the deck.** Ignore. | Minor emphasis difference. |

### 7. Availability / Reproducibility Mismatch

| Severity | Default Reconciliation | Rationale |
|----------|----------------------|-----------|
| High | **Refuse to state the disputed claim.** Use the most conservative availability statement. | Over-promising availability is a credibility risk. |
| Medium | **Prefer the supporting material.** Note the deck discrepancy. | The paper usually reflects actual availability; the deck may be aspirational. |
| Low | **Prefer the supporting material.** Ignore. | Minor wording difference ("public" vs. "available"). |

---

## Mandatory User Escalation Triggers

The Skill **must** escalate to the user (High-severity handling) when any of the following occur:

1. **Numerical result mismatch** where the two sources report different numbers for the same metric.
2. **Claim-strength mismatch** where the abstract or supporting material uses causal or universal language that the deck does not support.
3. **Method mismatch** where the deck and supporting material describe fundamentally different methodologies.
4. **Temporal mismatch** where the time period difference changes a main finding or sample size.
5. **Any contradiction** where the Skill cannot determine which source is more authoritative.

The escalation must be:
- **Explicit:** State exactly what contradicts what.
- **Concise:** One or two sentences per contradiction.
- **Non-speculative:** Do not guess why the discrepancy exists.
