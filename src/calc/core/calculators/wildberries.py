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
      - fbo logistics costs

    :param log_params: An instance of LogMainParams dataclass
    :param log_costs: An instance of WbLogCosts dataclass
    :return: Logistics fee value
    """
    # Constants
    MIN_LIMIT_1 = Decimal("0.2")
    MIN_LIMIT_2 = Decimal("0.4")
    MIN_LIMIT_3 = Decimal("0.6")
    MIN_LIMIT_4 = Decimal("0.8")
    AVG_LIMIT = Decimal("1")
    # Calculate 0.001-0.2l
    if log_params.box_volume <= MIN_LIMIT_1:
        return log_costs.min_lim_1_price * log_params.local_index
    # Calculate 0.2-0.4l
    if log_params.box_volume <= MIN_LIMIT_2:
        return log_costs.min_lim_2_price * log_params.local_index
    # Calculate 0.4-0.6l
    if log_params.box_volume <= MIN_LIMIT_3:
        return log_costs.min_lim_3_price * log_params.local_index
    # Calculate 0.6-0.8l
    if log_params.box_volume <= MIN_LIMIT_4:
        return log_costs.min_lim_4_price * log_params.local_index
    # Calculate 0.8-1l
    if log_params.box_volume <= AVG_LIMIT:
        return log_costs.min_lim_5_price * log_params.local_index
    # Calculate > 1l
    additional_volume_price = (
        log_params.box_volume - 1
    ) * log_costs.volume_factor
    return (
        additional_volume_price + log_costs.base_price
    ) * log_params.local_index


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
    :param logistics_fee: Calculated logistics fee value
    :return: Returns fee value
    """
    # Calculate returns fee value with logistics_fee
    return (
        (returns_params.nonredemption_processing_cost + logistics_fee)
        * (100 - returns_params.redemption_percentage)
    ) / returns_params.redemption_percentage
