from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
headers = {"username": "testuser"}

def test_add_and_get_expense():
    data = {"description": "Pizza", "amount": 25.0, "category": "Food"}
    res = client.post("/expenses", json=data, headers=headers)
    assert res.status_code == 200

    res = client.get("/expenses", headers=headers)
    assert res.status_code == 200
    assert any(exp["description"] == "Pizza" for exp in res.json())
