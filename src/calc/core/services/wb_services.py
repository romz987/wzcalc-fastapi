from decimal import Decimal

# dataclasses
from src.calc.core.domain import wb_calcdata, cm_calcdata

# service utils
from src.calc.core.services.utils.wb_utils import (
    wb_calculate_base_fees,
)

# calculators
from src.calc.core.calculators.wildberries import (
    wb_log_clc,
    wb_returns_clc,
    wb_profit_ts_simple_clc,
    wb_profit_ts_diff_clc,
)

#############################################################################
#                    Wildberries Calculation Services                       #
#############################################################################
#############################################################################
#                                  Returns                                  #
#############################################################################


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


#############################################################################
#                    Wildberries Calculation Services                       #
#############################################################################
#############################################################################
#                                  Profit                                   #
#############################################################################


def wb_calculate_profit(
    args: wb_calcdata.WbProfitArgs,
) -> wb_calcdata.WbProfitResult:
    """Calculate profit for Wildberries under both tax systems.

    Dispatches calculation logic based on the selected tax system
    ('simple' or 'difference'), calculates all fees (base, tax, risk),
    and derives the final profit value.

    :param args: An instance of WbProfitArgs dataclass
    :return: An instance of WbProfitResult dataclass
    """
    # Calculate cost row and base comissions
    base_fees = wb_calculate_base_fees(args)
    # Calculate profit
    match args.profit_params.tax_system:
        case "simple":
            tax_fee, risk_fee, total_profit = wb_profit_ts_simple_clc(
                args.profit_params,
                base_fees,
                args.log_fees,
            )
        case "difference":
            tax_fee, risk_fee, total_profit = wb_profit_ts_diff_clc(
                args.profit_params,
                base_fees,
                args.log_fees,
            )
        case _:
            raise ValueError("invalid tax_system value")
    # Make response
    return wb_calcdata.WbProfitResult(
        base_fees=base_fees,
        tax_fee=tax_fee,
        risk_fee=risk_fee,
        total_profit=total_profit,
    )


################################# Price #####################################


def wb_calculate_price():
    """Wildberries price value calculator

    :param :
    :param :
    :param :
    :return: tuple()
    """
    pass
