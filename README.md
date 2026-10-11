# spdx-expression-paths

Enumerate bounded conjunction alternatives, applying AND precedence, parentheses and atomic WITH exceptions.

For package maintainers inspecting alternatives in a license expression. Nested AND/OR expressions make the syntactic alternatives difficult to review without expanding them manually.

## Quickstart

Python 3.10 or newer. No runtime dependencies or service account. Build tooling downloads require access to PyPI; this repository is not published on PyPI.

```bash
git clone https://github.com/nripankadas07/spdx-expression-paths.git
cd spdx-expression-paths
python -m venv .venv
.venv/bin/python -m pip install .
.venv/bin/spdx-expression-paths '(MIT OR Apache-2.0) AND Zlib'
```

Windows: use `.venv\Scripts\python.exe` and `.venv\Scripts\spdx-expression-paths.exe` instead. Windows is not part of the tested CI matrix.

The supplied example is synthetic. JSON success exits 0, including valid findings such as unmet quorum, ineligible cookie or an ordering cycle; malformed or unsupported input exits 2 with an `error` field. Argument usage errors use argparse's stderr. No input files or live services are modified.

## Scope and limits

SPDX-style syntax, not a validated SPDX license registry. Unknown identifiers are retained; case is preserved; deprecated IDs are not normalized. No legal interpretation, compatibility, compliance, policy selection or license-text detection. Enumeration is bounded and deliberately fails when expansion exceeds limits.

Input limits: 4,096 characters, 256 tokens, 32 nested parentheses; default 128 alternatives, configurable to 1,024; intermediate Cartesian product at most 4,096.

## Inspectable evidence

- [Demo and input schema](DEMO.md)
- [Candidate brief and comparisons](RESEARCH.md)
- [Validation and untested behavior](VALIDATION.md)
- [Build instructions](BUILDING.md)
- [Security reporting](SECURITY.md) and [support/contribution guidance](SUPPORT.md)

MIT; original implementation. No competitor code or branding copied. No speed, adoption or superiority claim. CI executes core regressions, the demo, a fresh wheel installation outside source and the documented source installation on Python 3.10, 3.12 and 3.14.
