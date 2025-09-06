import pytest

##########################################################
#                    Единичный расчет                    #
##########################################################


@pytest.fixture
def wb_calc_good():
    return {
        "tax_system": "simple",
        "fbs_fbo_option": "fbs",
        "comission_percent": "20",
        "acquiring_percent": "2",
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
        "base_price": "45",
        "volume_factor": "25",
        "reverse_logistics_price": "1234",
    }


@pytest.fixture(
    params=[
        {"fbs_fbo_option": "fbz"},
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
def wb_calc_bad(request, wb_calc_good):
    bad_data = wb_calc_good.copy()
    bad_data.update(request.param)
    return bad_data


##########################################################
#                      BULK расчет                       #
##########################################################


@pytest.fixture
def wb_bulk_calc_good():
    return [
        {
            "tax_system": "simple",
            "fbs_fbo_option": "fbs",
            "comission_percent": "20",
            "acquiring_percent": "2",
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
            "base_price": "45",
            "volume_factor": "25",
            "reverse_logistics_price": "1234",
        },
        {
            "tax_system": "simple",
            "fbs_fbo_option": "fbs",
            "comission_percent": "20",
            "acquiring_percent": "2",
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
            "base_price": "45",
            "volume_factor": "25",
            "reverse_logistics_price": "1234",
        },
    ]


@pytest.fixture(
    params=[
        {"fbs_fbo_option": "fbz"},
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
def wb_bulk_calc_bad(request, wb_bulk_calc_good):
    bad_data = wb_bulk_calc_good.copy()
    bad_data[0].update(request.param)
    return bad_data


##########################################################
#               Расчет стоимости логистики               #
##########################################################


@pytest.fixture
def wb_log_good():
    return {
        "fbs_fbo_option": "fbs",
        "box_size": "125*125*99",
        "local_index": "1",
        "base_price": "45",
        "volume_factor": "123",
    }


@pytest.fixture(
    params=[
        {"box_size": "111*1011*10"},
        {"local_index": "0"},
        {"local_index": "0.11"},
        {"local_index": "10.1"},
        {"base_price": "0"},
        {"base_price": "100001.1"},
        {"base_price": "3456.12"},
        {"some_new_attr": "1"},
        {"fbs_fbo_option": "fbz"},
        {
            "fbs_fbo_option": "fbs",
            "local_index": "1.2",
        },
    ],
)
def wb_log_bad(request, wb_log_good):
    bad_data = wb_log_good.copy()
    bad_data.update(request.param)
    return bad_data


##########################################################
#               Расчет стоимости возвратов               #
##########################################################


@pytest.fixture
def wb_returns_good():
    return {
        "fbs_fbo_option": "fbs",
        "box_size": "125*125*99",
        "redemption_percentage": "92",
        "local_index": "1.8",
    }


@pytest.fixture(
    params=[
        {"fbs_fbo_option": "fbz"},
        {"box_size": "111*1011*10"},
        {"local_index": "0"},
        {"local_index": "0.11"},
        {"local_index": "10.1"},
        {"base_price": "0"},
        {"base_price": "100001.1"},
        {"base_price": "3456.12"},
        {"some_new_attr": "1"},
    ],
)
def wb_returns_bad(request, wb_returns_good):
    bad_data = wb_returns_good.copy()
    bad_data.update(request.param)
    return bad_data
