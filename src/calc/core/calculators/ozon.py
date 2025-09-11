import math
from decimal import Decimal

# dataclasses
from src.calc.core.domain import oz_calcdata, cm_calcdata


def oz_log_fbs_clc(
    log_params: cm_calcdata.LogMainParams,
    log_costs: oz_calcdata.OzLogFbsCosts,
) -> Decimal:
    """Ozon FBS logistics fee calculator
    based on:
      - box volume
      - fbs logistics costs

    :param log_params: An instance of LogMainParams dataclass
    :param log_costs: An instance of OzLogFbsCosts dataclass
    :return: Logistics fee value
    """
    # Constants
    MAX_LIMIT = 190
    MIN_LIMIT = 0.4
    AVG_LIMIT = 1
    # Calulate max volume
    if log_params.box_volume >= MAX_LIMIT:
        return log_costs.fix_large_fbs * log_params.local_index
    # Calculate < 0.4l volume
    if log_params.box_volume <= MIN_LIMIT:
        return log_costs.minimal_price_fbs * log_params.local_index
    # Calculate 0.4-1l volume
    if log_params.box_volume <= AVG_LIMIT:
        return log_costs.base_price_fbs * log_params.local_index
    # Calculate > 1l volume
    add_volume_price = (
        math.ceil(log_params.box_volume - 1) * log_costs.volume_factor_fbs
    )
    return (
        add_volume_price + log_costs.base_price_fbs
    ) * log_params.local_index


def oz_log_fbo_clc(
    log_params: cm_calcdata.LogMainParams,
    log_costs: oz_calcdata.OzLogFboCosts,
) -> Decimal:
    """Ozon FBO logistics fee calculator
    based on:
      - box volume
      - fbo logistics costs

    :param log_params: An instance of LogMainParams dataclass
    :param log_costs: An instance of OzLogFboCosts dataclass
    :return: Logistics fee value
    """
    # Constants
    MAX_LIMIT = 190
    AVG_LIMIT = 1
    # Calulate max volume
    if log_params.box_volume >= MAX_LIMIT:
        return log_costs.fix_large_fbo * log_params.local_index
    # Calculate =< 1l volume
    if log_params.box_volume <= AVG_LIMIT:
        return log_costs.base_price_fbo * log_params.local_index
    # Calculate > 1l volume
    add_volume_price = (
        math.ceil(log_params.box_volume - 1) * log_costs.volume_factor_fbo
    )
    return (
        add_volume_price + log_costs.base_price_fbo
    ) * log_params.local_index


def oz_returns_clc(
    returns_params: cm_calcdata.ReturnsParams,
    logistics_fee: Decimal,
    reverse_logistics_fee: Decimal,
) -> Decimal:
    """Ozon returns fee calculator
    based on:
      - redemption percentage
      - nonredemption processing cost
      - logistics fee value
      - reverse logistics fee value

    :param returns_params: An instance of ReturnsParams dataclass
    :logistics_fee: Calculated logistics fee value
    :reverse_logistics_fee: Calculated reverse logistics fee value
    :return: Returns fee value
    """
    # Calculate all nonredemptions processing cost
    processing_cost_total = (
        100 - returns_params.redemption_percentage
    ) * returns_params.nonredemption_processing_cost
    # Calculate total returns cost
    return (
        (
            (100 * logistics_fee)
            + (
                (100 - returns_params.redemption_percentage)
                * reverse_logistics_fee
            )
            + processing_cost_total
        )
        / returns_params.redemption_percentage
    ) - logistics_fee
