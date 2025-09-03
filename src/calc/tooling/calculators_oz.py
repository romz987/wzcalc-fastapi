# module for experiments
import math
from decimal import Decimal
from .calcdata import LogFbsData, LogFboData


def calc_returns(args) -> Decimal:
    """Calculate returns cost from:
    - redemption_percentage
    - nonredemption_processing_cost
    - logistics_fee
    - reverse_logistics_fee
    """
    # Считаем стоимость обработки невыкупов
    processing_cost_total = (
        100 - args.redemption_percentage
    ) * args.nonredemption_processing_cost
    # Считаем итоговую стоимость возвратов
    return (
        (
            (100 * args.logistics_fee)
            + ((100 - args.redemption_percentage) * args.reverse_logistics_fee)
            + processing_cost_total
        )
        / args.redemption_percentage
    ) - args.logistics_fee


def get_box_volume(box_size: str) -> Decimal:
    """Calculate the box volume in liters from its dimensions.

    :param box_size: Dimensions of the box in cm, e.g. 15*10*10
    :return: The volume of the box in liters
    """
    factors = map(Decimal, box_size.split("*"))
    return math.prod(list(factors)) / 1000  # pyright: ignore


def calc_log_fbs(args: LogFbsData) -> Decimal:
    """Calculate FBS logistics cost based on box volume

    :param args: An instance of LogFbsData
    :returns: Logistics cost
    """
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


def calc_log_fbo(args: LogFboData) -> Decimal:
    """Calculate FBO logistics cost based on box volume

    :param args: An instance of LogFbsData
    :returns: Logistics cost
    """
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

    return result  # pyright: ignore
