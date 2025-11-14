import pytest
from decimal import Decimal
from src.calc.core.domain import wb_calcdata

#############################################################################
#                   Fixtures: Wildberries calculators                       #
#############################################################################
#############################################################################
#                                Logistics                                  #
#############################################################################


@pytest.fixture
def fixture_log_costs():
    return wb_calcdata.WbLogCosts(
        base_price=Decimal("46"),
        volume_factor=Decimal("14"),
        # new costs
        min_lim_1_price=Decimal("23"),
        min_lim_2_price=Decimal("26"),
        min_lim_3_price=Decimal("29"),
        min_lim_4_price=Decimal("30"),
        min_lim_5_price=Decimal("32"),
    )
