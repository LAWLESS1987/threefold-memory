---
license: apache-2.0
pretty_name: Threefold Memory
tags:
  - agent-memory
  - provenance
  - ai-agents
---

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


---

## Part of one system — each piece usable on its own

These repositories are independent instruments that also compose into a single apparatus for **building and honestly auditing trustworthy multi-intelligence systems**. Any one can be used standalone; together they form the stack:

- **Governed core** — [covenant](https://huggingface.co/Lawless1987/covenant): a self-governing multi-agent system with an ethics gate inside the transaction path.
- **Observability & provenance** — [threefold](https://huggingface.co/Lawless1987/threefold) (the L-lens layer over Jacobian Lens) and [threefold-memory](https://huggingface.co/Lawless1987/threefold-memory) (its persistent, provenance-tracked memory): every action measured and recorded under one task identity.
- **Measurement instruments** — [contradiction-probe](https://huggingface.co/Lawless1987/contradiction-probe) and [flinch-observability](https://huggingface.co/Lawless1987/flinch-observability), with the session records [flinch-record](https://huggingface.co/Lawless1987/flinch-record) and [grokflinch](https://huggingface.co/Lawless1987/grokflinch): preregistered, blind-scored tests of AI behaviour that embody the covenant's rule — *investigate a signal, never convict on one*.
- **Neuromorphic research** — [spiking-experiments](https://huggingface.co/Lawless1987/spiking-experiments): from-scratch spiking-network experiments with the pass/fail bar declared before each run.
- **Ledger surface** — [Sentinel-Witness](https://huggingface.co/Lawless1987/Sentinel-Witness): the trading / ledger dashboard.

**This repository's place in it:** the persistent, provenance-tracked memory for that observability layer.
