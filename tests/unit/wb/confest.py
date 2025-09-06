import pytest
from decimal import Decimal
from src.calc.service.calculators.wb import calcdata_wb

##########################################################
#         Test Logistics and Returns Calculators         #
##########################################################


@pytest.fixture
def fixture_calc_log_fbs():
    return calcdata_wb.LogWbData(
        box_size="15*10*10",
        local_index=Decimal("1"),
        box_volume=Decimal("1.5"),
        base_price=Decimal("63"),
        volume_factor=Decimal("10"),
    )


@pytest.fixture
def fixture_calc_log_fbo():
    return calcdata_wb.LogWbData(
        box_size="15*10*10",
        local_index=Decimal("1.8"),
        box_volume=Decimal("1.5"),
        base_price=Decimal("63"),
        volume_factor=Decimal("10"),
    )


@pytest.fixture
def fixture_calc_returns():
    return calcdata_wb.ReturnsWbData(
        box_size="15*10*10",
        redemption_percentage=Decimal("92"),
        nonredemption_processing_cost=Decimal("50"),
        local_index=Decimal("1.8"),
        base_price=Decimal("38"),
        volume_factor=Decimal("9.5"),
        # flowing
        box_volume=Decimal("1.5"),
        logistics_fee=Decimal("131.4"),
    )
