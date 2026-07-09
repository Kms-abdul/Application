## 2024-05-24 - Missing Authorization Check on Create User Endpoint
**Vulnerability:** The `/api/users/add` endpoint in `erp-backend/routes/auth_routes.py` allowed any authenticated user to create new user accounts, including setting their role (e.g. creating other Admins).
**Learning:** The `@token_required` decorator only ensures that the request is made by an authenticated user but doesn't inherently check the user's role/privileges. The application doesn't enforce global endpoint access control by role by default.
**Prevention:** Ensure explicit role-based authorization checks (e.g., `if current_user.role != 'Admin': return jsonify({"error": "Unauthorized"}), 403`) are included on all administrative endpoints after verifying authentication.
