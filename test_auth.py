import unittest
import sys

# Mock modules BEFORE importing them in the environment
from unittest.mock import MagicMock
sys.modules['flask'] = MagicMock()
sys.modules['extensions'] = MagicMock()
sys.modules['models'] = MagicMock()
sys.modules['helpers'] = MagicMock()
sys.modules['jwt'] = MagicMock()
sys.modules['secrets'] = MagicMock()
sys.modules['hashlib'] = MagicMock()

# Setup mocks for decorators and jsonify
sys.modules['helpers'].token_required = lambda f: f
sys.modules['helpers']._validate_password_strength = lambda p: None
sys.modules['helpers'].hash_user_password = lambda p: p

def mock_jsonify(*args, **kwargs):
    if args:
        return args[0]
    return kwargs

sys.modules['flask'].jsonify = mock_jsonify
sys.modules['flask'].Blueprint = MagicMock()
bp_mock = MagicMock()
sys.modules['flask'].Blueprint.return_value = bp_mock
bp_mock.route.return_value = lambda f: f

# Now import the module to test
import os
sys.path.insert(0, os.path.abspath('erp-backend'))
from routes.auth_routes import create_user

class TestAuthRoutes(unittest.TestCase):
    def test_create_user_admin_role(self):
        # Admin user
        admin_user = MagicMock()
        admin_user.role = "Admin"

        sys.modules['flask'].request.json = {"username": "test", "password": "password123", "useremail": "test@test.com"}
        sys.modules['models'].User.query.filter_by.return_value.first.return_value = None

        # Test creation for Admin
        result = create_user(admin_user)
        # Should return success which in mock is going to be 201
        self.assertEqual(result[1], 201)

    def test_create_user_non_admin_role(self):
        # Non-admin user
        non_admin_user = MagicMock()
        non_admin_user.role = "User"

        # Test creation for Non-Admin
        result = create_user(non_admin_user)

        # Should return 403
        self.assertEqual(result, ({"error": "Admin privileges required"}, 403))

if __name__ == '__main__':
    unittest.main()
