## 2024-06-17 - Privilege Escalation in User Creation API
**Vulnerability:** The `/api/users/add` endpoint was protected by `@token_required` but lacked explicit role-based access control, allowing any authenticated user to create new accounts (including Admin accounts).
**Learning:** In this application's architecture, `@token_required` only verifies authentication (valid token). It does *not* enforce authorization. Administrative endpoints must explicitly verify `current_user.role == 'Admin'`.
**Prevention:** Always add `if current_user.role != 'Admin': return jsonify({"error": "Unauthorized"}), 403` to any route that performs administrative actions.
