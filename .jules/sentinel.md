## 2025-03-01 - [CRITICAL] Authorization Bypass on User Creation Endpoint
**Vulnerability:** The `/api/users/add` endpoint in `auth_routes.py` allowed any authenticated user to create new user accounts, including Admin accounts. It only checked `@token_required` without verifying the user's role.
**Learning:** The `@token_required` decorator only provides authentication (who is calling), not authorization (what they can do). Administrative endpoints must explicitly implement role-based access control (RBAC) to prevent privilege escalation.
**Prevention:** Always verify `current_user.role == 'Admin'` on sensitive endpoints that manage users, system configuration, or wide-ranging data modifications. Do not assume authentication implies authorization.
