from src.calc import schemas
from fastapi import HTTPException

# dataclasses
from src.calc.core.domain import wb_calcdata

# calculators
from src.calc.core.calculators.common import box_volume_clc
from src.calc.core.calculators.wildberries import wb_log_clc

# services
from src.calc.core.services.wb_services import (
    wb_calculate_returns,
    wb_calculate_profit,
)

# utils
from src.calc.core.interfaces.utils import wb_utils, cm_utils


#############################################################################
#                   Wildberries Calculation Interfaces                      #
#############################################################################
#############################################################################
#                           Logistics and returns                           #
#############################################################################


def get_wb_logistics_fee(
    payload: schemas.WbLogPayload,
) -> wb_calcdata.WbLogResponse:
    """Interface
    Wildberries logistics fee value calculation service

    :param payload: An instance of the WbLogPayload pydantic model
    :return: An instance of WbLogResponse dataclass
    """
    # Check FBS local_index == 1
    check_local_index(payload)
    # Calculate box volume
    box_volume = box_volume_clc(payload.box_size)
    # Create args
    log_params = cm_utils.request_fill_log_params(payload, box_volume)
    log_costs = wb_utils.request_fill_log_costs(payload)
    # Calculate logistics fee
    logistics_fee = wb_log_clc(log_params, log_costs)
    # Fill up and return response-dataclass
    return wb_utils.response_fill_log_fee(payload, box_volume, logistics_fee)


def get_wb_returns_fee(
    payload: schemas.WbReturnsPayload,
) -> wb_calcdata.WbReturnsResponse:
    """Interface
    Wildberries returns fee value calculation service

    :param payload: An instance of the WbReturnsPayload pydantic model
    :return: An instance of WbReturnsResponse dataclass
    """
    # Check FBS local_index == 1
    check_local_index(payload)
    # Calculate box volume
    box_volume = box_volume_clc(payload.box_size)
    # Create args
    log_params = cm_utils.request_fill_log_params(payload, box_volume)
    log_costs = wb_utils.request_fill_log_costs(payload)
    return_params = cm_utils.request_fill_return_params(payload)
    # Calculate
    logistics_fee, returns_fee = wb_calculate_returns(
        log_params,
        log_costs,
        return_params,
    )
    # Fill up and return response-dataclass
    return wb_utils.response_fill_returns_fee(
        payload,
        box_volume,
        logistics_fee,
        returns_fee,
    )


#############################################################################
#                   Wildberries Calculation Interfaces                      #
#############################################################################
#############################################################################
#                                  Profit                                   #
#############################################################################


def get_wb_profit(payload: schemas.WbProfitPayload):
    """Interface
    Wildberries profit value calculation service

    :param payload: An instance of the WbProfitPayload pydantic model
    :return: An instance of  dataclass
    """
    # Check FBS local_index == 1
    check_local_index(payload)
    # Calculate box volume
    box_volume = box_volume_clc(payload.box_size)
    # Create args
    log_params = cm_utils.request_fill_log_params(payload, box_volume)
    log_costs = wb_utils.request_fill_log_costs(payload)
    return_params = cm_utils.request_fill_return_params(payload)
    # Calculate logistics fee and returns fee
    logistics_fee, returns_fee = wb_calculate_returns(
        log_params,
        log_costs,
        return_params,
    )
    log_fees = wb_utils.request_fill_log_fees(
        box_volume,
        logistics_fee,
        returns_fee,
    )
    # Create args dataclass for profit calculation
    profit_params = wb_utils.request_fill_profit_params(payload)
    args = wb_utils.request_fill_profit_args(
        log_params,
        log_fees,
        return_params,
        profit_params,
    )
    # Calculate profit value and base comissions fees
    results = wb_calculate_profit(args)
    # Make response
    return wb_utils.response_fill_profit_fee(payload, log_fees, results)


#############################################################################
#                   Wildberries Calculation Interfaces                      #
#############################################################################
#############################################################################
#                                  Price                                    #
#############################################################################


def get_wb_price(payload: schemas.WbPricePayload):
    """Interface
    Wildberries price value calculation service

    :param payload: An instance of the WbPricePayload pydantic model
    :return: An instance of  dataclass
    """
    return {"service": "price"}


def get_wb_bulk_price(payloads: list[schemas.WbPricePayload]):
    """Interface
    Wildberries price value calculation service

    :param payload:
    :return:
    """
    return {"service": "bulk price"}


#############################################################################
#                   Wildberries Interfaces additionals                      #
#############################################################################


def check_local_index(
    payload: schemas.WbLogPayload | schemas.WbReturnsPayload,
) -> HTTPException | None:
    """Check local_index value in accordance with FBS/FBO option

    :param payload: JSON from request
    :return: Error message or None
    """
    if payload.fbs_fbo_option == "fbs" and payload.local_index != 1:
        raise HTTPException(
            status_code=422,
            detail="local_index must be == 1 for FBS logistics option",
        )
