## 2024-07-13 - [Missing Role-Based Authorization on Administrative Endpoint]
**Vulnerability:** The `/api/users/add` endpoint lacked an explicit check for the "Admin" role, allowing any authenticated user to create new users, including assigning the "Admin" role to them.
**Learning:** In this application architecture, the `@token_required` decorator only validates authentication (a valid JWT token). It does not enforce role-based access control. Endpoints that perform administrative actions must explicitly check `current_user.role`.
**Prevention:** Always verify `current_user.role` (e.g., `if current_user.role != "Admin":`) immediately after the route definition for endpoints restricted to specific roles, even if the endpoint is protected by `@token_required`.
