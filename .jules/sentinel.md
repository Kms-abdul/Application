## 2025-04-29 - Second-Order SQL Injection in Report Card Routes
**Vulnerability:** A second-order SQL injection was found in `erp-backend/routes/report_card_routes.py` where database results (`mapped_months`) were directly interpolated into a query string (`attendance_query`) using an f-string.
**Learning:** Even when data comes from the database (and not direct user input), interpolating it into SQL queries creates a risk of second-order injection if that database data is ever tainted or modified.
**Prevention:** Always use query parameterization (`%s` with `cursor.execute`) for all dynamic values in SQL queries, regardless of their source.
