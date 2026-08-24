# Templates

## Intake normalization (Stage 0)

For each pasted update, record:

```
U01 | program: <name> | period: <e.g. 2026-W34> | declared: Green/Amber/Red/— | source-format: email/tool-export/bullets
<raw text, untouched>
```

Programs expected but not received this period: list by name — they feed the coverage
disclosure. If the user hasn't said what's expected, ask once: "How many programs should be
reporting this period?" (M matters; without it, N-of-M is theater.)

## Brief output (Stage 5)

```markdown
# Portfolio Brief — <period>
**Gate: ✅ PASSED** (FAITHFUL · COMPLETE · NO-LAUNDER · ACTIONABLE)
   — or —
**Gate: ⚠️ FLAGGED — <criterion>**: <critique verbatim>

## 🍉 Flags — declared vs. evidence
| Program | Declared | Graded | Verdict | The sentence that decided it |
|---|---|---|---|---|
| <name> [U07] | Green | Red (4) | CONTRADICTS | "…verbatim quote…" |
(If none: "No divergence found between declared statuses and narratives this period —
N of N declared statuses corroborated.")

## Portfolio summary
<3–6 sentences. Every factual claim ends with [U-ids]. Honest Reds acknowledged as healthy
reporting. No portfolio fact (date, cost, count, percentage) that does not appear in an
update — grades and coverage arithmetic computed by the workflow are fine.>

## By program
- **<Program>** — Graded <status> (<grade>): <one line, cited> [U03]. Next step: <concrete,
  names an owner-type and an artifact/decision>.

## Coverage
Based on N of M expected updates. Not represented: <programs — "no update received" /
"excluded: <reason>">. Downgraded to unverified by the quote check: <U-ids, or "none">.
<If one program supplies >50% of the content: "Weighting note: …">

## Appendix — per-update grades
| ID | Program | Declared | Graded | Evidence quote |
```

## Single-update mode

When the user pastes one update ("is this status report honest?"): run Stages 1–2 only and
return the grade, the watermelon verdict, both quotes, and one sentence on what to ask the
program lead next. No brief, no gate banner.
