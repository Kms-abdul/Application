## 2025-02-18 - Parameterized Queries for Dynamically Constructed Conditions
**Vulnerability:** Second-order SQL injection risk in `report_card_routes.py` where database results (`mapped_months`) were directly interpolated into an SQL query string using f-strings inside a loop.
**Learning:** Even if data originates from the database (and is assumed safe), it must still be parameterized when used in subsequent queries to prevent second-order SQL injection and ensure proper query parsing.
**Prevention:** Always use `%s` placeholders and dynamic parameter lists (`att_params.extend([val1, val2])`), passing them as a tuple to `cursor.execute(query, tuple(params))`, avoiding f-strings entirely for SQL queries.
