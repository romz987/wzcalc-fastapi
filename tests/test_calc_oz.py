from fastapi.testclient import TestClient
from src.main import app

from .payloads import (
    OZON_FBS_CALC,
    OZON_FBO_CALC,
    OZON_LOG_FBS_CALC,
    OZON_LOG_FBO_CALC,
    OZON_FBS_BULK_CALC,
    OZON_FBO_BULK_CALC,
    OZON_RETURNS_FBS_CALC,
    OZON_RETURNS_FBO_CALC,
)

client = TestClient(app)


def test_ozon_calc_fbs():
    response = client.post(
        "/api/v1/ozon/prices/fbs/calculate/",
        json=OZON_FBS_CALC,
    )
    assert response.status_code == 200
    result = response.json()
    assert result["ok"] == "it works!"


def test_ozon_calc_fbo():
    response = client.post(
        "/api/v1/ozon/prices/fbo/calculate/",
        json=OZON_FBO_CALC,
    )
    assert response.status_code == 200
    result = response.json()
    assert result["ok"] == "it works!"


def test_ozon_calc_bulk_fbs():
    response = client.post(
        "/api/v1/ozon/prices/fbs/bulk/calculate/",
        json=OZON_FBS_BULK_CALC,
    )
    assert response.status_code == 200
    result = response.json()
    assert result["ok"] == "it works!"


def test_ozon_calc_bulk_fbo():
    response = client.post(
        "/api/v1/ozon/prices/fbo/bulk/calculate/",
        json=OZON_FBO_BULK_CALC,
    )
    assert response.status_code == 200
    result = response.json()
    assert result["ok"] == "it works!"


def test_ozon_calc_log_fbo():
    response = client.post(
        "/api/v1/ozon/logistics/fbs/calculate/",
        json=OZON_LOG_FBS_CALC,
    )
    assert response.status_code == 200
    result = response.json()
    assert result["ok"] == "it works!"


def test_ozon_calc_log_fbs():
    response = client.post(
        "/api/v1/ozon/logistics/fbo/calculate/",
        json=OZON_LOG_FBO_CALC,
    )
    assert response.status_code == 200
    result = response.json()
    assert result["ok"] == "it works!"


def test_ozon_calc_returns_fbo():
    response = client.post(
        "/api/v1/ozon/returns/fbs/calculate/",
        json=OZON_RETURNS_FBS_CALC,
    )
    assert response.status_code == 200
    result = response.json()
    assert result["ok"] == "it works!"


def test_ozon_calc_returns_fbs():
    response = client.post(
        "/api/v1/ozon/returns/fbo/calculate/",
        json=OZON_RETURNS_FBO_CALC,
    )
    assert response.status_code == 200
    result = response.json()
    assert result["ok"] == "it works!"
