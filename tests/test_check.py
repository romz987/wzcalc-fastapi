from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)


def test_root_route():
    response = client.get("/check/")
    assert response.status_code == 200
    result = response.json()
    assert result["status"] == "up"
