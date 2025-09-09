from fastapi import APIRouter
from src.calc import schemas
from src.calc.core.interfaces.oz_interfaces import (
    get_oz_logistics_fee_fbs,
    get_oz_logistics_fee_fbo,
    get_oz_returns_fee_fbs,
    get_oz_returns_fee_fbo,
    get_oz_profit_fbs,
    get_oz_profit_fbo,
    get_oz_price_fbs,
    get_oz_price_fbo,
    get_oz_bulk_price_fbs,
    get_oz_bulk_price_fbo,
)
from src.calc.core.interfaces.wb_interfaces import (
    get_wb_logistics_fee,
    get_wb_returns_fee,
    get_wb_profit,
    get_wb_price,
    get_wb_bulk_price,
)

router = APIRouter()


#############################################################################
#                         Ozon Calculation Routes                           #
#############################################################################

########################## Logistics and Returns ############################


# Single logistics calculation FBS
@router.post("/ozon/logistics/fbs/calculate")
def ozon_logistics_fbs_calc(payload: schemas.OzonLogFbsPayload):
    return get_oz_logistics_fee_fbs(payload)


# Single logistics calculation FBO
@router.post("/ozon/logistics/fbo/calculate")
def ozon_logistics_fbo_calc(payload: schemas.OzonLogFboPayload):
    return get_oz_logistics_fee_fbo(payload)


# Single returns calculation FBS
@router.post("/ozon/returns/fbs/calculate")
def ozon_returns_fbs_calc(payload: schemas.OzonReturnsFbsPayload):
    return get_oz_returns_fee_fbs(payload)


# Single returns calculation FBO
@router.post("/ozon/returns/fbo/calculate")
def ozon_returns_fbo_calc(payload: schemas.OzonReturnsFboPayload):
    return get_oz_returns_fee_fbo(payload)


################################## Profit ####################################


# Single profit calculation FBS
@router.post("/ozon/profits/fbs/calculate")
def ozon_profits_fbs_calc(payload: schemas.OzonProfitFbsPayload):
    return get_oz_profit_fbs(payload)


# Single profit calculation FBO
@router.post("/ozon/profits/fbo/calculate")
def ozon_profits_fbo_calc(payload: schemas.OzonProfitFboPayload):
    return get_oz_profit_fbo(payload)


################################## Price ####################################


# Single price calculation FBS
@router.post("/ozon/prices/fbs/calculate")
def ozon_prices_fbs_calc(payload: schemas.OzonPriceFbsPayload):
    return get_oz_price_fbs(payload)


# Single price calculation FBO
@router.post("/ozon/prices/fbo/calculate")
def ozon_prices_fbo_calc(payload: schemas.OzonPriceFboPayload):
    return get_oz_price_fbo(payload)


# Bulk price calculation FBS
@router.post("/ozon/prices/fbs/bulk/calculate/")
def ozon_prices_fbs_bulk_calc(payloads: list[schemas.OzonPriceFbsPayload]):
    return get_oz_bulk_price_fbs(payloads)


# Bulk price calculation FBO
@router.post("/ozon/prices/fbo/bulk/calculate/")
def ozon_prices_fbo_bulk_calc(payloads: list[schemas.OzonPriceFboPayload]):
    return get_oz_bulk_price_fbo(payloads)


#############################################################################
#                     Wildberries Calculation Routes                        #
#############################################################################

########################## Logistics and Returns ############################


# Single logistics calculation
@router.post("/wb/logistics/calculate")
def wb_logistics_calc(payload: schemas.WbLogPayload):
    return get_wb_logistics_fee(payload)


# Single returns calculation
@router.post("/wb/returns/calculate")
def wb_returns_calc(payload: schemas.WbReturnsPayload):
    return get_wb_returns_fee(payload)


################################## Profit ###################################


# Single profit calculation
@router.post("/wb/profits/calculate")
def wb_profits_calc(payload: schemas.WbProfitPayload):
    return get_wb_profit(payload)


################################### Price ###################################


# Single price calculation
@router.post("/wb/prices/calculate")
def wb_prices_calc(payload: schemas.WbPricePayload):
    return get_wb_price(payload)


# Bulk price calculation
@router.post("/wb/prices/bulk/calculate/")
def wb_prices_bulk_calc(payloads: list[schemas.WbPricePayload]):
    return get_wb_bulk_price(payloads)
