from decimal import Decimal, ROUND_UP
from src.calc import schemas
from src.calc.service.calculators.oz import calcdata_oz
from src.calc.service.calculators.common import get_box_volume
from src.calc.service.calculators.oz.logistics_oz import (
    calc_log_fbs_oz,
    calc_log_fbo_oz,
    calc_returns_oz,
)


def calculate_logistics_fbs_oz(
    payload: schemas.OzonLogFbsPayload,
) -> calcdata_oz.LogFbsData:
    """Calculate FBS logistics fee for Ozon

    :param payload: JSON from request
    :return: LogFbsData dataclass
    """
    # create args instance
    args = calcdata_oz.LogFbsData(
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
    logistics_fee = calc_log_fbs_oz(args)
    args.logistics_fee = logistics_fee.quantize(
        Decimal("0"),
        rounding=ROUND_UP,
    )
    return args


def calculate_logistics_fbo_oz(
    payload: schemas.OzonLogFboPayload,
) -> calcdata_oz.LogFboData:
    """Calculate FBO logistics fee for Ozon

    :param payload: JSON from request
    :return: LogFboData dataclass
    """
    # create args instance
    args = calcdata_oz.LogFboData(
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
    logistics_fee = calc_log_fbo_oz(args)
    args.logistics_fee = logistics_fee.quantize(
        Decimal("0"),
        rounding=ROUND_UP,
    )
    return args


def calculate_returns_fbs_oz(
    payload: schemas.OzonReturnsFbsPayload,
) -> calcdata_oz.ReturnsFbsData:
    """Calculate FBS returns fee for Ozon

    :param payload: JSON from request
    :return: ReturnsFbsData dataclass
    """
    # create args instance
    args = calcdata_oz.ReturnsFbsData(
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
    args.logistics_fee = calc_log_fbs_oz(args)
    # calculate reverse logistics fee
    current_local_index, args.local_index = (  # pyright: ignore
        args.local_index,
        1,
    )
    args.reverse_logistics_fee = calc_log_fbs_oz(args)
    args.local_index = current_local_index
    # calculate returns
    returns_fee = calc_returns_oz(args)
    args.returns_fee = returns_fee.quantize(Decimal("0.0"), rounding=ROUND_UP)
    return args


def calculate_returns_fbo_oz(
    payload: schemas.OzonReturnsFboPayload,
) -> calcdata_oz.ReturnsFboData:
    """Calculate FBO returns fee for Ozon

    :param payload: JSON from request
    :return: ReturnsFboData dataclass
    """
    # create args instance
    args = calcdata_oz.ReturnsFboData(
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
    args.logistics_fee = calc_log_fbo_oz(args)
    # calculate reverse logistics fee
    current_local_index, args.local_index = (  # pyright: ignore
        args.local_index,
        1,
    )
    args.reverse_logistics_fee = calc_log_fbs_oz(args)
    args.local_index = current_local_index
    # calculate returns
    returns_fee = calc_returns_oz(args)
    args.returns_fee = returns_fee.quantize(Decimal("0.0"), rounding=ROUND_UP)
    return args
