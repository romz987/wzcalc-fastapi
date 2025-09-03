from typing import Annotated
from enum import Enum
from pydantic import BaseModel, Field, ConfigDict, condecimal, conint

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
    comission_percent: condecimal(
        gt=0,
        le=100,
        max_digits=4,
        decimal_places=1,
    )  # pyright: ignore
    acquiring_percent: condecimal(
        gt=0,
        le=100,
        max_digits=4,
        decimal_places=1,
    )  # pyright: ignore
    local_index: condecimal(
        gt=0,
        le=10,
        max_digits=4,
        decimal_places=1,
    )  # pyright: ignore
    tax_percent: condecimal(
        gt=0,
        le=100,
        max_digits=4,
        decimal_places=1,
    )  # pyright: ignore
    risk_percent: condecimal(
        gt=0,
        le=100,
        max_digits=4,
        decimal_places=1,
    )  # pyright: ignore
    redemption_percentage: condecimal(
        gt=0,
        le=100,
        max_digits=4,
        decimal_places=1,
    )  # pyright: ignore
    profit_percent: condecimal(
        ge=0,
        le=100,
        max_digits=4,
        decimal_places=1,
    )  # pyright: ignore
    cost_per_one: condecimal(
        ge=0,
        max_digits=8,
        decimal_places=1,
    )  # pyright: ignore
    count: conint(ge=1, le=9999999)  # pyright: ignore
    wage_cost: condecimal(
        ge=0,
        max_digits=8,
        decimal_places=1,
    )  # pyright: ignore
    box_cost: condecimal(
        ge=0,
        max_digits=8,
        decimal_places=1,
    )  # pyright: ignore
    box_size: BoxSize

    model_config = ConfigDict(extra="forbid")


##################################
#              OZON              #
##################################


# Расчет цены для OZON FBS
class OzonFbsPayload(BasePayload):
    shipment_processing: conint(ge=1, le=9999999)  # pyright: ignore
    # новое
    nonredemption_processing_cost: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore
    last_mile_percent: condecimal(
        gt=0,
        le=100,
        max_digits=4,
        decimal_places=1,
    )  # pyright: ignore
    minimal_price_fbs: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore
    base_price_fbs: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore
    volume_factor_fbs: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore
    fix_large_fbs: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore


# Расчет цены для OZON FBO
class OzonFboPayload(BasePayload):
    shipment_processing: conint(ge=1, le=9999999)  # pyright: ignore
    # новое
    nonredemption_processing_cost: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore
    last_mile_percent: condecimal(
        gt=0,
        le=100,
        max_digits=4,
        decimal_places=1,
    )  # pyright: ignore
    base_price_fbo: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore
    volume_factor_fbo: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore
    fix_large_fbo: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore


# Расчет стоимости логистики для Ozon FBS
class OzonLogFbsPayload(BaseModel):
    box_size: BoxSize
    local_index: condecimal(
        gt=0,
        le=10,
        max_digits=4,
        decimal_places=1,
    )  # pyright: ignore
    # новое
    minimal_price_fbs: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore
    base_price_fbs: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore
    volume_factor_fbs: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore
    fix_large_fbs: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore

    model_config = ConfigDict(extra="forbid")


# Расчет стоимости логистики для Ozon FBO
class OzonLogFboPayload(BaseModel):
    box_size: BoxSize
    local_index: condecimal(
        gt=0,
        le=10,
        max_digits=4,
        decimal_places=1,
    )  # pyright: ignore
    # новое
    base_price_fbo: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore
    volume_factor_fbo: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore
    fix_large_fbo: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore

    model_config = ConfigDict(extra="forbid")


# Расчет стоимости возвратов для Ozon FBS
class OzonReturnsFbsPayload(BaseModel):
    box_size: BoxSize
    redemption_percentage: condecimal(
        gt=0,
        le=100,
        max_digits=4,
        decimal_places=1,
    )  # pyright: ignore
    local_index: condecimal(
        gt=0,
        le=10,
        max_digits=4,
        decimal_places=1,
    )  # pyright: ignore
    # новое
    nonredemption_processing_cost: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore
    minimal_price_fbs: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore
    base_price_fbs: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore
    volume_factor_fbs: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore
    fix_large_fbs: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore

    model_config = ConfigDict(extra="forbid")


# Расчет стоимости возвратов для Ozon FBO
class OzonReturnsFboPayload(BaseModel):
    box_size: BoxSize
    redemption_percentage: condecimal(
        gt=0,
        le=100,
        max_digits=4,
        decimal_places=1,
    )  # pyright: ignore
    local_index: condecimal(
        gt=0,
        le=10,
        max_digits=4,
        decimal_places=1,
    )  # pyright: ignore
    # новое
    nonredemption_processing_cost: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore
    base_price_fbo: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore
    volume_factor_fbo: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore
    fix_large_fbo: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore
    minimal_price_fbs: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore
    base_price_fbs: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore
    volume_factor_fbs: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore
    fix_large_fbs: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore

    model_config = ConfigDict(extra="forbid")


##################################
#           WILDBERRIES          #
##################################


# Расчет цены для Wildberries
class WbPayload(BasePayload):
    fbs_fbo_option: LogOptionEnum
    # новое
    base_price: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore
    volume_factor: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore
    reverse_logistics_price: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore


# Расчет стоимости логистики для Wildberries
class WbLogPayload(BaseModel):
    fbs_fbo_option: LogOptionEnum
    box_size: BoxSize
    local_index: condecimal(
        gt=0,
        le=10,
        max_digits=4,
        decimal_places=1,
    )  # pyright: ignore
    # новое
    base_price: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore
    volume_factor: condecimal(
        gt=0,
        le=99999,
        max_digits=6,
        decimal_places=1,
    )  # pyright: ignore

    model_config = ConfigDict(extra="forbid")


# Расчет стоимости возвратов для Wildberries
class WbReturnsPayload(BaseModel):
    fbs_fbo_option: LogOptionEnum
    box_size: BoxSize
    redemption_percentage: condecimal(
        gt=0,
        le=100,
        max_digits=4,
        decimal_places=1,
    )  # pyright: ignore
    local_index: condecimal(
        gt=0,
        le=10,
        max_digits=4,
        decimal_places=1,
    )  # pyright: ignore

    model_config = ConfigDict(extra="forbid")
