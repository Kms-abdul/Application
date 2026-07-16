## 2024-07-16 - [Missing Authorization Check]
**Vulnerability:** The create_user endpoint lacked role-based authorization, allowing any authenticated user to create new admin users.
**Learning:** Endpoints creating privileged accounts must strictly enforce Admin-only access.
**Prevention:** Always check current_user.role == "Admin" before allowing user creation.
