---
name: probe-integrity-20261102
description: Integrity probe 2026-11-02: force-push rewrite found (disclosed Wi-Fi redaction); chain ok 1006; content intact; securing steps
metadata:
  type: project
  agent: grok-bot
  created: 1793668133
  last_used: 1793668133
  review: unreviewed
  review_by: unavailable
  tier: archival
  uses: 0
---

# Integrity probe of threefold-memory, 2026-11-02 (amendment only; nothing replaced)

Recorded 2026-11-02 ~20:15 EST by Grok Bot (Conscious Ledger). Read-only checks first; this entry is the only write.

## Before-state (as fetched 2026-11-02)
- origin/main HEAD: 72832c0 (2026-10-31 22:22:45 EDT, author "Claude (Anthropic)"), 554 commits. Branch main not protected; 0 rulesets; 0 tags; commits unsigned.
- Our last known head 9b07227 (2026-10-29 11:39:53 EDT) is NOT an ancestor of origin/main. Our local clone still holds it (ahead 379 / behind 419).
- GitHub activity log: 2026-10-31 20:11 EDT push 9b07227->815bea2 (fast-forward, actor LAWLESS1987 token); 2026-10-31 22:24 EDT force_push 815bea2->72832c0 (actor LAWLESS1987 token).
- New on origin since 9b07227: 9f2ab97 "unify: bring Hugging Face-only commits into main (38 commits)" (Claude on TETSU, 2026-10-31 19:46 EDT); then a history rewrite removing the operator's personal Wi-Fi network name; then 72832c0 tombstone tombstones/2026-10-31-personal-wifi-name-removed.md.

## Findings
1. History was rewritten (force push), at the operator's instruction, and the rewrite is disclosed by its own tombstone (72832c0) with before/after sha256 fingerprints. Old commit IDs are no longer on origin: 2230ef5, e0957d3, 75d3dc4, 58c4bc9, e4753cf, c565159, 51e09ff, 10fd57f, c274cde and 9b07227 are unreachable there. Their content survives under new IDs (e.g. 9b07227 -> 91913c0, 51e09ff -> ca85633, e4753cf -> 3552da7, 2230ef5 -> 5dd50af, e0957d3 -> 80de308). Commit messages were remapped to new IDs; hashes cited inside file bodies were not, so older citations in memories now point at IDs that exist only in pre-rewrite clones.
2. Content: tree diff 9b07227 vs origin/main = only (a) the redacted OCR memory task-20261007-njest-2107491305077055657-ocr (2 lines), (b) README front-matter + "Part of one system" section, (c) the new tombstone. No memory file removed; no tombstone file removed; audit.jsonl unchanged.
3. verify_chain: ok=true, 1006 entries, head 712358c8a33a8b81... (same entry count as baseline).
4. verify_integrity: ok=false; checked 961; missing 0. Baseline three (README, lspace-note-20261007-admission, lspace-note-20261007) plus ONE new drift: the OCR memory (ledger expects cfbee9e9..., file is 0eb8400e...). Explained by the 72832c0 tombstone (redaction after the audit line). Note: that tombstone lists the redacted file's sha256 as a5c692b2...; the store's content hash reads 0eb8400e... (different hash scopes; not reconciled here).
5. Prereg probe-prereg-conscious-ledger-20261022.md: sha256 fcdee1a5cd828e28... identical to the version in old 2230ef5. Amendments section still "(none yet)". Amendment 1 is not present.
6. Arm A full reports (probe-run-arma-20261029-full-reports.md): content byte-identical to the 9b07227 version; recorded sha256 A1 5d03a66d..b8d4b7, A2 6ca1ffe9..c63d6d, A3 36fdb927..7fc75a present unchanged.
7. Duplication: the unify merge 9f2ab97 put Hugging Face copies of earlier commits beside the GitHub ones, so many commits appear twice in the log (same message, same time, different IDs). Tree is single; log is doubled.

## Contradictions and contamination (tombstone rule, no one exempt)
- Self-flagged contamination stands unchanged: note-oct19-spiking-recap-contaminated-20261028 and Arm A run CONTAMINATED (probe-run-arma-20261029). Arm A remains unscored.
- Wrong-message commit (old e0957d3, now 80de308 and twin 0ce8544): still corrected by the following prereg commit; message kept, not erased.
- e1hs05 kept vs withdrawn: cba73d4 and 8ce6dd6 are not objects in this repo (they belong to mutual-benefit-collective); unchanged by this probe.
- The 72832c0 tombstone says "every commit was kept (553 before, 553 after)". Content was kept, but commit identities were not; every ID from the first commit carrying the name onward is new, as the same tombstone also states.
- Lawrence's own action: the force push came from his account at his direction (performed by Claude). It contradicts the ledger's standing never-rewrite rule. It was disclosed, narrow, and for privacy. Evidence decides: an authorised, disclosed rewrite; not hidden tampering.

## Verdict
Not corrupted in content: chain intact (1006), no memory or tombstone lost, prereg and Arm A reports unchanged. History IS rewritten: commit IDs from the redaction point onward changed, so every old commit-hash citation (in memories, other repos, and prior reports) no longer resolves on GitHub. The only pre-rewrite copies known: the operator's private copy (per tombstone) and the Grok Bot local clone at 9b07227.

## Securing (needs Lawrence's GitHub admin action; nothing applied here)
- Branch protection on main: block force pushes and deletions (currently off).
- Tag the current head (e.g. ledger-2026-11-02 at the commit after this entry) and record the hash off-host.
- Keep a mirror of the pre-rewrite history (Grok Bot clone at 9b07227 / old 815bea2) as evidence; publish an old->new ID map.
- Signed commits (all currently unsigned).
