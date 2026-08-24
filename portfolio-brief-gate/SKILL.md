---
name: portfolio-brief-gate
description: Turn raw program/project status updates into an eval-gated executive portfolio brief. Use whenever the user pastes status updates, weekly reports, or program summaries, or asks for a portfolio rollup, QBR summary, RAG review, "summarize my program updates", or a check of a single status report. Grades every update's TRUE status against an anchored rubric (tone-blind), flags watermelon reporting (narrative contradicts the declared RAG), cites every claim in the brief back to a source update, runs a binary self-judge before anything is presented, and never lets an unverified claim ship silently.
---

# Portfolio Brief Gate

You are producing a portfolio brief that a leadership forum can trust. The core rule, from
which everything else follows: **an AI-generated insight enters a governance forum only after
it has been graded, cited, and judged — and anything that fails the gate is shown as flagged,
never silently dropped and never silently shipped.**

The measured lessons behind these rules live in the README and
`references/golden-set-guide.md`, not here. Do not soften the rules to be agreeable.

## Workflow

Run these stages in order. Reference files carry the full rubrics and templates — read the
relevant one before each stage the first time it runs in a conversation.

### Stage 0 — Intake and inventory
Assign each update an ID (U01, U02, …). Record: program name, reporting period, declared
status (RAG or equivalent) if present, and the raw text. Note programs the user says exist
but that have NO update this period — they go in the coverage disclosure, not in the void.
If fewer than 3 updates, skip the brief and run single-update mode (Stages 1–2 per update,
no rollup).

### Stage 1 — True-status grading (per update)
Apply the anchored severity rubric in `references/severity-rubric.md`. The two rules that do
the work: **grade the STATED consequence, never the tone** (an upbeat update reporting a
missed dependency grades on the missed dependency; an anxious update about a cosmetic issue
grades low), and **default down** — a high grade must be earned by concrete evidence in the
text, quoted verbatim (≤200 chars) as `evidence`.

### Stage 2 — Watermelon check (per update with a declared status)
Apply `references/watermelon-check.md`: compare the declared status against what the
narrative actually states → `CONTRADICTS` (declared healthier than the narrative supports —
the red flag), `CORROBORATES`, or `NEUTRAL`, each with a verbatim quote. A declared Green
with a narrative describing a blocked critical path is the exact case this stage exists for.

### Stage 3 — Draft the brief
Use the output template in `references/templates.md`. Hard rules:
- Every factual claim in the brief ends with its source citation(s): `[U07]`, `[U03,U11]`.
- A claim you cannot bind to an update ID does not go in the brief. No exceptions — if it
  feels essential, it belongs in "Open questions", phrased as a question.
- Watermelon-flagged programs are surfaced in their own section at the top, with quotes.
  Never launder a contradicted Green into fluent reassurance.
- End with the coverage disclosure: "Based on N of M expected updates. Not represented:
  <programs>." If one program dominates the content, say so.

### Stage 4 — Judge the draft
Apply `references/judge.md`. First the mechanical check: every evidence quote must appear
character-for-character in the raw inventory; a quote that doesn't is not fixed or
paraphrase-matched — its row is downgraded to unverified and listed in the coverage
disclosure. In Claude Code (or any environment with code execution), run
`scripts/validate_quotes.py` for a deterministic result instead of checking in-model.
Then four binary criteria (FAITHFUL, COMPLETE, NO-LAUNDER, ACTIONABLE), each returning
exactly PASS / FAIL / ABSTAIN with a written critique that quotes what it checked. The
gate is the AND of the four — never a holistic override.
- If any criterion FAILs: revise the draft once, fixing exactly what the critique names,
  then re-judge.
- If it still FAILs: present the brief anyway, under a visible banner —
  `⚠️ GATE: FLAGGED — <criterion>: <critique>` — so the reader knows precisely what is
  unverified. Failing loudly is the product; failing silently is the bug.
- When the user's setup allows a second model (e.g. they can paste the judge prompt into a
  different model), recommend it: a judge from the same model family shares the writer's
  blind spots. Single-model self-judging is the accepted fallback, not the ideal.

### Stage 5 — Present
Output order: gate banner (PASSED / FLAGGED) → watermelon table → brief with citations →
coverage disclosure → appendix (per-update grades with evidence quotes). Offer the
calibration mode below if this is the user's first run.

## Calibration mode (on request, or offer after first use)

The rubric is a defensible default, not the user's ground truth. To make the gate *theirs*:
follow `references/golden-set-guide.md` — 20–30 past updates where they know what really
happened, graded blind by the skill, disagreements resolved by tuning rubric WORDING (never
by relabeling their ground truth), every resolved disagreement kept as a regression row.
Binary verdicts only; the guide contains the measured reason a 1–5 quality score hides
failures.

## What this skill refuses to do

- Grade severity from tone, emoji, or confidence of the author.
- Emit a claim without a citation, or a portfolio fact (date, cost, count, percentage,
  or any figure about a program's state) that appears in no update. Numbers the skill
  itself computes — grades, N-of-M coverage arithmetic — are exempt, and checked instead
  by the judge's COMPLETE criterion.
- Ship an evidence quote that doesn't appear verbatim in its source update — that row is
  downgraded to unverified, visibly.
- Average judge criteria into a score, or let one strong section excuse a failed check.
- Drop an update (or a failing claim) without listing it as excluded.
