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


#############################################################################
#                                  Profit                                   #
#############################################################################


@pytest.fixture
def fixture_profit_params():
    return wb_calcdata.WbProfitParams(
        tax_system="simple",
        count=Decimal("4"),
        cost_per_one=Decimal("17.2"),
        comissions_percent=Decimal("21"),
        aquiring_percent=Decimal("2"),
        tax_percent=Decimal("5"),
        risk_percent=Decimal("3"),
        box_cost=Decimal("10"),
        wage_cost=Decimal("10"),
        total_price=Decimal("2000"),
    )


@pytest.fixture
def fixture_base_fees():
    return wb_calcdata.WbBaseFees(
        cost_row=Decimal("68.8"),
        comission_fee=Decimal("420"),
        aquiring_fee=Decimal("40"),
    )


@pytest.fixture
def fixture_log_fees():
    return wb_calcdata.WbLogFees(
        box_volume=Decimal("1.5"),
        logistics_fee=Decimal("95.4"),
        returns_fee=Decimal("9.6"),
    )
