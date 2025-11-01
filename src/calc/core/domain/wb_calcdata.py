from decimal import Decimal
from pydantic.dataclasses import dataclass

#############################################################################
#                      Request dataclasses Wildberries                      #
#############################################################################


########################## Logistics and Returns ############################


@dataclass(frozen=True)
class WbLogCosts:
    base_price: Decimal
    volume_factor: Decimal
    min_lim_1_price: Decimal
    min_lim_2_price: Decimal
    min_lim_3_price: Decimal
    min_lim_4_price: Decimal
    min_lim_5_price: Decimal


################################## Profit ###################################


################################### Price ###################################


#############################################################################
#                      Response dataclasses Wildberries                     #
#############################################################################

########################## Logistics and Returns ############################


@dataclass
class WbLogResponse:
    box_size: str
    box_volume: Decimal
    local_index: Decimal
    base_price: Decimal
    volume_factor: Decimal
    logistics_fee: Decimal


@dataclass
class WbReturnsResponse:
    box_size: str
    box_volume: Decimal
    local_index: Decimal
    # logistics constants
    base_price: Decimal
    volume_factor: Decimal
    # returns constants
    redemption_percentage: Decimal
    nonredemption_processing_cost: Decimal
    # new response data
    logistics_fee: Decimal
    returns_fee: Decimal


################################## Profit ###################################


################################### Price ###################################
