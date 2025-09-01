from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_ozon_calc_fbs(ozon_fbs_calc_good):
    response = client.post(
        "/api/v1/ozon/prices/fbs/calculate",
        json=ozon_fbs_calc_good,
    )
    assert response.status_code == 200


def test_ozon_calc_fbo(ozon_fbo_calc_good):
    response = client.post(
        "/api/v1/ozon/prices/fbo/calculate/",
        json=ozon_fbo_calc_good,
    )
    assert response.status_code == 200


def test_ozon_calc_bulk_fbs(ozon_fbs_bulk_calc_good):
    response = client.post(
        "/api/v1/ozon/prices/fbs/bulk/calculate/",
        json=ozon_fbs_bulk_calc_good,
    )
    assert response.status_code == 200


def test_ozon_calc_bulk_fbo(ozon_fbo_bulk_calc_good):
    response = client.post(
        "/api/v1/ozon/prices/fbo/bulk/calculate/",
        json=ozon_fbo_bulk_calc_good,
    )
    assert response.status_code == 200


def test_ozon_calc_log_fbs(ozon_fbs_log_good):
    response = client.post(
        "/api/v1/ozon/logistics/fbs/calculate",
        json=ozon_fbs_log_good,
    )
    assert response.status_code == 200


def test_ozon_calc_log_fbo(ozon_fbo_log_good):
    response = client.post(
        "/api/v1/ozon/logistics/fbo/calculate",
        json=ozon_fbo_log_good,
    )
    assert response.status_code == 200


def test_ozon_calc_returns_fbs(ozon_fbs_returns_good):
    response = client.post(
        "/api/v1/ozon/returns/fbs/calculate",
        json=ozon_fbs_returns_good,
    )
    assert response.status_code == 200


def test_ozon_calc_returns_fbo(ozon_fbo_returns_good):
    response = client.post(
        "/api/v1/ozon/returns/fbo/calculate",
        json=ozon_fbo_returns_good,
    )
    assert response.status_code == 200
