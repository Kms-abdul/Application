## 2024-07-15 - [CRITICAL] Missing Authentication on API Endpoints
**Vulnerability:** Found multiple endpoints in `erp-backend/routes/hifz_routes.py` (including POST, PUT, DELETE operations) that were missing the `@token_required` decorator, allowing unauthenticated modification of database records.
**Learning:** In Flask architectures where blueprints are not globally secured, it is very easy to forget to add the `@token_required` decorator to new routes. This leads to severe authorization bypass issues.
**Prevention:** Always verify that every route handling sensitive data or modifications has explicit authentication and authorization decorators. Consider adding automated tests or static analysis to check for missing decorators on all routes that don't explicitly opt-out (e.g. login).
