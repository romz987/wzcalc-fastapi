from decimal import Decimal
from pydantic.dataclasses import dataclass

#############################################################################
#                         Request dataclasses Ozon                          #
#############################################################################

########################## Logistics and Returns ############################


@dataclass(frozen=True)
class OzLogItemParams:
    local_index: Decimal
    box_volume: Decimal


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


@dataclass(frozen=True)
class OzReturnsParams:
    redemption_percentage: Decimal
    nonredemption_processing_cost: Decimal


################################## Profit ###################################


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


################################### Price ###################################
