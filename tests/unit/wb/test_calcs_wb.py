from decimal import Decimal, ROUND_UP
from src.calc.service.calculators.wb.logistics_wb import (
    calc_log_wb,
    calc_returns_wb,
)
from tests.unit.wb.confest import (
    fixture_calc_log_fbs,  # noqa: F401 # pyright: ignore
    fixture_calc_log_fbo,  # noqa: F401 # pyright: ignore
    fixture_calc_returns,  # noqa: F401 # pyright: ignore
)

##########################################################
#           Logistics and Returns Calculators            #
##########################################################


def test_calc_log_fbs_wb(fixture_calc_log_fbs):  # noqa: F811
    result = calc_log_wb(fixture_calc_log_fbs)
    assert result == Decimal("73.0")


def test_calc_log_fbo_wb(fixture_calc_log_fbo):  # noqa: F811
    result = calc_log_wb(fixture_calc_log_fbo)
    assert result == Decimal("131.4")


def test_calc_returns_wb(fixture_calc_returns):  # noqa: F811
    result = calc_returns_wb(fixture_calc_returns)
    result = result.quantize(Decimal("0.0"), rounding=ROUND_UP)
    assert result == Decimal("15.8")
