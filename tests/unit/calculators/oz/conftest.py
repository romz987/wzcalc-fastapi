import pytest
from decimal import Decimal
from src.calc.core.domain import oz_calcdata


#############################################################################
#                       Fixtures: Ozon calculators                          #
#############################################################################
#############################################################################
#                                Logistics                                  #
#############################################################################


@pytest.fixture
def fixture_log_costs_fbs():
    return oz_calcdata.OzLogFbsCosts(
        minimal_price_fbs=Decimal("43"),
        base_price_fbs=Decimal("76"),
        volume_factor_fbs=Decimal("12"),
        fix_large_fbs=Decimal("2344"),
    )


@pytest.fixture
def fixture_log_costs_fbo():
    return oz_calcdata.OzLogFboCosts(
        base_price_fbo=Decimal("63"),
        volume_factor_fbo=Decimal("10"),
        fix_large_fbo=Decimal("1953"),
    )
