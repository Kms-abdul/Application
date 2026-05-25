## 2026-05-25 - [SQL Injection Fix in Dynamic Query]
**Vulnerability:** Second-order SQL injection vulnerability via f-string dynamic SQL query generation for `attendance_query` condition array in `erp-backend/routes/report_card_routes.py`.
**Learning:** Dynamic condition building loop with ORs was directly injecting `mapped_months` database outputs.
**Prevention:** Replace formatted strings with SQL parameters (`%s`) inside loop and dynamically push parameter values into parameter list.
