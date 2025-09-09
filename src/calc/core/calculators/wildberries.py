import math
from decimal import Decimal
from src.calc.core.domain import oz_calcdata


def wb_log_clc(
    item_params: oz_calcdata.OzLogItemParams,
    log_costs,
) -> Decimal:
    """Wildberries FBS logistics fee value calculator
    based on:
      - box volume
      - fbo logistics logistics costs

    :param item_params: An instance of  dataclass
    :param log_costs: An instance of  dataclass
    :return: Logistics fee value
    """
    # Constants
    AVG_LIMIT = 1
    # Calculate < 1l volume
    if item_params.box_volume <= AVG_LIMIT:
        return log_costs.base_price * item_params.local_index
    # Calculate > 1l volume
    add_volume_price = (
        math.ceil(item_params.box_volume - 1) * log_costs.volume_factor
    )
    return (add_volume_price + log_costs.base_price) * item_params.local_index


def wb_returns_clc(
    returns_params,
    logistics_fee: Decimal,
) -> Decimal:
    """Wildberries returns fee value calculator
    based on:
      - redemption percentage
      - nonredemption processing cost
      - logistics fee

    :param returns_params: An instance of  dataclass
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
