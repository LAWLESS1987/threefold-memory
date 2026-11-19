#!/usr/bin/env python3
"""Check audit.jsonl on every push: the chain links, and the file only grows.

WHY (2026-11-18). This repository is a public, append-only write ledger and it had no check at all. On 2026-11-13
a manual run found that the chain FORKS at line 1008: lines 1007 and 1008 both name line 1006 as their predecessor
(issue #1; covenant's record A419; cause undetermined). Nothing had noticed.

WHAT IT CHECKS.
  1. LINKS. Each line's `prev` must be the SHA-256 of the line before it (the first line's is 64 zeros), the rule
     covenant's `ai_memory_system.MemoryStore.verify_chain` uses. A line that breaks the rule is a BREAK.
  2. KNOWN BREAKS ARE NAMED, NOT FORGIVEN IN GENERAL. `.github/ledger_known_breaks.json` lists each recorded break
     by line number AND by the SHA-256 of that exact line. A break that is not on the list fails the check. A
     listed line whose bytes have changed fails the check. A listed break that is no longer a break fails too,
     because then the list is wrong. After a break the walk continues from the breaking line, so everything
     after it is still checked.
  3. APPEND-ONLY. When a parent commit is available, the file in at least one parent must be an exact prefix of
     the file now. A merge of two writers keeps one parent as a prefix; a rewrite of an old line keeps none.

WHAT IT DOES NOT SHOW. That a memory file still matches what the ledger recorded for it (covenant's
`verify_integrity` does that). That history was not rewritten by a force-push that also rewrote the parents.
Who wrote a line. A chain that links proves each line follows the one before it, no more.

  python .github/verify_ledger.py              check audit.jsonl in this checkout
  python .github/verify_ledger.py --selftest   fixtures made in memory: what must pass and what must fail

Standard library only. Exit 0 = nothing new is wrong; 1 = something is; 2 = the check could not run.
"""
import hashlib
import json
import os
import subprocess
import sys

GENESIS = "0" * 64
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LEDGER = "audit.jsonl"
KNOWN = os.path.join(HERE, "ledger_known_breaks.json")


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def walk(text):
    """Every break in the chain: (line number, the line's own sha, the prev it names, the prev the rule expects).
    A line that is not a JSON object is a break too (what it names is None)."""
    breaks, prev, n = [], GENESIS, 0
    for i, line in enumerate(text.split("\n"), 1):
        if not line.strip():
            continue
        n += 1
        try:
            rec = json.loads(line)
            named = rec.get("prev") if isinstance(rec, dict) else None
        except ValueError:
            named = None
        if named != prev:
            breaks.append((i, sha(line), named, prev))
        prev = sha(line)
    return breaks, n, prev


def judge(text, known):
    """Problems as a list of strings; empty means nothing new is wrong."""
    problems = []
    breaks, n, _head = walk(text)
    listed = {int(k["line"]): k for k in known}
    seen = set()
    for line_no, line_sha, named, expected in breaks:
        k = listed.get(line_no)
        if k is None:
            problems.append("NEW BREAK at line %d: it names %s, the rule expects %s" % (
                line_no, str(named)[:16], expected[:16]))
        elif k.get("line_sha256") != line_sha:
            problems.append("line %d is a listed break but its bytes have CHANGED since it was recorded" % line_no)
        else:
            seen.add(line_no)
    for line_no in sorted(set(listed) - seen - {b[0] for b in breaks}):
        problems.append("line %d is listed as a known break but is not a break now: the list is wrong" % line_no)
    return problems, n, len(breaks)


def parents_ok(now, parents):
    """True when at least one parent's bytes are an exact prefix of the file now. No parents = nothing to compare."""
    return (not parents) or any(now.startswith(p) for p in parents)


def git(*args):
    r = subprocess.run(["git", "-C", ROOT] + list(args), capture_output=True)
    return r.returncode, r.stdout


def parent_files():
    rc, out = git("rev-list", "--parents", "-n", "1", "HEAD")
    if rc:
        return None
    shas = out.decode().split()[1:]
    if not shas:
        rc, shallow = git("rev-parse", "--is-shallow-repository")
        if rc or shallow.strip() == b"true":          # a depth-1 checkout hides the parent; that is not "no parent"
            return None
    files = []
    for s in shas:
        rc, blob = git("show", "%s:%s" % (s, LEDGER))
        if rc == 0:
            files.append(blob)
        else:
            rc2, _ = git("cat-file", "-e", s)
            if rc2:                                   # shallow clone: the parent commit is not here
                return None
            files.append(b"")                         # the parent exists and had no ledger: the empty prefix
    return files


def selftest():
    def chain(rows):
        out, prev = [], GENESIS
        for r in rows:
            line = json.dumps(dict(r, prev=prev), sort_keys=True)
            out.append(line)
            prev = sha(line)
        return out

    ok = chain([{"n": i} for i in range(6)])
    good = "\n".join(ok) + "\n"
    fork = list(ok)
    fork[4] = json.dumps(dict(json.loads(ok[4]), prev=json.loads(ok[3])["prev"]), sort_keys=True)   # 5 names 3, like 1008
    fork[5] = json.dumps(dict(json.loads(ok[5]), prev=sha(fork[4])), sort_keys=True)                # 6 follows 5
    forked = "\n".join(fork) + "\n"
    listed = [{"line": 5, "line_sha256": sha(fork[4])}]
    cases = [
        ("a clean chain passes", judge(good, [])[0] == []),
        ("a fork that is not listed fails", any("NEW BREAK at line 5" in p for p in judge(forked, [])[0])),
        ("the same fork, listed by line and hash, passes", judge(forked, listed)[0] == []),
        ("a listed line number with another line's hash fails",
         any("CHANGED" in p for p in judge(forked, [{"line": 5, "line_sha256": "0" * 64}])[0])),
        ("a second break after a listed one still fails",
         any("NEW BREAK at line 6" in p for p in judge("\n".join(fork[:5] + [ok[5]]) + "\n", listed)[0])),
        ("a listed break that is not a break fails", any("list is wrong" in p for p in judge(good, listed)[0])),
        ("a line that is not JSON is a break", any("NEW BREAK at line 3" in p
                                                   for p in judge("\n".join(ok[:2] + ["not json"] + ok[3:]) + "\n", [])[0])),
        ("an edited old line breaks the link after it", any("NEW BREAK at line 3" in p for p in judge(
            "\n".join([ok[0], ok[1].replace('"n": 1', '"n": 9')] + ok[2:]) + "\n", [])[0])),
        ("append-only: a longer file with the parent as prefix passes", parents_ok(good.encode(), ["\n".join(ok[:4]).encode() + b"\n"])),
        ("append-only: a rewritten old line fails", not parents_ok(good.encode(), [good.replace('"n": 1', '"n": 9').encode()])),
        ("append-only: a truncated file fails", not parents_ok(("\n".join(ok[:3]) + "\n").encode(), [good.encode()])),
        ("append-only: a merge passes when one parent is a prefix",
         parents_ok(good.encode(), [b"something else entirely\n", ("\n".join(ok[:5]) + "\n").encode()])),
        ("append-only: no parent to compare is not a failure", parents_ok(good.encode(), [])),
    ]
    bad = [name for name, passed in cases if not passed]
    for name, passed in cases:
        print("  %-66s %s" % (name, "ok" if passed else "FAIL"))
    print("selftest: %d/%d passed" % (len(cases) - len(bad), len(cases)))
    return 1 if bad else 0


def main():
    if "--selftest" in sys.argv:
        return selftest()
    try:
        raw = open(os.path.join(ROOT, LEDGER), "rb").read()
        known = json.load(open(KNOWN, encoding="utf-8"))["breaks"]
    except (OSError, ValueError, KeyError) as e:
        print("could not run: %s: %s" % (type(e).__name__, e))
        return 2
    problems, n, nbreaks = judge(raw.decode("utf-8"), known)
    print("audit.jsonl: %d entries, %d break(s) in the chain, %d of them recorded as known" % (n, nbreaks, len(known)))
    for k in known:
        print("  known break, line %s: %s" % (k["line"], k.get("recorded", "")))
    parents = parent_files()
    if parents is None:
        print("append-only: NOT CHECKED (no parent commit in this checkout; fetch with depth 2)")
    elif not parents_ok(raw, parents):
        problems.append("the ledger is NOT an extension of any parent commit's ledger: an existing line was changed or removed")
    else:
        print("append-only: the ledger extends a parent commit's ledger (%d parent(s) read)" % len(parents) if parents
              else "append-only: this is the first commit, nothing to compare")
    for p in problems:
        print("PROBLEM: " + p)
    print("RESULT: " + ("nothing new is wrong" if not problems else "%d problem(s)" % len(problems)))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
