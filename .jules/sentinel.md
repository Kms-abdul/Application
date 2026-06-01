## 2025-02-14 - Missing Authentication on Hifz Module Endpoints
**Vulnerability:** The endpoints in `erp-backend/routes/hifz_routes.py` (e.g., `/programs`, `/students`, `/bulk-progress`) were completely unauthenticated, exposing sensitive student progress and master settings data.
**Learning:** In this Flask architecture, new blueprint routes do not automatically inherit global authentication or authorization. Security decorators must be manually imported and applied to every new route.
**Prevention:** When creating new blueprints or API modules, explicitly include `from helpers import token_required` and ensure `@token_required` is applied immediately below the `@bp.route` decorator, updating the function signature to accept `current_user`.
