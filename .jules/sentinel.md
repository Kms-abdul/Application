## 2026-07-20 - Missing Role Authorization on User Creation
**Vulnerability:** The `/api/users/add` endpoint lacks an explicit role check (e.g., `if current_user.role != 'Admin':`), allowing any authenticated user to create new accounts, including Admin accounts, leading to privilege escalation.
**Learning:** The `@token_required` decorator only validates authentication. Administrative endpoints must also enforce authorization to prevent broken access control.
**Prevention:** Always verify `current_user.role == 'Admin'` in administrative route handlers before processing requests.
