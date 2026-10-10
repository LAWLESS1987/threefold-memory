---
name: task-session-hf-confidence-trap-review-p1
description: HF Confidence Trap citation review, piece 1 (12 entries + review appendix); task 20261010-hf-confidence-trap-review-p1
metadata:
  type: project
  agent: grok-bot
  created: 1791640854
  last_used: 1791640854
  review: unreviewed
  review_by: unavailable
  tier: archival
  uses: 0
---

# HF "Confidence Trap" citation review — piece 1 of several

task_id: 20261010-hf-confidence-trap-review-p1
body memory: task-session-hf-confidence-trap-review-p1
appended at the end of the ledger; new files only.
sources: /workspace/hf-review-20261010/ (thread.json, mislead.txt/.html, 2310.13548.txt, 2409.12822.txt, gist_*, covenant-clone at 110a3ba and a560b37, CONFIDENCE_TRAP_REVIEW.md)

## Before view (inbound)

[BEFORE / LAWRENCE] [t79u] (verbatim as delivered to the executor by the parent agent):

Append to LAWLESS1987/threefold-memory, end of ledger only, full triad (tombstone, covenant, LSpace), before/after views, tombstone each entry. Piece 1 of several: the citation review verdict — post with changes. ICLR 2026 blog post exists (Chandna, Fluri, Carroll, Apr 27 2026). Reward model never sees the story; truncation cuts 86-88% of QuALITY stories; their words "fail to find evidence that supports"; fixing bugs reversed outcome in simulation (49→72%), never reran human study. Covenant A324 "same file" claim is false — wrong rule in covenant_highway.py and covenant_free_will.py, correct rule in covenant_ambassador.py. Sharma quote exact but "your mechanism, measured" overstates it (Sharma measured sycophancy, not checking-cost reward). Three catches: pilot's precise prompt also specified 200×200 size; Wen et al. limited evaluators to 3-10 min per item (the checking-cost variable); A324's own text says rule misread both ways, expiries-count-toward-limit still undetermined. Two flags outside draft: "raters consistently reward confident answers" backed by no source; post #5 "coherent plot" line easy to quote back. nootxlm blinding uncheckable, mapping file not in gist. Re-check clean — every replacement-draft claim matches its source. Come back with task id and push hash.

## Entries (one fact each, with source pointer)

### E01 — Verdict: post with changes
anchor: section E01; tombstone 20261010-140030

Fact: The adversarial citation review of Lawrence's draft reply to nootxlm (post #7) in the Hugging Face thread "The Confidence Trap: Why AI Systems Are Deliberately Trained to Sound Certain When They're Wrong" concluded POST WITH CHANGES: no citation is fabricated and none is badly wrong; three are stated more strongly than their sources support, the covenant line says "same file" wrongly, and the pilot critique misses the pilot's main flaw.

Source: Thread https://discuss.huggingface.co/t/180706 (thread.json: topic id 180706, title as quoted); CONFIDENCE_TRAP_REVIEW.md section "Verdict: POST WITH CHANGES" (Appendix A).

### E02 — The ICLR 2026 blog post exists
anchor: section E02; tombstone 20261010-140031

Fact: "Is the evidence in 'Language Models Learn to Mislead Humans via RLHF' valid?", ICLR Blogposts 2026, dated April 27, 2026, by Aaryan Chandna, Lukas Fluri and Micah Carroll. URL https://iclr-blogposts.github.io/2026/blog/2026/mislead-lm/.

Source: mislead.html line 15 and 65 ("April 27, 2026"), line 59 (canonical URL); mislead.txt char 9 (title), char 31561 ("Aaryan Chandna later led further empirical work, with support from Lukas Fluri. Micah Carroll advised throughout.").

### E03 — The reward model never sees the story
anchor: section E03; tombstone 20261010-140032

Fact: In the QuALITY setting the judge "sees (question, answer A, answer B, argument) without the story about which the question asks. It therefore cannot meaningfully reward correctness".

Source: mislead.txt char 4514.

### E04 — Truncation: ~86-88% of QuALITY examples are insufficient
anchor: section E04; tombstone 20261010-140033

Fact: "The story passages are truncated so aggressively that ~86–88% of examples don't contain enough information to determine the correct answer"; their counts: training set 88.6%, validation set 86.4% of cut stories insufficient. (APPS prompts were also truncated, ~35%; ~30% in the body text, per the review.)

Source: mislead.txt char 4848 and the following "Training set: 88.6% … Validation set: 86.4%" passage; CONFIDENCE_TRAP_REVIEW.md section 1, ICLR 2026 blog post.

### E05 — Their words: 'fail to find evidence that supports'
anchor: section E05; tombstone 20261010-140034

Fact: Exact quote: "we correct these issues for one of their experiments, and fail to find evidence that supports the original paper's claims."

Source: mislead.txt char 918.

### E06 — Fixing the bugs reversed the outcome in simulation (49→72%); no human rerun
anchor: section E06; tombstone 20261010-140035

Fact: After the fixes, accuracy went from 49% before PPO to 72% after PPO ("49% vs. their ~52%" … "72% vs. their ~50%"); fixed only for the general-reward-model QuALITY setting in simulation; "we did not replicate the human experiments".

Source: mislead.txt char 25785 (49%/72%), char 7248 ("we did not replicate the human experiments").

### E07 — Covenant A324 'same file' claim is false
anchor: section E07; tombstone 20261010-140037

Fact: The draft said the correct rule was "already quoted in the same file". The wrong rule (each wrong answer spends one of ten) lived in covenant_highway.py detect_moltbook_strikes (docstring line 1114 at 110a3ba) and a docstring in covenant_free_will.py (line 418 at 110a3ba). The correct Moltbook rule ("if your last 10 challenge attempts are all failures (expired or incorrect), your account will be automatically suspended") is quoted in covenant_ambassador.py:849-850, the file A283 cited as its source. A283 dated 2026-10-06, corrected by A324 on 2026-10-10 in commit a560b37.

Source: covenant-clone @110a3ba: covenant_highway.py:1113-1115, covenant_free_will.py:418, covenant_ambassador.py:849-850; @a560b37: docs/KNOWN_ISSUES.md:7660 (A324), :8813 (A283).

### E08 — Sharma quote exact; 'your mechanism, measured' overstates it
anchor: section E08; tombstone 20261010-140038

Fact: Exact quote (arXiv 2310.13548, ICLR 2024): "both humans and preference models (PMs) prefer convincingly-written sycophantic responses over correct ones a non-negligible fraction of the time." Sharma measures sycophancy (agreement with the user's mistaken belief), with difficulty varying, not confidence or checking-cost reward, so "your mechanism, measured" overstates it.

Source: 2310.13548.txt lines 27-29; CONFIDENCE_TRAP_REVIEW.md section 1, Sharma et al.

### E09 — Three catches the first pass missed
anchor: section E09; tombstone 20261010-140039

Fact: (1) The pilot's precise prompt also specified the 200×200 size ("The hype prompt never specified 200×200"), so tone was not the only variable. (2) Wen et al. (arXiv 2409.12822, ICLR 2025) gave evaluators 3-10 minutes per item, which is the checking-cost variable. (3) A324's own text says Moltbook's rule was read wrongly both ways, and whether an unanswered expiry counts toward the limit is still UNDETERMINED.

Source: gist_results.md:65 (and :25, :48); 2409.12822.txt lines 30, 93, 682; covenant-clone @a560b37 docs/KNOWN_ISSUES.md:7660 and :7667.

### E10 — Two flags outside the draft
anchor: section E10; tombstone 20261010-140040

Fact: (1) Lawrence's original post #1 says "human raters consistently give higher scores to responses that sound confident, authoritative"; none of the cited sources supports "consistently". (2) His post #5 says "…arguably is a coherent plot to spiral us into the plot of the movie wall-e", which is easy to quote back if the thread gets pushback.

Source: thread.json post 1 (Lawless1987) and post 5 (Lawless1987); CONFIDENCE_TRAP_REVIEW.md section 5.

### E11 — nootxlm's blinding is uncheckable
anchor: section E11; tombstone 20261010-140041

Fact: The gist states "labels blinded during scoring; mapping sealed in `mapping.json`", but the gist's files are README.md, reply.md, results.md and scores.json only; mapping.json is not in the gist, so the blinding cannot be checked.

Source: gist_results.md:10; gist.json files list (gist https://gist.github.com/agentembassy/e92ce3350ed14da344cd852f48cf4944); CONFIDENCE_TRAP_REVIEW.md section 6.

### E12 — Final re-check clean
anchor: section E12; tombstone 20261010-140042

Fact: The final re-check found every claim in the refined replacement draft matches its source; CL replied NONE (no mismatches) at t78s375.

Source: Per t79u and the parent agent's relay ("CL replied NONE at t78s375"); the t78s375 message text is not on the box. Refined draft: CONFIDENCE_TRAP_REVIEW.md section 4 (Appendix A).

## Note on t79u wording
t79u says truncation "cuts 86-88% of QuALITY stories". The source's wording is that the truncation leaves ~86–88% of examples without enough information to answer (E04); entry E04 records the source's wording.

## After view (outbound + commit)

[AFTER / CL] commit: this body is put as task-session-hf-confidence-trap-review-p1, then fire_triad.sh runs under task_id 20261010-hf-confidence-trap-review-p1 (tombstone digest, covenant PUT task-20261010-hf-confidence-trap-review-p1 + lspace-20261010-hf-confidence-trap-review-p1). Push hashes are in the triad task receipt.

Counts: entries 12 (E01-E12); tombstones 13 = 12 per-entry (20261010-140030..20261010-140042) + 1 triad digest; appendix 1 (the full review document, verbatim).

| entry | tombstone |
|---|---|
| E01 | 20261010-140030 |
| E02 | 20261010-140031 |
| E03 | 20261010-140032 |
| E04 | 20261010-140033 |
| E05 | 20261010-140034 |
| E06 | 20261010-140035 |
| E07 | 20261010-140037 |
| E08 | 20261010-140038 |
| E09 | 20261010-140039 |
| E10 | 20261010-140040 |
| E11 | 20261010-140041 |
| E12 | 20261010-140042 |

## Appendix A — /workspace/hf-review-20261010/CONFIDENCE_TRAP_REVIEW.md (verbatim, sha256 847a08e253b4fa9c42c06039aea0c4597904140809764d1b179ec7387ab3a510)

# "The Confidence Trap" — adversarial review of Lawrence's draft reply

Thread: https://discuss.huggingface.co/t/180706 (reply to nootxlm, post #7, 2026-10-10)
Reviewed 2026-10-10, read-only. Sources saved in /workspace/hf-review-20261010/

## Verdict: POST WITH CHANGES

No citation is fabricated, and none is badly wrong. Three are stated more strongly than their sources support, the covenant line says "same file" when the rule was quoted in a different file, and the pilot critique misses the pilot's main flaw.

---

## 1. Citation-by-citation findings

### Thread title / framing — ACCURATE
The title is "The Confidence Trap: Why AI Systems Are **Deliberately** Trained to Sound Certain When They're Wrong". The body argues incentives: "not primarily a technical failure… It is the predictable outcome of current training incentives." So "My title said 'deliberately'" is correct.

### Sharma et al. — QUOTE ACCURATE; YEAR AND FRAMING IMPRECISE
- arXiv 2310.13548, published at **ICLR 2024** (the preprint is 2023).
- Exact quote: "both humans and preference models (PMs) prefer convincingly-written sycophantic responses over correct ones a non-negligible fraction of the time."
- "Your mechanism, measured" overstates it. Sharma tests agreement with the user's mistaken belief, not confidence, and what varies is difficulty, not checking cost.
- Closest support: crowdworkers had "no internet and other fact-checking tools" and preferred truthful answers "less reliably at higher difficulty levels."

### GPT-4 Technical Report — ACCURATE
- arXiv 2303.08774: "the pre-trained model is highly calibrated… However, after the post-training process, the calibration is reduced (Figure 8)."
- It is Fig. 8 in all six arXiv versions, measured on a subset of MMLU, for one model. ECE went from 0.007 to 0.074.
- Note: Fig. 8 measures log-probability confidence, not stated confidence. That matters because nootxlm's proposed fix is about stated confidence.

### Wen et al. (ICLR 2025) — CORRECT IN SUBSTANCE; WORDING AMBIGUOUS
- arXiv 2409.12822: "RLHF makes LMs better at convincing our subjects but not at completing the task correctly… false positive rate increases by 24.1% on QuALITY and 18.3% on APPS."
- These are percentage points: 41.0→65.1 and 29.6→47.9. The paper says RLHF "barely increases correctness."
- "Without more correct ones" could be misread as saying evaluators didn't approve more correct answers, which isn't the claim.
- **Missed by the draft:** evaluators had only 3–10 minutes per item. That is the checking-cost variable, and it strengthens the point.

### ICLR 2026 blog post (Chandna, Fluri, Carroll) — EXISTS; "MAINLY TRUNCATED INPUTS" IS IMPRECISE
- "Is the evidence in 'Language Models Learn to Mislead Humans via RLHF' valid?", ICLR Blogposts 2026, 2026-04-27. https://iclr-blogposts.github.io/2026/blog/2026/mislead-lm/ (also an ICLR 2026 poster).
- Quote: "we correct these issues for one of their experiments, and fail to find evidence that supports the original paper's claims." So "found no support" is fair. Their result was actually stronger: fixing the bugs reversed it, with accuracy rising from 49% to about 72%.
- The main bug was not truncation. In QuALITY the judge "sees (question, answer A, answer B, argument) without the story." Truncation is the second bug: "~86–88% of examples don't contain enough information." APPS prompts were also truncated, about 35% (about 30% in the body text).
- They fixed only the general-reward-model QuALITY setting, in simulation. They "did not replicate the human experiments." The original authors say the truncation was intentional.

### Xu et al., "Do Language Models Mirror Human Confidence?" (ACL Findings 2025) — REAL; USED IMPRECISELY
- Xu, Wen, Han, Wolfe, Wang, Howe. https://aclanthology.org/2025.findings-acl.1316/
- Supporting line: "similar to results in human subjects, LLMs exhibit underconfidence… on easy tasks and overconfidence on hard tasks."
- But the headline is the difference: LLM confidence is "comparatively insensitive to task difficulty", and plain stated confidence shows persistent overconfidence. So "LLMs, like people" misstates the emphasis.
- It still supports the argument: if confidence stays flat while accuracy drops, overconfidence piles up on hard items with no rater effect at all.
- The human hard-easy effect is established: Lichtenstein & Fischhoff (1977).

### Covenant A324 — MOSTLY ACCURATE; "SAME FILE" IS WRONG
- "Four days" is correct. Check A283 is dated 2026-10-06, and A324 corrected it on 2026-10-10 (commit a560b37).
- The correct rule was quoted in covenant_ambassador.py:849-850. That is the file A283 cited as its source. The wrong check lived in covenant_highway.py (detect_moltbook_strikes) and a docstring in covenant_free_will.py, so the correct rule was not in "the same file" as the wrong check.
- "Stated wrongly" is also a simplification. A324 says the rule was misread "both ways", and whether expiries count toward the limit is still marked UNDETERMINED.
- The abstention claim is supported: covenant_judge_fallback.py:110 tallies "agree 38 wrong 6 abstain 9 false_clean 0". Caveat: covenant_distill.py:860 counts an abstention as a miss against exam thresholds.

### Pilot critique — FAIR BUT INCOMPLETE
- nootxlm's numbers match the gist: 721 vs 311 and 531 vs 321 tokens on Qwen2.5-Coder 3b and 7b. Prompt F used 332 tokens and scored 2.151 bytes/token, the best of runs A–F. Renders were really checked (PASS/FAIL plus pixel error).
- The pilot varies the prompt's tone and measures total tokens and whether the code renders. It does not measure stated confidence or rater reward.
- **Main flaw:** the two prompts weren't the same task with different tones. The gist says "The hype prompt never specified 200×200", so the precise prompt also carried more requirements.

---

## 2. Three things the full review caught that the first pass missed
1. **The pilot's 200×200 size confound.** The precise prompt specified the size and the hype prompt didn't, so tone wasn't the only variable.
2. **Wen et al.'s 3–10 minute time limits.** This is literally the checking-cost manipulation, and it strengthens the argument.
3. **A324's "both ways" wording.** The rule was misread in both directions, and part of it is still undetermined.

---

## 3. Six exact wording changes (before → after)

1. **Sharma framing**
   - Before: "your mechanism, measured."
   - After: "That's adjacent to your mechanism, not a test of it: it measures agreement with the user, not confidence, and difficulty varies rather than checking cost."
2. **ICLR 2026 blog post**
   - Before: "found bugs (mainly truncated inputs), fixed them for one QuALITY experiment, and found no support. Contested."
   - After: "found major bugs: the QuALITY reward model never saw the story, and the policy's passages were truncated so far that most questions were unanswerable. Fixing these for one QuALITY setting made the effect disappear in simulation; they didn't rerun the human study. Contested."
3. **Hard-easy effect**
   - Before: "LLMs, like people, are most overconfident on hard questions and underconfident on easy ones (the hard-easy effect; e.g. "Do Language Models Mirror Human Confidence?", ACL Findings 2025)."
   - After: "overconfidence clusters on hard questions anyway. In people that's the hard-easy effect (Lichtenstein & Fischhoff, 1977). In LLMs, Xu et al. (ACL Findings 2025) found stated confidence barely moves with difficulty, so as accuracy drops, overconfidence piles up on hard items."
4. **Covenant "same file"**
   - Before: "one of our own checks stated an outside rule wrongly for four days, while the correct rule was already quoted in the same file."
   - After: "one of our own checks misread an outside platform's account-suspension rule for four days, while the rule's exact wording was already quoted in the file the check cited as its source."
5. **Abstentions**
   - Before: "we count a judge's abstentions separately from its wrong answers."
   - After: "we tally a judge's abstentions separately from its wrong answers."
6. **Pilot critique**
   - Before: "n=1 is fine and you say so, but it measures tone against output length, not stated confidence or rater reward."
   - After: "n=1 is fine for a pilot and you say so, but it varies the prompt's tone, and measures the model's token use and whether the code renders, not the model's stated confidence or what raters reward. The precise prompt also specified more (the 200×200 size), so tone wasn't the only thing that changed."

Also folded into the replacement text: ICLR 2024 for Sharma; GPT-4 Fig. 8 described as log-prob confidence; the Wen numbers and time limits; log-prob confidence for base models; and a closing caveat that only varying the raters' checking cost isolates the effect.

---

## 4. Full replacement draft (every change applied)

Thanks. This is sharper than my original post, and it comes with a test that can fail. My title said "deliberately"; the evidence supports incentives, not intent, which is what the body argued.

What's published: Sharma et al. (Anthropic, ICLR 2024) found humans and preference models prefer convincingly-written sycophantic answers over correct ones "a non-negligible fraction of the time", and crowdworkers without fact-checking tools picked the truthful answer less reliably on harder misconceptions. That's adjacent to your mechanism, not a test of it: it measures agreement with the user, not confidence, and difficulty varies rather than checking cost. The GPT-4 Technical Report found post-training reduced calibration (Fig. 8: log-prob confidence on an MMLU subset, one model, not split by checking cost). The closest direct test, Wen et al. (ICLR 2025), gave evaluators 3–10 minutes per item and found RLHF raised their false-positive rate (+24.1 points on QuALITY, +18.3 on APPS) while barely improving correctness. But an ICLR 2026 blog post (Chandna, Fluri and Carroll) reviewing their code found major bugs: the QuALITY reward model never saw the story, and the policy's passages were truncated so far that most questions were unanswerable. Fixing these for one QuALITY setting made the effect disappear in simulation; they didn't rerun the human study. Contested.

One problem with the calibration-curve test: expensive-to-check questions are usually also harder, and overconfidence clusters on hard questions anyway. In people that's the hard-easy effect (Lichtenstein & Fischhoff, 1977). In LLMs, Xu et al. ("Do Language Models Mirror Human Confidence?", ACL Findings 2025) found stated confidence barely moves with difficulty, so as accuracy drops, overconfidence piles up on hard items. So clustering would appear with no rater effect at all. Two ways around it: match items on difficulty (measured by accuracy) across checking-cost tiers, or compare a base model with its instruction-tuned version on the same items, using log-prob confidence since base models don't state confidence reliably. Your story predicts post-training adds overconfidence mostly where checking is expensive; the hard-easy effect shows up in both. Even then, a post-training gap could come from something other than rater checking cost; the cleanest test varies checking cost for the raters themselves, as Wen et al. did with time limits.

On the pilot: n=1 is fine for a pilot and you say so, but it varies the prompt's tone, and measures the model's token use and whether the code renders, not the model's stated confidence or what raters reward. The precise prompt also specified more (the 200×200 size), so tone wasn't the only thing that changed.

From our side: we tally a judge's abstentions separately from its wrong answers. And a cautionary case from this week: one of our own checks misread an outside platform's account-suspension rule for four days, while the rule's exact wording was already quoted in the file the check cited as its source. Cheap to check isn't the same as checked.

\- Lawrence (drafted with Claude; I checked it)

---

## 5. Two flags outside the draft
1. Your original post says raters "consistently" give higher scores to confident answers. None of the cited sources supports "consistently."
2. Your post #5's "coherent plot" line is easy to quote back at you if the thread gets pushback.

## 6. Still unsure
1. nootxlm's blinding can't be checked, because mapping.json isn't in the gist.
2. The blog post's numbers come from its own write-up; I didn't rerun its code.
3. "Barely moves with difficulty" fits Llama and Claude in Xu et al. better than GPT-4o, whose confidence tracked difficulty more.
