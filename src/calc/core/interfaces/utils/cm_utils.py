from decimal import Decimal
from src.calc import schemas

# dataclasses
from src.calc.core.domain import cm_calcdata


#############################################################################
#                   Common utils fill out dataclasses                       #
#############################################################################

#############################################################################
#                                Requests                                   #
#############################################################################


def request_fill_log_params(
    payload: (
        schemas.OzonLogFbsPayload
        | schemas.OzonLogFboPayload
        | schemas.OzonReturnsFbsPayload
        | schemas.OzonReturnsFboPayload
        | schemas.WbLogPayload
    ),
    box_volume: Decimal,
) -> cm_calcdata.LogMainParams:
    """Create an instance of the core dataclass
    based on payload from HTTP request

    :param payload: An instance of pydantic model
    :param box_volume: Package box volume based on box size
    :return: An instance of LogMainParams datalcass
    """
    return cm_calcdata.LogMainParams(
        local_index=payload.local_index,
        box_volume=box_volume,
    )


def request_fill_return_params(
    payload: schemas.OzonReturnsFbsPayload | schemas.OzonReturnsFboPayload,
) -> cm_calcdata.ReturnsParams:
    """Create an instance of the core dataclass
    based on payload from HTTP request

    :param payload: An instance of pydantic model
    :return: An instance of ReturnsParams datalcass
    """
    return cm_calcdata.ReturnsParams(
        redemption_percentage=payload.redemption_percentage,
        nonredemption_processing_cost=payload.nonredemption_processing_cost,
    )
