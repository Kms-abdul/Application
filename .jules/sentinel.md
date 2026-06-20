## 2026-06-20 - [Missing Authorization on User Creation Endpoint]
**Vulnerability:** The `/api/users/add` endpoint in `erp-backend/routes/auth_routes.py` only verifies authentication (`@token_required`) but lacks role-based authorization checks. This allows any authenticated user to create new accounts, including Admin accounts (privilege escalation).
**Learning:** Endpoints that handle administrative actions require explicit role verification (e.g., `if current_user.role != 'Admin':`) in addition to general authentication.
**Prevention:** Implement a consistent authorization pattern or a dedicated `@admin_required` decorator to protect administrative endpoints, and ensure it is applied whenever creating users, modifying roles, or accessing system-wide data.
