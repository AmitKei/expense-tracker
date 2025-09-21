import requests

def test_integration():
    base_url = "http://localhost:8000"
    response = requests.get(f"{base_url}/expenses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
