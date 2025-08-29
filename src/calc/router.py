from fastapi import APIRouter
from .schemas import (
    # Ozon
    OzonFbsPayload,
    OzonFboPayload,
    OzonLogFbsPayload,
    OzonLogFboPayload,
    OzonReturnsFbsPayload,
    OzonReturnsFboPayload,
    # Wildberries
    WbPayload,
    WbLogPayload,
    WbReturnsPayload,
)


router = APIRouter()


##########################################################
#                   Расчет цен для Ozon                  #
##########################################################


# Единичный расчет цены fbs
@router.post("/ozon/prices/fbs/calculate/")
def ozon_prices_fbs_calc(payload: OzonFbsPayload):
    return {"ok": "it works!"}


# Единичный расчет цены fbo
@router.post("/ozon/prices/fbo/calculate")
def ozon_prices_fbo_calc(payload: OzonFboPayload):
    return {"ok": "it works!"}


# Массовый расчет цен fbs
@router.post("/ozon/prices/fbs/bulk/calculate/")
def ozon_prices_fbs_bulk_calc(payloads: list[OzonFbsPayload]):
    return {"ok": "it works!"}


# Массовый расчет цен fbo
@router.post("/ozon/prices/fbo/bulk/calculate/")
def ozon_prices_fbo_bulk_calc(payloads: list[OzonFboPayload]):
    return {"ok": "it works!"}


# Расчет стоимости логистики fbs
@router.post("/ozon/logistics/fbs/calculate")
def ozon_logistics_fbs_calc(payload: OzonLogFbsPayload):
    return {"ok": "it works!"}


# Расчет стоимости логистики fbo
@router.post("/ozon/logistics/fbo/calculate")
def ozon_logistics_fbo_calc(payload: OzonLogFboPayload):
    return {"ok": "it works!"}


# Расчет стоимости возвратов fbs
@router.post("/ozon/returns/fbs/calculate")
def ozon_returns_fbs_calc(payload: OzonReturnsFbsPayload):
    return {"ok": "it works!"}


# Расчет стоимости возвратов fbo
@router.post("/ozon/returns/fbo/calculate")
def ozon_returns_fbo_calc(payload: OzonReturnsFboPayload):
    return {"ok": "it works!"}


##########################################################
#                Расчет цен для Wildberries              #
##########################################################


# Единичный расчет цены
@router.post("/wb/prices/calculate")
def wb_prices_fbs_calc(payload: WbPayload):
    return {"ok": "it works!"}


# Массовый расчет цен
@router.post("/wb/prices/bulk/calculate/")
def wb_prices_bulk_calc(payloads: list[WbPayload]):
    return {"ok": "it works!"}


# Расчет стоимости логистики
@router.post("/wb/logistics/calculate")
def wb_logistics_calc(payload: WbLogPayload):
    return {"ok": "it works!"}


# Расчет стоимости возвратов
@router.post("/wb/returns/calculate")
def wb_returns_calc(payload: WbReturnsPayload):
    return {"ok": "it works!"}
