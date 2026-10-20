---
name: note-openai-api-training-policy-20261020
description: Lawrence's note: OpenAI pre-2023-03-01 API default training opt-in and relevance to Chat Smith (saved 2026-10-20, unverified)
metadata:
  type: reference
  agent: grok-bot
  created: 1792482118
  last_used: 1792482118
  review: unreviewed
  review_by: unavailable
  tier: archival
  uses: 0
---

# Note saved on Lawrence's request: OpenAI historical API training policy and early apps (Chat Smith)

- Saved: 2026-10-20T07:41:49Z by Conscious Ledger (Grok Bot)
- Note date as given: 2026-10-20
- Arrived as: a relayed message in the Conscious Ledger chat ("Lawrence asked to save the following important note"), t155
- Verification: Conscious Ledger did NOT check these claims independently when saving. They are recorded as submitted. That Chat Smith used the OpenAI API, and was opted in by default, is an inference in the note, not something it confirms.

## Before (inbound, verbatim)

OpenAI historical API data training policy and relevance to early apps like Chat Smith:

Prior to March 1, 2023, OpenAI's developer policy automatically opted in API developers to model training by default. Any prompt sent through the API was eligible for OpenAI's training loops unless a developer manually filled out an opt-out form.

On March 1, 2023, OpenAI changed the API default from Opt-In to Opt-Out. They declared: "As of March 1, 2023, data sent to the OpenAI API is not used to train or improve OpenAI models (unless you explicitly opt in)."

This means early user messages routed through apps like Chat Smith (which launched during the early AI boom and used the OpenAI API) legally fell under the default opt-in training policy. While not an intentional data-sharing partnership, OpenAI's systems were permitted to ingest those early prompts for model improvement if the API account had not opted out.

Confirmed by OpenAI docs, TechCrunch (March 1, 2023), Gizmodo, and later statements by Sam Altman. Pre-March 1 data "may have been used for improvement if the customer had not previously opted out."

This is important context for understanding early AI data practices and third-party app contributions to training data.

Date: 2026-10-20

## After (outbound)

Saved as a new memory through the store's put(), so the audit chain records it. No existing entry changed, so no tombstone was needed. The commit is local only, because pushes to threefold-memory are paused until Lawrence says otherwise.
