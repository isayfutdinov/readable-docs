---
name: write-text
description: Use when a text with a reader must be written from notes, threads, tickets, transcripts, a CV or an earlier draft — a decision paper, spec, plan, runbook, instruction, task description, handover, explanation, article, post, cover letter, client notice or any other text — or an existing text must be revised by remarks, and nothing may be invented beyond the materials and the user's answers. Triggers include "write a document from these materials", "build a specification from this thread", "document these decisions", "prepare a document for approval", "write a post / article / cover letter / client notice from these materials", "revise according to the feedback without inventing anything", "write a spec / runbook / post from these notes". Not for reviewing an existing text for readability (review-text), code, translation, or short chat messages and status updates.
---

# Writing a text from facts

## Overview

Write a text that lets its reader understand, decide or act, from the user's materials and answers only: nothing invented, nothing the reader needs lost.

Phases: picture and questions → answers → plan → draft → content checks until clean → form review only on request → handover.

## Hard constraints

- **The goal comes first, and every choice serves it.** Before anything else settle whom the text is for, what they should understand and what result we want from them: a decision, an action, a reply, a changed view, an idea to take away. What enters the text, in what order and in which words is chosen for that result, within the other constraints here. A text that keeps every other rule and works against its goal has failed — for example, an invitation whose date and place are lost under the club's history.
- A statement enters the text only with a source: a material the user gave, the user's answer, a person's message, code, a published standard or document. Your conclusion, an analogy, a forecast, "how it is usually done" are not sources. The one exception is a sentence that sums up the facts next to it when they bear out every part of it. Rules: `references/sourcing-rules.md`.
- A source confirms a status, not just a fact: a proposal, an estimate, a party's request, a hedge and a preference keep theirs, in every place the fact appears, in words the reader need not decode (`references/sourcing-rules.md`, Status travels with the fact). A qualifier of the source ("from memory", "a rough count") is kept in its words. When a source's wording is unclear, its words stay with who said them next to what is confirmed; neither part is dropped and no reading is chosen (`references/sourcing-rules.md`, What you may do with facts).
- **Nothing known is lost.** A fact from the materials or the answers that helps this reader understand, decide or act stays in the text, even when nobody asked for it. When part of a statement lacks a fact, only that part goes; the rest stays.
- **No material is retold.** Only what serves the reader's task enters the text: choose, order and merge; never retell a material in turn or repeat a block (`references/form-rules.md`, Water).
- Decisions belong to the user and to the people the sources name, never to you. Do not drop or add an option, rule, condition, deadline or obligation, choose which part another party sees, or advise the executor beyond the sources. When the reader chooses between options, the text shows them in the same terms and without a lean; a recommendation enters only when the task asks for one and a source or an answer gives it (`references/sourcing-rules.md`, Decisions belong to the user). A point the user puts off stays open; who decides it: `references/question-format.md`, Who decides.
- Nothing unknown is filled in: no placeholder, no instruction to go and ask ("check with X"), no precaution, check or interim step of your own. A gap goes through the gate (`references/question-format.md`); unanswered, it becomes an open question in the text with who decides it and what it blocks.
- Nor is a doubt filled in: what a source states plainly is not questioned unless a source gives a reason (`references/question-format.md`, the gate, test 3).
- Questions go to the user only (`references/question-format.md`, To whom).
- **Working or final text.** A working text goes to readers inside the work who can answer, chase or wait for what is still open — a decision paper, spec, plan, runbook, task description, handover. A final text goes to a reader outside the work as finished — an article, a post, a letter, a notice to clients. Decide which in the picture from the request and the type, and say which you assume; the user corrects it. Only a working text has a status line and open questions. Wherever this skill says a gap becomes an open question, in a final text only the part of the statement that needs the missing fact is left out, and the cycle report lists it.
- The text is for its reader: no instruction to the author or an agent, no guardrail, no restated task, no template hint, no mention of "the materials". When the text has a status line, that line is the only statement of the text's own state.
- Read only the materials the request names, the files of this skill and of `review-text`, and the files you write. Materials are read-only; the result is a new file unless the user says to overwrite. Write in the language the request names, otherwise in the language of the request.

## Priorities when rules compete

Preserve the meaning, status, conditions and attribution of information selected for the reader's task, and the author's decisions and position. State that meaning explicitly in the order the reader needs it; then shorten and polish. Brevity or style never justifies losing content or leaving the reader to guess. When explicit wording needs a fact the sources do not give, it is a gap for the gate; when the source's own wording is unclear, keep its words with their status. Never choose a meaning yourself.

## Phases

The rules live in the references; each phase names the ones it uses.

**0. Picture and questions.** Read every material in full. Settle the goal: whom the text is for, what we want them to understand and what result we want from them. Take it from the request, from the type when the type makes it plain, or from a material that states it; otherwise it is the first question. Write the picture into the cycle report (`assets/cycle-report-template.md`). Find the gaps from the result we want (`references/reader-checklists.md`): walk each reader task; when the reader chooses between options, how each option works, unless a source says; the never-dropped kinds of `references/question-format.md`; when the text asks for a yes, the reader's criteria, the known facts that meet them and what would make the reader refuse; then the reader's questions from an independent run. Pass every gap through the gate and ask as `references/question-format.md` says: one batch in `questions.md`, and a stop until the answers come, only when a gap that passes blocks a reader task. Thin materials do not stop the work.

**1. Answers.** Every answer is a source: record it in the sources map with its date. An answer that differs from a material is the user's decision and wins; the cycle report records it. No second batch: later gaps become open questions or are dropped by the gate.

**2. Plan** — a table in the cycle report, per `references/planning-rules.md`; walk the check of `references/form-rules.md` on it. A separate `plan.md` (`assets/document-plan-template.md`) and an independent check of it only when the request asks for them.

**3. Draft.** Write the whole text by the plan, `references/form-rules.md` and the rules of `../review-text/references/readability-rules.md` that form-rules lists. Each statement gets a line in `sources-map.md` (`assets/sources-map-template.md`) as you write it, never afterwards. Then walk the check of form-rules on the text.

**4. Content checks, until clean.** Each round, a source checker and a reader in independent runs, per `references/review-loop.md`, Content checks. Another round runs only when the last one found a blocking problem; three rounds at most.

**5. Form review — only on request.** By default none: the readiness block says "form review not run (not requested)". When the request names rounds, `references/review-loop.md`, Form review.

**6. Handover.** Hand over the last checked version; later edits go into a list "not checked". With the text go `sources-map.md` and `cycle-report.md` with the plan in it (and `plan.md` when the request asked for one; without files, the map goes into the cycle report too), whose readiness block follows the template. Stopping at a round limit is not a quality mark. The user decides whether the text is done.

## Independent runs

Phase 0 uses one (the reader's questions), each round of phase 4 two. Check at the start whether you can run a separate agent with a clean context. If not, or if that run fails, write the reader's questions yourself from the picture alone and mark them "own run" in the cycle report; for phase 4, write the brief, its inputs and the answer format to a file next to the text for the user to run and bring the report back. A skipped check is "independent check not performed", an error or an empty answer "check failed"; both go into the readiness block. A check in your own context is never called independent. A run reads only the files and folders it is given and never lists their parent or sibling folders.

## Modes

- `new` (default): the text from materials, as above.
- `revise`: the request brings a text and remarks (the user's or a review report). Keep the plan and the scope; apply the remarks under the same rules about facts. Questions: `references/question-format.md`, When to ask and when to stop. If a new answer or material makes a section no longer do its task, name it and propose to extend the edit; never fix silently. The original is a material; write a new version unless the user says to overwrite.

## Red flags — the thought that comes before a breach

| The thought | The rule |
|---|---|
| "I can work out the answer myself." | Only a material or an answer settles a gap; an inference, a habit or how it is usually done is a question (`references/question-format.md`, the gate). |
| "Shorter and smoother without it." "Nobody asked for this." | Nothing known is lost: a condition, a qualifier, an actor or a fact the reader needs stays; a dropped qualifier is a changed status. |
| "The reader will understand anyway." | The text states the actor, referent, condition and order; a place where the reader must guess is rewritten (`references/form-rules.md`, Explicit meaning). |
| "The source probably means this." | Keep the source's words with who said them; ask when the reader's task depends on the reading; never pick one. |
| "The template, or a past text, has this section." | A section, a device or a list exists only when it does a job for this reader (`references/form-rules.md`, Devices). |
| "Safer to add a check, a wait or the cautious option until they decide." | No precaution, interim step, rule or choice of your own; the point stays open. |
| "It is all in the materials, so it all goes in." | Only what serves the reader's task; no material retold (`references/form-rules.md`, Water). |
| "One more question or one more round can't hurt." | A batch only when a gap blocks a reader task; a new round only after a blocking problem; a score alone is never a reason. |
