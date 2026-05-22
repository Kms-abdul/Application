## 2024-05-22 - SQL Injection in Dynamic Condition Building
**Vulnerability:** Second-order SQL injection vulnerability via f-string interpolation for SQL query building with data (`mapped_months` dictionary containing `month` and `year` retrieved from the database).
**Learning:** Even if data is fetched from the database immediately prior, injecting it directly into an SQL query using f-strings (e.g. `f"(MONTH(date) = {m['month']})"`) allows SQL injection if the database content is manipulated or user-controlled.
**Prevention:** Always use parameterized queries (e.g., `%s`) and append values to the execution parameters array, regardless of whether the source of the data is the user or the database itself.
