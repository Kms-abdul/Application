
## 2025-05-14 - Fix Second-Order SQL Injection in Query Loop
**Vulnerability:** In `erp-backend/routes/report_card_routes.py`, `m['month']` and `m['year']` were interpolated directly into a dynamic query condition using an f-string: `f"(MONTH(date) = {m['month']} AND YEAR(date) = {m['year']})"`.
**Learning:** Even when data originates from an earlier database query (like `mapped_months`), using string interpolation (f-strings or `.format()`) to construct SQL queries is dangerous. It exposes the application to second-order SQL injection if the database content is ever tampered with.
**Prevention:** Always use parameterized query placeholders (e.g., `%s`) for *all* dynamic values in SQL queries, regardless of the data's source. Append the values to the parameter list, such as `att_params.extend([m['month'], m['year']])`.
