## 2026-05-13 - Second-Order SQL Injection via Dynamic Query Construction
**Vulnerability:** A second-order SQL injection vulnerability existed in `erp-backend/routes/report_card_routes.py` where a dynamic query was built using f-strings with values (`month`, `year`) retrieved from the database table `test_attendance_months`.
**Learning:** Even when data originates from the database (not direct user input), interpolating it into a query can lead to second-order SQL injection if the stored values contain unexpected characters or have been tampered with.
**Prevention:** Always use `%s` parameterization (or parameterized equivalents) for dynamic query building, even when constructing dynamic `WHERE` conditions or iterating over results sourced from previous database queries.
