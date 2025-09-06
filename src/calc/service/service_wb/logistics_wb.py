from fastapi import HTTPException
from decimal import ROUND_UP, Decimal
from src.calc.service.calculators.common import get_box_volume
from src.calc.service.calculators.wb.logistics_wb import calc_log_wb
from src.calc import schemas
from src.calc.service.calculators.wb import calcdata_wb


def calculate_logistics_wb(payload: schemas.WbLogPayload):
    """Calculate logistics fee for Wildberries.
    Depends on check_local_index()

    :param payload: JSON from request
    :return: LogFbsData dataclass
    """
    # check fbs local_index is correct
    check_local_index(payload)
    # create args instance
    args = calcdata_wb.LogWbData(
        box_size=payload.box_size,
        local_index=payload.local_index,
        base_price=payload.base_price,
        volume_factor=payload.volume_factor,
    )
    # calculate box volume
    box_volume = get_box_volume(args.box_size)
    args.box_volume = box_volume.quantize(Decimal("0.0"), rounding=ROUND_UP)
    # calculate logistics fee
    logistics_fee = calc_log_wb(args)
    args.logistics_fee = logistics_fee.quantize(
        Decimal("0"),
        rounding=ROUND_UP,
    )
    return args


def calculate_returns_wb(payload):
    """Calculate returns fee for Wildberries

    :param payload: JSON from request
    :return: ReturnsData dataclass
    """
    # create args instance
    # calculate logistics fee
    # calculate reverse logistics fee
    # calculate returns
    return {"answer": "it works!"}


def check_local_index(payload: schemas.WbLogPayload) -> HTTPException | None:
    """Check local_index value in accordance with FBS/FBO option

    :param payload: JSON from request
    :return: Error message or None
    """
    if payload.fbs_fbo_option == "fbs" and payload.local_index != 1:
        raise HTTPException(
            status_code=422,
            detail="local_index must be == 1 for FBS logistics option",
        )
