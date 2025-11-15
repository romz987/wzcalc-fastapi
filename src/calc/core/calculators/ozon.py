import math
from decimal import Decimal

# calculators
from src.calc.core.calculators.common import comissions_fee_clc, round_decimal

# dataclasses
from src.calc.core.domain import oz_calcdata, cm_calcdata


#############################################################################
#                             Ozon Calculators                              #
#############################################################################
#############################################################################
#                                Logistics                                  #
#############################################################################


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
    ZERO = Decimal("0")
    MAX_LIMIT = Decimal("190")
    MIN_LIMIT = Decimal("0.4")
    AVG_LIMIT = Decimal("1")
    # Check ZERO
    if log_params.box_volume == ZERO:
        return ZERO
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
    ZERO = Decimal("0")
    MAX_LIMIT = Decimal("190")
    AVG_LIMIT = Decimal("1")
    # Check ZERO
    if log_params.box_volume == ZERO:
        return ZERO
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


#############################################################################
#                             Ozon Calculators                              #
#############################################################################
#############################################################################
#                                  Returns                                  #
#############################################################################


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
    # Calculate
    result = (
        (100 - returns_params.redemption_percentage)
        / returns_params.redemption_percentage
    ) * (
        logistics_fee
        + reverse_logistics_fee
        + returns_params.nonredemption_processing_cost
    )
    # Round and return result
    return round_decimal(result)


#############################################################################
#                             Ozon Calculators                              #
#############################################################################
#############################################################################
#                                  Profit                                   #
#############################################################################


def oz_profit_ts_simple_clc(
    profit_params: oz_calcdata.OzProfitParams,
    base_fees: oz_calcdata.OzBaseFees,
    log_fees: oz_calcdata.OzLogFees,
) -> tuple[Decimal, Decimal, Decimal]:
    """Calculate profit under the 'simple' tax system for Ozon.

    Calculates tax and risk fees, aggregates all cost components
    (logistics, returns, commissions, operational costs), and
    derives the final profit value.

    :param profit_params: An instance of OzProfitParams dataclass
    :param base_fees: An instance of OzBaseFees dataclass
    :param log_fees: An instance of OzLogFees dataclass
    :return: tuple(tax_fee, risk_fee, profit)
    """
    # Calculate tax fee and risk fee
    tax_fee = comissions_fee_clc(
        profit_params.tax_percent,
        profit_params.total_price,
    )
    risk_fee = comissions_fee_clc(
        profit_params.risk_percent,
        profit_params.total_price,
    )
    # Calculate all costs
    all_costs = (
        base_fees.last_mile_fee
        + base_fees.comission_fee
        + base_fees.aquiring_fee
        + tax_fee
        + risk_fee
        + base_fees.cost_row
        + profit_params.shipment_processing
        + profit_params.box_cost
        + profit_params.wage_cost
        + log_fees.logistics_fee
        + log_fees.returns_fee
    )
    # Calculate profit value
    total_profit = profit_params.total_price - all_costs
    return tax_fee, risk_fee, total_profit


def oz_profit_ts_diff_clc(
    profit_params: oz_calcdata.OzProfitParams,
    base_fees: oz_calcdata.OzBaseFees,
    log_fees: oz_calcdata.OzLogFees,
) -> tuple[Decimal, Decimal, Decimal]:
    """Calculate profit under the 'difference' tax system for Ozon.

    Calculates tax and risk fees based on net profit (price minus costs),
    aggregates all operational, commission, and logistics costs,
    and derives the final profit value.

    :param profit_params: An instance of OzProfitParams dataclass
    :param base_fees: An instance of OzBaseFees dataclass
    :param log_fees: An instance of OzLogFees dataclass
    :return: tuple(tax_fee, risk_fee, profit)
    """
    # Calculate all costs without risk fee and tax fee
    all_costs = (
        base_fees.last_mile_fee
        + base_fees.comission_fee
        + base_fees.aquiring_fee
        + base_fees.cost_row
        + profit_params.shipment_processing
        + profit_params.box_cost
        + profit_params.wage_cost
        + log_fees.logistics_fee
        + log_fees.returns_fee
    )
    # Calculate tax fee
    pc_diff = profit_params.total_price - all_costs
    tax_fee = comissions_fee_clc(profit_params.tax_percent, pc_diff)
    # Calculate risk fee
    risk_fee = comissions_fee_clc(
        profit_params.risk_percent,
        profit_params.total_price,
    )
    # Calculate profit value
    total_profit = profit_params.total_price - (all_costs + tax_fee + risk_fee)
    return tax_fee, risk_fee, total_profit


#############################################################################
#                             Ozon Calculators                              #
#############################################################################
#############################################################################
#                               Additional                                  #
#############################################################################


def oz_last_mile_clc(
    total_price: Decimal,
    last_mile_percent: Decimal,
) -> Decimal:
    """Ozon last mile fee calculator
    based on:
      - total_price
      - last_mile_percent

    :param total_price: Total price value
    :param last_mile_percent: Last mile percent value
    :return: Last mile fee
    """
    MAX_LIMIT = 500
    LIMIT_VALUE = "500"
    last_mile_fee = total_price * (last_mile_percent / 100)
    if last_mile_fee > MAX_LIMIT:
        return Decimal(LIMIT_VALUE)
    return last_mile_fee
