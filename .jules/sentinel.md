## 2026-04-26 - [Fix Hardcoded Dev Secret Key]
**Vulnerability:** A hardcoded string "dev-only-secret-key-change-before-production" was used as the fallback SECRET_KEY in `erp-backend/app.py`.
**Learning:** Hardcoded fallback secrets, even when intended for development only, can be flagged by security scanners and pose a risk if accidentally deployed to non-development environments without proper configuration.
**Prevention:** Use dynamically generated, cryptographically strong random strings (e.g., `os.urandom(32).hex()`) for development fallbacks instead of static strings.
