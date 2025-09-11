from src.calc import schemas
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

    :param payload: An instance of OzonLogFbsPayload pydantic model
    :return: An instance of OzLogFbsCosts datalcass
    """
    return wb_calcdata.WbLogCosts(
        base_price=payload.base_price,
        volume_factor=payload.volume_factor,
    )
