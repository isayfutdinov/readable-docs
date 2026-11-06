# Reader checklists

Phase 0 starts from the goal: whom the text is for and what result we want from them. For every reader the question is the same: what does this reader need to reach that result that no material says? Each such point, after the gate (`question-format.md`), is a question for the batch or an open question in the text; a point that enters the plan without a fact behind it is written as an open question, never skipped silently. The lists below are examples for two common readers, walked by the writer; they are questions about applicability, not sections to fill.

## The decider — can I say yes, no, or yes with conditions?

- What exactly is proposed, what do I approve, and by when?
- What happens if we do nothing?
- How does each option work? A label is not a mechanism (`question-format.md`, Never dropped).
- What does each option cost, risk and bind us to, in the same terms for every option, and where do the figures come from — measured, estimated, claimed?
- What must any option satisfy, and how will we know it worked?
- Is there a recommendation, whose (`sourcing-rules.md`, Decisions belong to the user)?
- What is still unknown, and who decides it (`question-format.md`, Who decides)?

## The executor — can I do it without asking the author?

- Why does this work exist, and when is it done — by what criterion?
- Who approves the work and whom to tell (`question-format.md`, Never dropped); what must be true before step 1?
- Who does each step — a person or role I can identify? "We", "someone" or a passive verb is not an actor.
- In what order, and where does each input come from?
- What does success look like at each step, and what do I do when a step fails?
- What is out of scope, and who decides what is left open?

For any other reader, ask the same question from their result; a reader asked for a yes (an invitation, an approval, adoption) needs their criteria met first (`form-rules.md`, When the text asks for a yes).

## The reader's questions — an independent run in phase 0

Before the batch, one independent run with a clean context, on a cheaper model than yours with a medium reasoning budget, asks as the reader. It gets:

- the reader's role and the result we want from them (the goal of the picture);
- the type of text and whether it is working or final;
- the facts per reader task from the picture, as short statements of what the text will be able to say — not the materials, and not your list of gaps.

It answers, per reader task, one line each and no advice on the text: which questions would I still have to ask the author before I could understand, decide, act, reply or reuse this; and, when the text asks me for a yes, what my criteria for a yes are, which of the facts given meet them, what would make me say no, and which facts answer it.

Each question it returns is answered by a material — then it is a fact this reader needs, and the plan places it — or it is a gap for the gate. Record the run in the cycle report: its questions, and for each, "fact placed in section N", "question N of the batch" or "dropped by the gate (reason)". Without a separate agent, or if the run fails, write the list yourself from the picture alone, as this reader, and mark it "own run".

## For the reader check

The reader checker gets only the text, the role and the reading task. Each finding names the place and its concrete effect on that task: what the reader could misunderstand, must reconstruct, cannot do, or spends unnecessary effort finding or reading. A stylistic preference alone is not a finding. There is no target number of findings; when a check finds no problem, say so. It reads in one pass, in order, and answers:

1. Can I do my task with no question to the author? It lists every place where it would have to guess or ask. A missing fact that the text itself lists as an open question, with who decides it (or "not determined") and what it blocks, is not a question to the author. An open question whose answer could change nothing I understand, decide or do is noise: it says so.
2. Does the opening give me what I need first — what is asked of me, the answer or the idea, and, when the text asks me for a yes, the facts that meet my criteria — or something I must get through first?
3. What did I have to collect from several places or work out myself to do my task, and where did the text slow me down or send me elsewhere? Where could I not tell what is decided and what is provisional?
4. For a decider: do I understand how each option works, what it costs and what follows from it — or does the text list it as an open question?
5. Which references, terms or people did I not identify in context? Can I tell who decides each open question and whether they are available when needed? Give a clearer wording when the text supports it, or say what remains unknown.
6. Will I do what this text wants of me — invite, approve, act, reply, take the idea? If not, what stops me, and where?
7. Meaning that needs a rewrite: each place where I chose between readings or supplied an unstated actor, referent, relation, condition or order needed for my task, with the readings or the missing link. It is a finding even when I guessed right; it is blocking when the readings lead to different decisions or actions (`../../review-text/references/readability-rules.md`, Blocking), otherwise wording. Do not judge a clear paraphrase I supplied as though it were in the text. Explicit unknowns are not ambiguities, and details outside my task are not missing links. I check whether the meaning is explicit, not whether it is factually true. Return the list, or "none".
