# Calibrating the gate to YOUR portfolio — the golden-set method

The rubric and judge shipped with this skill are defensible defaults distilled from systems
in production. They are not *your* ground truth. This guide is the method that turns them
into yours — the same loop that took a production release gate from **5/13 correct to 12/13
across four rubric iterations without ever changing the model**, and the discipline
(*define correct → build ground truth → measure → then tune the prompt*) behind a judge
suite whose autorater was validated against human labels before anyone trusted it.

## Why bother

Google's own guidance for AI evaluation says to validate the autorater against human
judgment before relying on it. Most teams skip the step because building ground truth feels
expensive. It is the cheapest thing you will do: a bad definition of "correct" costs the
same trust whether you're scoring 47 rows or an entire portfolio — and trust, once spent in
a governance forum, does not come back.

## The loop (Analyze → Measure → Improve)

**1. Collect 20–30 historical updates where you already know what really happened.**
Mix them deliberately: a few known watermelons (declared Green, later slipped), honest
Reds, thin Greens with no evidence, one or two sandbagged Reds, and plain healthy rows.
Real texts, lightly anonymized, beat invented ones — invented cases inherit your blind
spots.

**2. Write YOUR label first, before running the skill.** For each update: the true status
grade (1–5), the watermelon verdict, and one sentence on why. Label what the *outcome*
proved, not what you believed at the time. These labels are operator-ratified ground truth:
the skill never overrules them, and neither should you retro-fit them to match the model.

**3. Run the skill blind over the set** (paste updates without your labels). Tabulate
agreement per dimension: grade within ±1, watermelon verdict exact.

**4. Adjudicate every disagreement — in one of exactly two ways:**
- The skill was wrong → tune the RUBRIC WORDING (add an anchor example, tighten a rule) and
  re-run. Never fix a disagreement by prompt-begging ("be more careful").
- Your label was wrong (it happens — in the source system, roughly half of early gate
  failures were the *grader's* fault, e.g. bands demanding one specific synonym) → fix the
  label, and write down why.

**5. Keep every resolved disagreement as a regression row.** Next time you change a rubric
word, re-run the set; a change that fixes one case and breaks two is visible instead of
silent. Gate rule of thumb: don't trust the skill unattended below ~90% agreement on grades
and 100% on known watermelons.

## Two measured warnings

- **Binary beats scales.** A 4.9/5 average hid a 42% binary FAIL rate in the source system.
  If a stakeholder asks for a 1–10 quality score for the gate, decline: report
  PASS-rate-over-golden-set instead.
- **Brittle-but-honest graders have a virtue nobody advertises: immunity to eloquence.**
  A fluent, confident, wrong brief will charm a casual reader and an LLM judge alike; a
  quote-matching check refuses it. Keep at least one dumb check in the loop.

## What to record per golden row

```json
{"id": "G07", "update_text": "…", "declared_status": "Green",
 "label": {"severity": 4, "watermelon": "CONTRADICTS", "why": "…", "labeled_by": "you, date"},
 "skill_output_at_v1": {…}, "resolution": "rubric-tuned | label-fixed | agreed", "notes": "…"}
```
