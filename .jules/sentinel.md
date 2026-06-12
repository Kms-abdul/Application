## 2024-05-28 - Second-Order SQL Injection in Dynamic Query

**Vulnerability:** A second-order SQL injection vulnerability existed in `erp-backend/routes/report_card_routes.py` where database-derived values (`m['month']` and `m['year']`) were interpolated directly into an SQL query string using f-strings (`f"(MONTH(date) = {m['month']} AND YEAR(date) = {m['year']})"`).

**Learning:** Even when data originates from the database (e.g., from a previous `SELECT` query like `test_attendance_months`), it must not be trusted for direct interpolation in subsequent SQL queries. Doing so creates a second-order SQL injection vulnerability if those initial database values were maliciously crafted or unexpectedly formatted. In Python's MySQL connector, all dynamic values must use `%s` parameterization regardless of their source.

**Prevention:** Never use f-strings or `.format()` for SQL query interpolation. Always use parameterized queries (e.g., `cursor.execute(query, tuple(params))`) with `%s` placeholders for all dynamic data, accumulating parameters in a list alongside building the query string.
