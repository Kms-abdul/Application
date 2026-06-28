## 2026-06-28 - [Broken Access Control in User Creation]
**Vulnerability:** The `/api/users/add` endpoint was only checking for authentication (`@token_required`), but completely missing role-based authorization, allowing any authenticated user to create new accounts (including Admin accounts).
**Learning:** In Flask/Python backends using custom authentication decorators, `@token_required` only guarantees identity, not permissions. Sensitive endpoints need explicit role checks inside the function body (e.g., `if current_user.role != "Admin":`).
**Prevention:** Always follow up authentication decorators with strict authorization checks for endpoints that modify system state or manage access. Consider a `@role_required("Admin")` decorator for broader enforcement.
