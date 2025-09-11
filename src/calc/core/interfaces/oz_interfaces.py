from src.calc import schemas

# dataclasses
from src.calc.core.domain import oz_calcdata

# calculators
from src.calc.core.calculators.common import box_volume_clc
from src.calc.core.calculators.ozon import oz_log_fbs_clc, oz_log_fbo_clc

# services
from src.calc.core.services.oz_services import (
    oz_calculate_returns_fbs,
    oz_calculate_returns_fbo,
)

# utils
from src.calc.core.interfaces.utils import oz_utils, cm_utils


#############################################################################
#                       Ozon Calculation Interfaces                         #
#############################################################################

########################## Logistics and Returns ############################


def get_oz_logistics_fee_fbs(
    payload: schemas.OzonLogFbsPayload,
) -> oz_calcdata.OzLogFbsResponse:
    """Interface
    Ozon FBS logistics fee value calculation service

    :param payload: An instance of the OzonLogFbsPayload pydantic model
    :return: An instance of OzLogFbsResponse dataclass
    """
    # Calculate box volume
    box_volume = box_volume_clc(payload.box_size)
    # Create args
    log_params = cm_utils.request_fill_log_params(payload, box_volume)
    log_costs = oz_utils.request_fill_log_costs_fbs(payload)
    # Calculate logistics fee
    logistics_fee = oz_log_fbs_clc(log_params, log_costs)
    # Fill up and return response-dataclass
    return oz_utils.response_fill_fbs_log_fee(
        payload,
        box_volume,
        logistics_fee,
    )


def get_oz_logistics_fee_fbo(
    payload: schemas.OzonLogFboPayload,
) -> oz_calcdata.OzLogFboResponse:
    """Interface
    Ozon FBO logistics fee value calculation service

    :param payload: An instance of the OzonLogFboPayload pydantic model
    :return: An instance of OzLogFboResponse dataclass
    """
    # Calculate box box volume
    box_volume = box_volume_clc(payload.box_size)
    # Create args
    log_params = cm_utils.request_fill_log_params(payload, box_volume)
    log_costs = oz_utils.request_fill_log_costs_fbo(payload)
    # Calculate logistics fee
    logistics_fee = oz_log_fbo_clc(log_params, log_costs)
    # Fill up and return response-dataclass
    return oz_utils.response_fill_fbo_log_fee(
        payload,
        box_volume,
        logistics_fee,
    )


def get_oz_returns_fee_fbs(
    payload: schemas.OzonReturnsFbsPayload,
) -> oz_calcdata.OzReturnsFbsResponse:
    """Interface
    Ozon FBS returns fee value calculation service

    :param payload: An instance of the OzonReturnsFbsPayload pydantic model
    :return: An instance of OzReturnsFbsResponse dataclass
    """
    # Calculate box box volume
    box_volume = box_volume_clc(payload.box_size)
    # Create args
    log_params = cm_utils.request_fill_log_params(payload, box_volume)
    log_costs = oz_utils.request_fill_log_costs_fbs(payload)
    return_params = cm_utils.request_fill_return_params(payload)
    # Calculate
    logistics_fee, reverse_logistics_fee, returns_fee = (
        oz_calculate_returns_fbs(log_params, log_costs, return_params)
    )
    # Fill up and return response-dataclass
    return oz_utils.response_fill_fbs_returns_fee(
        payload,
        box_volume,
        logistics_fee,
        reverse_logistics_fee,
        returns_fee,
    )


def get_oz_returns_fee_fbo(
    payload: schemas.OzonReturnsFboPayload,
) -> oz_calcdata.OzReturnsFboResponse:
    """Interface
    Ozon FBO returns fee value calculation service

    :param payload: An instance of the OzonReturnsFboPayload pydantic model
    :return: An instance of OzReturnsFboResponse dataclass
    """
    # Calculate box box volume
    box_volume = box_volume_clc(payload.box_size)
    # Create args
    log_params = cm_utils.request_fill_log_params(payload, box_volume)
    log_costs_fbs = oz_utils.request_fill_log_costs_fbs(payload)
    log_costs_fbo = oz_utils.request_fill_log_costs_fbo(payload)
    return_params = cm_utils.request_fill_return_params(payload)
    # Calculate returns_fee
    logistics_fee, reverse_logistics_fee, returns_fee = (
        oz_calculate_returns_fbo(
            log_params,
            log_costs_fbs,
            log_costs_fbo,
            return_params,
        )
    )
    # Fill up and return response-dataclass
    return oz_utils.response_fill_fbo_returns_fee(
        payload,
        box_volume,
        logistics_fee,
        reverse_logistics_fee,
        returns_fee,
    )


################################# Profit ####################################


def get_oz_profit_fbs(payload: schemas.OzonProfitFbsPayload):
    """Interface
    Ozon FBS profit value calculation service

    :param payload: An instance of the OzonProfitFbsPayload pydantic model
    :return: An instance of  dataclass
    """
    return {"service": "profit_fbs"}


def get_oz_profit_fbo(payload: schemas.OzonProfitFboPayload):
    """Interface
    Ozon FBS profit value calculation service

    :param payload: An instance of the OzonProfitFboPayload pydantic model
    :return: An instance of  dataclass
    """
    return {"service": "profit_fbo"}


################################## Price ####################################


def get_oz_price_fbs(payload: schemas.OzonPriceFbsPayload):
    """Interface
    Ozon FBS price value calculation service

    :param payload: An instance of the OzonPriceFbsPayload pydantic model
    :return: An instance of  dataclass
    """
    return {"service": "price_fbs"}


def get_oz_price_fbo(payload: schemas.OzonPriceFboPayload):
    """Interface
    Ozon FBO price value calculation service

    :param payload: An instance of the OzonPriceFboPayload pydantic model
    :return: An instance of  dataclass
    """
    return {"service": "price_fbo"}


def get_oz_bulk_price_fbs(payloads: list[schemas.OzonPriceFbsPayload]):
    """Interface
    Ozon FBS bulk price value calculation service

    :param payloads:
    :return:
    """
    return {"service": "bulk_price_fbs"}


def get_oz_bulk_price_fbo(payloads: list[schemas.OzonPriceFboPayload]):
    """Interface
    Ozon FBO bulk price value calculation service

    :param payloads:
    :return:
    """
    return {"service": "bulk_price_fbo"}
