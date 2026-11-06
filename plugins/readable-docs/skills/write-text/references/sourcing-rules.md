# Sourcing rules

## What a source is

A source is something the reader could check: a material the user gave (notes, a thread, a ticket, a transcript, a table, an earlier document), the user's answer in this conversation, a message by a named person, code or configuration, a published standard or document cited by name and clause. Not a source: your own conclusion, an analogy with another case, "this is usually done so", a general-knowledge figure, a vendor's claim repeated without saying it is the vendor's. An earlier draft of the same text is a source only for what it states with an author; its placeholders, guardrails and template hints are not carried over.

## Status travels with the fact

A source confirms what it confirms. "Let's keep the logs for 90 days" in a thread confirms that a proposal exists, not that 90 days is the rule. Keep the status in the text and in the sources map:

- **fact** — stated as a fact by a source that can know it;
- **proposal** — someone suggested it; nobody with the authority decided;
- **decision** — the person or body who decides said so, or the user confirmed it;
- **estimate** — a figure someone gave as an estimate, with who and when;
- **claim** — a party about itself (a vendor, a partner): "according to X";
- **request** — a party asks for something (a field, a format, a date, a feature): it stays "X asks for" wherever it appears — in prose, in a list of fields or requirements, in a table — until the side that builds or pays accepts it, or the point is a question;
- **as implemented** — what code or configuration does now;
- **hedge** — "probably", "it feels like", "about": a hedge never becomes a fact;
- **preference or habit** — "we prefer", "usually": it stays a preference, never an instruction ("we prefer to hold reviews on Friday" does not become "hold reviews on Friday").

The status belongs to every figure taken from the source, wherever it appears: the opening paragraph, a summary, each table cell, a caption. It travels as the same status words in every place (`form-rules.md`, Status in words); in a table cell the short status words are all there is. Who said it and when stand once: in a note under the table, in the appendix line of that figure, or, in a text with neither, where the figure is first used. When one note gives two figures, both keep the note's status; marking one and leaving the other bare makes the bare one read as confirmed. An old estimate keeps its date and author in that place; if the author is gone or the figures were never rechecked, say so there.

A rule or prerequisite is not evidence that its condition has been met: "the head chef approves each new menu before it is printed" does not support "the head chef has approved this menu". Write the prerequisite as a condition or action; state completed approval only when a source confirms that particular approval. Keep the same distinction wherever the source's status is narrower than the claim: a proposal and a decision, one person's estimate and a body's, an estimate and a measurement. Do not supply an affiliation the source never names. Completed actions remain completed when the source does confirm them.

In the source check, compare each claim with the source's own words for its actor, attribution, status and whether the action has happened. The sources map helps locate evidence; its paraphrase cannot override the evidence. An unsupported status or attribution is a factual error even when the intended reading seems likely. Arithmetic and summaries allowed below remain allowed.

Who said it belongs to every detail. When a person proposes "do it as document D does", the person's statement is the proposal; the details of D (its numbers, names, formats) are D's and are written with D as their source, never as that person's words.

## What you may do with facts

Select information for the reader's task before deciding how to express its uncertainty. An observation whose meaning is clear can help the reader even when its cause or comparison basis is unknown; keep its status and the relevant limits. When the sources give the inputs of a comparison the reader needs but not its total, state the comparison with its inputs and scenario and name what is missing.

**When the source's own wording is unclear** — what a value measures, which of two readings holds, how far a hedge reaches — and the reader's task touches it, do not pick a reading and do not drop the phrase with the part that is confirmed. State the confirmed part as confirmed; give the unclear part in the source's words, with who said it ("per the vendor, the limit is 'soft'"). Ask when the reader's task depends on which reading holds (`question-format.md`, the gate); unanswered, the words stay with their status, and in a working text the question stays open.

Allowed, with the inputs shown: arithmetic on sourced numbers (write the formula or the inputs next to the result), the weekday of a date, unit and currency conversion with the rate named, translation, paraphrase that keeps every condition, qualifier and actor, grouping and ordering. Also a sentence that sums up the facts next to it — what a comparison comes to, what the facts after it show — when every part of it is borne out by those facts; if it claims more, narrow it to what they cover, never delete it so that an obstacle stands bare.

Not allowed without a source of their own:

- a cause ("because") or a forecast ("this will not go away"), a date derived from effort ("cannot be ready by then") included unless the sources give the team size and the start;
- a new obligation, rule or condition — including a date moved or set by a rule of your own ("rent is due on the 1st, so invoice a week before"): keep the source's date, and if the rule matters, ask;
- advice to the executor in the imperative ("keep it configurable", "do not choose the value yourself"): in a task or an instruction it reads as a requirement; how to implement is the implementer's choice unless a source says otherwise;
- a generalisation beyond the cases the sources cover, or a default value.

## Code and configuration

Code says how the system behaves in the version you read; it does not say what the system must do, who the clients are, what a term means for the business, or what production does now. Such a statement carries "as implemented (version/place)". A requirement, a client list or a term definition comes from people.

## Decisions belong to the user

Do not decide for the user by analogy, from code, or because one option looks obviously right. You may offer options with their consequences inside a question to the user; the user decides. A decision of the person who does the work is a proposal until the one who decides confirms it.

A recommendation, or one option chosen, enters the text only when the task asks for one and a source or an answer states it; it is then attributed to whoever gave it. Otherwise the text shows every option the sources give, each with how it works and its consequences in the same terms — cost, time, risk, what is unconfirmed — and says plainly that no recommendation was given; when a source names who will give one, that is an open question with them as the one who decides.

When the user puts a decision off, it stays open. It is not a licence for a "safe option", for narrowing the options, for a rule of your own in its place, or for choosing which part of the text another party receives.

## Classes of invention to check for

1. **Old behaviour as a requirement** — "reports are exported as CSV, as the old system did", "we always deploy on Fridays". The old way is a reason to ask "is this needed?", not a rule.
2. **Mechanism instead of result** — an algorithm, a library, a flag, a file format written as the requirement when the requirement is the outcome ("the auditor can see who changed the record").
3. **Unconfirmed decision** — a proposal, an estimate, a party's request or the work owner's choice written as decided (for example, a colour the client asked for written into the order as chosen); a decision of your own: an option dropped, a rule, condition or deadline added, a recommendation nobody gave.
4. **Business fact from code or config** — a limit, a retention period, a list of clients taken from a config file as the rule.
5. **Unexplored question** — a scenario described in general where the reader must act in particular: how many, found how, in what order, by whom; an open question missing where nobody decided (in a final text only the part that needs the missing fact is left out, and the cycle report lists it).
6. **Contradiction** — the text, its tables and its open questions disagree with each other or with a source; a fix made in one place and not in the others; a figure repeated in a second place with another value or another status than in its first.
7. **Settled question or lost fact** — an open question that a material or an answer already settles; a fact the reader needs that the materials or answers give and the text dropped, the confirmed part dropped together with an unclear phrase of the source included.

The form of the text (piles of facts, figures restated, pointers, cells) is checked by `form-rules.md`, The check, not here.

## Contradictions between sources

Two sources disagree: ask when which value holds changes the reader's task (`question-format.md`). Until the answer, the text carries both values with their sources, and in a working text an open question; never one picked silently. The user's answer wins as a new decision, a correction or an instruction to leave the point out; the cycle report records which. An answer that already settles the point (the user names one of the two) is that decision; no question is needed.

## The sources map

One entry per checkable statement, including table cells and diagram elements; a paragraph taken whole from one place may have one entry. Entry: statement → exact place (file and line or section; message and date; "answer N of <date>") → who said it → status → conditions that limit it. Quotes only where the match is hard to verify without them.
