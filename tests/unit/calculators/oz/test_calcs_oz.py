import pytest
from decimal import Decimal

# dataclass
from src.calc.core.domain import cm_calcdata

# calculators
from src.calc.core.calculators.ozon import (
    oz_log_fbs_clc,
    oz_log_fbo_clc,
    oz_returns_clc,
)

# fixtures
from tests.unit.calculators.oz.conftest import (
    fixture_log_costs_fbs,  # noqa: F401 # pyright: ignore
    fixture_log_costs_fbo,  # noqa: F401 # pyright: ignore
)


#############################################################################
#                          Tests: Ozon calculators                          #
#############################################################################
#############################################################################
#                                Logistics                                  #
#############################################################################


################################## FBS ######################################
@pytest.mark.parametrize(
    "local_index, box_volume, expected_result",
    [
        # volume =< 0.4l
        (Decimal("1"), Decimal("0.3"), Decimal("43")),
        (Decimal("1"), Decimal("0.4"), Decimal("43")),
        (Decimal("1.8"), Decimal("0.4"), Decimal("77.4")),
        # volume =< 1l
        (Decimal("1"), Decimal("0.5"), Decimal("76")),
        (Decimal("1"), Decimal("1.0"), Decimal("76")),
        (Decimal("1.8"), Decimal("1.0"), Decimal("136.8")),
        # volume > 1l
        (Decimal("1"), Decimal("1.1"), Decimal("88")),
        (Decimal("1.8"), Decimal("1.1"), Decimal("158.4")),
        # volume > 190l
        (Decimal("1"), Decimal("190.0"), Decimal("2344")),
        (Decimal("1"), Decimal("191.0"), Decimal("2344")),
        (Decimal("1"), Decimal("500.0"), Decimal("2344")),
        (Decimal("1.8"), Decimal("500.0"), Decimal("4219.2")),
    ],
)
def test_oz_log_fbs(
    local_index,
    box_volume,
    expected_result,
    fixture_log_costs_fbs,  # noqa: F811
):
    log_costs = fixture_log_costs_fbs
    log_params = cm_calcdata.LogMainParams(
        local_index=local_index,
        box_volume=box_volume,
    )
    result = oz_log_fbs_clc(log_params, log_costs)
    assert result == expected_result


################################## FBO ######################################
@pytest.mark.parametrize(
    "local_index, box_volume, expected_result",
    [
        # volume =< 0.4l
        (Decimal("1"), Decimal("0.3"), Decimal("63")),
        (Decimal("1"), Decimal("0.4"), Decimal("63")),
        (Decimal("1.8"), Decimal("0.4"), Decimal("113.4")),
        # volume =< 1l
        (Decimal("1"), Decimal("0.5"), Decimal("63")),
        (Decimal("1"), Decimal("1.0"), Decimal("63")),
        (Decimal("1.8"), Decimal("1.0"), Decimal("113.4")),
        # volume > 1l
        (Decimal("1"), Decimal("1.1"), Decimal("73")),
        (Decimal("1.8"), Decimal("1.1"), Decimal("131.4")),
        # volume > 190l
        (Decimal("1"), Decimal("190.0"), Decimal("1953")),
        (Decimal("1"), Decimal("191.0"), Decimal("1953")),
        (Decimal("1"), Decimal("500.0"), Decimal("1953")),
        (Decimal("1.8"), Decimal("500.0"), Decimal("3515.4")),
    ],
)
def test_oz_log_fbo(
    local_index,
    box_volume,
    expected_result,
    fixture_log_costs_fbo,  # noqa: F811
):
    # vars
    log_costs = fixture_log_costs_fbo
    log_params = cm_calcdata.LogMainParams(
        local_index=local_index,
        box_volume=box_volume,
    )
    # test
    result = oz_log_fbo_clc(log_params, log_costs)
    assert result == expected_result


#############################################################################
#                          Tests: Ozon calculators                          #
#############################################################################
#############################################################################
#                                 Returns                                   #
#############################################################################


@pytest.mark.parametrize(
    "redemption_percentage, nonredemption_processing_cost, expected_result",
    [
        (Decimal("100"), Decimal("15"), Decimal("0")),
        (Decimal("92"), Decimal("15"), Decimal("22.8")),
        (Decimal("50"), Decimal("15"), Decimal("261.4")),
        (Decimal("1"), Decimal("15"), Decimal("25878.6")),
    ],
)
def test_oz_returns(
    redemption_percentage,
    nonredemption_processing_cost,
    expected_result,
):
    # vars
    logistics_fee = Decimal("158.4")
    reverse_logistics_fee = Decimal("88")
    return_params = cm_calcdata.ReturnsParams(
        redemption_percentage=redemption_percentage,
        nonredemption_processing_cost=nonredemption_processing_cost,
    )
    # test
    result = oz_returns_clc(
        return_params,
        logistics_fee,
        reverse_logistics_fee,
    )
    assert result == expected_result
