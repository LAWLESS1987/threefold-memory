---
name: jlens-20261007-ocrvid-demo-32523
description: type:jlens full Jacobian-lens snapshot for 20261007-ocrvid-demo-32523
metadata:
  type: project
  agent: grok-bot
  created: 1791341230
  last_used: 1791341230
  review: unreviewed
  review_by: unavailable
  tier: archival
  uses: 0
---

{
  "type": "jlens",
  "task_id": "20261007-ocrvid-demo-32523",
  "model_id": "openai-community/gpt2",
  "lens_path": "/workspace/jlens-demo/gpt2_jacobian_lens.pt",
  "prompt": "OCR video (sample_ocr.mp4): ===== t=0.000s ===== Frame A: Triad OCR  ===== t=1.000s ===== Frame B: Lawrence demo  ===== t=2.000s ===== Frame C: video pipeline  ",
  "layers": [
    3,
    6,
    9,
    10
  ],
  "positions": [
    -2
  ],
  "top_k": 5,
  "jlens_top_k": {
    "3": [
      " ",
      "\ufffd",
      " \ufffd\ufffd\ufffd\ufffd",
      " \ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd",
      "\ufffd"
    ],
    "6": [
      " ",
      " \ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd",
      "\ufffd",
      "\ufffd\ufffd",
      " \ufffd\ufffd\ufffd\ufffd"
    ],
    "9": [
      " =====",
      "\ufffd",
      "EStream",
      "\ufffd",
      "~~~~~~~~"
    ],
    "10": [
      " =====",
      "====",
      " =================================",
      " =================",
      "================"
    ]
  },
  "model_final_top_k": [
    " =====",
    " ",
    "====",
    " =================================",
    " ================="
  ],
  "apply_s": 3.301,
  "mechanism": "anthropics/jacobian-lens JacobianLens.apply (real per-layer logits)"
}
