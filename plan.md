1. **Fix missing authorization check in user creation endpoint**
   - The `@bp.route("/api/users/add", methods=["POST"])` endpoint in `erp-backend/routes/auth_routes.py` has a `@token_required` decorator, but it does not check if the `current_user.role` is `"Admin"`.
   - This means any authenticated user can create new users, including giving them "Admin" privileges.
   - I will add `if current_user.role != "Admin": return jsonify({"error": "Admin privileges required"}), 403` to `create_user()`.
2. **Pre-commit step**
   - Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.
3. **Submit PR**
   - Create a PR with a description containing the vulnerability, impact, fix, and verification.
