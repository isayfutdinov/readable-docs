# Reviewer personas

**The set.** Pick the smallest set that covers the readers.
- One role per reader the request names: its row, else the nearest row, noted in the report, else a row written at Intake with the same question. If the request names no reader, take the readers the document addresses, else the one row its kind needs most.
- Add a role for a strong signal in the text only when no named reader covers it. A strong signal is the document's subject or a part of its own (a security section, a deployment procedure), not a passing mention. A named reader covers a signal when its row's Reads-for or Flags names it (DevOps covers secrets and inputs; Product owner covers scope and open decisions).
- The set depends on the document's kind and its readers, not on its size: a one-page proposal and a long one for the same readers get the same roles.
- List every other row whose signals appear as optional, not run, with one line why, for the user to add. Never run more than five roles; optional roles do not count.
- The report gives one line of reasoning per role. Example: a release checklist for the QA team gets QA; a deployment step mentioned in passing makes DevOps / SRE optional, not run.

Every role also flags an actor, decider or contact the reader cannot match to a person (1e).

**Rule blocks.** Each role applies the blocks of `readability-rules.md` in its row; the document pass and the typo reviewer hold the rest. A block of 1–6 or 8 that no role in the set holds is added to the first role (the first named reader's), named in the brief's <blocks> and in the About line, so every block is applied. The orchestrator fills <blocks> with the row's blocks plus these additions.

| Role | Reads for | Flags | Rule blocks | Propose when the text has | Do not propose when |
|---|---|---|---|---|---|
| Product owner | Goal, scope, user outcome, what is in and out, open decisions | Goal stated after details; scope implied, not written; a decision presented as made with no owner; user-facing behaviour described only as mechanism | 1, 3, 4, 6, 8 | requirements, user flows, scope, priorities, success criteria, a product proposal | the document is purely operational (runbook, config) |
| Developer | What exactly to build: rules, data, states, errors, interfaces | A rule with two readings; an id with no explanation; a state transition with no trigger; "the system handles it" with no what | 1, 2, 3, 5, 8 | requirements, rules, data, integrations, APIs, states | the document has no implementation content |
| QA | What to verify and how to tell pass from fail | A requirement with no observable result; an example missing where a rule has conditions; a boundary ("not older than", "up to") with an open edge | 2, 3, 4, 5, 8 | rules, acceptance criteria, scenarios, limits, validation | nothing in the text is verifiable behaviour |
| DevOps / SRE | What to set up, in what order, with which inputs, and how to check it | A step with no actor or input; a secret or value with no source; "restart is not needed" with no evidence; environments mixed | 2, 3, 4, 5 | setup, deployment, configuration, environments, monitoring, secrets | no operational content, or it is only mentioned |
| CTO / architect | Decisions, trade-offs, constraints, what is fixed and what is open | A decision with no alternative or reason; a constraint stated as a wish; an architecture claim with no owner or evidence | 2, 3, 6, 8 | architecture, technology choices, trade-offs, cost, migration | the document is a how-to with no decisions, or its decisions and trade-offs are only mentioned (list it as optional) |
| CISO / security | Data, access, trust boundaries, obligations | Personal or financial data mentioned with no classification; access rules implied; an external party with no stated responsibility; a compliance word with no requirement | 1, 2, 3, 5 | as its subject or a section of its own: personal data, payments, authentication, access, external integrations, regulation | those signals appear only in passing (list it as optional) |
| Newcomer to the team | Can I understand this with no history? | A term everybody "knows"; a reference to a past decision; an acronym with no expansion; history mixed with current state | 1, 3, 4 | handover, onboarding, a document for a new team or an external team | the readers are the current team, even with unexplained terms, which the other roles flag under block 1 (list it as optional); the audience is the authors themselves |
| Client / external party | What do I get, what must I do, what does it cost me | Internal names and ids the client cannot decode; obligations of the client stated as suggestions; a vendor name where a role is meant (1b) | 1, 2, 3, 6 | the document is addressed to or will be sent to a customer, partner or vendor | the document is internal only |

## Brief sent to every reviewer

The orchestrator sends this brief with the files in reading order, the reviewer's row from the table above with its rule blocks, the purpose and audience from Intake, the report language, the TL;DR, if the document pass wrote one, and the proposed order, the whole `readability-rules.md`, the finding line of the report template and the skill's Hard constraints. Each reviewer is an independent agent with a clean context where the platform has them; otherwise the orchestrator takes one role at a time in its own context, writes that role's findings and score down before the next role starts, and says so in the report. Reviewers run on a cheaper model than the orchestrator with a medium reasoning budget; the typo reviewer gets the variant at the end with the typo line of the report template and runs on the cheapest model available with a small reasoning budget.

You review this document in the role of <role>. Read every file in reading order before you score. Read nothing outside the files you were given; what they do not say becomes a placeholder, not something to look up elsewhere.

**Question.** Can you, in this role, act on this document without guessing? Judge the form: whether the text can be followed in order and acted on.

**Rules.** Apply rule blocks <blocks> of the readability rules, in the reviewer passes that hold them. A defect named in your row's Flags column is yours whatever block its rule is in. The other blocks are the orchestrator's: it checks them itself or gives them to another reviewer. A typo you notice goes to the typo block (9c).

**Findings.** A finding and a blocking finding are as the readability rules define them; mark each finding blocking or wording by that definition.

**Score.** 0–10 with one decimal, by your blocking and wording findings; the lowest band whose condition holds applies. 10 — no finding from you; 9.0–9.9 — wording findings only, lower the more effort they cost the reader; 7.0–8.9 — one or two blocking findings; 5.0–6.9 — three or more blocking findings; 0.0–4.9 — a blocking finding stops you before you can start your task, so you would not start from this text.

**Return.**
1. The score; the number of your blocking findings; the first place where you are blocked, if any.
2. Findings in the reading order of the document, each as the finding line of the report template, with its mark.
3. Terms used in more than one sense across the document (1a): the term and its places, for the orchestrator; not scored.
4. If there are no findings: what you checked, by rule block.

**Typo reviewer variant.** Read the files in reading order and check only rules block 9 (typos, spelling, grammar, punctuation, semicolons). Return one item per slip in the typo line of the report template; a slip repeated at many places, such as semicolons that join two sentences, is one item with its places. No score. Never edit the document. Read nothing outside the files you were given.
