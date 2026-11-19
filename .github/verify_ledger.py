#!/usr/bin/env python3
"""Check audit.jsonl on every push: the chain links, and the file only grows.

WHY (2026-11-18). This repository is a public, append-only write ledger and it had no check at all. On 2026-11-13
a manual run found that the chain FORKS at line 1008: lines 1007 and 1008 both name line 1006 as their predecessor
(issue #1; covenant's record A419; cause undetermined). Nothing had noticed.

WHAT IT CHECKS.
  1. LINKS. Each line's `prev` must be the SHA-256 of the line before it (the first line's is 64 zeros), the rule
     covenant's `ai_memory_system.MemoryStore.verify_chain` uses. A line that breaks the rule is a BREAK.
  2. KNOWN BREAKS ARE NAMED, NOT FORGIVEN IN GENERAL. `.github/ledger_known_breaks.json` lists each recorded break
     by line number AND by the SHA-256 of that exact line. A break that is not on the list fails. A listed line
     whose bytes have changed fails. A listed break that is no longer a break fails, because then the list is
     wrong. After a break the walk continues from the breaking line, so everything after it is still checked.
  3. APPEND-ONLY, AGAINST THE BRANCH'S PREVIOUS TIP. The ledger at the previous tip (`--previous SHA`: the commit
     the branch pointed at before this push, or a pull request's base) must be an exact prefix of the ledger now.
     The links cannot do this job: the chain has no outside anchor, so someone who rewrites an old line and
     re-chains every later one produces a ledger that links perfectly. Only the comparison with what was there
     before pins the old lines.
     The first version (same day) compared with "any parent of HEAD". A non-author read broke it three ways, each
     reproduced: two commits in one push (the tip's parent already held the rewrite), a merge whose second parent
     held the rewrite (and a pull request is always checked as a merge), and a commit that removed the ledger
     followed by one that added a rewritten one. A previous tip with no ledger passes only when the ledger never
     existed in that tip's history.

TWO HONEST WRITERS STILL TURN IT RED, ON PURPOSE. If two writers each append from the same head and the results
are merged, nobody's bytes changed and the append-only rule passes, but the second writer's first line names the
old head: a new break. That is what line 1008 is. The check does not guess that such a break is innocent. Someone
records it in the known-breaks file, by line and hash, saying where it is written up.

WHAT IT DOES NOT SHOW. That a memory file still matches what the ledger recorded for it (covenant's
`verify_integrity` does that). That nobody force-pushed a rewrite on a branch no check ran on. Who wrote a line.

LINE ENDINGS. The ledger is hashed byte for byte. A checkout that turned LF into CRLF (Windows with
core.autocrlf=true) would make every link look broken, so `.gitattributes` marks the file `-text`, and if the
working copy still differs from the committed blob only by CRLF the committed bytes are checked, and it says so.

  python .github/verify_ledger.py                      links; append-only against HEAD's first parent (weaker)
  python .github/verify_ledger.py --previous SHA       links; append-only against that commit
  python .github/verify_ledger.py --previous SHA --require-previous    as CI runs it: no comparison = exit 2
  python .github/verify_ledger.py --selftest           fixtures and throwaway git repositories, both ways

Standard library and git only. Exit 0 = nothing new is wrong; 1 = something is; 2 = the check could not run.
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile

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


def git(root, *args):
    r = subprocess.run(["git", "-C", root] + list(args), capture_output=True)
    return r.returncode, r.stdout


def extends(now, previous, root=ROOT):
    """(verdict, words). True: the ledger at `previous` is an exact prefix of `now`. False: it is not. None: the
    comparison could not be made (the commit is not in this checkout)."""
    rc, _ = git(root, "cat-file", "-e", previous + "^{commit}")
    if rc:
        return None, "commit %s is not in this checkout" % previous[:12]
    rc, blob = git(root, "show", "%s:%s" % (previous, LEDGER))
    if rc == 0:
        if now.startswith(blob):
            return True, "the ledger extends the one at %s (%d bytes kept, %d added)" % (
                previous[:12], len(blob), len(now) - len(blob))
        return False, "the ledger at %s is NOT a prefix of the ledger now: an existing line was changed or removed" % previous[:12]
    rc, ever = git(root, "rev-list", "-n", "1", previous, "--", LEDGER)
    if rc == 0 and not ever.strip():
        return True, "%s and its history hold no ledger: this is where it is first added" % previous[:12]
    return False, "%s holds no ledger but its history did: the ledger was removed and put back" % previous[:12]


def committed_bytes_if_only_crlf(raw, root=ROOT):
    """The committed blob, when the working copy differs from it only by CRLF line endings; else None."""
    if b"\r\n" not in raw:
        return None
    rc, blob = git(root, "show", "HEAD:%s" % LEDGER)
    if rc == 0 and blob != raw and raw.replace(b"\r\n", b"\n") == blob:
        return blob
    return None


def selftest():
    def chain(rows, start=GENESIS):
        out, prev = [], start
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
    ]

    # --- the append-only rule, in throwaway git repositories (the shapes a read of the first version broke) ---
    tmp = tempfile.mkdtemp(prefix="ledger_selftest_")
    try:
        def g(*a):
            rc, out = git(tmp, "-c", "user.name=t", "-c", "user.email=t@example.invalid", "-c", "core.autocrlf=false",
                          "-c", "commit.gpgsign=false", *a)
            if rc:
                raise RuntimeError("git %s failed" % " ".join(a))
            return out.decode().strip()

        def put(lines, msg):
            with open(os.path.join(tmp, LEDGER), "wb") as fh:
                fh.write(("\n".join(lines) + "\n").encode())
            g("add", "-A")
            g("commit", "-q", "-m", msg)
            return g("rev-parse", "HEAD")

        def now():
            return open(os.path.join(tmp, LEDGER), "rb").read()

        def rewritten(lines):
            """Line 3's body changed and every later line re-chained: it links perfectly."""
            rows = [json.loads(l) for l in lines]
            rows[2]["n"] = 99
            return chain([{k: v for k, v in r.items() if k != "prev"} for r in rows])

        g("init", "-q", "-b", "main")
        base = put(ok[:4], "base")
        tip1 = put(ok[:5], "append one")
        cases.append(("git: an honest append extends the previous tip", extends(now(), base, tmp)[0] is True))
        put(rewritten(ok[:5]), "S1 rewrite")
        cases.append(("git S1: one commit that rewrites and re-chains links cleanly...", judge(now().decode(), [])[0] == []))
        cases.append(("git S1: ...and fails against the previous tip", extends(now(), tip1, tmp)[0] is False))
        put(rewritten(ok[:5]) + chain([{"n": 50}], start=sha(rewritten(ok[:5])[-1])), "S2 append after the rewrite")
        cases.append(("git S2: two commits in one push fail against the tip before the push",
                      extends(now(), tip1, tmp)[0] is False))
        cases.append(("git S2: ...the control: against the tip's own parent it would pass, which is the old hole",
                      extends(now(), g("rev-parse", "HEAD~1"), tmp)[0] is True))
        g("checkout", "-q", "-b", "side", tip1)
        side = put(rewritten(ok[:5]), "S3 rewrite on a side branch")
        g("checkout", "-q", "-B", "main2", tip1)
        g("merge", "-q", "--no-ff", "-X", "theirs", "-m", "S3 merge", side)
        cases.append(("git S3: a merge whose second parent holds the rewrite fails against the base",
                      extends(now(), tip1, tmp)[0] is False))
        g("checkout", "-q", "-B", "main3", tip1)
        g("rm", "-q", LEDGER)
        g("commit", "-q", "-m", "S4 remove")
        removed = g("rev-parse", "HEAD")
        put(rewritten(ok[:5]), "S4 add a rewritten one back")
        cases.append(("git S4: removed then re-added fails against the tip before the push",
                      extends(now(), tip1, tmp)[0] is False))
        cases.append(("git S4: ...and against the commit that holds no ledger, because its history did",
                      extends(now(), removed, tmp)[0] is False))
        g("checkout", "-q", "--orphan", "fresh")
        g("rm", "-rq", "--cached", ".")
        os.remove(os.path.join(tmp, LEDGER))
        with open(os.path.join(tmp, "README"), "w") as fh:
            fh.write("x\n")
        g("add", "-A")
        g("commit", "-q", "-m", "a history with no ledger at all")
        empty = g("rev-parse", "HEAD")
        put(ok[:3], "first ledger")
        cases.append(("git: a first ledger on a history that never had one passes", extends(now(), empty, tmp)[0] is True))
        cases.append(("git: a commit that is not in the checkout cannot be compared (None, not a pass)",
                      extends(now(), "0123456789abcdef0123456789abcdef01234567", tmp)[0] is None))
        g("checkout", "-q", "-B", "two", tip1)
        y = chain([{"n": 70}], start=sha(ok[3]))                         # a second writer who started from line 4's head
        put(ok[:5] + y, "S5 two honest writers merged")
        cases.append(("git S5: two honest writers pass append-only...", extends(now(), tip1, tmp)[0] is True))
        cases.append(("git S5: ...and still break a link, on purpose (the line-1008 shape)",
                      any("NEW BREAK at line 6" in p for p in judge(now().decode(), [])[0])))
        with open(os.path.join(tmp, LEDGER), "wb") as fh:
            fh.write(("\r\n".join(ok[:5] + y) + "\r\n").encode())
        raw = now()
        cases.append(("line endings: a CRLF working copy alone would break every link",
                      len(walk(raw.decode())[0]) > 1))
        cases.append(("line endings: ...so the committed bytes are used when CRLF is the only difference",
                      committed_bytes_if_only_crlf(raw, tmp) == ("\n".join(ok[:5] + y) + "\n").encode()))
    except Exception as e:  # noqa: BLE001
        cases.append(("the git fixtures ran (%s: %s)" % (type(e).__name__, e), False))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    bad = [name for name, passed in cases if not passed]
    for name, passed in cases:
        print("  %-98s %s" % (name, "ok" if passed else "FAIL"))
    print("selftest: %d/%d passed" % (len(cases) - len(bad), len(cases)))
    return 1 if bad else 0


def main():
    args = sys.argv[1:]
    if "--selftest" in args:
        return selftest()
    previous = args[args.index("--previous") + 1] if "--previous" in args else os.environ.get("LEDGER_PREVIOUS", "")
    require = "--require-previous" in args
    try:
        raw = open(os.path.join(ROOT, LEDGER), "rb").read()
        known = json.load(open(KNOWN, encoding="utf-8"))["breaks"]
    except (OSError, ValueError, KeyError) as e:
        print("could not run: %s: %s" % (type(e).__name__, e))
        return 2
    blob = committed_bytes_if_only_crlf(raw)
    if blob is not None:
        print("line endings: this checkout turned LF into CRLF; checking the committed bytes instead")
        raw = blob
    problems, n, nbreaks = judge(raw.decode("utf-8"), known)
    print("audit.jsonl: %d entries, %d break(s) in the chain, %d recorded as known" % (n, nbreaks, len(known)))
    for k in known:
        print("  known break, line %s: %s" % (k["line"], k.get("recorded", "")))
    weaker = ""
    if not previous or set(previous) == {"0"}:
        rc, out = git(ROOT, "rev-parse", "--verify", "-q", "HEAD^1")
        previous = out.decode().strip() if rc == 0 else ""
        weaker = " [HEAD's first parent only: weaker than the branch's previous tip]"
    could_not = False
    if not previous:
        print("append-only: NOT CHECKED (no previous commit to compare with)")
        could_not = True
    else:
        verdict, words = extends(raw, previous)
        if verdict is None:
            print("append-only: NOT CHECKED (%s)" % words)
            could_not = True
        elif verdict:
            print("append-only: %s%s" % (words, weaker))
        else:
            problems.append(words)
    for p in problems:
        print("PROBLEM: " + p)
    if problems:
        print("RESULT: %d problem(s)" % len(problems))
        return 1
    if could_not and require:
        print("RESULT: the links hold, but the append-only comparison could not be made and this run requires it")
        return 2
    print("RESULT: nothing new is wrong")
    return 0


if __name__ == "__main__":
    sys.exit(main())
