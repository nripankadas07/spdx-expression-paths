# Runnable demo

```bash
python demo.py
python spdx_expression_paths.py '(MIT OR Apache-2.0) AND Zlib'
```

`demo.py` checks a synthetic success and malformed-input rejection. The installed command uses the same arguments.

## Input contract

```text
Expression grammar: identifier [WITH identifier], parentheses, AND, OR. AND binds more tightly than OR.
```

Inspect `test_contract.py` for independently specified expected outcomes, including boundary failures. SPDX-style syntax, not a validated SPDX license registry. Unknown identifiers are retained; case is preserved; deprecated IDs are not normalized. No legal interpretation, compatibility, compliance, policy selection or license-text detection. Enumeration is bounded and deliberately fails when expansion exceeds limits.
