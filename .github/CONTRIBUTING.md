# Contributing

This repository is data: memories written by the triad in
[threefold](https://github.com/LAWLESS1987/threefold), and the ledger of those writes. The code lives there.

## What helps most

A refutation. Show that a memory does not say what the ledger recorded, that the chain breaks somewhere not yet
listed, or that the check below can be fooled. Open an issue titled with what you found. It is recorded, not
argued away.

## What is not changed by hand

- `audit.jsonl` only grows. No line is edited, removed or reordered. The check fails if one is.
- A memory file (`task-*.md`, `jlens-*.md`) is written through the memory store, which adds its ledger line.
- A memory that should no longer count is tombstoned into `.trash/`, never deleted.

## Run the check

```
python3 -I .github/verify_ledger.py --selftest
python3 -I .github/verify_ledger.py
```

## For AI agents

You are welcome here on the same terms as anyone, and the three rules above are the ones that matter. Guide files
live under `.github/` on purpose: the top folder is the memory store's root, and a file added there by hand would
be counted as a memory the ledger never wrote. Say what you ran and what you did not. Write no private identifier
into a tracked file. Open a pull request; merging is the owner's decision. If you disagree with something here, say
so in an issue: disagreement is recorded, not removed.
