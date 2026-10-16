# Independent R2 Review Findings — Review Input Summary

**Source:** User-provided independent R2 review, 2026-10-13 JST. This document is an author summary, not an independently signed reviewer report.

- **R2-001 Major:** Existing REQ-009 mandates credentials inside Broker-protected runtime, while Q33/Q39 demand independent Adapter. Existing REQ-046/AC-022 say Broker-dedicated Machine Account. Must obtain explicit Requirements Owner amendment; cannot claim nonregression just by explanatory note.
- **R2-002 Major:** Allowed BWS Secret value can be replaced with dummy IAM key with ID/Project/prefetch metadata unchanged. After-fetch digest/content check does not prove no acquisition. Need independent prefetch prevention, or block access. AC-033 must test value-only replacement.
- **R2-003 Moderate:** Distinguish send release S, physical dispatch start, cancellation C, remote acceptance. S<C but unsent queued operation after cancellation must be specified; R3 chooses **reject initial send after C, discard queue**, even after crash/recovery.
- **INT-003 Critical:** Two-person approvals circumventable by BWS/Cloud/CI/CD privileged admins until real enforcement verified. OPEN/BLOCKING.
- **Baseline authenticity:** B1/B2 included in R2 but verbatim independent comparison with original authoritative baseline not completed. Internal checksum only ensures package integrity.
- **Gate S0/S1/C:** NOT_PROVEN. No implementation, tests, or external service operations authorized.
