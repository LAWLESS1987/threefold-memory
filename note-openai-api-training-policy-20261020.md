---
name: note-openai-api-training-policy-20261020
description: Lawrence's note: OpenAI pre-2023-03-01 API default training opt-in and relevance to Chat Smith (saved 2026-10-20, unverified) [amended 2026-10-20: verified]
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

## Amendment 1 (2026-10-20, verification, on Lawrence's yes; the before above is unchanged)

- Chat Smith did run on OpenAI's API. Vulcan Labs' App Store listing (app id 1559479889, version 3.7, late 2022 or later) says "powered by GPT-3 by OpenAI" and "built on top of GPT-3 from OpenAI, and Simsimi AI Chatbots technology" (https://www.chartoo.ch/itunes/app/1559479889-chat-smith-ki-chatbot-agent). Vulcan's Feb 2024 FAQ says it is an OpenAI partner at the "Enterprise Partner level" (https://vulcanlabs.freshdesk.com/en/support/solutions/articles/69000843734-chat-assistant-app-frequently-asked-questions-part-1-).
- Qualifier 1: per the listing, the "emotional conversation" bot ran on Simsimi, not OpenAI, so not every Chat Smith chat went to OpenAI.
- The March 1, 2023 quote matches OpenAI's docs word for word (https://developers.openai.com/api/docs/guides/your-data). TechCrunch covered it on 2023-03-01 (https://techcrunch.com/2023/03/01/addressing-criticism-openai-will-no-longer-use-customer-data-to-train-its-models-by-default/).
- Qualifier 2: the old policy permitted training on API data, but no evidence shows it actually happened. In May 2023 Altman told CNBC "We don't train on any API data at all, we haven't for a while" (https://www.cnbc.com/2023/05/05/sam-altman-openai-wont-tap-into-customer-apis.html).
- No source was found for the quoted phrase "may have been used for improvement if the customer had not previously opted out." Treat it as unsourced.
