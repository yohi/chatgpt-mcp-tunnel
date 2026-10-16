# AWS MCP Broker v1.1 — Option A Decision Record limited correction R1

**Status:** `LIMITED_CORRECTION_CANDIDATE / OWNER_ATTESTATION_PENDING / NOT_EFFECTIVE`
**Review:** 2026-10-14 JST, supplied independent static review

## Purpose

This package remedies only `ODR-IR-001`: the Section 4 summary overstates the scope of two-person approval. It clarifies that high-risk/privilege-expanding changes need independent two-person approval, while Q40 / candidate REQ-057 allow a single authorized administrator to perform emergency stop, access reduction, and token revocation. Restoration/re-enablement is not a one-person exception.

`REQ-009` / `REQ-046` / `AC-022` adopted candidate bodies are **unchanged**. Source baseline B1/B2/B3 and candidate-text bytes are copied from the original Option A handoff. No Owner approval is claimed.

## Hashes

| Evidence | SHA-256 |
|---|---|
| Original Owner Decision Record | `fe77bbaaed64427778817bdda1e830a3dc0e276fcba2956ec5332be9a7942225` |
| Independent static review | `bf783e7720c590a5d85349efd755bf10ecbdf46ce171c9785c1c1b846f7b3d0e` |
| Revised Decision Record | `92cef5b23ca9696ede0c9a6d5ca979056c20b6c17853598afcf6af914f60865e` |
| Original Option A handoff ZIP | `595eb470dd3a6470bb528bf11f732a20929e50e9e3a204cdd3f6e7f6ec464cb9` |
| R4 reconciliation ZIP | `cd9611654f17d5eee73d47d5d32ce6d94459c24016c2dc3a1a157f90fbd8a15c` |
| B1 | `39002fc2ce5f21e9e686a427c793a7fd42fc84e5bdb02684be9e1e3a4305f4bc` |
| B2 | `3078acc5c31b5e900697dbb585e5ed604dfca89fe82b56cfc9528ac3c91350e2` |
| B3 | `f287966ac61f467704f99c545f2d7a9756b9f21a70a5f90a814367ab7a113aa4` |

## Review / gate status

- `ODR-IR-001`: Corrective wording included; **independent closure review pending**.
- `ODR-IR-002`: Owner identity/authority, signature, actual decision time, binding to 3 clause Digests **PENDING**.
- `ODR-IR-003`: External authoritative baseline provenance **NOT_VERIFIED**.
- `REQ-050〜059 / AC-025〜036`: R4 candidates, not adopted.
- `INT-003`: **CRITICAL OPEN / BLOCKING**.
- `Gate S0/S1/C`: **NOT_PROVEN**.
- `Feasibility / Design / Implementation / Production`: **NOT_AUTHORIZED**.

Only the Section 4 summary sentence changed. Other original record content, including the metadata, Owner attestation area, and the three full texts, is unchanged.
