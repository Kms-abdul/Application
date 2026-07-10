## 2024-06-03 - [CRITICAL] Missing Authorization Check on Admin Endpoint
**Vulnerability:** The `/api/users/add` endpoint lacked an authorization check. Although it had `@token_required`, any authenticated user (even non-Admins) could potentially access it and create new users (including Admins), leading to broken access control and privilege escalation.
**Learning:** Never assume `@token_required` implies administrative privileges. Flask endpoints that perform administrative actions must explicitly verify `current_user.role == "Admin"`.
**Prevention:** Always implement explicit role-based authorization checks alongside authentication checks on sensitive endpoints.
