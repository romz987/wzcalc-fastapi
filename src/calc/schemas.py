from typing import Annotated
from enum import Enum
from pydantic import BaseModel, Field
from decimal import Decimal

# Проверка строки с размерами упакровки
BoxSize = Annotated[str, Field(pattern=r"^\d{1,3}\*\d{1,3}\*\d{1,3}$")]

##################################
#              ENUM              #
##################################


# Диапазон значений для tax_system
class TaxsystemEnum(str, Enum):
    SIMPLE = "simple"
    DIFFERENCE = "difference"


# Диапазон значений для логистики
class LogOptionEnum(str, Enum):
    FBS = "fbs"
    FBO = "fbo"


##################################
#          VERIFICATION          #
##################################


# Базовый класс расчета цен
class BasePayload(BaseModel):
    tax_system: TaxsystemEnum
    comission_percent: Decimal
    acquiring_percent: Decimal
    local_index: Decimal
    tax_percent: Decimal
    risk_percent: Decimal
    nonredemption_percentage: Decimal
    profit_percent: Decimal
    cost_per_one: Decimal
    count: Decimal
    wage_cost: Decimal
    box_cost: Decimal
    box_size: BoxSize


##################################
#              OZON              #
##################################


# Расчет цены для OZON FBS
class OzonFbsPayload(BasePayload):
    shipment_processing: Decimal
    # новое
    nonredemption_processing_cost: Decimal
    last_mile_percent: Decimal
    minimal_price_fbs: Decimal
    base_price_fbs: Decimal
    volume_factor_fbs: Decimal
    fix_large_fbs: Decimal


# Расчет цены для OZON FBO
class OzonFboPayload(BasePayload):
    shipment_processing: Decimal
    # новое
    nonredemption_processing_cost: Decimal
    last_mile_percent: Decimal
    base_price_fbo: Decimal
    volume_factor_fbo: Decimal
    fix_large_fbo: Decimal


# Расчет стоимости логистики для Ozon FBS
class OzonLogFbsPayload(BaseModel):
    box_size: Decimal
    local_index: Decimal
    # новое
    minimal_price_fbs: Decimal
    base_price_fbs: Decimal
    volume_factor_fbs: Decimal
    fix_large_fbs: Decimal


# Расчет стоимости логистики для Ozon FBO
class OzonLogFboPayload(BaseModel):
    box_size: Decimal
    local_index: Decimal
    # новое
    base_price_fbo: Decimal
    volume_factor_fbo: Decimal
    fix_large_fbo: Decimal


# Расчет стоимости возвратов для Ozon FBS
class OzonReturnsFbsPayload(BaseModel):
    box_size: Decimal
    nonredemption_percentage: Decimal
    local_index: Decimal
    # новое
    minimal_price_fbs: Decimal
    base_price_fbs: Decimal
    volume_factor_fbs: Decimal
    fix_large_fbs: Decimal


# Расчет стоимости возвратов для Ozon FBO
class OzonReturnsFboPayload(BaseModel):
    box_size: Decimal
    nonredemption_percentage: Decimal
    local_index: Decimal
    # новое
    base_price_fbo: Decimal
    volume_factor_fbo: Decimal
    fix_large_fbo: Decimal


##################################
#           WILDBERRIES          #
##################################


# Расчет цены для Wildberries
class WbPayload(BasePayload):
    fbs_fbo_option: LogOptionEnum
    # новое
    base_price: Decimal
    volume_factor: Decimal
    reverse_logistics_price: Decimal


# Расчет стоимости логистики для Wildberries
class WbLogPayload(BaseModel):
    fbs_fbo_option: LogOptionEnum
    box_size: Decimal
    local_index: Decimal
    # новое
    base_price: Decimal
    volume_factor: Decimal


# Расчет стоимости возвратов для Wildberries
class WbReturnsPayload(BaseModel):
    fbs_fbo_option: LogOptionEnum
    box_size: Decimal
    nonredemption_percentage: Decimal
    local_index: Decimal
