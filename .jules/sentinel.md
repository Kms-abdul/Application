## 2026-04-30 - Second-Order SQL Injection in Query Building
**Vulnerability:** A second-order SQL injection vulnerability existed in `erp-backend/routes/report_card_routes.py` where dynamic values from a database (specifically, `m['month']` and `m['year']`) were interpolated into an SQL query using f-strings instead of being parameterized.
**Learning:** Even when data originates from the database (e.g., from an initial SELECT query), it must be parameterized in subsequent queries. Failing to do so can result in second-order SQL injection vulnerabilities, particularly when the initial data was user-supplied and unsanitized.
**Prevention:** Always use parameterized queries (e.g., `%s` for `mysql.connector`) for all dynamic values, regardless of their source.
