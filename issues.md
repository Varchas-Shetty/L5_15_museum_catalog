# Issues found

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| SQL injection risk | Security, medium | 11 | Artifact values were joined into an SQL command, so unusual input could change the query. | Use `?` placeholders and pass values separately. |
| Hardcoded password | Security, low | 7 | A password was stored in the source code and was not used by the program. | Remove the unused password instead of keeping a secret in source code. |
| Shell command in subprocess | Security, low | 37 | The backup notice ran through a shell even though it only printed text. | Print the notice directly without starting a shell process. |
| Non-snake-case function names | Style | 10, 15, 24, 31, 36 | Function names did not follow the usual Python naming style. | Rename functions to snake_case and update their calls. |
| Unused import and argument | Quality | 2, 15 | `datetime` and the `curator` argument were never used. | Remove them. |
| Long lines and missing docstrings | Style | Multiple | Several lines exceeded style limits, and module/functions had no descriptions. | Wrap long statements and add short docstrings. |
| Missing artifact handling | Correctness | 16 | Looking up an unknown artifact caused an error when the result was `None`. | Return a clear message when no artifact matches the ID. |
