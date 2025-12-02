import pytest
from decimal import Decimal

# dataclass
from src.calc.core.domain import cm_calcdata

# calculators
from src.calc.core.calculators.wildberries import (
    wb_log_clc,
    wb_returns_clc,
    wb_profit_ts_simple_clc,
    wb_profit_ts_diff_clc,
)

# fixtures
from tests.unit.calculators.wb.conftest import (
    fixture_log_costs,  # noqa: F401 # pyright: ignore
    fixture_profit_params,  # noqa: F401 # pyright: ignore
    fixture_base_fees,  # noqa: F401 # pyright: ignore
    fixture_log_fees,  # noqa: F401 # pyright: ignore
)


#############################################################################
#                     Tests: Wildberries calculators                        #
#############################################################################
#############################################################################
#                                Logistics                                  #
#############################################################################


@pytest.mark.parametrize(
    "local_index, box_volume, expected_result",
    [
        # zero box volume
        (Decimal("1"), Decimal("0"), Decimal("0")),
        # 0 < volume < 0.2l
        (Decimal("1"), Decimal("0.1"), Decimal("23")),
        (Decimal("1"), Decimal("0.2"), Decimal("23")),
        (Decimal("1.8"), Decimal("0.2"), Decimal("41.4")),
        # volume 0.2 -> 0.4l
        (Decimal("1"), Decimal("0.3"), Decimal("26")),
        (Decimal("1"), Decimal("0.4"), Decimal("26")),
        (Decimal("1.8"), Decimal("0.4"), Decimal("46.8")),
        # volume 0.4 -> 0.6l
        (Decimal("1"), Decimal("0.5"), Decimal("29")),
        (Decimal("1"), Decimal("0.6"), Decimal("29")),
        (Decimal("1.8"), Decimal("0.6"), Decimal("52.2")),
        # volume 0.6 -> 0.8l
        (Decimal("1"), Decimal("0.7"), Decimal("30")),
        (Decimal("1"), Decimal("0.8"), Decimal("30")),
        (Decimal("1.8"), Decimal("0.8"), Decimal("54")),
        # volume 0.8 -> 1l
        (Decimal("1"), Decimal("0.9"), Decimal("32")),
        (Decimal("1"), Decimal("1"), Decimal("32")),
        (Decimal("1.8"), Decimal("1"), Decimal("57.6")),
        # volume > 1l
        (Decimal("1"), Decimal("1.2"), Decimal("48.8")),
        (Decimal("1"), Decimal("2"), Decimal("60")),
        (Decimal("1.8"), Decimal("2"), Decimal("108")),
    ],
)
def test_wb_log(
    local_index,
    box_volume,
    expected_result,
    fixture_log_costs,  # noqa: F811
):
    log_costs = fixture_log_costs
    log_params = cm_calcdata.LogMainParams(
        local_index=local_index,
        box_volume=box_volume,
    )
    result = wb_log_clc(log_params, log_costs)
    assert result == expected_result


#############################################################################
#                    Tests: Wildberries calculators                         #
#############################################################################
#############################################################################
#                                 Returns                                   #
#############################################################################


@pytest.mark.parametrize(
    "redemption_percentage, nonredemption_processing_cost, expected_result",
    [
        (Decimal("1"), Decimal("50"), Decimal("11880")),
        (Decimal("50"), Decimal("50"), Decimal("120")),
        (Decimal("92"), Decimal("50"), Decimal("10.5")),
        (Decimal("100"), Decimal("50"), Decimal("0")),
    ],
)
def test_wb_returns(
    redemption_percentage,
    nonredemption_processing_cost,
    expected_result,
):
    # vars
    logistics_fee = Decimal("70")
    return_params = cm_calcdata.ReturnsParams(
        redemption_percentage=redemption_percentage,
        nonredemption_processing_cost=nonredemption_processing_cost,
    )
    # test
    result = wb_returns_clc(return_params, logistics_fee)
    assert result == expected_result


#############################################################################
#                                  Profit                                   #
#############################################################################


def test_wb_profit_simple(
    fixture_profit_params,  # noqa: F811
    fixture_base_fees,  # noqa: F811
    fixture_log_fees,  # noqa: F811
):
    # args
    profit_params = fixture_profit_params
    base_fees = fixture_base_fees
    log_fees = fixture_log_fees
    # test
    result = wb_profit_ts_simple_clc(profit_params, base_fees, log_fees)
    assert result == (Decimal("100"), Decimal("60"), Decimal("1186.2"))


def test_wb_profit_diff(
    fixture_profit_params,  # noqa: F811
    fixture_base_fees,  # noqa: F811
    fixture_log_fees,  # noqa: F811
):
    # args
    profit_params = fixture_profit_params
    base_fees = fixture_base_fees
    log_fees = fixture_log_fees
    # test
    result = wb_profit_ts_diff_clc(profit_params, base_fees, log_fees)
    assert result == (Decimal("67.31"), Decimal("60"), Decimal("1218.89"))
