## 2024-06-12 - Unauthenticated Setup Routes
**Vulnerability:** The `/api/setup/seed-branches` route was publicly accessible without any authentication or authorization.
**Learning:** Initial application setup routes are often left unguarded during development. If exposed in production, they can allow attackers to reset, overwrite, or access critical initial database state.
**Prevention:** All setup or seed routes must have `@token_required` and explicitly verify `current_user.role == 'Admin'` before proceeding, or ideally be moved out of the web API entirely into a CLI script.
