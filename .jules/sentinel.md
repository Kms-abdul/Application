## 2024-05-24 - [SQL Injection via String Interpolation]
**Vulnerability:** Found a second-order SQL injection vulnerability in `erp-backend/routes/report_card_routes.py` where a SQL query string was being constructed using string interpolation (`f"(MONTH(date) = {m['month']} AND YEAR(date) = {m['year']})"`).
**Learning:** Even if the data (`m['month']` and `m['year']`) originates from a previous database query, constructing SQL queries with string interpolation creates a risk of second-order SQL injection if the original data was tampered with or not strictly typed.
**Prevention:** Always use parameterized queries (`%s` for MySQL connector) and pass the values via a tuple or list of arguments (`cursor.execute(query, tuple(params))`), regardless of the data's source.
