## 2025-02-14 - Broken Access Control in User Creation
**Vulnerability:** The `/api/users/add` endpoint lacked role-based authorization, allowing any authenticated user to create new users, including assigning them the 'Admin' role, leading to privilege escalation.
**Learning:** The `@token_required` decorator only validates the presence of a valid session token but does not restrict access by user role.
**Prevention:** Always implement explicit role checks (e.g., `if current_user.role != 'Admin':`) in administrative or sensitive endpoints after the authentication layer.
