from dataclasses import replace
from decimal import Decimal
from src.calc.core.domain import oz_calcdata
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
    item_params: oz_calcdata.OzLogItemParams,
    log_costs: oz_calcdata.OzLogFbsCosts,
    return_params: oz_calcdata.OzReturnsParams,
) -> tuple[Decimal, Decimal, Decimal]:
    """Ozon FBS returns fee value calculator

    :param item_params: An instance of OzLogItemParams dataclass
    :param log_costs: An instance of OzLogFbsCosts dataclass
    :param return_params: An instance of OzReturnsParams dataclass
    :return: tuple(logistics_fee, reverse_logistics_fee, returns_fee)
    """
    # Calculate logistics fee
    logistics_fee = oz_log_fbs_clc(item_params, log_costs)
    # Calculate reverse logistics fee
    reverse_logistics_fee = oz_calculate_reverse_logistics_fee(
        item_params,
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
    item_params: oz_calcdata.OzLogItemParams,
    log_costs_fbs: oz_calcdata.OzLogFbsCosts,
    log_costs_fbo: oz_calcdata.OzLogFboCosts,
    return_params: oz_calcdata.OzReturnsParams,
) -> tuple[Decimal, Decimal, Decimal]:
    """Ozon FBO returns fee value calculator

    :param item_params: An instance of OzLogItemParams dataclass
    :param log_costs_fbs: An instance of OzLogFbsCosts dataclass
    :param log_costs_fbo: An instance of OzLogFboCosts dataclass
    :param return_params: An instance of OzReturnsParams dataclass
    :return: tuple(logistics_fee, reverse_logistics_fee, returns_fee)
    """
    # Calculate logistics fee
    logistics_fee = oz_log_fbo_clc(item_params, log_costs_fbo)
    # Calculate reverse logistics fee
    reverse_logistics_fee = oz_calculate_reverse_logistics_fee(
        item_params,
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
    item_params: oz_calcdata.OzLogItemParams,
    log_costs: oz_calcdata.OzLogFbsCosts,
) -> Decimal:
    """Ozon reverse logistics fee value calculator

    :param item_params: An instance of OzLogItemParams dataclass
    :param log_costs: An instance of OzLogFbsCosts
    :return: Reverse logistics fee value
    """
    reverse_log_item_params = replace(item_params, local_index=Decimal("1"))
    return oz_log_fbs_clc(reverse_log_item_params, log_costs)


################################# Profit ####################################


################################## Price ####################################
