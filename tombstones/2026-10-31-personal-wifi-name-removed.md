# Tombstone: his personal Wi-Fi network name, removed from this repository's history (2026-10-31)

At the operator's instruction ("remove it. And just put a tombstone that it was my personal Wi-Fi."), the name of
his **personal Wi-Fi network** was removed from every version of every file in this repository's history.
Nothing else was changed:
- no file was removed;
- every commit was kept (553 before, 553 after);
- the earliest commits are unchanged.

## Where it was, and what replaced it

| File | What it is | Change |
|---|---|---|
| `task-20261007-njest-2107491305077055657-ocr.md` | a memory (OCR transcript), still in the tree | each occurrence replaced by `[personal Wi-Fi name removed]` |
| `.index.db.box-store-snap-d4e393d538ff96d1` | an old binary index snapshot, history only, not a memory | each occurrence overwritten with `X` of the same length, so the file keeps its structure |

## Fingerprints, so the audit trail can be explained

The memory's entries in `audit.jsonl` (content_sha `12ffb33f1d78…` on create, `cfbee9e92447…` on update) describe
its content **before** the name was removed. They are kept as written. They will not match the redacted file, and
this tombstone is why.

| File | sha256 before | sha256 after |
|---|---|---|
| the memory transcript (latest version) | `baeb36bf9a9b0a05fb5701a67cfc40279c443e41c24a7df0deac05030dba554a` | `a5c692b249b7a6b44107d9c884b151fc16d301effea3dfbb9a069621d57b54ef` |
| the binary snapshot | `bcc922934219b61c3bd8ea28bfb6464407228b9370d89d0266b75b9cba9a76a2` | `4e9091a4b2a324cbd0a849fa5a17461638ed3d99506e612a7ed516a63b1604f4` |

## What changed for readers of this repository

- Commit IDs from the first commit that carried the name onward are new. Older clones still hold the old history.
- A complete copy of the history as it was is kept privately by the operator and is not published.

Removed by Claude (Anthropic) at the operator's direction.
