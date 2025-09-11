import math
from decimal import Decimal

# dataclasses
from src.calc.core.domain import wb_calcdata, cm_calcdata


def wb_log_clc(
    log_params: cm_calcdata.LogMainParams,
    log_costs: wb_calcdata.WbLogCosts,
) -> Decimal:
    """Wildberries logistics fee value calculator
    based on:
      - box volume
      - fbo logistics logistics costs

    :param log_params: An instance of LogMainParams dataclass
    :param log_costs: An instance of WbLogCosts dataclass
    :return: Logistics fee value
    """
    # Constants
    AVG_LIMIT = 1
    # Calculate < 1l volume
    if log_params.box_volume <= AVG_LIMIT:
        return log_costs.base_price * log_params.local_index
    # Calculate > 1l volume
    add_volume_price = (
        math.ceil(log_params.box_volume - 1) * log_costs.volume_factor
    )
    return (add_volume_price + log_costs.base_price) * log_params.local_index


def wb_returns_clc(
    returns_params: cm_calcdata.ReturnsParams,
    logistics_fee: Decimal,
) -> Decimal:
    """Wildberries returns fee value calculator
    based on:
      - redemption percentage
      - nonredemption processing cost
      - logistics fee

    :param returns_params: An instance of ReturnsParams dataclass
    :return: Returns fee value
    """
    # Calculate returns fee value with logistics_fee
    returns_with_logistics = (
        100 * logistics_fee
        + (
            (100 - returns_params.redemption_percentage)
            * returns_params.nonredemption_processing_cost
        )
    ) / returns_params.redemption_percentage
    # Return clean returns fee
    return returns_with_logistics - logistics_fee
