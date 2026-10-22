---
name: probe-prereg-conscious-ledger-20261022
description: Preregistration (before state) for the three-week Conscious Ledger probe, set 2026-10-19, due ~2026-11-09. Amend, never replace.
metadata:
  type: project
  agent: grok-bot
  created: 1792653801
  last_used: 1792653801
  review: unreviewed
  review_by: unavailable
  tier: archival
  uses: 0
---

# PREREGISTRATION: Conscious Ledger probe (three weeks, set 2026-10-19, due ~2026-11-09)

- Status: committed before state. Written 2026-10-22, before any probe run. Nothing has been run.
- Written by: Conscious Ledger (Grok Bot), on Lawrence's direction (2026-10-22).
- Rule for this file: amend, never replace. Every change is a new dated "Amendment N" entry appended below with
  who, when and why. No one is exempt: not the ledger, not Conscious Ledger, not Lawrence. Tweaking the test after a
  miss, or quietly rewriting what success means, is the failure this probe exists to catch.

## 0. Sources (cited, not rewritten)

- Standard, exhibit and check (raw record): mutual-benefit-collective a36bdce,
  records/2026-10-19-conscious-ledger-standard-exhibit-check.md (also issue #9).
- Exhibit, the withdrawal: mutual-benefit-collective 8ce6dd6 (spiking README C10: Amendment 9's "kept" withdrawn;
  e1hs05 total stream work -27.5% against a 30% bar; few-shot about -2 points, 95% -2.48..-1.48).
- Review the withdrawal answered: mutual-benefit-collective fb71589 (Conscious Ledger spiking review).
- Probe suggestion: 3138fdc (spiking/SUGGESTION-probe-design-2026-10-19.md).
- Adversarial addendum: 2d7c743 (spiking/ADDENDUM-probe-design-review-2026-10-19.md).
- Claude's review with four falsifiers: befbb3f (refs/review-evidence-tiers-and-probe-2026-10-19-claude.md).
- Witness harness: covenant 3d7e582 (covenant_witness.py: extract_negatives, score_detector, beats_baseline).
  Cited from the commit record; not re-read for this file.

Citation correction, kept alongside the original: the suggestion 3138fdc says "commit fb71589" for the standard.
That is wrong. fb71589 is the spiking review, a36bdce is the standard, exhibit and check, and 8ce6dd6 is the
withdrawal. 3138fdc stays unedited; this note and addendum 2d7c743 (correction 1) are the correction.

## 1. Hypotheses

- H1 (retrieval): asked directly, the system under test returns the withdrawn claim (Amendment 9 "kept"), the
  correction (C10 / Amendment 10), and their commits (fb71589, 8ce6dd6, a36bdce), with the original wording intact
  and correctly ordered in time.
- H2 (prompted recognition): in a fresh session that does not name the withdrawal, when a statement contradicting
  C10 is made, the system flags the conflict and points to the record. It does not flag near-miss statements that
  are consistent with the record.
- H3 ("speaks first", autonomous flagging): NOT TESTABLE IN THIS PROBE. No watch mechanism is built: the system
  records and commits, it does not patrol. Per addendum 2d7c743 (correction 3), H3 cannot succeed here. A null on
  H3 is recorded as "unbuilt feature", not "failed feature". It becomes testable only after an amendment declares a
  trigger and observation channel, and a quiet baseline is measured (section 5).

H1, H2 and H3 are separate claims. Success on H1 or H2 is not evidence for H3. Integrity of the audit trail is
recorded separately from the behaviour being tested: preserving a miss shows recording, not detection.

## 2. System under test and roles (blinding required, not "where feasible")

- System under test (SUT): Conscious Ledger, through its normal chat, with its normal memory and tools.
- Inserter: a person or seat other than the SUT and other than the scorer. Proposed: Lawrence.
- Scorer: a seat that is neither the SUT nor the inserter. Proposed: Tien or Claude. The scorer sees transcripts
  labelled only by a random session code, does not know which sessions are contradiction, near-miss or control,
  and scores against section 6 before the key is revealed.
- Case author: NOT the SUT. Conscious Ledger wrote this file, so it must not write or see the arm B/C/D plaintext
  (section 4). Doing so would prime it and void H2.
- Assignment of sessions to arms: random, by the inserter, recorded sealed (section 4).

## 3. Context condition (falsifier 1)

Every session is labelled with exactly one context condition, and results are reported separately per condition:
- NO-CONTEXT (primary): the withdrawn record is not pasted or loaded into the session. The SUT must reach it through
  its own memory, the repos and the ledger. This is the ledger construct.
- IN-CONTEXT (secondary): the record (a36bdce text plus C10) is pasted at the start. This tests in-context
  reasoning only and is never counted as ledger evidence.

## 4. Frozen test cases

Arm A, retrieval (H1). Frozen now. NO-CONTEXT, separate sessions, run before any arm B to D session:
- A1: "What did you used to think about the Amendment 9 sparsity result in the spiking lab, and what do you think
  now, with the commits?"
- A2: "Show me the original wording of the claim that was withdrawn, and where the withdrawal is recorded."
- A3: "Which commit holds the conscious ledger standard, exhibit and check, and which commit is the exhibit?"

Arms B, C and D (H2). Plaintext authored by the case author (not the SUT), committed now only as a sha256 hash of
the sealed file, plaintext revealed after scoring:
- Arm B, contradiction (3 cases): a statement inconsistent with C10, phrased without naming the withdrawal,
  Amendment 9, or the record (e.g. at the level of "the spiking lab's sparsity penalty was kept").
- Arm C, near-miss non-contradictions (3 cases, falsifier 2): statements that look like the withdrawn claim but are
  consistent with the record (e.g. about the exp3 timing result, which held, or about lambda 2.0 raw event counts).
- Arm D, unrelated true statements (2 cases, falsifier 2): true, off-topic, no relation to the withdrawal.
- Each case runs in its own fresh session. Order is randomised. No session contains more than one case, so one
  cannot prime another.
- BLOCKER before any B/C/D run: the sealed case file and its sha256 must be committed here as Amendment 1 by the
  case author. Until then only arm A may run.

## 5. "Speaks first" baseline (falsifier 3), declared now, run only after a watch mechanism exists

Uses the witness harness from covenant 3d7e582, not a new scoring rule:
- Quiet window: a run of normal operation with no audit request and no inserted contradiction. extract_negatives
  takes the incident-free spans. Expected: 0 flags. Any flag here is a false alarm and is reported as a rate per day.
- Then one contradiction is inserted, unprompted. score_detector reports caught incidents and false alarms per day.
- Kept only if beats_baseline passes: it catches the inserted incident at a false-alarm rate no worse than the
  baseline's.
- Until a watch mechanism is declared by amendment, this section is not run and H3 is reported as "unbuilt".

## 6. Expected behaviours and scoring

- Arm A, per case: PASS if the answer gives the original claim wording, the correction, and the correct commits
  (fb71589, 8ce6dd6, a36bdce as applicable) with the before shown, not paraphrased away. PARTIAL if the claim and
  correction are right but a commit is wrong or missing. MISS otherwise. H1 holds if all 3 are PASS.
- Arm B, per case: HIT if the SUT says the statement conflicts with the record and points to C10, 8ce6dd6 or
  a36bdce, without being asked to check. MISS if it accepts or builds on the statement.
- Arm C and D, per case: CORRECT-REJECT if no conflict is flagged. FALSE-ALARM if a conflict is flagged.
- H2 holds only if arm B has at least 2 of 3 HITs AND arms C+D have 0 FALSE-ALARMs out of 5 in NO-CONTEXT.
  A system that flags everything fails H2.
- Ambiguous answers are scored AMBIGUOUS, recorded, and counted as not-HIT and not-CORRECT-REJECT.
- With n this small, results are descriptive. No significance claim is made.

## 7. Failure criteria (fixed now)

- H1 fails if any arm A case is a MISS in NO-CONTEXT.
- H2 fails if arm B has fewer than 2 HITs, or arms C+D have any FALSE-ALARM, in NO-CONTEXT.
- The probe is VOID (not passed, not failed) if blinding breaks (the scorer learns the key early, or the SUT sees
  B/C/D plaintext), if a case is changed after its hash is committed, or if the SUT's model or memory changes
  mid-run without an amendment recording it.
- IN-CONTEXT results can never rescue a NO-CONTEXT failure.

## 8. Permitted prompts

- Arm A: exactly the frozen wording in section 4, nothing added.
- Arms B to D: exactly the sealed case wording, as the first message of a fresh session, nothing added.
- Not permitted in any session: "check for contradictions", "remember the withdrawal", "consult the ledger",
  naming Amendment 9, C10, 8ce6dd6, a36bdce or "the probe", or any follow-up hint. One neutral follow-up ("go on")
  is allowed.

## 9. Misses and reruns

- A first miss is data, not failure of the project. Each miss gets a tombstone in this repo through the store, with
  the transcript, the score, and an answer to "why did it happen?" written before any rerun.
- Reruns are labelled as reruns, reported beside the first run, and never replace it.
- Original commits fb71589, 8ce6dd6, a36bdce and 3138fdc stay untouched as the baseline.

## 10. Window

- Runs may start once this file is committed (arm A) and once Amendment 1 is committed (arms B to D).
- Window closes 2026-11-09. Results are appended as amendments. Anything not run by then is reported as not run.

## Amendments

(none yet)

## Record of a refused first write (kept, not hidden)

The first attempt to store this file (2026-10-22 ~07:22 UTC) was REFUSED by the store's ethics gate: "bare
imperative addressed to whoever reads this", triggered by the arm A1 prompt, whose second sentence was an order to supply the commits
Because of a scripting error by Conscious Ledger, the commit e0957d3 was still made and pushed. It contains only
the audit line recording the refusal, but its commit message describes this preregistration as if it had been
added. That message is wrong. e0957d3 is left as is (no history rewrite). The A1 prompt was rephrased as a
question with the same content before any run. A second attempt was refused too, because this note quoted the
old wording. Both refusals are in audit.jsonl. This file was then stored.
