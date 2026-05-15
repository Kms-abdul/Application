## 2026-05-15 - Second-Order SQL Injection via f-strings
**Vulnerability:** Constructing SQL queries using f-strings for variables sourced from the database (e.g. `mapped_months`).
**Learning:** Data originating from the database should still be treated as potentially unsafe. Interpolating it directly creates a risk of second-order SQL injection and violates the rule against using f-strings or `.format()` for SQL query interpolation.
**Prevention:** Always use parameterization (e.g. `%s`) for all dynamic values in raw SQL queries, regardless of their source.
