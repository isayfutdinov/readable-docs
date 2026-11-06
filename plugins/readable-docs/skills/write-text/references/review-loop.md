# Check loops

## Content checks (phase 4)

Each round has two independent runs with a clean context, started together where possible, on a cheaper model than yours with a medium reasoning budget.

**The source checker** gets the text, the cycle report with the plan, the materials, the answers and the sources map. It checks each statement's source and status and the classes of invention in `sourcing-rules.md`, and walks the materials and answers back to the text, even where the plan omits them. It compares each claim with the source's own words (`sourcing-rules.md`, Status travels with the fact). An error is also a doubt or open question about what a source states plainly with no source giving a reason (`question-format.md`, the gate, test 3). A sentence that sums up facts is checked against the facts it sums up. For each proposed omission it shows what the reader could not understand, decide or do without the information; presence in a source alone is not a reason to add it. It reports unsupported claims and justified omissions separately.

**The reader** gets only the text, the role and the reading task, and answers `reader-checklists.md`, For the reader check.

**Applying the findings.** Rewrite each fragment so the text itself states the needed meaning; an explanation only in a report does not fix the text. An unsupported claim is removed or narrowed to what its facts cover (`sourcing-rules.md`, What you may do with facts); a justified omission is restored. Where the unclear wording is the source's own, keep its words with their status instead of choosing a reading. A finding that needs a new fact passes the gate and becomes an open question (in a final text, only the part that needs it is left out). The rest of the form follows `form-rules.md`; walk its check after the fixes.

**Rounds.** A problem is blocking when it is an invention, a wrong status or attribution, a justified omission, or an ambiguity whose readings lead to different decisions or actions (`../../review-text/references/readability-rules.md`, Blocking). Another round, both runs on the changed sections, runs only when the last round found a blocking problem; wording findings are fixed but start no round. Stop when a round finds no blocking problem, or after three rounds; the findings still open then go into the readiness block. Record each round in the cycle report: what each run found, what was blocking, what was applied.

## Form review (phase 5)

Only when the request asks for it.

### Briefing the review

Read `../../review-text/SKILL.md` (same plugin, relative to this file) and run one round of its default review in an independent run with a clean context where possible. Give it:

- the text;
- the readers and the purpose from the picture;
- the user's glossary and the previous review report, if any (it numbers the round from that report);
- where to write its report (`review-round-<N>.md` next to the text) and in which language;
- the note "automated run: nobody can answer questions; run the reviewer set and say so in About";
- for an executor text with open blocking questions: "a draft blocked by N questions: judge the form and the clarity of the table at the end, not readiness";
- `form-rules.md` as the form the text follows, so that the review does not ask for what it forbids.

It never edits the text; this skill reads each role's score and findings from the report. If the review skill is absent, write "form review not performed" in the readiness block.

### Rounds and stopping

- No round by default. The request names the number ("review rounds: 2"; "with form review" means one); honour it and record it in the picture.
- Round 2 and later run only if the round before had a blocking finding for some role, and read the fixed text.
- A finding is **blocking** or **wording** as `../../review-text/references/readability-rules.md` defines them (its opening, "Finding" and "Blocking").
- Stop when a round has no blocking finding for any role, or at the number asked.
- A score below 9.0 is never a reason to go on; read the score together with its findings and record the findings, not the threshold.

### Applying the findings

- Apply a small fix's replacement text yourself, condition by condition against the original, only where it adds no fact. A fix that reads smoother because it dropped a condition, a qualifier or an actor is rejected.
- Apply blocking findings in every round; apply wording-only findings in round 1 only.
- A fix never adds a pointer to an open question, a hedge sentence or a status sentence to a table cell, and never adds an open question whose answer could change nothing a reader understands, decides or does. A finding that needs a fact passes the gate of `question-format.md`. A finding that proposes a precaution, a check or an interim step no source gives is dropped.
- A fix that would touch more than a third of a section rewrites the section whole from the plan and the sources map, under the form rules, instead of patching it sentence by sentence: patches accumulate hedges and pointers.
- After the last fix walk the check of `form-rules.md` and fix what it finds by rewriting.
- Rejected and dropped findings go into the cycle report with the reason. Each round is recorded there: scores per role, number of blocking findings, applied, rejected, needs a fact, and why the loop stopped.
- If a fix moved or removed a figure, the content check is repeated for that section.

### Handover

The readiness block names how many rounds ran and why the loop stopped: no blocking findings, the number asked, or "not run (not requested)". Reaching the number asked is a handover with the remaining findings, not a quality mark.
