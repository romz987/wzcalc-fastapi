from src.calc import schemas
from src.calc.core.domain import oz_calcdata
from src.calc.core.calculators.common import box_volume_clc
from src.calc.core.calculators.ozon import oz_log_fbs_clc, oz_log_fbo_clc
from src.calc.core.services.oz_services import (
    oz_calculate_returns_fbs,
    oz_calculate_returns_fbo,
)

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
    # Calculate box box volume
    box_volume = box_volume_clc(payload.box_size)
    # Create args
    item_params = oz_calcdata.OzLogItemParams(
        local_index=payload.local_index,
        box_volume=box_volume,
    )
    log_costs = oz_calcdata.OzLogFbsCosts(
        minimal_price_fbs=payload.minimal_price_fbs,
        base_price_fbs=payload.base_price_fbs,
        volume_factor_fbs=payload.volume_factor_fbs,
        fix_large_fbs=payload.fix_large_fbs,
    )
    # Calculate logistics fee
    logistics_fee = oz_log_fbs_clc(item_params, log_costs)
    # Fill up and return response-dataclass
    return oz_calcdata.OzLogFbsResponse(
        box_size=payload.box_size,
        box_volume=box_volume,
        local_index=payload.local_index,
        minimal_price_fbs=payload.minimal_price_fbs,
        base_price_fbs=payload.base_price_fbs,
        volume_factor_fbs=payload.volume_factor_fbs,
        fix_large_fbs=payload.fix_large_fbs,
        logistics_fee=logistics_fee,
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
    item_params = oz_calcdata.OzLogItemParams(
        local_index=payload.local_index,
        box_volume=box_volume,
    )
    log_costs = oz_calcdata.OzLogFboCosts(
        base_price_fbo=payload.base_price_fbo,
        volume_factor_fbo=payload.volume_factor_fbo,
        fix_large_fbo=payload.fix_large_fbo,
    )
    # Calculate logistics fee
    logistics_fee = oz_log_fbo_clc(item_params, log_costs)
    # Fill up and return response-dataclass
    return oz_calcdata.OzLogFboResponse(
        box_size=payload.box_size,
        box_volume=box_volume,
        local_index=payload.local_index,
        base_price_fbo=payload.base_price_fbo,
        volume_factor_fbo=payload.volume_factor_fbo,
        fix_large_fbo=payload.fix_large_fbo,
        logistics_fee=logistics_fee,
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
    item_params = oz_calcdata.OzLogItemParams(
        local_index=payload.local_index,
        box_volume=box_volume,
    )
    log_costs = oz_calcdata.OzLogFbsCosts(
        minimal_price_fbs=payload.minimal_price_fbs,
        base_price_fbs=payload.base_price_fbs,
        volume_factor_fbs=payload.volume_factor_fbs,
        fix_large_fbs=payload.fix_large_fbs,
    )
    return_params = oz_calcdata.OzReturnsParams(
        redemption_percentage=payload.redemption_percentage,
        nonredemption_processing_cost=payload.nonredemption_processing_cost,
    )
    logistics_fee, reverse_logistics_fee, returns_fee = (
        oz_calculate_returns_fbs(item_params, log_costs, return_params)
    )
    # Fill up and return response-dataclass
    return oz_calcdata.OzReturnsFbsResponse(
        box_size=payload.box_size,
        box_volume=box_volume,
        local_index=payload.local_index,
        # logistics constants
        minimal_price_fbs=payload.minimal_price_fbs,
        base_price_fbs=payload.base_price_fbs,
        volume_factor_fbs=payload.volume_factor_fbs,
        fix_large_fbs=payload.fix_large_fbs,
        # returns constants
        redemption_percentage=payload.redemption_percentage,
        nonredemption_processing_cost=payload.nonredemption_processing_cost,
        # new response data
        logistics_fee=logistics_fee,
        reverse_logistics_fee=reverse_logistics_fee,
        returns_fee=returns_fee,
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
    item_params = oz_calcdata.OzLogItemParams(
        local_index=payload.local_index,
        box_volume=box_volume,
    )
    log_costs_fbs = oz_calcdata.OzLogFbsCosts(
        minimal_price_fbs=payload.minimal_price_fbs,
        base_price_fbs=payload.base_price_fbs,
        volume_factor_fbs=payload.volume_factor_fbs,
        fix_large_fbs=payload.fix_large_fbs,
    )
    log_costs_fbo = oz_calcdata.OzLogFboCosts(
        base_price_fbo=payload.base_price_fbo,
        volume_factor_fbo=payload.volume_factor_fbo,
        fix_large_fbo=payload.fix_large_fbo,
    )
    return_params = oz_calcdata.OzReturnsParams(
        redemption_percentage=payload.redemption_percentage,
        nonredemption_processing_cost=payload.nonredemption_processing_cost,
    )
    # Calculate returns_fee
    logistics_fee, reverse_logistics_fee, returns_fee = (
        oz_calculate_returns_fbo(
            item_params,
            log_costs_fbs,
            log_costs_fbo,
            return_params,
        )
    )
    # Fill up and return response-dataclass
    return oz_calcdata.OzReturnsFboResponse(
        box_size=payload.box_size,
        box_volume=box_volume,
        local_index=payload.local_index,
        # logistics constants fbs
        minimal_price_fbs=payload.minimal_price_fbs,
        base_price_fbs=payload.base_price_fbs,
        volume_factor_fbs=payload.volume_factor_fbs,
        fix_large_fbs=payload.fix_large_fbs,
        # logistics constants fbo
        base_price_fbo=payload.base_price_fbo,
        volume_factor_fbo=payload.volume_factor_fbo,
        fix_large_fbo=payload.fix_large_fbo,
        # returns constants
        redemption_percentage=payload.redemption_percentage,
        nonredemption_processing_cost=payload.nonredemption_processing_cost,
        # new response data
        logistics_fee=logistics_fee,
        reverse_logistics_fee=reverse_logistics_fee,
        returns_fee=returns_fee,
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
