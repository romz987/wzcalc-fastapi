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
    payload: schemas.WbLogPayload,
) -> wb_calcdata.WbLogCosts:
    """Create an instance of the core dataclass
    based on payload from HTTP request

    :param payload: An instance of pydantic model
    :return: An instance of WbLogCosts datalcass
    """
    return wb_calcdata.WbLogCosts(
        base_price=payload.base_price,
        volume_factor=payload.volume_factor,
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
    :params box_volume: Package box volume based on box size
    :param logistics_fee: Calculated logistics fee value
    :return: An instance of WbLogResponse datalcass
    """
    return wb_calcdata.WbLogResponse(
        # base
        box_size=payload.box_size,
        local_index=payload.local_index,
        # base logistics costs
        base_price=payload.base_price,
        volume_factor=payload.volume_factor,
        # calculated
        box_volume=box_volume,
        logistics_fee=logistics_fee,
    )
