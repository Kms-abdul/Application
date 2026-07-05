
## 2025-07-05 - Fix Broken Access Control in User Creation
**Vulnerability:** Broken Access Control / Privilege Escalation in `/api/users/add`. Any authenticated user could create new accounts, including Admin accounts, because the `@token_required` decorator only checks authentication, not authorization.
**Learning:** Flask blueprints in this app don't enforce global authorization. Endpoints that perform administrative actions must explicitly verify `current_user.role == 'Admin'`.
**Prevention:** Always check `current_user.role` on sensitive endpoints alongside `@token_required`.
