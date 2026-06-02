## 2025-02-27 - [Broken Access Control in User Creation]
**Vulnerability:** The `/api/users/add` endpoint lacked role-based access control, allowing any authenticated user to create new accounts, potentially assigning themselves 'Admin' privileges.
**Learning:** While authentication (`@token_required`) was enforced globally or per-route, explicit role checks (authorization) were missing on this administrative function.
**Prevention:** Always verify both authentication and authorization levels when granting access to endpoints that mutate application state or manage users.
