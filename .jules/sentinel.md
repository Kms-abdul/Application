## 2025-02-28 - [CRITICAL] Missing Authentication on Blueprint Routes
**Vulnerability:** The entire `hifz_routes.py` blueprint containing sensitive student data and program settings was completely unauthenticated. It lacked the `@token_required` decorator on all its endpoints, allowing arbitrary data access and modification.
**Learning:** In Flask applications where global authentication isn't enforced at the blueprint or app level, every single new route must be manually decorated. Developers often forget this when scaffolding new modules.
**Prevention:** Consider implementing blueprint-level before_request handlers to enforce authentication globally per blueprint, rather than relying on route-level decorators which are prone to human error.
