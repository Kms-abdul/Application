## 2024-05-24 - [Second-Order SQL Injection in Dynamic Queries]
**Vulnerability:** Dynamic SQL query constructed using f-strings with data retrieved from a previous database query (second-order SQL injection risk).
**Learning:** Even when data comes from the database, string interpolation should not be used in SQL queries. This breaks parameterized query best practices and creates risk if the original data source is compromised or later modified to include user input.
**Prevention:** Always use parameterized queries (`%s`) and append values to the parameter list, regardless of the data source.
