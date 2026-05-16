#!/usr/bin/env python3
"""
Lightweight timing estimator for research presentation scripts.

Usage:
    python estimate_timing.py < script.txt
    python estimate_timing.py --target 20 --pace default script.txt

Input format:
    Sections are separated by blank lines.
    The first line of each section is the section label.
    Everything after the first line is the script text for that section.

Example input:
    Slide 1 — Title
    Welcome everyone. Today I will present...

    Slide 2 — Background
    Let me start with the problem...
"""

import argparse
import re
import sys


# Base words-per-minute by pace profile
BASE_WPM = {
    "default": 130,
    "dense": 110,
    "fast": 150,
}

# Complexity penalty multipliers
PENALTY_EQUATION = 0.20
PENALTY_JARGON = 0.10
PENALTY_NUMBERS = 0.10
BONUS_TRANSITION = -0.10
BONUS_QA = -0.20
MAX_PENALTY = 0.50

# Heuristic jargon list (technical terms that slow speech)
JARGON_WORDS = {
    "algorithm", "estimator", "regression", "covariance", "heteroskedasticity",
    "endogeneity", "identification", "perplexity", "burstiness", "entropy",
    "generalization", "regularization", "optimization", "convergence",
    "equilibrium", "differential", "stochastic", "variational", "posterior",
    "likelihood", "bootstrap", "placebo", "counterfactual", "ablation",
    "tokenization", "embedding", "attention", "transformer", "backpropagation",
}

# Transition keywords
TRANSITION_WORDS = {"transition", "summary", "overview", "outline", "agenda", "toc"}

# Q&A / closing keywords (must match label, not body text)
QA_WORDS = {"q&a", "questions", "closing", "wrap up"}

# Density keywords
DENSITY_WORDS = {"formally", "theorem", "proof", "lemma", "derivation", "proposition"}


def count_words(text):
    """Simple whitespace tokenization."""
    return len(text.split())


def has_equations(text):
    """Detect equation-like content: =, \sum, \int, Greek letters, superscripts."""
    patterns = [
        r"=",
        r"\\(?:sum|int|frac|partial|alpha|beta|gamma|delta|epsilon|lambda|sigma|theta)",
        r"[\^_]\{",
        r"[αβγδελσθ]",
    ]
    return any(re.search(p, text) for p in patterns)


def has_dense_jargon(text):
    """More than 3 uncommon technical terms per 50 words."""
    words = text.lower().split()
    if not words:
        return False
    jargon_count = sum(1 for w in words if w.strip(".,;:!?()") in JARGON_WORDS)
    ratio = jargon_count / len(words)
    return ratio > (3 / 50)


def has_many_numbers(text):
    """More than 3 numbers or percentages per 50 words."""
    words = text.split()
    if not words:
        return False
    number_count = len(re.findall(r"\b\d+(?:\.\d+)?(?:%|\s*percent)?\b", text))
    ratio = number_count / len(words)
    return ratio > (3 / 50)


def is_transition_section(label, text):
    """Check if section is a transition, TOC, or summary."""
    combined = (label + " " + text).lower()
    return any(w in combined for w in TRANSITION_WORDS)


def is_qa_section(label, text):
    """Check if section is Q&A or closing based primarily on label."""
    label_lower = label.lower()
    return any(w in label_lower for w in QA_WORDS)


def compute_complexity_penalty(label, text):
    """Compute total complexity penalty for a section."""
    penalty = 0.0
    if has_equations(text):
        penalty += PENALTY_EQUATION
    if has_dense_jargon(text):
        penalty += PENALTY_JARGON
    if has_many_numbers(text):
        penalty += PENALTY_NUMBERS
    if is_transition_section(label, text):
        penalty += BONUS_TRANSITION
    if is_qa_section(label, text):
        penalty += BONUS_QA
    return min(penalty, MAX_PENALTY)


def parse_sections(content):
    """Parse input into list of (label, text) sections."""
    sections = []
    raw_sections = re.split(r"\n\s*\n+", content.strip())
    for raw in raw_sections:
        lines = raw.strip().splitlines()
        if not lines:
            continue
        label = lines[0].strip()
        text = "\n".join(lines[1:]).strip()
        sections.append((label, text))
    return sections


def format_duration(seconds):
    """Format seconds as 'M min S sec' or 'S sec'."""
    minutes = int(seconds // 60)
    secs = int(round(seconds % 60))
    if minutes > 0:
        return f"{minutes} min {secs} sec"
    return f"{secs} sec"


def estimate_timing(sections, target_minutes=None, pace="default"):
    """Estimate timing for all sections."""
    base_wpm = BASE_WPM.get(pace, BASE_WPM["default"])
    results = []
    total_words = 0
    total_seconds = 0

    for label, text in sections:
        words = count_words(text)
        penalty = compute_complexity_penalty(label, text)
        effective_wpm = base_wpm / (1 + penalty)
        seconds = (words / effective_wpm) * 60
        flag = "DENSE" if penalty > 0.15 else ""
        results.append({
            "label": label,
            "words": words,
            "wpm": round(effective_wpm),
            "seconds": seconds,
            "duration_str": format_duration(seconds),
            "flag": flag,
            "penalty": penalty,
        })
        total_words += words
        total_seconds += seconds

    avg_wpm = (total_words / total_seconds) * 60 if total_seconds > 0 else 0

    # Budget comparison
    budget_status = ""
    if target_minutes is not None:
        target_seconds = target_minutes * 60
        diff = target_seconds - total_seconds
        if abs(diff) < 30:
            budget_status = f"ON BUDGET (~{abs(int(diff))} sec variance)"
        elif diff > 0:
            budget_status = f"UNDER BUDGET by {format_duration(diff)}"
        else:
            budget_status = f"OVER BUDGET by {format_duration(abs(diff))}"

    # Overrun risk ranking
    if target_minutes is not None and total_seconds > 0:
        fair_share = target_seconds / len(results) if results else 0
        overrun_risks = [
            r for r in results
            if r["seconds"] > fair_share * 1.3
        ]
        overrun_risks.sort(key=lambda x: x["seconds"], reverse=True)
    else:
        overrun_risks = sorted(results, key=lambda x: x["seconds"], reverse=True)[:3]

    # Cut-for-time candidates (longest non-critical sections)
    cut_candidates = [
        r for r in results
        if r["words"] > 40 and r["flag"] != "DENSE" and not is_qa_section(r["label"], "")
    ]
    cut_candidates.sort(key=lambda x: x["seconds"], reverse=True)

    return {
        "sections": results,
        "total_words": total_words,
        "avg_wpm": round(avg_wpm),
        "total_seconds": total_seconds,
        "total_duration_str": format_duration(total_seconds),
        "target_minutes": target_minutes,
        "budget_status": budget_status,
        "overrun_risks": overrun_risks,
        "cut_candidates": cut_candidates,
    }


def print_report(report):
    """Print human-readable timing report."""
    # Header
    print(f"{'Section':<40} {'Words':>6} {'WPM':>5} {'Duration':>10} {'Flag':>6}")
    print("-" * 75)

    for sec in report["sections"]:
        flag = sec["flag"] if sec["flag"] else ""
        print(f"{sec['label']:<40} {sec['words']:>6} {sec['wpm']:>5} {sec['duration_str']:>10} {flag:>6}")

    print("-" * 75)
    print(f"{'TOTAL':<40} {report['total_words']:>6} {report['avg_wpm']:>5} {report['total_duration_str']:>10}")
    print()

    if report["target_minutes"] is not None:
        print(f"Target: {report['target_minutes']:.1f} min")
        print(f"Status: {report['budget_status']}")
        print()

    if report["overrun_risks"]:
        print("Overrun risk ranking:")
        for i, sec in enumerate(report["overrun_risks"], 1):
            pct = (sec["seconds"] / report["total_seconds"] * 100) if report["total_seconds"] > 0 else 0
            print(f"  {i}. {sec['label']}  {sec['duration_str']}  ({pct:.0f}% of total)")
        print()

    if report["cut_candidates"]:
        print("Cut-for-time candidates:")
        for i, sec in enumerate(report["cut_candidates"][:3], 1):
            suggested = max(sec["seconds"] * 0.6, sec["seconds"] - 30)
            print(f"  {i}. {sec['label']}  {sec['duration_str']}  (compress to ~{format_duration(suggested)})")
        print()

    print("Note: Estimates assume continuous speaking. Add buffer for pauses, questions, and transitions.")


def main():
    parser = argparse.ArgumentParser(description="Estimate timing for a presentation script.")
    parser.add_argument("file", nargs="?", help="Input script file (default: stdin)")
    parser.add_argument("--target", type=float, default=None, help="Target duration in minutes")
    parser.add_argument("--pace", choices=["default", "dense", "fast"], default="default", help="Pace profile")
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = sys.stdin.read()

    if not content.strip():
        print("Error: No input provided.", file=sys.stderr)
        sys.exit(1)

    sections = parse_sections(content)
    if not sections:
        print("Error: No sections found. Separate sections with blank lines.", file=sys.stderr)
        sys.exit(1)

    report = estimate_timing(sections, target_minutes=args.target, pace=args.pace)
    print_report(report)


if __name__ == "__main__":
    main()
