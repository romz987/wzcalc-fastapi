from decimal import Decimal
from pydantic.dataclasses import dataclass

# dataclasses
from src.calc.core.domain import cm_calcdata


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


@dataclass(frozen=True)
class WbProfitParams:
    # tax system
    tax_system: str
    # cost row
    count: int
    cost_per_one: Decimal
    # comissions percentages
    comissions_percent: Decimal
    aquiring_percent: Decimal
    # tax & risk percentages
    tax_percent: Decimal
    risk_percent: Decimal
    # box and wage costs
    box_cost: Decimal
    wage_cost: Decimal
    # totals
    total_price: Decimal


@dataclass(frozen=True)
class WbBaseFees:
    cost_row: Decimal
    comission_fee: Decimal
    aquiring_fee: Decimal


@dataclass(frozen=True)
class WbLogFees:
    box_volume: Decimal
    logistics_fee: Decimal
    returns_fee: Decimal


@dataclass(frozen=True)
class WbProfitArgs:
    log_params: cm_calcdata.LogMainParams
    log_fees: WbLogFees
    return_params: cm_calcdata.ReturnsParams
    profit_params: WbProfitParams


@dataclass(frozen=True)
class WbProfitResult:
    base_fees: WbBaseFees
    tax_fee: Decimal
    risk_fee: Decimal
    total_profit: Decimal


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


@dataclass
class WbProfitResponse:
    # tax system
    tax_system: str
    # incomed main params
    local_index: Decimal
    box_size: str
    # incomed logistics params
    base_price: Decimal
    volume_factor: Decimal
    min_lim_1_price: Decimal
    min_lim_2_price: Decimal
    min_lim_3_price: Decimal
    min_lim_4_price: Decimal
    min_lim_5_price: Decimal
    # incomed profit params
    count: int
    cost_per_one: Decimal
    comissions_percent: Decimal
    aquiring_percent: Decimal
    tax_percent: Decimal
    risk_percent: Decimal
    box_cost: Decimal
    wage_cost: Decimal
    total_price: Decimal
    # calculated main param
    box_volume: Decimal
    # calculated logistics
    logistics_fee: Decimal
    # calculated returns
    returns_fee: Decimal
    # calculated marketplace fees
    comission_fee: Decimal
    aquiring_fee: Decimal
    # calculated tax and risk fees
    tax_fee: Decimal
    risk_fee: Decimal
    # calculated cost row and profit
    cost_row: Decimal
    total_profit: Decimal


#############################################################################
#                     Wildberries: Response dataclasses                     #
#############################################################################
#############################################################################
#                                  Price                                    #
#############################################################################
