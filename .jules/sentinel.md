## 2025-05-02 - SQL Injection via F-String Interpolation in Dynamic Queries

**Vulnerability:** Found a potential second-order SQL injection vulnerability in `erp-backend/routes/report_card_routes.py` where a dynamic `attendance_query` used f-strings to insert `month` and `year` values directly into the SQL query (`f"(MONTH(date) = {m['month']} AND YEAR(date) = {m['year']})"`), even though these values originated from a previous database lookup.

**Learning:** Data coming from a database (`mapped_months` in this case) should still be treated with caution, especially if it was originally user-controlled or could be modified maliciously in the database. Using f-strings or `.format()` to inject variables directly into a SQL query string bypasses the parameterized query protection provided by the database connector, leaving the system vulnerable to second-order SQL injection attacks.

**Prevention:** Always use parameterized queries (e.g., `%s` for `mysql.connector`) for inserting variables into SQL queries, regardless of whether the data comes directly from a user request or from a previous database query. Build the list of parameters (`att_params.extend([m['month'], m['year']])`) dynamically along with the query string and pass it to `cursor.execute(query, params)`.
