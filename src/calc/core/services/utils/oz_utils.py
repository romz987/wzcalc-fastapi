from decimal import Decimal

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


################################# Profits ###################################


def oz_calculate_profit_base(
    args: oz_calcdata.OzProfitFbsArgs | oz_calcdata.OzProfitFboArgs,
) -> oz_calcdata.OzProfitFees:
    """Calculate base fee components used in Ozon profit calculation

    :param args: An instance of core dataclass
    :return: An instance of OzProfitFees dataclass
    """
    # Data
    data = args.profit_params
    # Cost row
    cost_row = data.count * data.cost_per_one
    # Last mile fee
    last_mile_fee = oz_last_mile_clc(data.total_price, data.last_mile_percent)
    # Comission fee
    comission_fee = comissions_fee_clc(
        data.comissions_percent,
        data.total_price,
    )
    # Aquiring fee
    aquiring_fee = comissions_fee_clc(data.aquiring_percent, data.total_price)
    # Create and return dataclass
    return oz_calcdata.OzProfitFees(
        cost_row=cost_row,
        last_mile_fee=last_mile_fee,
        comission_fee=comission_fee,
        aquiring_fee=aquiring_fee,
    )


def oz_fill_log_base(
    logistics_fee: Decimal,
    returns_fee: Decimal,
) -> oz_calcdata.OzLogFees:
    """Fill up intercommunicate dataclass

    :param logistics_fee: Logistics fee value
    :param returns_fee: Return fee value
    :return: An instance of OzLogBase
    """
    return oz_calcdata.OzLogFees(
        logistics_fee=logistics_fee,
        returns_fee=returns_fee,
    )
