import pytest

##########################################################
#                    Единичный расчет                    #
##########################################################


@pytest.fixture
def ozon_fbs_calc_good():
    return {
        "tax_system": "simple",
        "comission_percent": "20",
        "acquiring_percent": "2",
        "shipment_processing": "20",
        "local_index": "1",
        "tax_percent": "15",
        "risk_percent": "3",
        "redemption_percentage": "92",
        "profit_percent": "50",
        "cost_per_one": "17.2",
        "count": "4",
        "wage_cost": "10",
        "box_cost": "10",
        "box_size": "11*10*10",
        "nonredemption_processing_cost": "15",
        "last_mile_percent": "5.5",
        "minimal_price_fbs": "123",
        "base_price_fbs": "45",
        "volume_factor_fbs": "25",
        "fix_large_fbs": "1234",
    }


@pytest.fixture(
    params=[
        {"tax_system": "simpl"},
        {"box_size": "1111*10*10"},
        {"comission_percent": "-1"},
        {"comission_percent": "0"},
        {"comission_percent": "1.11"},
        {"comission_percent": "100.1"},
        {"local_index": "0"},
        {"local_index": "0.11"},
        {"local_index": "10.1"},
        {"cost_per_one": "-1"},
        {"cost_per_one": "0.111"},
        {"cost_per_one": "12345678"},
        {"minimal_price_fbs": "0"},
        {"minimal_price_fbs": "100001.1"},
        {"minimal_price_fbs": "3456.12"},
        {"some_new_attr": "1"},
    ],
)
def ozon_fbs_calc_bad(request, ozon_fbs_calc_good):
    bad_data = ozon_fbs_calc_good.copy()
    bad_data.update(request.param)
    return bad_data


@pytest.fixture
def ozon_fbo_calc_good():
    return {
        "tax_system": "simple",
        "comission_percent": "20",
        "acquiring_percent": "2",
        "shipment_processing": "20",
        "local_index": "1",
        "tax_percent": "15",
        "risk_percent": "3",
        "redemption_percentage": "92",
        "profit_percent": "50",
        "cost_per_one": "17.2",
        "count": "4",
        "wage_cost": "10",
        "box_cost": "10",
        "box_size": "11*10*10",
        "nonredemption_processing_cost": "15",
        "last_mile_percent": "5.5",
        "base_price_fbo": "123",
        "volume_factor_fbo": "123",
        "fix_large_fbo": "123",
    }


@pytest.fixture(
    params=[
        {"tax_system": "simpl"},
        {"box_size": "1111*10*10"},
        {"comission_percent": "-1"},
        {"comission_percent": "0"},
        {"comission_percent": "1.11"},
        {"comission_percent": "100.1"},
        {"local_index": "0"},
        {"local_index": "0.11"},
        {"local_index": "10.1"},
        {"cost_per_one": "-1"},
        {"cost_per_one": "0.111"},
        {"cost_per_one": "12345678"},
        {"minimal_price_fbo": "0"},
        {"minimal_price_fbo": "100001.1"},
        {"minimal_price_fbo": "3456.12"},
        {"some_new_attr": "1"},
    ],
)
def ozon_fbo_calc_bad(request, ozon_fbo_calc_good):
    bad_data = ozon_fbo_calc_good.copy()
    bad_data.update(request.param)
    return bad_data


##########################################################
#                      BULK расчет                       #
##########################################################


@pytest.fixture
def ozon_fbs_bulk_calc_good():
    return [
        {
            "tax_system": "simple",
            "comission_percent": "20",
            "acquiring_percent": "2",
            "shipment_processing": "20",
            "local_index": "1",
            "tax_percent": "15",
            "risk_percent": "3",
            "redemption_percentage": "92",
            "profit_percent": "50",
            "cost_per_one": "17.2",
            "count": "4",
            "wage_cost": "10",
            "box_cost": "10",
            "box_size": "11*10*10",
            "nonredemption_processing_cost": "15",
            "last_mile_percent": "5.5",
            "minimal_price_fbs": "123",
            "base_price_fbs": "45",
            "volume_factor_fbs": "25",
            "fix_large_fbs": "1234",
        },
        {
            "tax_system": "simple",
            "comission_percent": "20",
            "acquiring_percent": "2",
            "shipment_processing": "20",
            "local_index": "1",
            "tax_percent": "15",
            "risk_percent": "3",
            "redemption_percentage": "92",
            "profit_percent": "50",
            "cost_per_one": "17.2",
            "count": "4",
            "wage_cost": "10",
            "box_cost": "10",
            "box_size": "11*10*10",
            "nonredemption_processing_cost": "15",
            "last_mile_percent": "5.5",
            "minimal_price_fbs": "123",
            "base_price_fbs": "45",
            "volume_factor_fbs": "25",
            "fix_large_fbs": "1234",
        },
    ]


@pytest.fixture(
    params=[
        {"tax_system": "simpl"},
        {"box_size": "1111*10*10"},
        {"comission_percent": "-1"},
        {"comission_percent": "0"},
        {"comission_percent": "1.11"},
        {"comission_percent": "100.1"},
        {"local_index": "0"},
        {"local_index": "0.11"},
        {"local_index": "10.1"},
        {"cost_per_one": "-1"},
        {"cost_per_one": "0.111"},
        {"cost_per_one": "12345678"},
        {"minimal_price_fbs": "0"},
        {"minimal_price_fbs": "100001.1"},
        {"minimal_price_fbs": "3456.12"},
        {"some_new_attr": "1"},
    ],
)
def ozon_fbs_bulk_calc_bad(request, ozon_fbs_bulk_calc_good):
    bad_data = ozon_fbs_bulk_calc_good.copy()
    bad_data[0].update(request.param)
    return bad_data


@pytest.fixture
def ozon_fbo_bulk_calc_good():
    return [
        {
            "tax_system": "simple",
            "comission_percent": "20",
            "acquiring_percent": "2",
            "shipment_processing": "20",
            "local_index": "1",
            "tax_percent": "15",
            "risk_percent": "3",
            "redemption_percentage": "92",
            "profit_percent": "50",
            "cost_per_one": "17.2",
            "count": "4",
            "wage_cost": "10",
            "box_cost": "10",
            "box_size": "11*10*10",
            "nonredemption_processing_cost": "15",
            "last_mile_percent": "5.5",
            "base_price_fbo": "123",
            "volume_factor_fbo": "123",
            "fix_large_fbo": "123",
        },
        {
            "tax_system": "simple",
            "comission_percent": "20",
            "acquiring_percent": "2",
            "shipment_processing": "20",
            "local_index": "1",
            "tax_percent": "15",
            "risk_percent": "3",
            "redemption_percentage": "92",
            "profit_percent": "50",
            "cost_per_one": "17.2",
            "count": "4",
            "wage_cost": "10",
            "box_cost": "10",
            "box_size": "11*10*10",
            "nonredemption_processing_cost": "15",
            "last_mile_percent": "5.5",
            "base_price_fbo": "123",
            "volume_factor_fbo": "123",
            "fix_large_fbo": "123",
        },
    ]


@pytest.fixture(
    params=[
        {"tax_system": "simpl"},
        {"box_size": "1111*10*10"},
        {"comission_percent": "-1"},
        {"comission_percent": "0"},
        {"comission_percent": "1.11"},
        {"comission_percent": "100.1"},
        {"local_index": "0"},
        {"local_index": "0.11"},
        {"local_index": "10.1"},
        {"cost_per_one": "-1"},
        {"cost_per_one": "0.111"},
        {"cost_per_one": "12345678"},
        {"minimal_price_fbo": "0"},
        {"minimal_price_fbo": "100001.1"},
        {"minimal_price_fbo": "3456.12"},
        {"some_new_attr": "1"},
    ],
)
def ozon_fbo_bulk_calc_bad(request, ozon_fbo_bulk_calc_good):
    bad_data = ozon_fbo_bulk_calc_good.copy()
    bad_data[0].update(request.param)
    return bad_data


##########################################################
#               Расчет стоимости логистики               #
##########################################################


@pytest.fixture
def ozon_fbs_log_good():
    return {
        "box_size": "125*125*125",
        "local_index": "1",
        "minimal_price_fbs": "10",
        "base_price_fbs": "10",
        "volume_factor_fbs": "10",
        "fix_large_fbs": "102",
    }


@pytest.fixture(
    params=[
        {"box_size": "111*1011*10"},
        {"local_index": "0"},
        {"local_index": "0.11"},
        {"local_index": "10.1"},
        {"minimal_price_fbs": "0"},
        {"minimal_price_fbs": "100001.1"},
        {"minimal_price_fbs": "3456.12"},
        {"some_new_attr": "1"},
    ],
)
def ozon_fbs_log_bad(request, ozon_fbs_log_good):
    bad_data = ozon_fbs_log_good.copy()
    bad_data.update(request.param)
    return bad_data


@pytest.fixture
def ozon_fbo_log_good():
    return {
        "box_size": "125*125*99",
        "local_index": "1.5",
        "base_price_fbo": "123",
        "volume_factor_fbo": "123",
        "fix_large_fbo": "123",
    }


@pytest.fixture(
    params=[
        {"box_size": "111*1011*10"},
        {"local_index": "0"},
        {"local_index": "0.11"},
        {"local_index": "10.1"},
        {"base_price_fbo": "0"},
        {"base_price_fbo": "100001.1"},
        {"base_price_fbo": "3456.12"},
        {"some_new_attr": "1"},
    ],
)
def ozon_fbo_log_bad(request, ozon_fbo_log_good):
    bad_data = ozon_fbo_log_good.copy()
    bad_data.update(request.param)
    return bad_data


##########################################################
#               Расчет стоимости возвратов               #
##########################################################


@pytest.fixture
def ozon_fbs_returns_good():
    return {
        "box_size": "125*125*125",
        "redemption_percentage": "92",
        "local_index": "1",
        "minimal_price_fbs": "10",
        "base_price_fbs": "10",
        "volume_factor_fbs": "10",
        "fix_large_fbs": "102",
    }


@pytest.fixture(
    params=[
        {"box_size": "111*1011*10"},
        {"local_index": "0"},
        {"local_index": "0.11"},
        {"local_index": "10.1"},
        {"redemption_percentage": "-1"},
        {"redemption_percentage": "0"},
        {"redemption_percentage": "1.11"},
        {"redemption_percentage": "100.1"},
        {"minimal_price_fbs": "0"},
        {"minimal_price_fbs": "100001.1"},
        {"minimal_price_fbs": "3456.12"},
        {"some_new_attr": "1"},
    ],
)
def ozon_fbs_returns_bad(request, ozon_fbs_returns_good):
    bad_data = ozon_fbs_returns_good.copy()
    bad_data.update(request.param)
    return bad_data


@pytest.fixture
def ozon_fbo_returns_good():
    return {
        "box_size": "125*125*99",
        "redemption_percentage": "1.5",
        "local_index": "1.8",
        "base_price_fbo": "123",
        "volume_factor_fbo": "123",
        "fix_large_fbo": "123",
    }


@pytest.fixture(
    params=[
        {"box_size": "111*1011*10"},
        {"local_index": "0"},
        {"local_index": "0.11"},
        {"local_index": "10.1"},
        {"redemption_percentage": "-1"},
        {"redemption_percentage": "0"},
        {"redemption_percentage": "1.11"},
        {"redemption_percentage": "100.1"},
        {"base_price_fbo": "0"},
        {"base_price_fbo": "100001.1"},
        {"base_price_fbo": "3456.12"},
        {"some_new_attr": "1"},
    ],
)
def ozon_fbo_returns_bad(request, ozon_fbo_returns_good):
    bad_data = ozon_fbo_returns_good.copy()
    bad_data.update(request.param)
    return bad_data
