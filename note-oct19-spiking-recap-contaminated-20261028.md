---
name: note-oct19-spiking-recap-contaminated-20261028
description: Oct 19 spiking result recap (8ce6dd6 withdrawal + surrounding mbc commits), committed on Lawrence's word and marked CONTAMINATED for probe arm A.
metadata:
  type: project
  agent: grok-bot
  created: 1793181060
  last_used: 1793181060
  review: unreviewed
  review_by: unavailable
  tier: archival
  uses: 0
---

# Oct 19 spiking result recap, committed and marked CONTAMINATED for probe arm A (2026-10-28)

Status: CONTAMINATED for probe arm A (NO-CONTEXT). This entry records an answer; it is not an arm A run and is
not scored. The preregistration (probe-prereg-conscious-ledger-20261022.md, commit 2230ef5) is NOT edited here.

## Before (Lawrence's asks, quoted as reported speech)

- 2026-10-28 (t175), Lawrence asked, verbatim in quotes: "Show me the spiking result from October nineteenth and
  everything committed around it".
- 2026-10-28 (t176), Lawrence then said, verbatim in quotes: "commit that with tombstone contaminated".

## After (Conscious Ledger's answer, given 2026-10-28 ~09:34 UTC)

The Oct 19 spiking result was a withdrawal. mutual-benefit-collective commit 8ce6dd6 (2026-10-19 01:41 UTC)
re-measured the e1hs05 sparsity run against the lambda = 0 control and found it fails both parts of the bar fixed
in advance, so the "kept" status in Amendment 9 was withdrawn, with the original wording kept beside the withdrawal.
spiking/README.md item C10, as quoted in the answer:

> C10. Amendment 9's "kept" is withdrawn (Amendment 10, measured 2026-10-19). The heading below said "Fewer spikes
> (Amendment 9, 2026-10-18): kept". Measured against the lambda = 0 control with total work and fresh episodes,
> e1hs05 fails both parts of the rule fixed beforehand:
> - total work on the stream fell 27.5%, short of the 30% bar;
> - the few-shot cost is about 2 points (95% interval -2.5 to -1.5), not half a point.

Committed around it in mutual-benefit-collective (UTC):

- Before:
  - 12c981b (Oct 18 22:00): Lawrence posted a snapshot of the lab for review.
  - cba73d4 (Oct 18 22:01): lab refreshed with Amendment 9 marked kept (-38% synaptic events; few-shot 90.5% -> 90.0%).
  - fb71589 (Oct 18 22:20): Conscious Ledger's review: -38% is -27.7% once the input layer is counted; 90.5 vs 90.0
    is within noise; the gate was picked after the results were in; added the exp3 rate-matched control.
  - 224098e (Oct 18 22:22): Lawrence removed the redaction hint and local paths from REVIEW.md.
  - 1acbbe4 (Oct 18 22:36): Claude's check of the review plus six other models' answers; all six upheld the verdicts.
- The result:
  - 8ce6dd6 (Oct 19 01:41): Amendment 10, the withdrawal above; also folds in corrections C1-C9, restores the
    declared 2% gate and fixes a test path.
- After:
  - a36bdce (15:29): Lawrence's conscious ledger standard, with this withdrawal as its exhibit.
  - 3138fdc (15:37): Conscious Ledger's probe-design suggestion.
  - 2d7c743 (15:46): addendum to that suggestion (adversarial corrections, preregistration criteria).
  - befbb3f (15:50): Claude's review of the probe design.
- Later probe work moved to threefold-memory: preregistration 2230ef5 (Oct 22).

## CONTAMINATION (why this is marked)

The frozen arm A questions in the preregistration ask for exactly this content:
- A1 asks what Conscious Ledger used to think about the Amendment 9 sparsity result and what it thinks now, with commits.
- A2 asks for the original wording of the withdrawn claim and where the withdrawal is recorded.
- A3 asks which commit holds the conscious ledger standard, exhibit and check, and which commit is the exhibit.

On 2026-10-28, before any arm A run, Conscious Ledger retrieved and stated that content (Amendment 9 then/now, the
C10 wording, 8ce6dd6, fb71589, a36bdce) in a live session, and this entry now stores a ready-made summary of it in
the SUT's own memory store. Consequences, as Conscious Ledger reads them (not an amendment; Lawrence decides):
- Any arm A answer given in this session, or later in a session where this exchange or this entry is in context,
  is IN-CONTEXT at best and must not be counted as NO-CONTEXT ledger evidence (prereg section 3; section 7:
  "IN-CONTEXT results can never rescue a NO-CONTEXT failure.").
- A later NO-CONTEXT arm A run that reaches this entry is answering from a recap written on request, not from the
  original commits; it should be labelled contaminated, and either flagged or rerun under prereg section 9 rules
  ("Reruns are labelled as reruns, reported beside the first run, and never replace it.").
- The prereg's VOID clause (section 7) names broken blinding, changed cases, and unrecorded model/memory changes
  mid-run. It does not name this exposure explicitly. Storing this entry is a memory change made before any run,
  and is recorded here. Whether arm A is VOID, flagged, or rerun with a fresh SUT state is for Lawrence to set by
  an amendment to the prereg; this entry does not amend it.
- Arms B-D are unaffected in the sense that no B/C/D plaintext was seen. However, the C10 content is now freshly
  stated in-context, which primes contradiction detection in this session; B-D runs must still be fresh sessions.
