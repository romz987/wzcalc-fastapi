from fastapi.testclient import TestClient
from src.main import app
from .payloads import WB_CALC, WB_BULK_CALC, WB_LOG_CALC, WB_RETURNS_CALC


client = TestClient(app)


# Сделать фикстурами
def test_wb_calc():
    response = client.post("/api/v1/wb/prices/calculate", json=WB_CALC)
    assert response.status_code == 200
    result = response.json()
    assert result["ok"] == "it works!"


def test_wb_bulk_calc():
    response = client.post(
        "/api/v1/wb/prices/bulk/calculate/",
        json=WB_BULK_CALC,
    )
    assert response.status_code == 200
    result = response.json()
    assert result["ok"] == "it works!"


def test_wb_logistics():
    response = client.post("/api/v1/wb/logistics/calculate", json=WB_LOG_CALC)
    assert response.status_code == 200
    result = response.json()
    assert result["ok"] == "it works!"


def test_wb_returns():
    response = client.post(
        "/api/v1/wb/returns/calculate",
        json=WB_RETURNS_CALC,
    )
    assert response.status_code == 200
    result = response.json()
    assert result["ok"] == "it works!"
