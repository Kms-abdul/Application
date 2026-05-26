## 2024-05-26 - [SQL Injection in report_card_routes.py]
**Vulnerability:** Found a SQL injection vulnerability in `erp-backend/routes/report_card_routes.py` where raw f-strings were used to build a SQL condition string `f"(MONTH(date) = {m['month']} AND YEAR(date) = {m['year']})"`.
**Learning:** This repo has custom SQL queries constructed using `mysql.connector`. Developers need to be careful not to introduce string formatting vulnerabilities when building lists of conditions. Even if data feels safe (coming from DB in this case), it sets a bad precedent and risks second-order injections.
**Prevention:** Always use `%s` placeholders and dynamically extend the `params` list corresponding to the built query, instead of direct string interpolation.
