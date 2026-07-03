## 2024-05-24 - Missing Authentication on Hifz Blueprint Routes
**Vulnerability:** The endpoints within `erp-backend/routes/hifz_routes.py` (such as getting, creating, updating, or deleting Hifz programs and updating student bulk progress) were entirely exposed. They lacked the `@token_required` decorator, allowing unauthenticated attackers to fetch student data, manipulate Hifz programs, and modify progress reports.
**Learning:** In a Flask application where global authentication isn't enforced at the blueprint level via a `before_request` hook, developers must manually add the custom authentication decorator to *every* route within *every* new blueprint. Forgetting to apply this results in complete access control bypass for that module's endpoints.
**Prevention:**
- Enforce authentication globally for API routes or use a blueprint-wide `before_request` middleware to apply the `@token_required` logic.
- Alternatively, include automated security linting or unit tests that verify all endpoints registered under `/api/` (except login/password resets) throw a 401 Unauthorized error when accessed without a Bearer token.
