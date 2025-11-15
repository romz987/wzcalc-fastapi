from decimal import Decimal
from pydantic.dataclasses import dataclass


#############################################################################
#                    Wildberries: Request dataclasses                       #
#############################################################################
#############################################################################
#                           Logistics and returns                           #
#############################################################################


@dataclass(frozen=True)
class WbLogCosts:
    base_price: Decimal
    volume_factor: Decimal
    min_lim_1_price: Decimal
    min_lim_2_price: Decimal
    min_lim_3_price: Decimal
    min_lim_4_price: Decimal
    min_lim_5_price: Decimal


#############################################################################
#                     Wildberries: Request dataclasses                      #
#############################################################################
#############################################################################
#                                  Profit                                   #
#############################################################################


#############################################################################
#                     Wildberries: Request dataclasses                      #
#############################################################################
#############################################################################
#                                  Price                                    #
#############################################################################


#############################################################################
#                    Wildberries: Response dataclasses                      #
#############################################################################
#############################################################################
#                           Logistics and returns                           #
#############################################################################


@dataclass
class WbLogResponse:
    box_size: str
    local_index: Decimal
    # logistics costs
    base_price: Decimal
    volume_factor: Decimal
    min_lim_1_price: Decimal
    min_lim_2_price: Decimal
    min_lim_3_price: Decimal
    min_lim_4_price: Decimal
    min_lim_5_price: Decimal
    # response data
    box_volume: Decimal
    logistics_fee: Decimal


@dataclass
class WbReturnsResponse:
    box_size: str
    local_index: Decimal
    # logistics costs
    base_price: Decimal
    volume_factor: Decimal
    min_lim_1_price: Decimal
    min_lim_2_price: Decimal
    min_lim_3_price: Decimal
    min_lim_4_price: Decimal
    min_lim_5_price: Decimal
    # nonredemption costs
    redemption_percentage: Decimal
    nonredemption_processing_cost: Decimal
    # response data
    box_volume: Decimal
    logistics_fee: Decimal
    returns_fee: Decimal


#############################################################################
#                     Wildberries: Response dataclasses                     #
#############################################################################
#############################################################################
#                                  Profit                                   #
#############################################################################


#############################################################################
#                     Wildberries: Response dataclasses                     #
#############################################################################
#############################################################################
#                                  Price                                    #
#############################################################################
