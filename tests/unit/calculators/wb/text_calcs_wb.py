import pytest
from decimal import Decimal

# dataclass
from src.calc.core.domain import cm_calcdata

# calculators
from src.calc.core.calculators.wildberries import wb_log_clc

# fixtures
from tests.unit.calculators.wb.conftest import (
    fixture_log_costs,  # noqa: F401 # pyright: ignore
)


#############################################################################
#                     Tests: Wildberries calculators                        #
#############################################################################
#############################################################################
#                                Logistics                                  #
#############################################################################


################################## FBS ######################################


################################## FBO ######################################
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
def test_wb_log_fbs(
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
