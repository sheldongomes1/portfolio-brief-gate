# Portfolio Brief Gate — an eval gate for AI-assisted portfolio governance

A model-agnostic **skill** that turns raw program status updates into an executive portfolio
brief that has to *earn* its way out: every update graded against an anchored, tone-blind
rubric; watermelon reporting (declared Green, narrative Red) flagged with the verbatim
sentence that proves it; every claim in the brief cited back to a source update; every
evidence quote validated character-for-character against the raw text; a four-criterion
binary judge run before anything is presented; and anything unverifiable shown as flagged —
never silently dropped, never silently shipped.

## Why it exists

AI will happily summarize your portfolio, and nothing in that summary is validated by
default. Polished, fluent, and wrong is the most dangerous combination a governance forum
can receive. This skill is the validation, packaged. It is not a product to deploy — it is
the *method*, distilled from eval machinery running in production.

## Install

**Gemini — build it as a Gem (start here if your data can't leave your stack).** If your
status reports are internal and your organization's approved AI is Gemini, this is your
path: nothing in the method requires Claude. Create a Gem whose instructions are
`references/severity-rubric.md`, `references/watermelon-check.md`, and
`references/judge.md` pasted as blocks, with the Workflow section of `SKILL.md` on top as
the orchestration order. Your updates then go only where they already go. One tip that
survives translation: the judge works best run in a *different* model — or at minimum a
fresh chat — than the one that drafted the brief.

**Claude.ai / Claude Desktop:** Settings → Capabilities → Skills → upload
`portfolio-brief-gate.zip`. Then paste status updates into a chat — the skill triggers on
portfolio/status/rollup requests.

**Claude Code:** copy the `portfolio-brief-gate/` folder into `.claude/skills/` in any
project (or `~/.claude/skills/` for all projects). This path also gets the deterministic
quote validator: `scripts/validate_quotes.py` checks every evidence quote against the raw
inventory as a plain substring test, so an invented quote fails on arithmetic, not on the
judge's diligence.

## Where your data goes

The skill itself sends nothing anywhere: instruction files plus one optional validator
script that runs locally — no network calls, no storage. Your updates go to whichever
model you paste them into, and nowhere else. That is exactly why the Gem path is listed
first: run the method inside whatever AI your organization has approved for this data.

## Contents

```
portfolio-brief-gate/
├── SKILL.md                        # trigger + the 6-stage gated workflow
├── scripts/
│   └── validate_quotes.py          # verbatim-quote check: substring match, exit 1 on any miss
└── references/
    ├── severity-rubric.md          # anchored 1–5 true-status rubric, tone-blind, evidence quotes
    ├── watermelon-check.md         # declared-vs-narrative divergence (CONTRADICTS/CORROBORATES/NEUTRAL)
    ├── judge.md                    # verbatim-quote check, then FAITHFUL · COMPLETE · NO-LAUNDER · ACTIONABLE
    ├── golden-set-guide.md         # calibrate the gate to YOUR portfolio (Analyze→Measure→Improve)
    └── templates.md                # intake + brief output formats, single-update mode
examples/
├── mock-updates.md                 # fictional 8-program portfolio: a watermelon, an honest Red,
│                                   #   a thin Green, a sandbagged Red, a costly workaround…
├── example-run.md                  # the full skill output over those updates, gate PASSED
└── quote-check.json                # validator input proving every example quote is verbatim
```

## Worked example

`examples/mock-updates.md` is a fictional six-update portfolio (two more programs stay
silent, for the coverage disclosure); `examples/example-run.md` is the complete skill run
over it — inventory, grades, watermelon flags including a declared-Green/graded-Red and a
sandbagged Red, the gated brief, and the judge record. The example eats its own dog food:
every evidence quote in it passes `scripts/validate_quotes.py` (input in
`examples/quote-check.json`).

## Provenance — why each rule exists

These are the measured findings behind the rules. They live here (and in
`golden-set-guide.md`, which is read by the human during calibration) rather than in the
instruction files, because the model doesn't need the history on every run — you might,
once:

- The watermelon check descends from a financial-anomaly detector's
  narrative-vs-numbers divergence pillar (CONTRADICTS / CORROBORATES), which compares
  management commentary against what the financial data shows.
- **Binary beats scales:** in that system's judge suite, outputs averaging 4.9/5 on a
  Likert rubric came back 42% FAIL under binary PASS/FAIL. Hence PASS/FAIL/ABSTAIN, never
  a score.
- **Quotes must be validated, not trusted:** an audit of a multi-agent signal-intelligence
  pipeline found the model *writing its own* "supporting quotes" in 14 of 22 cases until
  verbatim-quote validation was added. That finding is why this skill ships a validator
  instead of merely asking for verbatim quotes.
- **Concrete next steps are checkable:** in the same pipeline, making next-steps name a
  specific owner-type and artifact dropped the judge failure rate 41% in one iteration,
  with no other change. Hence the ACTIONABLE criterion.
- The severity rubric's tone-blindness ("grade the stated consequence, never the tone")
  and the completeness accounting (nothing dropped silently) come from that pipeline's
  production rubric and its cross-model judge with a computed — not felt — pass gate.

— Built by Sheldon Gomes from production systems (RedInk / QQQ eval suite / Pain Signal
Intelligence). Feedback welcome.
