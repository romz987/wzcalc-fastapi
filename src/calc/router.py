from fastapi import APIRouter
from src.calc import schemas
from src.calc.service.service_oz.logistics_oz import (
    calculate_logistics_fbs_oz,
    calculate_logistics_fbo_oz,
    calculate_returns_fbs_oz,
    calculate_returns_fbo_oz,
)


router = APIRouter()


##########################################################
#                   Расчет цен для Ozon                  #
##########################################################


# Единичный расчет цены fbs
@router.post("/ozon/prices/fbs/calculate")
def ozon_prices_fbs_calc(payload: schemas.OzonFbsPayload):
    return {"ok": "it works!"}


# Единичный расчет цены fbo
@router.post("/ozon/prices/fbo/calculate")
def ozon_prices_fbo_calc(payload: schemas.OzonFboPayload):
    return {"ok": "it works!"}


# Массовый расчет цен fbs
@router.post("/ozon/prices/fbs/bulk/calculate/")
def ozon_prices_fbs_bulk_calc(payloads: list[schemas.OzonFbsPayload]):
    return {"ok": "it works!"}


# Массовый расчет цен fbo
@router.post("/ozon/prices/fbo/bulk/calculate/")
def ozon_prices_fbo_bulk_calc(payloads: list[schemas.OzonFboPayload]):
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
def wb_prices_fbs_calc(payload: schemas.WbPayload):
    return {"ok": "it works!"}


# Массовый расчет цен
@router.post("/wb/prices/bulk/calculate/")
def wb_prices_bulk_calc(payloads: list[schemas.WbPayload]):
    return {"ok": "it works!"}


# Расчет стоимости логистики
@router.post("/wb/logistics/calculate")
def wb_logistics_calc(payload: schemas.WbLogPayload):
    return {"ok": "it works!"}


# Расчет стоимости возвратов
@router.post("/wb/returns/calculate")
def wb_returns_calc(payload: schemas.WbReturnsPayload):
    return {"ok": "it works!"}
