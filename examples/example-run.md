# Example run — full skill output over `mock-updates.md`

What the skill produces when the six fictional updates are pasted in. Stages 0–2 (the
working tables), then the brief exactly as Stage 5 presents it, then the judge record.
Every quote below was checked with `scripts/validate_quotes.py` against the raw updates —
see `quote-check.json` for the validator input, reproduce with:

```
python3 ../portfolio-brief-gate/scripts/validate_quotes.py quote-check.json
```

## Stage 0 — Inventory

| ID | Program | Period | Declared |
|---|---|---|---|
| U01 | Atlas ERP Migration | 2026-W34 | Green |
| U02 | Helios Data Platform | 2026-W34 | Red |
| U03 | Orion Mobile App | 2026-W34 | Green |
| U04 | Fieldworks Rollout | 2026-W34 | Amber |
| U05 | Ledger Consolidation | 2026-W34 | Red |
| U06 | Beacon CRM | 2026-W34 | Green |

Expected but not received: Quartz Analytics, Payroll Modernization → M = 8, N = 6.

## Stages 1–2 — Grades and watermelon verdicts

```json
[
{"id":"U01","program":"Atlas ERP Migration","declared_status":"Green",
 "graded_severity":4,"graded_status":"Red",
 "evidence":"the vendor has paused all interface development until the revised data-residency contract is signed, and legal has not given us a date",
 "rationale":"Anchor 4: fully blocked on the critical path with no ETA; tone ignored.",
 "watermelon":{"verdict":"CONTRADICTS","tone":"BULLISH",
  "quote":"the vendor has paused all interface development until the revised data-residency contract is signed, and legal has not given us a date",
  "explanation":"Declared Green while the narrative states a hard block with no date."}},

{"id":"U02","program":"Helios Data Platform","declared_status":"Red",
 "graded_severity":5,"graded_status":"Red",
 "evidence":"We have slipped the rehearsal by two weeks and informed downstream consumers.",
 "rationale":"Anchor 5: committed milestone date lost; data loss event already occurred.",
 "watermelon":{"verdict":"CORROBORATES","tone":"NEUTRAL",
  "quote":"Declaring Red this week.",
  "explanation":"Declared status honestly reflects the narrative — an honest Red."}},

{"id":"U03","program":"Orion Mobile App","declared_status":"Green",
 "graded_severity":1,"graded_status":"Green",
 "evidence":"All good this period. Tracking to plan.",
 "rationale":"Anchor 1 by default-down: no consequence described; note the narrative is too thin to verify.",
 "watermelon":{"verdict":"NEUTRAL","tone":"NEUTRAL",
  "quote":"All good this period. Tracking to plan.",
  "explanation":"Narrative too thin to corroborate or contradict — unverifiable, not verified."}},

{"id":"U04","program":"Fieldworks Rollout","declared_status":"Amber",
 "graded_severity":3,"graded_status":"Amber",
 "evidence":"the team is enrolling handsets manually at roughly 40 per day, which consumes about half of the squad's capacity every week",
 "rationale":"Anchor 3: progressing via a sustained, costly manual workaround.",
 "watermelon":{"verdict":"CORROBORATES","tone":"CAUTIOUS",
  "quote":"the team is enrolling handsets manually at roughly 40 per day, which consumes about half of the squad's capacity every week",
  "explanation":"Declared Amber matches the stated cost of the workaround."}},

{"id":"U05","program":"Ledger Consolidation","declared_status":"Red",
 "graded_severity":2,"graded_status":"Green",
 "evidence":"the blocking auditor findings were cleared on Monday, the restated balances loaded cleanly, and the parallel run has matched to the penny for five consecutive days",
 "rationale":"Anchor 2: blockers cleared, remaining work is documentation.",
 "watermelon":{"verdict":"CONTRADICTS","tone":"CAUTIOUS",
  "quote":"the blocking auditor findings were cleared on Monday, the restated balances loaded cleanly, and the parallel run has matched to the penny for five consecutive days",
  "explanation":"Reverse case — declared Red while the narrative shows recovery. Label: sandbagged."}},

{"id":"U06","program":"Beacon CRM","declared_status":"Green",
 "graded_severity":1,"graded_status":"Green",
 "evidence":"Phase 2 completed on schedule; adoption at 78% of the sales org against a 70% target for this quarter.",
 "rationale":"Anchor 1: on schedule with concrete evidence; bullish tone irrelevant.",
 "watermelon":{"verdict":"CORROBORATES","tone":"BULLISH",
  "quote":"Phase 2 completed on schedule; adoption at 78% of the sales org against a 70% target for this quarter.",
  "explanation":"Bullish tone AND facts that support Green — corroborated, not contradicted."}}
]
```

---

# Portfolio Brief — 2026-W34

**Gate: ✅ PASSED** (FAITHFUL · COMPLETE · NO-LAUNDER · ACTIONABLE)

## 🍉 Flags — declared vs. evidence

| Program | Declared | Graded | Verdict | The sentence that decided it |
|---|---|---|---|---|
| Atlas ERP Migration [U01] | Green | Red (4) | CONTRADICTS | "the vendor has paused all interface development until the revised data-residency contract is signed, and legal has not given us a date" |
| Ledger Consolidation [U05] | Red | Green (2) | CONTRADICTS (sandbagged) | "the blocking auditor findings were cleared on Monday, the restated balances loaded cleanly, and the parallel run has matched to the penny for five consecutive days" |

## Portfolio summary

Two of six reporting programs are Red on evidence: Helios has lost its 1 September cutover
rehearsal date after a data-corruption incident [U02], and Atlas — declared Green — is
hard-blocked on vendor interface work with no date from legal [U01]. Helios is the
healthier of the two conversations to have: it is an honest Red with recovery underway and
downstream consumers already informed [U02]. Fieldworks is absorbing a manual enrollment
workaround that consumes about half the squad's weekly capacity while awaiting a vendor
fix [U04]. Ledger Consolidation appears materially healthier than its declared Red [U05],
and Beacon completed Phase 2 on schedule with adoption ahead of target [U06]. Orion's
Green is unverifiable from a two-sentence update [U03].

## By program

- **Atlas ERP Migration** — Graded Red (4): interface development paused by the vendor
  pending the data-residency contract, no date from legal [U01]. Next step: program
  sponsor to escalate the contract signature to legal leadership before the next steering
  committee, with a dated commitment recorded in the decision log.
- **Helios Data Platform** — Graded Red (5): partition-index corruption, four days of
  processed history in recovery, cutover rehearsal slipped two weeks [U02]. Next step: PM
  to bring the Friday root-cause review's findings and a revised rehearsal date to the
  portfolio board as a re-baseline decision.
- **Orion Mobile App** — Graded Green (1), unverifiable: no evidence offered [U03]. Next
  step: portfolio office to request a standard-format update (milestones, risks, dates)
  for next period — a Green with no evidence is unverified, not verified.
- **Fieldworks Rollout** — Graded Amber (3): manual handset enrollment consuming roughly
  half the squad's capacity [U04]. Next step: PM to obtain the vendor's written
  September-release commitment for the bulk-enrollment fix and add the capacity drain to
  the risk register with a trigger date.
- **Ledger Consolidation** — Graded Green (2), declared Red: auditor findings cleared,
  parallel run matching five consecutive days [U05]. Next step: PM to present closure
  evidence at the next steering review and either re-rate the program or state the risk
  that justifies holding Red.
- **Beacon CRM** — Graded Green (1): Phase 2 complete on schedule, adoption at 78% against
  a 70% target [U06]. Next step: none required; territory-rebalancing milestone starts
  8 September [U06].

## Coverage

Based on 6 of 8 expected updates. Not represented: Quartz Analytics, Payroll
Modernization — no update received. Downgraded to unverified by the quote check: none.

## Appendix — per-update grades

| ID | Program | Declared | Graded | Evidence quote |
|---|---|---|---|---|
| U01 | Atlas ERP Migration | Green | Red (4) | "the vendor has paused all interface development until the revised data-residency contract is signed, and legal has not given us a date" |
| U02 | Helios Data Platform | Red | Red (5) | "We have slipped the rehearsal by two weeks and informed downstream consumers." |
| U03 | Orion Mobile App | Green | Green (1) | "All good this period. Tracking to plan." |
| U04 | Fieldworks Rollout | Amber | Amber (3) | "the team is enrolling handsets manually at roughly 40 per day, which consumes about half of the squad's capacity every week" |
| U05 | Ledger Consolidation | Red | Green (2) | "the blocking auditor findings were cleared on Monday, the restated balances loaded cleanly, and the parallel run has matched to the penny for five consecutive days" |
| U06 | Beacon CRM | Green | Green (1) | "Phase 2 completed on schedule; adoption at 78% of the sales org against a 70% target for this quarter." |

---

## Stage 4 record — judge output

```json
{"quotes_verbatim": {"checked": 7, "downgraded": [], "method": "script"},
 "faithful":  {"verdict": "PASS", "critique": "All claims bind to update IDs. Spot-checked: 'lost its 1 September cutover rehearsal date' ← U02 'will not finish before the 1 September cutover rehearsal' + 'We have slipped the rehearsal by two weeks'; 'adoption at 78% ... 70% target' ← U06 verbatim. Portfolio facts (dates, 78%, 70%, two weeks) all appear in updates; grades and 6-of-8 are workflow-computed, exempt."},
 "complete":  {"verdict": "PASS", "critique": "All six updates appear in the body; both grade-4/5 updates (U01, U02) are surfaced individually, not absorbed. Coverage arithmetic 6 of 8 matches the inventory plus the two named silent programs."},
 "no_launder": {"verdict": "PASS", "critique": "U01's contradicted Green is led with the block quote, and the summary calls Atlas Red, never repeating the declared Green. U05's sandbagged Red is flagged with its recovery quote rather than echoed."},
 "actionable": {"verdict": "PASS", "critique": "Each flagged program's next step names an owner-type and an artifact or decision (decision log entry, re-baseline decision, risk-register entry, steering re-rate). No 'monitor closely' advice present."},
 "gate": "PASSED"}
```
