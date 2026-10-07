# threefold-memory

Public **AI_MEMORY_ROOT** for [LAWLESS1987/threefold](https://github.com/LAWLESS1987/threefold).

This repo holds covenant-style agent memories written by the triad:

- `task-<task_id>.md` — what was done / decided
- `jlens-<task_id>.md` — full Jacobian-lens snapshot (`type:jlens` in body/description)
- `audit.jsonl` — hash-chained write ledger from covenant `ai_memory_system`
- `.trash/` — tombstoned memories (not silent deletes)

Code lives in **threefold**. Data lives here. Clone this repo and point:

```bash
export AI_MEMORY_ROOT=/path/to/threefold-memory
```

Triad writes (`put_covenant_memory.sh`) commit and push here after each put when `git` remotes are configured.
