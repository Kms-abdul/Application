## 2024-05-20 - [Missing Role-Based Access Control on Admin Endpoints]
**Vulnerability:** The `/api/users/add` endpoint lacked an explicit authorization check (`current_user.role != 'Admin'`), allowing any authenticated user (even non-admins) to create new users, including admin accounts (Broken Access Control/Privilege Escalation).
**Learning:** The `@token_required` decorator only validates the token and provides the `current_user` object. It does NOT enforce role-based access control. Admin-only endpoints must explicitly verify the user's role.
**Prevention:** Always verify `current_user.role == 'Admin'` at the beginning of sensitive or administrative endpoints, even if they are protected by `@token_required`.
