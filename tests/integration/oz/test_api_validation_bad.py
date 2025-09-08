from fastapi.testclient import TestClient
from src.main import app
from tests.integration.oz.conftest import (
    fixture_oz_price_calc_fbs_bad,  # noqa: F401
    fixrure_oz_price_calc_fbo_bad,  # noqa: F401
    fixture_oz_profit_calc_fbs_bad,  # noqa: F401
    fixrure_oz_profit_calc_fbo_bad,  # noqa: F401
    fixture_oz_price_bulk_calc_fbs_bad,  # noqa: F401
    fixture_oz_price_bulk_calc_fbo_bad,  # noqa: F401
    fixture_oz_log_calc_fbs_bad,  # noqa: F401
    fixture_oz_log_calc_fbo_bad,  # noqa: F401
    fixture_oz_returns_calc_fbs_bad,  # noqa: F401
    fixture_oz_returns_calc_fbo_bad,  # noqa: F401
)

client = TestClient(app)

######################### Price ##########################


def test_ozon_price_calc_fbs(fixture_oz_price_calc_fbs_bad):  # noqa: F811
    response = client.post(
        "/api/v1/ozon/prices/fbs/calculate",
        json=fixture_oz_price_calc_fbs_bad,
    )
    assert response.status_code == 422


def test_ozon_price_calc_fbo(fixrure_oz_price_calc_fbo_bad):  # noqa: F811
    response = client.post(
        "/api/v1/ozon/prices/fbo/calculate/",
        json=fixrure_oz_price_calc_fbo_bad,
    )
    assert response.status_code == 422


######################## Profit ##########################


def test_ozon_profit_calc_fbs(fixture_oz_profit_calc_fbs_bad):  # noqa: F811
    response = client.post(
        "/api/v1/ozon/profits/fbs/calculate/",
        json=fixture_oz_profit_calc_fbs_bad,
    )
    assert response.status_code == 422


def test_ozon_profit_calc_fbo(fixrure_oz_profit_calc_fbo_bad):  # noqa: F811
    response = client.post(
        "/api/v1/ozon/profits/fbo/calculate/",
        json=fixrure_oz_profit_calc_fbo_bad,
    )
    assert response.status_code == 422


######################### Bulk ###########################


def test_ozon_price_calc_bulk_fbs(
    fixture_oz_price_bulk_calc_fbs_bad,  # noqa: F811
):
    response = client.post(
        "/api/v1/ozon/prices/fbs/bulk/calculate/",
        json=fixture_oz_price_bulk_calc_fbs_bad,
    )
    assert response.status_code == 422


def test_ozon_price_calc_bulk_fbo(
    fixture_oz_price_bulk_calc_fbo_bad,  # noqa: F811
):
    response = client.post(
        "/api/v1/ozon/prices/fbo/bulk/calculate/",
        json=fixture_oz_price_bulk_calc_fbo_bad,
    )
    assert response.status_code == 422


###################### Logistics #########################


def test_ozon_calc_log_fbs(fixture_oz_log_calc_fbs_bad):  # noqa: F811
    response = client.post(
        "/api/v1/ozon/logistics/fbs/calculate",
        json=fixture_oz_log_calc_fbs_bad,
    )
    assert response.status_code == 422


def test_ozon_calc_log_fbo(fixture_oz_log_calc_fbo_bad):  # noqa: F811
    response = client.post(
        "/api/v1/ozon/logistics/fbo/calculate",
        json=fixture_oz_log_calc_fbo_bad,
    )
    assert response.status_code == 422


####################### Returns ##########################


def test_ozon_calc_returns_fbs(fixture_oz_returns_calc_fbs_bad):  # noqa: F811
    response = client.post(
        "/api/v1/ozon/returns/fbs/calculate",
        json=fixture_oz_returns_calc_fbs_bad,
    )
    assert response.status_code == 422


def test_ozon_calc_returns_fbo(fixture_oz_returns_calc_fbo_bad):  # noqa: F811
    response = client.post(
        "/api/v1/ozon/returns/fbo/calculate",
        json=fixture_oz_returns_calc_fbo_bad,
    )
    assert response.status_code == 422
