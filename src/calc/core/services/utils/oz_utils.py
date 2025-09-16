# dataclasses
from src.calc.core.domain import oz_calcdata

# calculators
from src.calc.core.calculators.common import comissions_fee_clc
from src.calc.core.calculators.ozon import (
    oz_last_mile_clc,
)


#############################################################################
#                            Ozon Services Utils                            #
#############################################################################
#############################################################################
#                                  Profit                                   #
#############################################################################


def oz_calculate_base_fees(
    args: oz_calcdata.OzProfitArgs,
) -> oz_calcdata.OzBaseFees:
    """Calculate base cost components for Ozon profit calculation.

    Derives the fundamental expense elements such as product cost,
    last-mile delivery fee, commission fee, and acquiring fee.
    These values are later used as inputs for full profit calculations.

    :param args: An instance of OzProfitArgs dataclass
    :return: An instance of OzBaseFees dataclass
    """
    # Unpack required data
    data = args.profit_params
    # Calculate cost row
    cost_row = data.count * data.cost_per_one
    # Calculate last mile fee
    last_mile_fee = oz_last_mile_clc(data.total_price, data.last_mile_percent)
    # Calculate marketplace comission fee
    comission_fee = comissions_fee_clc(
        data.comissions_percent,
        data.total_price,
    )
    # Calculate aquiring fee
    aquiring_fee = comissions_fee_clc(data.aquiring_percent, data.total_price)
    # Create and return dataclass
    return oz_calcdata.OzBaseFees(
        cost_row=cost_row,
        last_mile_fee=last_mile_fee,
        comission_fee=comission_fee,
        aquiring_fee=aquiring_fee,
    )
