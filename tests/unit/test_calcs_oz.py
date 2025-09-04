from decimal import Decimal, ROUND_UP
from src.calc.service.calculators.common import get_box_volume
from src.calc.service.calculators.oz.logistics_oz import (
    calc_log_fbs,
    calc_log_fbo,
    calc_returns,
)


def test_get_box_volume():
    box_size = "15*10*10"
    result = get_box_volume(box_size)
    assert result == Decimal("1.5")


def test_calc_log_fbs(fixture_calc_log_fbs):
    result = calc_log_fbs(fixture_calc_log_fbs)
    assert result == Decimal("158.4")


def test_calc_log_fbo(fixture_calc_log_fbo):
    result = calc_log_fbo(fixture_calc_log_fbo)
    assert result == Decimal("131.4")


def test_calc_returns_cost_fbs(fixture_calc_fbs_returns):
    # box volume
    fixture_calc_fbs_returns.box_volume = get_box_volume(
        fixture_calc_fbs_returns.box_size,
    )
    assert fixture_calc_fbs_returns.box_volume == Decimal("1.5")
    # logistics_fee
    fixture_calc_fbs_returns.logistics_fee = calc_log_fbs(
        fixture_calc_fbs_returns,
    )
    assert fixture_calc_fbs_returns.logistics_fee == Decimal("158.4")
    # reverse logistics fbs
    current_local_index, fixture_calc_fbs_returns.local_index = (
        fixture_calc_fbs_returns.local_index,
        1,
    )
    fixture_calc_fbs_returns.reverse_logistics_fee = calc_log_fbs(
        fixture_calc_fbs_returns,
    )
    fixture_calc_fbs_returns.local_index = current_local_index
    assert fixture_calc_fbs_returns.reverse_logistics_fee == Decimal("88")
    assert fixture_calc_fbs_returns.local_index == Decimal("1.8")
    # nonredemptions_cost
    result = calc_returns(fixture_calc_fbs_returns)
    result = result.quantize(Decimal("0.0"), rounding=ROUND_UP)
    assert result == Decimal("22.8")
