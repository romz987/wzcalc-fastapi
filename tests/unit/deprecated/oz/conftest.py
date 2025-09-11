import pytest
from decimal import Decimal
from src.calc.service.calculators.oz import calcdata_oz

##########################################################
#         Test Logistics and Returns Calculators         #
##########################################################


@pytest.fixture
def fixture_calc_log_fbs():
    return calcdata_oz.LogFbsData(
        local_index=Decimal("1.8"),
        box_volume=Decimal("1.5"),
        minimal_price_fbs=Decimal("43"),
        base_price_fbs=Decimal("76"),
        volume_factor_fbs=Decimal("12"),
        fix_large_fbs=Decimal("2344"),
        box_size="15*10*10",
    )


@pytest.fixture
def fixture_calc_log_fbo():
    return calcdata_oz.LogFboData(
        local_index=Decimal("1.8"),
        box_volume=Decimal("1.1"),
        base_price_fbo=Decimal("63"),
        volume_factor_fbo=Decimal("10"),
        fix_large_fbo=Decimal("1953"),
        box_size="15*10*10",
    )


@pytest.fixture
def fixture_calc_fbs_returns():
    return calcdata_oz.ReturnsFbsData(
        box_size="15*10*10",
        redemption_percentage=Decimal("92"),
        nonredemption_processing_cost=Decimal("15"),
        local_index=Decimal("1.8"),
        # fbs logistics vars
        minimal_price_fbs=Decimal("43"),
        base_price_fbs=Decimal("76"),
        volume_factor_fbs=Decimal("12"),
        fix_large_fbs=Decimal("2344"),
        # flowing
        box_volume=Decimal("1.5"),
        logistics_fee=Decimal("158.4"),
        reverse_logistics_fee=Decimal("88"),
    )


@pytest.fixture
def fixture_calc_fbo_returns():
    return calcdata_oz.ReturnsFboData(
        box_size="15*10*10",
        redemption_percentage=Decimal("92"),
        nonredemption_processing_cost=Decimal("15"),
        local_index=Decimal("1.8"),
        # fbs logistics vars
        minimal_price_fbs=Decimal("43"),
        base_price_fbs=Decimal("76"),
        volume_factor_fbs=Decimal("12"),
        fix_large_fbs=Decimal("2344"),
        # fbo logistics vars
        base_price_fbo=Decimal("63"),
        volume_factor_fbo=Decimal("10"),
        fix_large_fbo=Decimal("1953"),
        # flowing
        box_volume=Decimal("1.5"),
        logistics_fee=Decimal("131.4"),
        reverse_logistics_fee=Decimal("88"),
    )
