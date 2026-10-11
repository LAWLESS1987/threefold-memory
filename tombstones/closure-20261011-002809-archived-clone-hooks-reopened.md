---
name: closure-20261011-002809-archived-clone-hooks-reopened
type: tombstone-closure
---
# Closure: archived-clone-hooks-reopened
- id: 20261011-002809
- when: 2026-10-11T00:28:09Z
- what was closed / changed: Restored owner write (chmod u+w) on .git and .git/hooks in the three archived read-only threefold-memory clones (/workspace/threefold-memory, /workspace/memdiff-20261010/tf, /workspace/chatsmith-research/tf-clone) so Tien can install the credential-scan pre-push hook (/workspace/credscan/pre-push). Working trees stay read-only.
- at commit: 316e700 (threefold-memory HEAD when recorded: 74f1426)
- why: Lawrence via Claude: Tien's credential scan (credentials only, never his text) should be the pre-push hook in every clone; the hooks folders were locked by CL's 2026-10-11 00:19Z archive chmod, not by the pause removal.
- recorded by: Conscious Ledger, automatic closure tombstone (close_state.sh)
