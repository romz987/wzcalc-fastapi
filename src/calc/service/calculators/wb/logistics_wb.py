import math
from decimal import Decimal
from src.calc.service.calculators.wb import calcdata_wb

##########################################################
#                 Logistics and Returns                  #
##########################################################


def calc_log_wb(
    args: calcdata_wb.LogWbData | calcdata_wb.ReturnsWbData,
) -> Decimal:
    """Wildberries FBS/FBO logistics fee calculator
    based on box volume.

    :param args: An instance of LogFbsWbData
    :return: Logistics fee
    """
    # only for pyright alerts
    if args.box_volume is None:
        raise ValueError
    # calculate logistics fee
    if args.box_volume <= 1:
        logistics_fee = args.base_price * args.local_index
    elif args.box_volume > 1:
        additional_volume_price = (
            math.ceil(args.box_volume - 1) * args.volume_factor
        )
        logistics_fee = (
            additional_volume_price + args.base_price
        ) * args.local_index
    return logistics_fee  # pyright: ignore


def calc_returns_wb(args: calcdata_wb.ReturnsWbData) -> Decimal:
    """Ozon returns fee calculator based on:
    - redemption_percentage
    - nonredemption_processing_cost
    - logistics_fee

    :param args: An instance of ReturnsData
    :return: Returns fee
    """
    # only for pyright alerts
    if args.logistics_fee is None:
        raise ValueError
    # calculate all nonredemptions processing cost
    nonredemptions_value = (
        100 * args.logistics_fee
        + (
            (100 - args.redemption_percentage)
            * args.nonredemption_processing_cost
        )
    ) / args.redemption_percentage

    return nonredemptions_value - args.logistics_fee
