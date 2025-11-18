# dataclasses
from src.calc.core.domain import wb_calcdata

# calculators
from src.calc.core.calculators.common import comissions_fee_clc


#############################################################################
#                       Wildberries Services Utils                          #
#############################################################################
#############################################################################
#                                  Profit                                   #
#############################################################################


def wb_calculate_base_fees(
    args: wb_calcdata.WbProfitArgs,
) -> wb_calcdata.WbBaseFees:
    """Calculate base cost components for Wildberries profit calculation.

    Derives the fundamental expense elements such as product cost,
    last-mile delivery fee, commission fee, and acquiring fee.
    These values are later used as inputs for full profit calculations.

    :param args: An instance of WbProfitArgs dataclass
    :return: An instance of WbBaseFees dataclass
    """
    # Unpack required data
    data = args.profit_params
    # Calculate cost row
    cost_row = data.count * data.cost_per_one
    # Calculate marketplace comission fee
    comission_fee = comissions_fee_clc(
        data.comissions_percent,
        data.total_price,
    )
    # Calculate aquiring fee
    aquiring_fee = comissions_fee_clc(data.aquiring_percent, data.total_price)
    # Create and return dataclass
    return wb_calcdata.WbBaseFees(
        cost_row=cost_row,
        comission_fee=comission_fee,
        aquiring_fee=aquiring_fee,
    )
