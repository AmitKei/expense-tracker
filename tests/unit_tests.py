# tests/unit_tests.py

def test_invalid_add_expense_missing_fields(test_app):
    response = test_app.post("/expenses", json={
        "description": "Missing amount"
    })
    assert response.status_code == 422  # Unprocessable Entity

def test_invalid_expense_amount_type(test_app):
    response = test_app.post("/expenses", json={
        "amount": "not-a-number",
        "description": "Bad data",
        "category": "Other"
    })
    assert response.status_code == 422
