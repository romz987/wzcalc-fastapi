from decimal import Decimal

# dataclasses
from src.calc.core.domain import wb_calcdata, cm_calcdata

# calculators
from src.calc.core.calculators.wildberries import wb_log_clc, wb_returns_clc

#############################################################################
#                        Ozon Calculation Services                          #
#############################################################################

################################# Returns ###################################


def wb_calculate_returns(
    log_params: cm_calcdata.LogMainParams,
    log_costs: wb_calcdata.WbLogCosts,
    return_params: cm_calcdata.ReturnsParams,
) -> tuple[Decimal, Decimal]:
    """Wildberries returns fee value calculator

    :param log_params: An instance of LogMainParams dataclass
    :param log_costs: An instance of WbLogCosts dataclass
    :param return_params: An instance of ReturnsParams dataclass
    :return: tuple(logistics_fee, returns_fee)
    """
    # Calculate logistics fee
    logistics_fee = wb_log_clc(log_params, log_costs)
    # Calculate returns fee
    returns_fee = wb_returns_clc(return_params, logistics_fee)
    return logistics_fee, returns_fee


################################# Profit ####################################


def wb_calculate_profit():
    """Wildberries profit value calculator

    :param :
    :param :
    :param :
    :return: tuple()
    """
    pass


################################# Price #####################################


def wb_calculate_price():
    """Wildberries price value calculator

    :param :
    :param :
    :param :
    :return: tuple()
    """
    pass
