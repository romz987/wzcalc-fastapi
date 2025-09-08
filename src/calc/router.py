from fastapi import APIRouter
from src.calc import schemas
from src.calc.service.service_oz.logistics_oz import (
    calculate_logistics_fbs_oz,
    calculate_logistics_fbo_oz,
    calculate_returns_fbs_oz,
    calculate_returns_fbo_oz,
)
from src.calc.service.service_wb.logistics_wb import (
    calculate_logistics_wb,
    calculate_returns_wb,
)

router = APIRouter()


##########################################################
#                   Расчет цен для Ozon                  #
##########################################################


# Единичный расчет цены fbs
@router.post("/ozon/prices/fbs/calculate")
def ozon_prices_fbs_calc(payload: schemas.OzonPriceFbsPayload):
    return {"ok": "it works!"}


# Единичный расчет цены fbo
@router.post("/ozon/prices/fbo/calculate")
def ozon_prices_fbo_calc(payload: schemas.OzonPriceFboPayload):
    return {"ok": "it works!"}


# Единичный расчет профита fbs
@router.post("/ozon/profits/fbs/calculate")
def ozon_profits_fbs_calc(payload: schemas.OzonProfitFbsPayload):
    return {"ok": "it works!"}


# Единичный расчет профита fbo
@router.post("/ozon/profits/fbo/calculate")
def ozon_profits_fbo_calc(payload: schemas.OzonProfitFboPayload):
    return {"ok": "it works!"}


# Массовый расчет цен fbs
@router.post("/ozon/prices/fbs/bulk/calculate/")
def ozon_prices_fbs_bulk_calc(payloads: list[schemas.OzonPriceFbsPayload]):
    return {"ok": "it works!"}


# Массовый расчет цен fbo
@router.post("/ozon/prices/fbo/bulk/calculate/")
def ozon_prices_fbo_bulk_calc(payloads: list[schemas.OzonPriceFboPayload]):
    return {"ok": "it works!"}


# Расчет стоимости логистики fbs
@router.post("/ozon/logistics/fbs/calculate")
def ozon_logistics_fbs_calc(payload: schemas.OzonLogFbsPayload):
    return calculate_logistics_fbs_oz(payload)


# Расчет стоимости логистики fbo
@router.post("/ozon/logistics/fbo/calculate")
def ozon_logistics_fbo_calc(payload: schemas.OzonLogFboPayload):
    return calculate_logistics_fbo_oz(payload)


# Расчет стоимости возвратов fbs
@router.post("/ozon/returns/fbs/calculate")
def ozon_returns_fbs_calc(payload: schemas.OzonReturnsFbsPayload):
    return calculate_returns_fbs_oz(payload)


# Расчет стоимости возвратов fbo
@router.post("/ozon/returns/fbo/calculate")
def ozon_returns_fbo_calc(payload: schemas.OzonReturnsFboPayload):
    return calculate_returns_fbo_oz(payload)


##########################################################
#                Расчет цен для Wildberries              #
##########################################################


# Единичный расчет цены
@router.post("/wb/prices/calculate")
def wb_prices_calc(payload: schemas.WbPricePayload):
    return {"ok": "it works!"}


# Единичный расчет профита
@router.post("/wb/profits/calculate")
def wb_profits_calc(payload: schemas.WbProfitPayload):
    return {"ok": "it works!"}


# Массовый расчет цен
@router.post("/wb/prices/bulk/calculate/")
def wb_prices_bulk_calc(payloads: list[schemas.WbPricePayload]):
    return {"ok": "it works!"}


# Расчет стоимости логистики
@router.post("/wb/logistics/calculate")
def wb_logistics_calc(payload: schemas.WbLogPayload):
    return calculate_logistics_wb(payload)


# Расчет стоимости возвратов
@router.post("/wb/returns/calculate")
def wb_returns_calc(payload: schemas.WbReturnsPayload):
    return calculate_returns_wb(payload)
