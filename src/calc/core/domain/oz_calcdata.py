from decimal import Decimal
from pydantic.dataclasses import dataclass

# constrains
from src.calc.core.domain import enums

# dataclasses
from src.calc.core.domain import cm_calcdata


#############################################################################
#                        Ozon: Request dataclasses                          #
#############################################################################
#############################################################################
#                           Logistics and returns                           #
#############################################################################


@dataclass(frozen=True)
class OzLogFbsCosts:
    minimal_price_fbs: Decimal
    base_price_fbs: Decimal
    volume_factor_fbs: Decimal
    fix_large_fbs: Decimal


@dataclass(frozen=True)
class OzLogFboCosts:
    base_price_fbo: Decimal
    volume_factor_fbo: Decimal
    fix_large_fbo: Decimal


#############################################################################
#                        Ozon: Request dataclasses                          #
#############################################################################
#############################################################################
#                                  Profit                                   #
#############################################################################


@dataclass(frozen=True)
class OzProfitParams:
    # tax system
    tax_system: enums.TaxSystemEnum
    # cost row
    count: int
    cost_per_one: Decimal
    # last mile percantage
    last_mile_percent: Decimal
    # comissions percentages
    comissions_percent: Decimal
    aquiring_percent: Decimal
    # tax & risk percentages
    tax_percent: Decimal
    risk_percent: Decimal
    # box and wage costs
    box_cost: Decimal
    wage_cost: Decimal
    # ozon specific costs
    shipment_processing: Decimal
    # totals
    total_price: Decimal


@dataclass(frozen=True)
class OzBaseFees:
    cost_row: Decimal
    last_mile_fee: Decimal
    comission_fee: Decimal
    aquiring_fee: Decimal


@dataclass(frozen=True)
class OzLogFees:
    box_volume: Decimal
    logistics_fee: Decimal
    reverse_logistics_fee: Decimal
    returns_fee: Decimal


@dataclass(frozen=True)
class OzProfitArgs:
    log_params: cm_calcdata.LogMainParams
    log_fees: OzLogFees
    return_params: cm_calcdata.ReturnsParams
    profit_params: OzProfitParams


@dataclass(frozen=True)
class OzProfitResult:
    base_fees: OzBaseFees
    tax_fee: Decimal
    risk_fee: Decimal
    total_profit: Decimal


#############################################################################
#                        Ozon: Response dataclasses                         #
#############################################################################
#############################################################################
#                           Logistics and returns                           #
#############################################################################


@dataclass
class OzLogFbsResponse:
    box_size: str
    box_volume: Decimal
    local_index: Decimal
    minimal_price_fbs: Decimal
    base_price_fbs: Decimal
    volume_factor_fbs: Decimal
    fix_large_fbs: Decimal
    logistics_fee: Decimal


@dataclass
class OzLogFboResponse:
    box_size: str
    box_volume: Decimal
    local_index: Decimal
    base_price_fbo: Decimal
    volume_factor_fbo: Decimal
    fix_large_fbo: Decimal
    logistics_fee: Decimal


@dataclass
class OzReturnsFbsResponse:
    box_size: str
    box_volume: Decimal
    local_index: Decimal
    # logistics constants
    minimal_price_fbs: Decimal
    base_price_fbs: Decimal
    volume_factor_fbs: Decimal
    fix_large_fbs: Decimal
    # returns constants
    redemption_percentage: Decimal
    nonredemption_processing_cost: Decimal
    # new response data
    logistics_fee: Decimal
    reverse_logistics_fee: Decimal
    returns_fee: Decimal


@dataclass
class OzReturnsFboResponse:
    box_size: str
    box_volume: Decimal
    local_index: Decimal
    # logistics constants fbs
    minimal_price_fbs: Decimal
    base_price_fbs: Decimal
    volume_factor_fbs: Decimal
    fix_large_fbs: Decimal
    # logistics constants fbo
    base_price_fbo: Decimal
    volume_factor_fbo: Decimal
    fix_large_fbo: Decimal
    # returns constants
    redemption_percentage: Decimal
    nonredemption_processing_cost: Decimal
    # new response data
    logistics_fee: Decimal
    reverse_logistics_fee: Decimal
    returns_fee: Decimal


#############################################################################
#                        Ozon: Response dataclasses                         #
#############################################################################
#############################################################################
#                                  Profit                                   #
#############################################################################


@dataclass
class OzProfitFbsResponse:
    # tax system
    tax_system: enums.TaxSystemEnum
    # incomed main params
    local_index: Decimal
    box_size: str
    # incomed logistics params
    minimal_price_fbs: Decimal
    base_price_fbs: Decimal
    volume_factor_fbs: Decimal
    fix_large_fbs: Decimal
    # incomed profit params
    count: int
    cost_per_one: Decimal
    last_mile_percent: Decimal
    comissions_percent: Decimal
    aquiring_percent: Decimal
    tax_percent: Decimal
    risk_percent: Decimal
    box_cost: Decimal
    wage_cost: Decimal
    shipment_processing: Decimal
    total_price: Decimal
    # calculated main param
    box_volume: Decimal
    # calculated logistics
    logistics_fee: Decimal
    # calculated returns
    reverse_logistics_fee: Decimal
    returns_fee: Decimal
    # calculated marketplace fees
    comission_fee: Decimal
    aquiring_fee: Decimal
    last_mile_fee: Decimal
    # calculated tax and risk fees
    tax_fee: Decimal
    risk_fee: Decimal
    # calculated cost row and profit
    cost_row: Decimal
    total_profit: Decimal


@dataclass
class OzProfitFboResponse:
    # tax system
    tax_system: enums.TaxSystemEnum
    # incomed main params
    local_index: Decimal
    box_size: str
    # incomed logistics params fbs
    minimal_price_fbs: Decimal
    base_price_fbs: Decimal
    volume_factor_fbs: Decimal
    fix_large_fbs: Decimal
    # incomed logistics params fbo
    base_price_fbo: Decimal
    volume_factor_fbo: Decimal
    fix_large_fbo: Decimal
    # incomed profit params
    count: int
    cost_per_one: Decimal
    last_mile_percent: Decimal
    comissions_percent: Decimal
    aquiring_percent: Decimal
    tax_percent: Decimal
    risk_percent: Decimal
    box_cost: Decimal
    wage_cost: Decimal
    shipment_processing: Decimal
    total_price: Decimal
    # calculated main param
    box_volume: Decimal
    # calculated logistics
    logistics_fee: Decimal
    # calculated returns
    reverse_logistics_fee: Decimal
    returns_fee: Decimal
    # calculated profit fees
    cost_row: Decimal
    comission_fee: Decimal
    aquiring_fee: Decimal
    last_mile_fee: Decimal
    # tax, risk and profit
    tax_fee: Decimal
    risk_fee: Decimal
    total_profit: Decimal
