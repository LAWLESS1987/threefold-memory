# Security policy

## Reporting a problem

Report a suspected vulnerability privately, by email to contact@lawless1987.com with the subject `SECURITY`.
Please do not open a public issue for a vulnerability that is not fixed yet. GitHub's private advisories are not
switched on for this repository, so email is the private road.

## What matters here

- The ledger (`audit.jsonl`): any way to change, drop or reorder a line and still pass `.github/verify_ledger.py`.
- A memory file that no longer says what the ledger recorded for it.
- Private information: if a memory here exposes something about a person that should not be public, report it
  privately the same way.

## How a finding is handled

It is reproduced, then recorded beside the thing it concerns. Nothing here is deleted to make a finding go away: a
tombstoned memory moves to `.trash/`, and a break in the chain is listed by line and hash in
`.github/ledger_known_breaks.json`. The longer policy this follows is covenant's:
https://github.com/LAWLESS1987/covenant/blob/main/SECURITY.md
