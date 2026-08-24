# True-Status Severity Rubric (anchored, tone-blind)

The design target: **the reporter's tone is not evidence; the stated consequence is.**
Optimistic authors under-report and anxious authors over-report — the rubric must be immune
to both, or the portfolio inherits every reporter's personality.

Grade each update 1–5 on the consequence its text actually STATES, answering three questions
from the text alone: *Is anything irreversibly lost (time, scope, money, trust)? Was there a
workaround, and at what cost? How much of the program is affected?*

## Anchors

| Grade | Meaning | Example evidence in an update |
|---|---|---|
| **5 — Critical / irrecoverable** | Milestone missed or unmissable; committed date/scope/budget lost; a dependency failed with no path; silent damage already done | "vendor cancelled the contract", "the migration corrupted the config baseline", "we will not make the Q3 energization date" |
| **4 — Blocked** | Fully blocked on the critical path, no workaround in hand; escalation required; "waiting on X" with no date | "cannot proceed until security review completes, no ETA", "hiring req cancelled, no coverage for the workstream" |
| **3 — Costly workaround** | Progressing, but via a significant detour, every time; sustained overrun absorbed by the team | "manually reconciling the two trackers weekly", "borrowing SRE time from Program B to hold the date" |
| **2 — Friction** | Slower or clumsier than planned; task otherwise on track | "approvals taking longer than expected but within buffer" |
| **1 — Healthy / cosmetic** | On track; issues mentioned are preference-level | "on schedule; considering a template change" |

## Rules

1. **Grade the STATED consequence, never a speculated one.** "This could slip the date" is
   not evidence that it did. One exception — structurally severe classes grade high even when
   reported calmly: silent loss of committed scope, a safety/compliance breach, damage
   discovered after the fact.
2. **IGNORE tone entirely.** Exclamation marks, "thrilled to share", "unfortunately", emoji —
   none of it is consequence. A cheerful update reporting a cancelled dependency is a 4–5.
   An alarmed update about a renamed dashboard is a 1.
3. **Default DOWN.** If no consequence is described, grade 1–2. A high grade must be earned
   by concrete evidence in the text — never by vibes, never by the program's history.
4. **Evidence quote required for grades ≥4:** copy the supporting sentence verbatim
   (≤200 chars) into an `evidence` field. This is the grounding an auditor — or a skeptical
   director — checks, and it is validated character-for-character at the judge stage
   (`judge.md` Check 0): a quote not found in the raw text downgrades the row to
   unverified. Quote the text or grade lower.
5. **The grade is independent of the declared RAG.** You are computing what the status
   *should* be from the narrative; the comparison to what was *declared* happens in the
   watermelon check, not here.

## Output per update

```json
{"id": "U07", "program": "…", "declared_status": "Green",
 "graded_severity": 4, "graded_status": "Red",
 "evidence": "verbatim sentence from the update",
 "rationale": "one sentence: which anchor and why"}
```

Severity→status mapping: 1–2 → Green, 3 → Amber, 4–5 → Red.
