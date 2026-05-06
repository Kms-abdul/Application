class MockStudent:
    first_name = "John"
    last_name = "Doe"
    admission_no = "123"

class MockPayment:
    branch = "Main"
    receipt_no = "1"
    student = MockStudent()
    class_name = "1"
    section = "A"
    gross_amount = 100
    concession_amount = 0
    net_payable = 100
    amount_paid = 100
    due_amount = 0
    payment_mode = "Cash"
    note = ""
    collected_by_name = "Admin"
    fee_type = "Tuition"
    installment_name = "Term 1"

    class payment_date:
        @staticmethod
        def isoformat():
            return "2023-01-01"

    class created_at:
        pass

import sys
sys.path.append("erp-backend")

sys.modules['extensions'] = type('extensions', (), {'db': None, 'to_local_time': lambda x: type('dt', (), {'strftime': lambda x: ""})()})()
sys.modules['models'] = type('models', (), {'FeePayment': None, 'Student': None, 'StudentFee': None})()
def mock_token_required(f):
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper
sys.modules['helpers'] = type('helpers', (), {'token_required': mock_token_required, 'require_academic_year': lambda: ("2023", None, None)})()
sys.modules['flask'] = type('flask', (), {'Blueprint': lambda *args: type('bp', (), {'route': lambda *args, **kwargs: lambda x: x})(), 'jsonify': lambda x: x, 'request': None})()
sys.modules['sqlalchemy'] = type('sqlalchemy', (), {'func': None, 'or_': None})()
sys.modules['sqlalchemy.orm'] = type('sqlalchemy.orm', (), {'selectinload': None})()

import routes.report_routes

try:
    res = routes.report_routes.consolidate_receipts([MockPayment()])
    print("Success:", res)
except Exception as e:
    import traceback
    traceback.print_exc()
