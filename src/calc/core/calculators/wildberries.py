from decimal import Decimal

# calculators
from src.calc.core.calculators.common import round_decimal, comissions_fee_clc

# dataclasses
from src.calc.core.domain import wb_calcdata, cm_calcdata


#############################################################################
#                        Wildberries Calculators                            #
#############################################################################
#############################################################################
#                                Logistics                                  #
#############################################################################


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
    ZERO = Decimal("0")
    MIN_LIMIT_1 = Decimal("0.2")
    MIN_LIMIT_2 = Decimal("0.4")
    MIN_LIMIT_3 = Decimal("0.6")
    MIN_LIMIT_4 = Decimal("0.8")
    AVG_LIMIT = Decimal("1")
    # Zero
    if log_params.box_volume == ZERO:
        return ZERO
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


#############################################################################
#                        Wildberries Calculators                            #
#############################################################################
#############################################################################
#                                 Returns                                   #
#############################################################################


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
    result = (
        (returns_params.nonredemption_processing_cost + logistics_fee)
        * (100 - returns_params.redemption_percentage)
    ) / returns_params.redemption_percentage
    return round_decimal(result)


#############################################################################
#                         Wildberries Calculators                           #
#############################################################################
#############################################################################
#                                  Profit                                   #
#############################################################################


def wb_profit_ts_simple_clc(
    profit_params: wb_calcdata.WbProfitParams,
    base_fees: wb_calcdata.WbBaseFees,
    log_fees: wb_calcdata.WbLogFees,
) -> tuple[Decimal, Decimal, Decimal]:
    """Calculate profit under the 'simple' tax system for Wildberries.

    Calculates tax and risk fees, aggregates all cost components
    (logistics, returns, commissions, operational costs), and
    derives the final profit value.

    :param profit_params: An instance of WbProfitParams dataclass
    :param base_fees: An instance of WbBaseFees dataclass
    :param log_fees: An instance of WbLogFees dataclass
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
        base_fees.comission_fee
        + base_fees.aquiring_fee
        + tax_fee
        + risk_fee
        + base_fees.cost_row
        + profit_params.box_cost
        + profit_params.wage_cost
        + log_fees.logistics_fee
        + log_fees.returns_fee
    )
    # Calculate profit value
    total_profit = profit_params.total_price - all_costs
    return tax_fee, risk_fee, total_profit


def wb_profit_ts_diff_clc(
    profit_params: wb_calcdata.WbProfitParams,
    base_fees: wb_calcdata.WbBaseFees,
    log_fees: wb_calcdata.WbLogFees,
) -> tuple[Decimal, Decimal, Decimal]:
    """Calculate profit under the 'difference' tax system for Wildberries.

    Calculates tax and risk fees based on net profit (price minus costs),
    aggregates all operational, commission, and logistics costs,
    and derives the final profit value.

    :param profit_params: An instance of WbProfitParams dataclass
    :param base_fees: An instance of WbBaseFees dataclass
    :param log_fees: An instance of WbLogFees dataclass
    :return: tuple(tax_fee, risk_fee, profit)
    """
    # Calculate all costs without risk fee and tax fee
    all_costs = (
        base_fees.comission_fee
        + base_fees.aquiring_fee
        + base_fees.cost_row
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
