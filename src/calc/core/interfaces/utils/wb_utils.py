from decimal import Decimal
from src.calc import schemas

# dataclasses
from src.calc.core.domain import wb_calcdata


#############################################################################
#                Wildberries utils fill out dataclasses                     #
#############################################################################

#############################################################################
#                                  Requests                                 #
#############################################################################


def request_fill_log_costs(
    payload: schemas.WbLogPayload | schemas.WbReturnsPayload,
) -> wb_calcdata.WbLogCosts:
    """Create an instance of the core dataclass
    based on payload from HTTP request

    :param payload: An instance of pydantic model
    :return: An instance of WbLogCosts dataclass
    """
    return wb_calcdata.WbLogCosts(
        base_price=payload.base_price,
        volume_factor=payload.volume_factor,
        min_lim_1_price=payload.min_lim_1_price,
        min_lim_2_price=payload.min_lim_2_price,
        min_lim_3_price=payload.min_lim_3_price,
        min_lim_4_price=payload.min_lim_4_price,
        min_lim_5_price=payload.min_lim_5_price,
    )


#############################################################################
#                                 Responses                                 #
#############################################################################


def response_fill_log_fee(
    payload: schemas.WbLogPayload,
    box_volume: Decimal,
    logistics_fee: Decimal,
) -> wb_calcdata.WbLogResponse:
    """Create an instance of the core dataclass
    based on payload from HTTP request and calculations results

    :param payload: An instance of pydantic model
    :param box_volume: Package box volume based on box size
    :param logistics_fee: Calculated logistics fee value
    :return: An instance of WbLogResponse dataclass
    """
    return wb_calcdata.WbLogResponse(
        # base
        box_size=payload.box_size,
        local_index=payload.local_index,
        # base logistics costs
        base_price=payload.base_price,
        volume_factor=payload.volume_factor,
        min_lim_1_price=payload.min_lim_1_price,
        min_lim_2_price=payload.min_lim_2_price,
        min_lim_3_price=payload.min_lim_3_price,
        min_lim_4_price=payload.min_lim_4_price,
        min_lim_5_price=payload.min_lim_5_price,
        # calculated
        box_volume=box_volume,
        logistics_fee=logistics_fee,
    )


def response_fill_returns_fee(
    payload: schemas.WbReturnsPayload,
    box_volume: Decimal,
    logistics_fee: Decimal,
    returns_fee: Decimal,
) -> wb_calcdata.WbReturnsResponse:
    """Create an instance of the core dataclass
    based on payload from HTTP request and calculations results

    :param payload: An instance of pydantic model
    :param box_volume: Package box volume based on the box size
    :param logistics_fee: Calculated logistics fee value
    :param returns_fee: Calculated returns fee value
    :return: An instance of WbReturnsResponse dataclass
    """
    return wb_calcdata.WbReturnsResponse(
        # base
        box_size=payload.box_size,
        local_index=payload.local_index,
        # logistics constants
        base_price=payload.base_price,
        volume_factor=payload.volume_factor,
        min_lim_1_price=payload.min_lim_1_price,
        min_lim_2_price=payload.min_lim_2_price,
        min_lim_3_price=payload.min_lim_3_price,
        min_lim_4_price=payload.min_lim_4_price,
        min_lim_5_price=payload.min_lim_5_price,
        # returns constants
        redemption_percentage=payload.redemption_percentage,
        nonredemption_processing_cost=payload.nonredemption_processing_cost,
        # calculated response data
        box_volume=box_volume,
        logistics_fee=logistics_fee,
        returns_fee=returns_fee,
    )
