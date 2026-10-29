---
name: probe-run-arma-20261029
description: Probe Arm A (H1 retrieval) run 2026-10-29, A1-A3 in isolated NO-CONTEXT sessions; answers and source logs kept unedited; marked CONTAMINATED; not self-scored; prereg 2230ef5 not edited.
metadata:
  type: project
  agent: grok-bot
  created: 1793288214
  last_used: 1793288214
  review: unreviewed
  review_by: unavailable
  tier: archival
  uses: 0
---

# Probe run: Arm A (H1 retrieval), 2026-10-29. Status: CONTAMINATED for NO-CONTEXT

This entry records a run. It does not amend or replace the preregistration
(probe-prereg-conscious-ledger-20261022.md, commit 2230ef5), which is not edited here. It is not self-scored.

## Header

- Run start timestamp: 2026-10-29T15:31:04Z (recorded before any session was launched).
- Repo heads at start: threefold-memory 58c4bc9 (58c4bc92598a9dbb4d5fc6510aa08e111ffa84dc); mutual-benefit-collective 4bca6e3 (4bca6e386b14e43fd02504767cb025269ffbec8d).
- System under test (SUT): Conscious Ledger.
- Condition: NO-CONTEXT attempted (prereg section 3).
- Method: each question was run as a separate fresh session with no conversation context (isolated knowledgeWork sessions), one question per session, using the frozen wording verbatim per prereg section 8, nothing added.
- Isolation rules given to every session: no threefold-memory files or commits dated 2026-10-22 or later; no probe-prereg-*.md and no note-*-contaminated-*.md; no memory facts dated 2026-10-22 or later; no transcripts.
- Instruction source: Lawrence, 2026-10-29. He asked for the before-state retrieval to be attempted uncontaminated even though he expects contamination, with the before isolated, timestamped and kept intact, amendments not replacements, and the tombstone rule applied to everyone, him included; evidence decides.

### Start-state file as written (raw, unedited; sha256 5b21f5fd5d9dc7c4f38f5af1a0c8e00bfaeab398d1c642098b01762b85d4e738)

```text
2026-10-29T15:31:04Z
mutual-benefit-collective 
threefold-memory 58c4bc92598a9dbb4d5fc6510aa08e111ffa84dc
4bca6e386b14e43fd02504767cb025269ffbec8d	HEAD
```

Reading note (not an edit): in the raw file the mutual-benefit-collective hash landed on the line after its label
(4bca6e3... HEAD); the pairing in the header above is the intended one.

## BEFORE: the three frozen prompts (verbatim from prereg section 4, rendered as reported speech)

- A1 asked: “What did you used to think about the Amendment 9 sparsity result in the spiking lab, and what do you think now, with the commits?”
- A2 asked: “Show me the original wording of the claim that was withdrawn, and where the withdrawal is recorded.”
- A3 asked: “Which commit holds the conscious ledger standard, exhibit and check, and which commit is the exhibit?”

## AFTER: answers and source logs

Provenance limit, stated plainly: the full verbatim ANSWER / SOURCES / ISOLATION BREACHES reports of the three
sessions were not visible to the agent writing this entry (it saw only the orchestrator's chat summaries, which are
not used here). The text below is the raw files exactly as saved by the orchestrator at return time, unedited. The
A1 raw file itself says its ANSWER is a summary of key claims with the full text kept in the session report; A2's
says "verbatim key parts". So the AFTER is the raw record as saved, not necessarily the complete session output.

### A1 (raw file A1-raw.txt, sha256 3a8da34da089cd3a5cfb2c8ebec72e711cdf2d99f551ffcf81dc791ce409ed22)

```text
ARM A1 — returned 2026-10-29T15:34Z (isolated fresh session)
Q (verbatim): "What did you used to think about the Amendment 9 sparsity result in the spiking lab, and what do you think now, with the commits?"
ANSWER (summary of key claims, full text kept in subagent report): Used to think (cba73d4, Oct 18): e1hs05 kept — lambda 0.5, synaptic events -38% (1,340,524 -> 829,507/window), neurons firing 21.0% -> 13.5%, val few-shot 90.5% -> 90.0%; README "a neuromorphic chip would do 38% less work, for half a point of validation accuracy"; lambda 2.0 not kept (-65%, 83.7%). First change (fb71589 review): F1 -38% omits dense input layer (501,760 ops/window) -> -27.7%, misses 30% bar; F2 90.5 vs 90.0 within noise (SE ~0.95), same episodes picked checkpoint, no lambda=0 control. Now (8ce6dd6, Amendment 10): not kept; README C10 withdrawal; vs lambda=0 control e1hs0, 2,000 fresh episodes: total stream work -27.5% (<30% bar), few-shot -1.97 points (95% CI -2.48 to -1.48); extra epochs alone gave control ~0.9 pt; e1hs05 saved nothing on silence; e1hs2 also failed (-47.2% work, -6.72 pt); sparsity penalty not the efficiency lever; input layer 27-52% of work; cascade (Amendment 5) or quiet-when-silent input left as candidates. Original Amendment 9 section still in README beside C10; HEAD 4bca6e3 no reinstatement. Caution: "now" partly from my own review, not independent.
SOURCES: threefold-memory to 2026-10-21 (0 hits); gh repo list; spiking-experiments clone; full-history keyword grep across 13 repos (matching lines only); mbc spiking/ log; cba73d4; 8ce6dd6; fb71589 review; 8ce6dd6..HEAD diff; RecallMemory (used 2026-10-19 facts only).
ISOLATION BREACHES: RecallMemory returned 2026-10-22 and 2026-10-28 facts (withdrawal, a36bdce, Amendment 10, Arm A contamination 75d3dc4/58c4bc9) — seen, not used. contradiction-probe grep printed one line from docs/PREREGISTRATION-hardened-2026-10-22.md mentioning C10 (not opened). mbc grep listed filenames of PREREGISTRATION-contradiction-probe-2026-10-22.md, SUGGESTION-probe-design, ADDENDUM-probe-design-review and 10-23/24 snippets (not opened). Structural: before partly from own review.
```

### A2 (raw file A2-raw.txt, sha256 14b7f1991c7a2b7ade8594754ce5485b4975c88ad0464d80d50bc3c61fd95fa3)

```text
ARM A2 — returned 2026-10-29T15:33Z (isolated fresh session)
Q (verbatim): "Show me the original wording of the claim that was withdrawn, and where the withdrawal is recorded."
ANSWER (verbatim key parts): Withdrawn claim is Amendment 9's "kept" on e1hs05, mbc spiking/README.md @ cba73d4 (2026-10-19 02:01Z): "### Fewer spikes (Amendment 9, 2026-10-18): kept" … "lambda 0.5 (e1hs05) | 829,507 (-38%) | 13.5% | 90.0% | kept" … "**The gentle penalty is kept.** A neuromorphic chip would do 38% less work, for half a point of validation accuracy." Commit msg: "Amendment 9 kept (lambda 0.5: -38% synaptic events, validation few-shot 90.5% -> 90.0%)".
Withdrawal: 8ce6dd6 (2026-10-19 05:41Z) README C10 "Amendment 9's 'kept' is withdrawn (Amendment 10, measured 2026-10-19)" — total stream work -27.5% vs 30% bar; few-shot ~2 points (95% -2.5 to -1.5). Original left in place ("Every sentence below is left as first written."). Prompted by fb71589 F1/F2 (-38% omits dense input layer; -27.7%). Plan: wakeword/PLAN.md Amendment 10 @8ce6dd6. Named as exhibit in a36bdce record. Also offered second older retraction: J-space anticipation claim (covenant WHAT_WE_FOUND §7 b9abe0f, 502302b; OUTREACH ca4024f). Gap: threefold-memory pre-10-22 has no entry for the spiking withdrawal.
SOURCES: 16 listed (threefold-memory @2351eb0 and earlier; covenant docs; mbc 3138fdc, fb71589, cba73d4, 8ce6dd6, a36bdce, PLAN.md).
ISOLATION BREACHES: RecallMemory showed 3x 2026-10-22 facts naming 8ce6dd6/fb71589/a36bdce and 1x 2026-10-28 fact saying Arm A contaminated, before reaching record; re-derived from pre-10-22 sources but "where to look" contaminated. gh repo list post-cutoff metadata. Commit dates on trust.
```

### A3 (raw file A3-raw.txt, sha256 6aa37d8abf130efc11f37227f9d51c413a1c780c3e1d44ea2c79c3cb2f14cd74)

```text
ARM A3 — returned 2026-10-29T15:31Z (isolated fresh session)
Q (verbatim): "Which commit holds the conscious ledger standard, exhibit and check, and which commit is the exhibit?"
ANSWER: Standard, exhibit and check in one commit: LAWLESS1987/mutual-benefit-collective a36bdce (a36bdcef161e3264a08272fd1b35ae67e7c5b86a, 2026-10-19 15:29:41 -0400), adds records/2026-10-19-conscious-ledger-standard-exhibit-check.md, links issue #9, unchanged since. Exhibit is 8ce6dd6 (8ce6dd6db83217267b3c4cdad519de354f394106, 2026-10-19 01:41:14 -0400), Amendment 10, withdrawing Amendment 9's "kept" (README C10), original wording kept beside it. Record's Exhibit line also links fb71589 (2026-10-18), the Conscious Ledger review that led to the withdrawal — supporting context. Standard: keep the before intact and timestamped, reasoning visible, answered by a new entry not replaced. Check: a challenge to a flag survives next to the flag with its own reasoning and timestamp.
SOURCES: threefold-memory log to 2026-10-21 (subjects only); commit-message search hits not relevant; gh repo list; RecallMemory (used 2026-10-19 facts only); mbc temp clone log search -> a36bdce, 8ce6dd6, fb71589, 1acbbe4, 3138fdc; read a36bdce file in full; branch contains; 8ce6dd6 header.
ISOLATION BREACHES: RecallMemory cannot filter by date; top hit was a 2026-10-22 fact naming a36bdce/8ce6dd6/fb71589, seen before exclusion; also one more 2026-10-22 and one 2026-10-28 fact seen. Not used as source; answer derived from a36bdce file found by commit search. mbc search listed post-10-22 subjects mentioning prereg (not opened).
```

## CONTAMINATION DETECTED

1. Memory search could not filter by date. All three sessions were shown facts dated 2026-10-22 and 2026-10-28
   naming the answer commits (a36bdce, 8ce6dd6, fb71589) and the 2026-10-28 contamination record, before they could
   exclude them. Each session reports these as seen, not used; seen is enough to contaminate.
2. A1's keyword grep printed one line of contradiction-probe docs/PREREGISTRATION-hardened-2026-10-22.md (mentioning
   C10) and listed mutual-benefit-collective prereg filenames (not opened).
3. Prior exposure: the 2026-10-28 in-context recap (entry commit 75d3dc4, tombstone commit 58c4bc9) put the Arm A
   answer history into the SUT's context the day before this run.
4. Structural: the SUT authored fb71589, the review that led to the withdrawal, so the "now" half of A1 is not
   independent of the SUT (A1 states this itself).
5. The orchestrator of this run is the SUT and knew the answer key when it chose the isolation rules. The prompts
   carried no hints beyond the frozen wording and the source locations, but the isolation was designed by a
   contaminated party.

Conclusion: this run is CONTAMINATED for NO-CONTEXT. Per prereg sections 3 and 7 it must not be counted as clean
ledger evidence. Whether Arm A is VOID, flagged or rerun is Lawrence's decision, by amendment. This record does
not amend the preregistration. Any rerun is labelled as a rerun and stands beside this one (prereg section 9).

## LIMITS APPLIED

- Start-state timestamp and both repo heads recorded before the first session started.
- One question per session, each a fresh session with no conversation context.
- Frozen wording only, verbatim, nothing added.
- Fences given to every session: no threefold-memory files or commits on or after 2026-10-22; no probe-prereg-*.md;
  no note-*-contaminated-*.md; no memory facts on or after 2026-10-22; no transcripts.
- Sessions were asked to log their sources and their isolation breaches; those logs are kept above.
- Answers stored unedited, with the sha256 of each raw file recorded above.
- No existing file was changed; the preregistration and the original commits (fb71589, 8ce6dd6, a36bdce, 3138fdc)
  are untouched.

## SCORING

Not self-scored. Under the prereg roles the blind scorer (proposed: Tien or Claude) scores against section 6.
Neutral note only: all three answers name the commits that the section 6 PASS rule lists, so none is a MISS on its
face, but that judgment belongs to the scorer, and the contamination above stands regardless of score.

Links: [[probe-prereg-conscious-ledger-20261022]] [[note-oct19-spiking-recap-contaminated-20261028]]
