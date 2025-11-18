from decimal import Decimal
from src.calc import schemas

# dataclasses
from src.calc.core.domain import wb_calcdata, cm_calcdata


#############################################################################
#                 Requests: Wildberries interfaces utils                    #
#############################################################################
#############################################################################
#                                  Logistics                                #
#############################################################################


def request_fill_log_costs(
    payload: schemas.WbLogPayload | schemas.WbReturnsPayload,
) -> wb_calcdata.WbLogCosts:
    """Create an instance of the core dataclass
    based on payload from HTTP request

    :param payload: An instance of pydantic model
    :return: An instance of WbLogCosts dataclass
    """
    return wb_calcdata.WbLogCosts(
        base_price=payload.base_price,
        volume_factor=payload.volume_factor,
        min_lim_1_price=payload.min_lim_1_price,
        min_lim_2_price=payload.min_lim_2_price,
        min_lim_3_price=payload.min_lim_3_price,
        min_lim_4_price=payload.min_lim_4_price,
        min_lim_5_price=payload.min_lim_5_price,
    )


#############################################################################
#                 Requests: Wildberries interfaces utils                    #
#############################################################################
#############################################################################
#                                  Profit                                   #
#############################################################################


def request_fill_log_fees(
    box_volume: Decimal,
    logistics_fee: Decimal,
    returns_fee: Decimal,
) -> wb_calcdata.WbLogFees:
    """Create an instance of the core dataclass
    based on core dataclasses

    :param logistics_fee: Logistics fee value
    :param returns_fee: Return fee value
    :return: An instance of WbLogBase
    """
    return wb_calcdata.WbLogFees(
        box_volume=box_volume,
        logistics_fee=logistics_fee,
        returns_fee=returns_fee,
    )


def request_fill_profit_params(
    payload: schemas.WbProfitPayload,
) -> wb_calcdata.WbProfitParams:
    """Create an instance of the core dataclass
    based on payload from HTTP request

    :param payload: An instance of pydantic model
    :return: An instance of WbProfitParams dataclass
    """
    return wb_calcdata.WbProfitParams(
        # tax system
        tax_system=payload.tax_system,
        # cost row
        count=payload.count,
        cost_per_one=payload.cost_per_one,
        # comissions percentages
        comissions_percent=payload.comission_percent,
        aquiring_percent=payload.acquiring_percent,
        # tax & risk percentages
        tax_percent=payload.tax_percent,
        risk_percent=payload.risk_percent,
        # box and wage costs
        box_cost=payload.box_cost,
        wage_cost=payload.wage_cost,
        # totals
        total_price=payload.total_price,
    )


def request_fill_profit_args(
    log_params: cm_calcdata.LogMainParams,
    log_fees: wb_calcdata.WbLogFees,
    return_params: cm_calcdata.ReturnsParams,
    profit_params: wb_calcdata.WbProfitParams,
) -> wb_calcdata.WbProfitArgs:
    """Create an instance of the core dataclass
    based on core dataclasses

    :param log_params: LogMainParams
    :param log_fees: WbLogFees
    :param return_params: ReturnsParams
    :param profit_params: WbProfitParams
    :return: An instance of WbProfitArgs dataclass
    """
    return wb_calcdata.WbProfitArgs(
        log_params=log_params,
        log_fees=log_fees,
        return_params=return_params,
        profit_params=profit_params,
    )


#############################################################################
#                 Responses: Wildberries interfaces utils                   #
#############################################################################
#############################################################################
#                           Logistics and returns                           #
#############################################################################


def response_fill_log_fee(
    payload: schemas.WbLogPayload,
    box_volume: Decimal,
    logistics_fee: Decimal,
) -> wb_calcdata.WbLogResponse:
    """Create an instance of the core dataclass
    based on payload from HTTP request and calculations results

    :param payload: An instance of pydantic model
    :param box_volume: Package box volume based on box size
    :param logistics_fee: Calculated logistics fee value
    :return: An instance of WbLogResponse dataclass
    """
    return wb_calcdata.WbLogResponse(
        # base
        box_size=payload.box_size,
        local_index=payload.local_index,
        # base logistics costs
        base_price=payload.base_price,
        volume_factor=payload.volume_factor,
        min_lim_1_price=payload.min_lim_1_price,
        min_lim_2_price=payload.min_lim_2_price,
        min_lim_3_price=payload.min_lim_3_price,
        min_lim_4_price=payload.min_lim_4_price,
        min_lim_5_price=payload.min_lim_5_price,
        # calculated
        box_volume=box_volume,
        logistics_fee=logistics_fee,
    )


def response_fill_returns_fee(
    payload: schemas.WbReturnsPayload,
    box_volume: Decimal,
    logistics_fee: Decimal,
    returns_fee: Decimal,
) -> wb_calcdata.WbReturnsResponse:
    """Create an instance of the core dataclass
    based on payload from HTTP request and calculations results

    :param payload: An instance of pydantic model
    :param box_volume: Package box volume based on the box size
    :param logistics_fee: Calculated logistics fee value
    :param returns_fee: Calculated returns fee value
    :return: An instance of WbReturnsResponse dataclass
    """
    return wb_calcdata.WbReturnsResponse(
        # base
        box_size=payload.box_size,
        local_index=payload.local_index,
        # logistics constants
        base_price=payload.base_price,
        volume_factor=payload.volume_factor,
        min_lim_1_price=payload.min_lim_1_price,
        min_lim_2_price=payload.min_lim_2_price,
        min_lim_3_price=payload.min_lim_3_price,
        min_lim_4_price=payload.min_lim_4_price,
        min_lim_5_price=payload.min_lim_5_price,
        # returns constants
        redemption_percentage=payload.redemption_percentage,
        nonredemption_processing_cost=payload.nonredemption_processing_cost,
        # calculated response data
        box_volume=box_volume,
        logistics_fee=logistics_fee,
        returns_fee=returns_fee,
    )


#############################################################################
#                Responses: Wildberries interfaces utils                    #
#############################################################################
#############################################################################
#                                  Profit                                   #
#############################################################################


def response_fill_profit_fee(
    payload: schemas.WbProfitPayload,
    log_fees: wb_calcdata.WbLogFees,
    results: wb_calcdata.WbProfitResult,
) -> wb_calcdata.WbProfitResponse:
    """Create an instance of the core dataclass
    based on payload from HTTP request and calculations results

    :param payload: An instance of pydantic model
    :param log_fees: An instance of WbLogFees dataclass
    :param results: An instance of WbProfitResult dalaclass
    :return: An instance of WbProfitFbsResponse dataclass
    """
    return wb_calcdata.WbProfitResponse(
        # tax system
        tax_system=payload.tax_system,
        # incomed main params
        local_index=payload.local_index,
        box_size=payload.box_size,
        # incomed logistics params
        base_price=payload.base_price,
        volume_factor=payload.volume_factor,
        min_lim_1_price=payload.min_lim_1_price,
        min_lim_2_price=payload.min_lim_2_price,
        min_lim_3_price=payload.min_lim_3_price,
        min_lim_4_price=payload.min_lim_4_price,
        min_lim_5_price=payload.min_lim_5_price,
        # incomed profit params
        count=payload.count,
        cost_per_one=payload.cost_per_one,
        comissions_percent=payload.comission_percent,
        aquiring_percent=payload.acquiring_percent,
        tax_percent=payload.tax_percent,
        risk_percent=payload.risk_percent,
        box_cost=payload.box_cost,
        wage_cost=payload.wage_cost,
        total_price=payload.total_price,
        # calculated main param
        box_volume=log_fees.box_volume,
        # calculated logistics
        logistics_fee=log_fees.logistics_fee,
        # calculated returns
        returns_fee=log_fees.returns_fee,
        # calculated marketplce fees
        comission_fee=results.base_fees.comission_fee,
        aquiring_fee=results.base_fees.aquiring_fee,
        # calculated tax and risk fees
        tax_fee=results.tax_fee,
        risk_fee=results.risk_fee,
        # calculated cost row and profit
        cost_row=results.base_fees.cost_row,
        total_profit=results.total_profit,
    )
