from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)


# Сделать фикстурами
def test_wb_calc(wb_calc_good):
    response = client.post("/api/v1/wb/prices/calculate", json=wb_calc_good)
    assert response.status_code == 200


def test_wb_bulk_calc(wb_bulk_calc_good):
    response = client.post(
        "/api/v1/wb/prices/bulk/calculate/",
        json=wb_bulk_calc_good,
    )
    assert response.status_code == 200


def test_wb_logistics(wb_log_good):
    response = client.post("/api/v1/wb/logistics/calculate", json=wb_log_good)
    assert response.status_code == 200


def test_wb_returns(wb_returns_good):
    response = client.post(
        "/api/v1/wb/returns/calculate",
        json=wb_returns_good,
    )
    assert response.status_code == 200
