from decimal import Decimal, ROUND_UP
from . import schemas
from .tooling import calcdata
from .tooling.calculators_oz import (
    get_box_volume,
    calc_log_fbs,
    calc_log_fbo,
    calc_returns,
)


def calculate_logistics_fbs_oz(
    payload: schemas.OzonLogFbsPayload,
) -> calcdata.LogFbsData:
    """Calculate FBS logistics cost for Ozon

    :param payload: JSON from request
    :return: LogFbsData dataclass
    """
    # create args instance
    args = calcdata.LogFbsData(
        local_index=payload.local_index,
        box_size=payload.box_size,
        minimal_price_fbs=payload.minimal_price_fbs,
        base_price_fbs=payload.base_price_fbs,
        volume_factor_fbs=payload.volume_factor_fbs,
        fix_large_fbs=payload.fix_large_fbs,
    )
    # calculate box volume
    box_volume = get_box_volume(args.box_size)  # pyright: ignore
    args.box_volume = box_volume.quantize(Decimal("0.0"), rounding=ROUND_UP)
    # calculate fbs logistics fee
    logistics_fee = calc_log_fbs(args)
    args.logistics_fee = logistics_fee.quantize(
        Decimal("0"),
        rounding=ROUND_UP,
    )
    return args


def calculate_logistics_fbo_oz(
    payload: schemas.OzonLogFboPayload,
) -> calcdata.LogFboData:
    """Calculate FBO logistics cost for Ozon

    :param payload: JSON from request
    :return: LogFboData dataclass
    """
    # create args instance
    args = calcdata.LogFboData(
        local_index=payload.local_index,
        box_size=payload.box_size,
        base_price_fbo=payload.base_price_fbo,
        volume_factor_fbo=payload.volume_factor_fbo,
        fix_large_fbo=payload.fix_large_fbo,
    )
    # calculate box volume
    box_volume = get_box_volume(args.box_size)  # pyright: ignore
    args.box_volume = box_volume.quantize(Decimal("0.0"), rounding=ROUND_UP)
    # calculate fbs logistics fee
    logistics_fee = calc_log_fbo(args)
    args.logistics_fee = logistics_fee.quantize(
        Decimal("0"),
        rounding=ROUND_UP,
    )
    return args


def calculate_returns_fbs_oz(
    payload: schemas.OzonReturnsFbsPayload,
) -> calcdata.ReturnsFbsData:
    """Calculate FBS returns cost for Ozon

    :param payload: JSON from request
    :return: ReturnsData dataclass
    """
    # create args instance
    args = calcdata.ReturnsFbsData(
        box_size=payload.box_size,
        redemption_percentage=payload.redemption_percentage,
        nonredemption_processing_cost=payload.nonredemption_processing_cost,
        local_index=payload.local_index,
        minimal_price_fbs=payload.minimal_price_fbs,
        base_price_fbs=payload.base_price_fbs,
        volume_factor_fbs=payload.volume_factor_fbs,
        fix_large_fbs=payload.fix_large_fbs,
    )
    # calculate box volume
    box_volume = get_box_volume(args.box_size)  # pyright: ignore
    args.box_volume = box_volume.quantize(Decimal("0.0"), rounding=ROUND_UP)
    # calculate logistics fee
    args.logistics_fee = calc_log_fbs(args)
    # calculate reverse logistics fee
    current_local_index, args.local_index = (  # pyright: ignore
        args.local_index,
        1,
    )
    args.reverse_logistics_fee = calc_log_fbs(args)
    args.local_index = current_local_index
    # calculate returns
    returns_fee = calc_returns(args)
    args.returns_fee = returns_fee.quantize(Decimal("0.0"), rounding=ROUND_UP)
    return args


def calculate_returns_fbo_oz(
    payload: schemas.OzonReturnsFboPayload,
) -> calcdata.ReturnsFboData:
    """Calculate FBO returns cost for Ozon

    :param payload: JSON from request
    :return: ReturnsData dataclass
    """
    # create args instance
    args = calcdata.ReturnsFboData(
        box_size=payload.box_size,
        redemption_percentage=payload.redemption_percentage,
        nonredemption_processing_cost=payload.nonredemption_processing_cost,
        local_index=payload.local_index,
        minimal_price_fbs=payload.minimal_price_fbs,
        base_price_fbs=payload.base_price_fbs,
        volume_factor_fbs=payload.volume_factor_fbs,
        fix_large_fbs=payload.fix_large_fbs,
        base_price_fbo=payload.base_price_fbo,
        volume_factor_fbo=payload.volume_factor_fbo,
        fix_large_fbo=payload.fix_large_fbo,
    )
    # calculate box volume
    box_volume = get_box_volume(args.box_size)  # pyright: ignore
    args.box_volume = box_volume.quantize(Decimal("0.0"), rounding=ROUND_UP)
    # calculate logistics fee
    args.logistics_fee = calc_log_fbs(args)
    # calculate reverse logistics fee
    current_local_index, args.local_index = (  # pyright: ignore
        args.local_index,
        1,
    )
    args.reverse_logistics_fee = calc_log_fbs(args)
    args.local_index = current_local_index
    # calculate returns
    returns_fee = calc_returns(args)
    args.returns_fee = returns_fee.quantize(Decimal("0.0"), rounding=ROUND_UP)
    return args
