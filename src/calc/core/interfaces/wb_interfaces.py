from src.calc import schemas

#############################################################################
#                      Wildberries Calculation Routes                       #
#############################################################################

########################## Logistics and Returns ############################


def get_wb_logistics_fee(payload: schemas.WbLogPayload):
    """Interface
    Wildberries logistics fee value calculation service

    :param payload: An instance of the WbLogPayload pydantic model
    :return: An instance of  dataclass
    """
    return {"service": "logistics"}


def get_wb_returns_fee(payload: schemas.WbReturnsPayload):
    """Interface
    Wildberries returns fee value calculation service

    :param payload: An instance of the WbReturnsPayload pydantic model
    :return: An instance of  dataclass
    """
    return {"service": "returns"}


################################# Profit ####################################


def get_wb_profit(payload: schemas.WbProfitPayload):
    """Interface
    Wildberries profit value calculation service

    :param payload: An instance of the WbProfitPayload pydantic model
    :return: An instance of  dataclass
    """
    return {"service": "profit"}


################################## Price ####################################


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
