## 2024-05-24 - Missing Authorization on User Creation
**Vulnerability:** The `/api/users/add` endpoint was missing role-based access control, allowing any authenticated user to create new accounts, including Admin accounts.
**Learning:** The `@token_required` decorator only ensures a user is authenticated, it does not enforce authorization or role checks.
**Prevention:** Always verify that sensitive operations, especially account creation and role modification, have an explicit `if current_user.role != 'Admin':` check immediately inside the route function.
