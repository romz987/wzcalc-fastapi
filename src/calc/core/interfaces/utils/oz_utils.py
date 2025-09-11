from decimal import Decimal
from src.calc import schemas

# dataclasses
from src.calc.core.domain import oz_calcdata


#############################################################################
#                     Ozon utils fill out dataclasses                       #
#############################################################################

#############################################################################
#                                  Requests                                 #
#############################################################################


def request_fill_log_costs_fbs(
    payload: (
        schemas.OzonLogFbsPayload
        | schemas.OzonReturnsFbsPayload
        | schemas.OzonReturnsFboPayload
    ),
) -> oz_calcdata.OzLogFbsCosts:
    """Create an instance of the core dataclass
    based on payload from HTTP request

    :param payload: An instance of pydantic model
    :return: An instance of OzLogFbsCosts dataclass
    """
    return oz_calcdata.OzLogFbsCosts(
        minimal_price_fbs=payload.minimal_price_fbs,
        base_price_fbs=payload.base_price_fbs,
        volume_factor_fbs=payload.volume_factor_fbs,
        fix_large_fbs=payload.fix_large_fbs,
    )


def request_fill_log_costs_fbo(
    payload: schemas.OzonLogFboPayload | schemas.OzonReturnsFboPayload,
) -> oz_calcdata.OzLogFboCosts:
    """Create an instance of the core dataclass
    based on payload from HTTP request

    :param payload: An instance of pydantic model
    :return: An instance of OzLogFboCosts dataclass
    """
    return oz_calcdata.OzLogFboCosts(
        base_price_fbo=payload.base_price_fbo,
        volume_factor_fbo=payload.volume_factor_fbo,
        fix_large_fbo=payload.fix_large_fbo,
    )


#############################################################################
#                                 Responses                                 #
#############################################################################


def response_fill_fbs_log_fee(
    payload: schemas.OzonLogFbsPayload,
    box_volume: Decimal,
    logistics_fee: Decimal,
) -> oz_calcdata.OzLogFbsResponse:
    """Create an instance of the core dataclass
    based on payload from HTTP request and calculations results

    :param payload: An instance of pydantic model
    :param box_volume: Package box volume based on box size
    :param logistics_fee: Calculated logistics fee value
    :return: An instance of OzLogFbsResponse dataclass
    """
    return oz_calcdata.OzLogFbsResponse(
        # base
        box_size=payload.box_size,
        local_index=payload.local_index,
        # base logistics costs
        minimal_price_fbs=payload.minimal_price_fbs,
        base_price_fbs=payload.base_price_fbs,
        volume_factor_fbs=payload.volume_factor_fbs,
        fix_large_fbs=payload.fix_large_fbs,
        # calculated
        box_volume=box_volume,
        logistics_fee=logistics_fee,
    )


def response_fill_fbo_log_fee(
    payload: schemas.OzonLogFboPayload,
    box_volume: Decimal,
    logistics_fee: Decimal,
) -> oz_calcdata.OzLogFboResponse:
    """Create an instance of the core dataclass
    based on payload from HTTP request and calculations results

    :param payload: An instance of pydantic model
    :param box_volume: Package box volume based on the box size
    :param logistics_fee: Calculated logistics fee value
    :return: An instance of OzLogFboResponse dataclass
    """
    return oz_calcdata.OzLogFboResponse(
        # base
        box_size=payload.box_size,
        local_index=payload.local_index,
        base_price_fbo=payload.base_price_fbo,
        volume_factor_fbo=payload.volume_factor_fbo,
        fix_large_fbo=payload.fix_large_fbo,
        # calculated
        box_volume=box_volume,
        logistics_fee=logistics_fee,
    )


def response_fill_fbs_returns_fee(
    payload: schemas.OzonReturnsFbsPayload,
    box_volume: Decimal,
    logistics_fee: Decimal,
    reverse_logistics_fee: Decimal,
    returns_fee: Decimal,
) -> oz_calcdata.OzReturnsFbsResponse:
    """Create an instance of the core dataclass
    based on payload from HTTP request and calculations results

    :param payload: An instance of pydantic model
    :param box_volume: Package box volume based on the box size
    :param logistics_fee: Calculated logistics fee value
    :param reverse_logistics_fee: Calculated reverse logistics fee value
    :param returns_fee: Calculated returns fee value
    :return: An instance of OzReturnsFbsResponse dataclass
    """
    return oz_calcdata.OzReturnsFbsResponse(
        # base
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
        # calculated response data
        logistics_fee=logistics_fee,
        reverse_logistics_fee=reverse_logistics_fee,
        returns_fee=returns_fee,
    )


def response_fill_fbo_returns_fee(
    payload: schemas.OzonReturnsFboPayload,
    box_volume: Decimal,
    logistics_fee: Decimal,
    reverse_logistics_fee: Decimal,
    returns_fee: Decimal,
) -> oz_calcdata.OzReturnsFboResponse:
    """Create an instance of the core dataclass
    based on payload from HTTP request and calculations results

    :param payload: An instance of pydantic model
    :param box_volume: Package box volume based on the box size
    :param logistics_fee: Calculated logistics fee value
    :param reverse_logistics_fee: Calculated reverse logistics fee value
    :param returns_fee: Calculated returns fee value
    :return: An instance of OzReturnsFboResponse dataclass
    """
    return oz_calcdata.OzReturnsFboResponse(
        # base
        box_size=payload.box_size,
        box_volume=box_volume,
        local_index=payload.local_index,
        # fbs logistics constants
        minimal_price_fbs=payload.minimal_price_fbs,
        base_price_fbs=payload.base_price_fbs,
        volume_factor_fbs=payload.volume_factor_fbs,
        fix_large_fbs=payload.fix_large_fbs,
        # fbo logistics constants
        base_price_fbo=payload.base_price_fbo,
        volume_factor_fbo=payload.volume_factor_fbo,
        fix_large_fbo=payload.fix_large_fbo,
        # returns constants
        redemption_percentage=payload.redemption_percentage,
        nonredemption_processing_cost=payload.nonredemption_processing_cost,
        # calculated response data
        logistics_fee=logistics_fee,
        reverse_logistics_fee=reverse_logistics_fee,
        returns_fee=returns_fee,
    )
