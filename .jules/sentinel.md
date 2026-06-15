## 2024-06-15 - Missing Authorization Check on User Creation Endpoint
**Vulnerability:** The `/api/users/add` endpoint in `erp-backend/routes/auth_routes.py` had a `@token_required` decorator to check for authentication, but lacked an authorization check to ensure the user making the request has 'Admin' privileges.
**Learning:** Any authenticated user could potentially create new users (including granting them Admin privileges), leading to broken access control and privilege escalation.
**Prevention:** Always combine authentication checks (`@token_required`) with explicit authorization checks (e.g., `if current_user.role != 'Admin':`) on sensitive endpoints, especially those dealing with user management or system configurations.
