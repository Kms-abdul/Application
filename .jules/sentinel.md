## 2025-02-23 - [Missing Authentication on New Feature Endpoints]
**Vulnerability:** Newly added feature routes (`hifz_routes.py`) were implemented without the global authentication decorator (`@token_required`), leaving sensitive endpoints (e.g., student progress, master settings) completely exposed to unauthenticated public access.
**Learning:** When creating new blueprints or adding entire feature modules, standard security middleware or decorators must be explicitly imported and applied. The system does not enforce global authentication by default, relying instead on per-route opt-in.
**Prevention:** Always verify that all sensitive endpoints in new blueprints are wrapped with appropriate authentication and authorization decorators before shipping.
