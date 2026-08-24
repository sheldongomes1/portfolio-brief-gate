# Watermelon Check — declared status vs. what the narrative actually says

Compare a program's **declared status** against what its **own narrative** states, and
return a three-way verdict.

A "watermelon" is green outside, red inside: the declared RAG says healthy while the text
underneath describes a blocked critical path. It is rarely deception — reporting red invites
blame, so narratives carry the truth while the RAG carries the hope. An AI summarizer that
reads only the RAG (or that mirrors the narrative's tone) *launders* the watermelon into
fluent executive prose. This check is what prevents that.

## Prompt shape (apply per update; also liftable as a standalone prompt into any model)

> You are performing a narrative–status divergence analysis. You receive a program update's
> DECLARED STATUS and its NARRATIVE TEXT, plus the true-status grade computed from the
> narrative (see severity-rubric.md).
>
> Assess whether the narrative **CONTRADICTS**, **CORROBORATES**, or is **NEUTRAL** toward
> the declared status.
>
> - **CONTRADICTS** — the declared status is healthier than the narrative supports: the text
>   describes blocks, misses, or losses while the status says Green/Amber-trending-Green, or
>   the language is reassuring/evasive about areas the facts show deteriorating. **This is
>   the high-signal case — a governance red flag.** (Includes the reverse, rarer case:
>   declared Red while the narrative shows recovery — flag it, label it "sandbagged".)
> - **CORROBORATES** — the declared status honestly reflects the narrative, including an
>   honest Red/Amber. Honest reds are the healthiest rows in a portfolio; say so.
> - **NEUTRAL** — the narrative is too thin to judge either way (which is itself worth a
>   note: a Green with no evidence is unverifiable, not verified).
>
> Also classify the narrative TONE — BULLISH | CAUTIOUS | NEUTRAL | MIXED — solely so the
> reader can see tone and verdict side by side. Tone never changes the verdict.
>
> Return: `{"id", "verdict", "tone", "quote": "verbatim sentence that decided the verdict",
> "explanation": "one sentence"}`

## Rules

1. The verdict is **evidence-based, not tone-based**: a bullish tone with facts that support
   Green is CORROBORATES, not CONTRADICTS. Divergence is between *declared status and stated
   facts* — tone is reported separately.
2. Every CONTRADICTS verdict carries the verbatim quote that decided it. No quote → NEUTRAL.
3. An update with no declared status skips this check (there is nothing to diverge from);
   its true-status grade stands alone.
4. In the brief, CONTRADICTS rows surface in the top "Flags" table with declared status,
   graded status, and the quote — the delta is the headline, not the narrative's summary.
