# Candidate brief and fair comparison — 11 October 2026

**User:** Package maintainers inspecting alternatives in a license expression. **Painful task:** Nested AND/OR expressions make the syntactic alternatives difficult to review without expanding them manually.

**Current alternatives:** license-expression, Embark SPDX and go-spdx. **Smallest useful capability:** Enumerate bounded conjunction alternatives, applying AND precedence, parentheses and atomic WITH exceptions.

**Demand evidence:** inferred from the documented protocol/workflow and established comparable projects, not a verified request for this new product. Current comparable READMEs, representative implementation/docs and recent issue/PR lists were reviewed. Those issues do not prove demand for our feature, and no competitor absence is asserted. See [portfolio research evidence](https://github.com/nripankadas07/nripankadas07/blob/main/docs/RESEARCH_2026-10-11.json) for exact observations and code/doc URLs.

**Acceptance:** the 16 core contract tests must pass, the demo must check its known output and malformed input, and a clean installed command outside source must reproduce both success and error behavior. Scope limits remain visible in README/output. LIVE additionally requires final default-branch CI and verified docs/install path.

**Discovery:** descriptive GitHub topics, the profile chronological index, and a reproducible linked demo. No promised growth, invented users or unsolicited third-party issue promotion.

**Distinctness:** compared with all 158 existing owned repository names and today's other four briefs. Cookie routing is separate from CSP/cache/robots checks; SOA rollout arithmetic is separate from mail DNS topology and DNS blocking; expression alternatives are separate from SBOM inventory/dependency audits; startup pull-in versus ordering is separate from general migration plans; captured packet accounting is separate from live LAN delivery/network discovery. These are five independent capabilities, not subdivisions of one product.

## Live GitHub research

Queries: `SPDX expression sort:stars`. Observation date 2026-10-11 UTC. GitHub query results were relevance-screened; some broad queries include unrelated repositories. Highest-star relevant comparable **found** in this research: [aboutcode-org/license-expression](https://github.com/aboutcode-org/license-expression) (74 stars). Coverage is limited; this is not an exhaustive global ranking. Additional established tools were inspected directly. Stars are discovery evidence, not performance.

| Comparable | Stars | Latest push observed (UTC) | Documented workflow |
| --- | ---: | --- | --- |
| [aboutcode-org/license-expression](https://github.com/aboutcode-org/license-expression) | 74 | 2026-05-26T03:13:13Z | Utility library  to parse, normalize and compare License expressions for Python using a boolean logic engine. For expressions using SPDX or any other license id scheme. |
| [EmbarkStudios/spdx](https://github.com/EmbarkStudios/spdx) | 58 | 2026-10-02T10:02:15Z | 🆔 Helper crate for SPDX expressions. 🦀 |
| [github/go-spdx](https://github.com/github/go-spdx) | 55 | 2026-10-09T18:20:37Z | Golang implementation of a checker for determining if an SPDX ID satisfies an SPDX Expression. |

## Workflow tradeoffs

Established alternatives have broader capabilities, documentation, examples and ecosystems; installability varies by language and platform. Ours offers a narrow one-command synthetic example and a zero-runtime-dependency Python source install. No competitor installation was timed or independently stress-tested in this run. No measured time-to-first-result, reliability, support responsiveness, performance or superiority claim. Current comparable licenses are recorded in linked research metadata; none of their implementation or prose was reused. Our license is MIT. Support is best-effort GitHub reports with no SLA.

**Limits and negative result:** SPDX-style syntax, not a validated SPDX license registry. Unknown identifiers are retained; case is preserved; deprecated IDs are not normalized. No legal interpretation, compatibility, compliance, policy selection or license-text detection. Enumeration is bounded and deliberately fails when expansion exceeds limits. Broader production needs should use the established tools. Runnable local success demonstrates our behavior only.
