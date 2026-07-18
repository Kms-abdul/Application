
## 2024-05-18 - Missing Authentication on Backend Routes
**Vulnerability:** Several backend endpoints (e.g., `/api/classes`, `/api/students/template`, `/api/academic/subjects`, `/api/org/locations`) lacked the `@token_required` decorator, exposing them to unauthenticated access. Some of these endpoints (like `/api/setup/seed-branches`) could cause data modification or disclose system structure without proper auth checks.
**Learning:** The application does not enforce global authentication on Flask blueprints. Each endpoint must individually opt-in via `@token_required`. When creating or reviewing endpoints, especially those not immediately tied to user-specific data, it's easy to forget this decorator.
**Prevention:** Establish a pre-commit hook or linter rule to check for `@bp.route` declarations missing `@token_required` (except for explicitly whitelisted public routes like login/password reset).
