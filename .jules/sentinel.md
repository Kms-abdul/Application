## 2024-07-11 - [Authorization Bypass in create_user]
**Vulnerability:** The `/api/users/add` endpoint was protected by `@token_required` but lacked explicit authorization checks, allowing any authenticated user to create a new user, potentially an Admin user (Privilege Escalation).
**Learning:** In Flask/Python backends using `@token_required` for authentication, role-based authorization must still be enforced manually if a global RBAC mechanism is not in place.
**Prevention:** Always verify that endpoints performing sensitive actions (like user creation) include explicit role checks (e.g., `if current_user.role != 'Admin':`) in addition to authentication.
