from dataclasses import replace
from decimal import Decimal

# dataclasses
from src.calc.core.domain import oz_calcdata, cm_calcdata

# calculators
from src.calc.core.calculators.ozon import (
    oz_log_fbs_clc,
    oz_log_fbo_clc,
    oz_returns_clc,
)


#############################################################################
#                        Ozon Calculation Services                          #
#############################################################################

################################# Returns ###################################


def oz_calculate_returns_fbs(
    log_params: cm_calcdata.LogMainParams,
    log_costs: oz_calcdata.OzLogFbsCosts,
    return_params: cm_calcdata.ReturnsParams,
) -> tuple[Decimal, Decimal, Decimal]:
    """Ozon FBS returns fee value calculator

    :param log_params: An instance of LogMainParams dataclass
    :param log_costs: An instance of OzLogFbsCosts dataclass
    :param return_params: An instance of ReturnsParams dataclass
    :return: tuple(logistics_fee, reverse_logistics_fee, returns_fee)
    """
    # Calculate logistics fee
    logistics_fee = oz_log_fbs_clc(log_params, log_costs)
    # Calculate reverse logistics fee
    reverse_logistics_fee = oz_calculate_reverse_logistics_fee(
        log_params,
        log_costs,
    )
    # Calculate returns_fee
    returns_fee = oz_returns_clc(
        return_params,
        logistics_fee,
        reverse_logistics_fee,
    )
    return logistics_fee, reverse_logistics_fee, returns_fee


def oz_calculate_returns_fbo(
    log_params: cm_calcdata.LogMainParams,
    log_costs_fbs: oz_calcdata.OzLogFbsCosts,
    log_costs_fbo: oz_calcdata.OzLogFboCosts,
    return_params: cm_calcdata.ReturnsParams,
) -> tuple[Decimal, Decimal, Decimal]:
    """Ozon FBO returns fee value calculator

    :param log_params: An instance of LogMainParams dataclass
    :param log_costs_fbs: An instance of OzLogFbsCosts dataclass
    :param log_costs_fbo: An instance of OzLogFboCosts dataclass
    :param return_params: An instance of ReturnsParams dataclass
    :return: tuple(logistics_fee, reverse_logistics_fee, returns_fee)
    """
    # Calculate logistics fee
    logistics_fee = oz_log_fbo_clc(log_params, log_costs_fbo)
    # Calculate reverse logistics fee
    reverse_logistics_fee = oz_calculate_reverse_logistics_fee(
        log_params,
        log_costs_fbs,
    )
    # Calculate returns_fee
    returns_fee = oz_returns_clc(
        return_params,
        logistics_fee,
        reverse_logistics_fee,
    )
    return logistics_fee, reverse_logistics_fee, returns_fee


def oz_calculate_reverse_logistics_fee(
    log_params: cm_calcdata.LogMainParams,
    log_costs: oz_calcdata.OzLogFbsCosts,
) -> Decimal:
    """Ozon reverse logistics fee value calculator

    :param log_params: An instance of LogMainParams dataclass
    :param log_costs: An instance of OzLogFbsCosts dataclass
    :return: Reverse logistics fee value
    """
    reverse_log_params = replace(log_params, local_index=Decimal("1"))
    return oz_log_fbs_clc(reverse_log_params, log_costs)


################################# Profit ####################################


################################## Price ####################################
