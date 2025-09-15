from decimal import Decimal
from pydantic.dataclasses import dataclass

# constrains
# from calc.core.domain import enums

# dataclasses
from calc.core.domain import cm_calcdata

#############################################################################
#                         Request dataclasses Ozon                          #
#############################################################################

########################## Logistics and Returns ############################


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


################################## Profit ###################################


@dataclass(frozen=True)
class OzProfitParams:
    # tax system
    tax_system: str  # TODO: must be the tax_system constraint
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
class OzProfitFbsArgs:
    log_params: cm_calcdata.LogMainParams
    log_costs: OzLogFbsCosts
    return_params: cm_calcdata.ReturnsParams
    profit_params: OzProfitParams


@dataclass(frozen=True)
class OzProfitFboArgs:
    log_params: cm_calcdata.LogMainParams
    log_costs_fbs: OzLogFbsCosts
    log_costs_fbo: OzLogFboCosts
    return_params: cm_calcdata.ReturnsParams
    profit_params: OzProfitParams


################################### Price ###################################


#############################################################################
#                        Response dataclasses Ozon                          #
#############################################################################

########################## Logistics and Returns ############################


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


################################## Profit ###################################


################################### Price ###################################


#############################################################################
#                   Intercommunicate dataclasses Ozon                       #
#############################################################################


################################## Profit ###################################


@dataclass(frozen=True)
class OzProfitFees:
    cost_row: Decimal
    last_mile_fee: Decimal
    comission_fee: Decimal
    aquiring_fee: Decimal


@dataclass(frozen=True)
class OzLogFees:
    logistics_fee: Decimal
    returns_fee: Decimal


################################### Price ###################################
