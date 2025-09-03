import math
from decimal import Decimal
from . import calcdata

##########################################################
#                 Logistics and Returns                  #
##########################################################


def get_box_volume(box_size: str) -> Decimal:
    """Calculate the box volume in liters from its dimensions.

    :param box_size: Dimensions of the box in cm, e.g. 15*10*10
    :return: The volume of the box in liters
    """
    factors = map(Decimal, box_size.split("*"))
    return math.prod(list(factors)) / 1000  # pyright: ignore


def calc_log_fbs(
    args: (
        calcdata.LogFbsData | calcdata.ReturnsFbsData | calcdata.ReturnsFboData
    ),
) -> Decimal:
    """Calculate FBS logistics cost based on box volume

    :param args: An instance of LogFbsData
    :return: Logistics cost
    """
    # only for pyright alerts
    if args.box_volume is None:
        raise ValueError
    # calculate logistics fee
    if args.box_volume >= 190:
        result = args.fix_large_fbs * args.local_index
    elif args.box_volume <= 0.4:
        result = args.minimal_price_fbs * args.local_index
    elif args.box_volume <= 1:
        result = args.base_price_fbs * args.local_index
    elif args.box_volume > 1:
        additional_volume_price = (
            math.ceil(args.box_volume - 1) * args.volume_factor_fbs
        )
        result = (
            additional_volume_price + args.base_price_fbs
        ) * args.local_index

    return result  # pyright: ignore


def calc_log_fbo(
    args: calcdata.LogFboData | calcdata.ReturnsFboData,
) -> Decimal:
    """Calculate FBO logistics cost based on box volume

    :param args: An instance of LogFboData
    :return: Logistics cost
    """
    # only for pyright alerts
    if args.box_volume is None:
        raise ValueError
    # calculate logistics fee
    if args.box_volume >= 190:
        result = args.fix_large_fbo * args.local_index
    elif args.box_volume <= 1:
        result = args.base_price_fbo * args.local_index
    else:
        additional_volume_price = (
            math.ceil(args.box_volume - 1) * args.volume_factor_fbo
        )
        result = (
            additional_volume_price + args.base_price_fbo
        ) * args.local_index

    return result


def calc_returns(
    args: calcdata.ReturnsFbsData | calcdata.ReturnsFboData,
) -> Decimal:
    """Calculate returns cost from:
    - redemption_percentage
    - nonredemption_processing_cost
    - logistics_fee
    - reverse_logistics_fee

    :param args: An instance of ReturnsData
    :return: Returns cost
    """
    # only for pyright alerts
    if args.logistics_fee is None or args.reverse_logistics_fee is None:
        raise ValueError
    # calculate all nonredemptions processing cost
    processing_cost_total = (
        100 - args.redemption_percentage
    ) * args.nonredemption_processing_cost
    # calculate total returns cost
    return (
        (
            (100 * args.logistics_fee)
            + ((100 - args.redemption_percentage) * args.reverse_logistics_fee)
            + processing_cost_total
        )
        / args.redemption_percentage
    ) - args.logistics_fee
