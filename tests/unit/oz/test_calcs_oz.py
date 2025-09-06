from decimal import Decimal, ROUND_UP
from src.calc.service.calculators.common import get_box_volume
from src.calc.service.calculators.oz.logistics_oz import (
    calc_log_fbs_oz,
    calc_log_fbo_oz,
    calc_returns_oz,
)

##########################################################
#         Test Logistics and Returns Calculators         #
##########################################################


def test_get_box_volume():
    box_size = "15*10*10"
    result = get_box_volume(box_size)
    assert result == Decimal("1.5")


def test_calc_log_fbs_oz(fixture_calc_log_fbs):
    result = calc_log_fbs_oz(fixture_calc_log_fbs)
    assert result == Decimal("158.4")


def test_calc_log_fbo_oz(fixture_calc_log_fbo):
    result = calc_log_fbo_oz(fixture_calc_log_fbo)
    assert result == Decimal("131.4")


def test_calc_returns_oz_cost_fbs(fixture_calc_fbs_returns):
    result = calc_returns_oz(fixture_calc_fbs_returns)
    result = result.quantize(Decimal("0.0"), rounding=ROUND_UP)
    assert result == Decimal("22.8")


def test_calc_returns_oz_cost_fbo(fixture_calc_fbo_returns):
    result = calc_returns_oz(fixture_calc_fbo_returns)
    result = result.quantize(Decimal("0.0"), rounding=ROUND_UP)
    assert result == Decimal("20.4")
