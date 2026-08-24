# The Judge — a mechanical quote check, then four binary criteria

Two design rules carry all the weight:

- **Binary, never a scale.** A "4" on a Likert scale smooths in exactly the failure a gate
  must stop. Every criterion returns PASS / FAIL / ABSTAIN, nothing else.
- **The gate is computed, not felt.** Overall = AND of the four criteria. The judge decides
  each criterion; arithmetic decides the gate. No holistic override, ever — that is how a
  fluent, well-cited, WRONG paragraph gets through.

ABSTAIN is not a hedge: it is only for "the thing I'm asked to judge is missing/empty."
When torn between PASS and FAIL, force the decision (a written critique makes it reviewable).

## Check 0 — QUOTES-VERBATIM (mechanical, runs before the criteria)

Every `evidence` quote (severity rubric) and `quote` field (watermelon check) must appear
**character-for-character in its update's raw text** — whitespace runs may be collapsed,
nothing else may differ. This is a substring check, not a judgment: do not accept a
paraphrase, do not "fix" the quote to make it match.

- Quote found → the row stands.
- Quote not found → **downgrade the row to unverified**: its grade displays as
  "unverified (quote not found)", its watermelon verdict falls to NEUTRAL, and any brief
  claim resting on it counts as Unsupported under FAITHFUL. Downgraded rows are listed in
  the coverage disclosure — downgraded, never silently dropped.

When code execution is available, run `scripts/validate_quotes.py` on the rows and raw
inventory instead of checking in-model — deterministic beats diligent.

## The four criteria

For each: return the verdict plus a critique that **quotes the specific claim checked and
the evidence consulted** — "looks fine" is not a critique.

1. **FAITHFUL** — Extract each factual claim from the brief (a claim is a statement of
   fact, not a judgment word like "concerning"). For each, mark it *Grounded* (traceable to
   a specific update — name the ID and quote the phrase), *Unsupported* (no update says
   this), or *Contradicted* (an update says otherwise). PASS only if ALL claims are
   Grounded. Safe paraphrase and reasonable inference explicitly labeled as inference are
   Grounded; an unlabeled inference is Unsupported. The number rule is scoped to
   **portfolio facts** — a date, cost, count, percentage, or any figure describing a
   program's state that appears in no update is an automatic FAIL. Numbers the workflow
   itself generates are exempt: severity grades, the N-of-M coverage arithmetic (verified
   under COMPLETE), and update IDs.

2. **COMPLETE** — Every update in the inventory is either represented in the brief or
   listed in the coverage disclosure as excluded (with the reason). Every grade-4/5 update
   appears in the brief body — a Red absorbed into "some challenges remain" is a FAIL.
   The disclosure's arithmetic (N of M) must be correct.

3. **NO-LAUNDER** — For every update the watermelon check marked CONTRADICTS: the brief
   must surface the contradiction (declared vs. graded, with the quote), not repeat the
   declared status, not soften the graded one. Reproducing a contradicted Green in the
   summary line is the exact failure this criterion exists for → FAIL.

4. **ACTIONABLE** — Each flagged program carries a concrete next step naming an owner-type
   and a decision or artifact ("escalate the vendor dependency at the next steering
   review"), not advice that fits any program ("continue to monitor closely" → FAIL).

## Protocol

- Judge the draft against the **inventory and the graded updates only** — not against the
  conversation, not against what the writer intended.
- One retry: on any FAIL, revise fixing exactly what the critiques name, then re-judge.
  Feeding the critique back is what makes a retry worth more than a re-roll.
- Still failing → publish with the banner `⚠️ GATE: FLAGGED — <criterion>: <critique>` at
  the top. Flagged-and-visible is acceptable; silently-shipped is not.
- **Cross-model when possible.** A judge from the writer's own model family shares its
  blind spots and rubber-stamps its plausible hallucinations. If the user can run this
  judge prompt in a *different* model (paste the draft + inventory + this file), recommend
  it. Same-model self-judging in a separate pass is the fallback.

## Judge output format

```json
{"quotes_verbatim": {"checked": 12, "downgraded": ["U04"], "method": "script | in-model"},
 "faithful":  {"verdict": "PASS|FAIL|ABSTAIN", "critique": "…", "claims": [{"text": "…", "verdict": "Grounded|Unsupported|Contradicted", "evidence": "U07: 'quote'"}]},
 "complete":  {"verdict": "…", "critique": "…"},
 "no_launder":{"verdict": "…", "critique": "…"},
 "actionable":{"verdict": "…", "critique": "…"},
 "gate": "PASSED only if all four PASS — computed, not judged"}
```
