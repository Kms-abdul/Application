
## 2024-05-24 - Missing Authorization on User Creation Endpoint
**Vulnerability:** The `/api/users/add` endpoint was protected by `@token_required` but lacked explicit role-based authorization, allowing any authenticated user to create new administrative accounts or general users.
**Learning:** The `@token_required` decorator only validates authentication status. In Flask applications where global role-based access control isn't enforced at the blueprint level, each sensitive endpoint must independently verify user privileges (e.g., `if current_user.role != 'Admin':`).
**Prevention:** Always implement an explicit role verification check immediately after authentication validation for endpoints that modify system access, manage users, or access sensitive global configuration. Consider implementing a `@role_required('Admin')` decorator to standardize this pattern and prevent omissions.
