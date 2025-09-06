import math
from decimal import Decimal
from src.calc.service.calculators.oz import calcdata_oz

##########################################################
#                 Logistics and Returns                  #
##########################################################


def calc_log_fbs_oz(
    args: (
        calcdata_oz.LogFbsData
        | calcdata_oz.ReturnsFbsData
        | calcdata_oz.ReturnsFboData
    ),
) -> Decimal:
    """Ozon FBS logistics fee calculator
    based on box volume.

    :param args: An instance of LogFbsData
    :return: Logistics fee
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


def calc_log_fbo_oz(
    args: calcdata_oz.LogFboData | calcdata_oz.ReturnsFboData,
) -> Decimal:
    """Ozon FBO logistics fee calculator
    based on box volume.

    :param args: An instance of LogFboData
    :return: Logistics fee
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


def calc_returns_oz(
    args: calcdata_oz.ReturnsFbsData | calcdata_oz.ReturnsFboData,
) -> Decimal:
    """Ozon returns fee calculator based on:
    - redemption_percentage
    - nonredemption_processing_cost
    - logistics_fee
    - reverse_logistics_fee

    :param args: An instance of ReturnsData
    :return: Returns fee
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
