from decimal import Decimal
from src.calc import schemas

# dataclasses
from src.calc.core.domain import oz_calcdata, cm_calcdata


#############################################################################
#                      Requests: Ozon interfaces utils                      #
#############################################################################
#############################################################################
#                                  Logistics                                #
#############################################################################


def request_fill_log_costs_fbs(
    payload: (
        schemas.OzonLogFbsPayload
        | schemas.OzonReturnsFbsPayload
        | schemas.OzonReturnsFboPayload
        | schemas.OzonProfitFbsPayload
        | schemas.OzonProfitFboPayload
    ),
) -> oz_calcdata.OzLogFbsCosts:
    """Create an instance of the core dataclass
    based on payload from HTTP request

    :param payload: An instance of pydantic model
    :return: An instance of OzLogFbsCosts dataclass
    """
    return oz_calcdata.OzLogFbsCosts(
        minimal_price_fbs=payload.minimal_price_fbs,
        base_price_fbs=payload.base_price_fbs,
        volume_factor_fbs=payload.volume_factor_fbs,
        fix_large_fbs=payload.fix_large_fbs,
    )


def request_fill_log_costs_fbo(
    payload: (
        schemas.OzonLogFboPayload
        | schemas.OzonReturnsFboPayload
        | schemas.OzonProfitFboPayload
    ),
) -> oz_calcdata.OzLogFboCosts:
    """Create an instance of the core dataclass
    based on payload from HTTP request

    :param payload: An instance of pydantic model
    :return: An instance of OzLogFboCosts dataclass
    """
    return oz_calcdata.OzLogFboCosts(
        base_price_fbo=payload.base_price_fbo,
        volume_factor_fbo=payload.volume_factor_fbo,
        fix_large_fbo=payload.fix_large_fbo,
    )


#############################################################################
#                      Requests: Ozon interfaces utils                      #
#############################################################################
#############################################################################
#                                  Profit                                   #
#############################################################################


def request_fill_profit_params(
    payload: schemas.OzonProfitFbsPayload | schemas.OzonProfitFboPayload,
) -> oz_calcdata.OzProfitParams:
    """Create an instance of the core dataclass
    based on payload from HTTP request

    :param payload: An instance of pydantic model
    :return: An instance of OzProfitParams dataclass
    """
    return oz_calcdata.OzProfitParams(
        # tax system
        tax_system=payload.tax_system,
        # cost row
        count=payload.count,
        cost_per_one=payload.cost_per_one,
        # last mile percentage
        last_mile_percent=payload.last_mile_percent,
        # comissions percentages
        comissions_percent=payload.comission_percent,
        aquiring_percent=payload.acquiring_percent,
        # tax & risk percentages
        tax_percent=payload.tax_percent,
        risk_percent=payload.risk_percent,
        # box and wage costs
        box_cost=payload.box_cost,
        wage_cost=payload.wage_cost,
        # ozon specific costs
        shipment_processing=payload.shipment_processing,
        # totals
        total_price=payload.total_price,
    )


def request_fill_profit_args(
    log_params: cm_calcdata.LogMainParams,
    log_fees: oz_calcdata.OzLogFees,
    return_params: cm_calcdata.ReturnsParams,
    profit_params: oz_calcdata.OzProfitParams,
) -> oz_calcdata.OzProfitArgs:
    """Create an instance of the core dataclass
    based on core dataclasses

    :param log_params: LogMainParams
    :param log_fees: OzLogFees
    :param return_params: ReturnsParams
    :param profit_params: OzProfitParams
    :return: An instance of OzProfitArgs dataclass
    """
    return oz_calcdata.OzProfitArgs(
        log_params=log_params,
        log_fees=log_fees,
        return_params=return_params,
        profit_params=profit_params,
    )


def request_fill_log_fees(
    box_volume: Decimal,
    logistics_fee: Decimal,
    reverse_logistics_fee: Decimal,
    returns_fee: Decimal,
) -> oz_calcdata.OzLogFees:
    """Create an instance of the core dataclass
    based on core dataclasses

    :param logistics_fee: Logistics fee value
    :param returns_fee: Return fee value
    :return: An instance of OzLogBase
    """
    return oz_calcdata.OzLogFees(
        box_volume=box_volume,
        logistics_fee=logistics_fee,
        reverse_logistics_fee=reverse_logistics_fee,
        returns_fee=returns_fee,
    )


#############################################################################
#                      Responses: Ozon interfaces utils                     #
#############################################################################
#############################################################################
#                           Logistics and returns                           #
#############################################################################


def response_fill_fbs_log_fee(
    payload: schemas.OzonLogFbsPayload,
    box_volume: Decimal,
    logistics_fee: Decimal,
) -> oz_calcdata.OzLogFbsResponse:
    """Create an instance of the core dataclass
    based on payload from HTTP request and calculations results

    :param payload: An instance of pydantic model
    :param box_volume: Package box volume based on box size
    :param logistics_fee: Calculated logistics fee value
    :return: An instance of OzLogFbsResponse dataclass
    """
    return oz_calcdata.OzLogFbsResponse(
        # base
        box_size=payload.box_size,
        local_index=payload.local_index,
        # base logistics costs
        minimal_price_fbs=payload.minimal_price_fbs,
        base_price_fbs=payload.base_price_fbs,
        volume_factor_fbs=payload.volume_factor_fbs,
        fix_large_fbs=payload.fix_large_fbs,
        # calculated
        box_volume=box_volume,
        logistics_fee=logistics_fee,
    )


def response_fill_fbo_log_fee(
    payload: schemas.OzonLogFboPayload,
    box_volume: Decimal,
    logistics_fee: Decimal,
) -> oz_calcdata.OzLogFboResponse:
    """Create an instance of the core dataclass
    based on payload from HTTP request and calculations results

    :param payload: An instance of pydantic model
    :param box_volume: Package box volume based on the box size
    :param logistics_fee: Calculated logistics fee value
    :return: An instance of OzLogFboResponse dataclass
    """
    return oz_calcdata.OzLogFboResponse(
        # base
        box_size=payload.box_size,
        local_index=payload.local_index,
        base_price_fbo=payload.base_price_fbo,
        volume_factor_fbo=payload.volume_factor_fbo,
        fix_large_fbo=payload.fix_large_fbo,
        # calculated
        box_volume=box_volume,
        logistics_fee=logistics_fee,
    )


def response_fill_fbs_returns_fee(
    payload: schemas.OzonReturnsFbsPayload,
    box_volume: Decimal,
    logistics_fee: Decimal,
    reverse_logistics_fee: Decimal,
    returns_fee: Decimal,
) -> oz_calcdata.OzReturnsFbsResponse:
    """Create an instance of the core dataclass
    based on payload from HTTP request and calculations results

    :param payload: An instance of pydantic model
    :param box_volume: Package box volume based on the box size
    :param logistics_fee: Calculated logistics fee value
    :param reverse_logistics_fee: Calculated reverse logistics fee value
    :param returns_fee: Calculated returns fee value
    :return: An instance of OzReturnsFbsResponse dataclass
    """
    return oz_calcdata.OzReturnsFbsResponse(
        # base
        box_size=payload.box_size,
        box_volume=box_volume,
        local_index=payload.local_index,
        # logistics constants
        minimal_price_fbs=payload.minimal_price_fbs,
        base_price_fbs=payload.base_price_fbs,
        volume_factor_fbs=payload.volume_factor_fbs,
        fix_large_fbs=payload.fix_large_fbs,
        # returns constants
        redemption_percentage=payload.redemption_percentage,
        nonredemption_processing_cost=payload.nonredemption_processing_cost,
        # calculated response data
        logistics_fee=logistics_fee,
        reverse_logistics_fee=reverse_logistics_fee,
        returns_fee=returns_fee,
    )


def response_fill_fbo_returns_fee(
    payload: schemas.OzonReturnsFboPayload,
    box_volume: Decimal,
    logistics_fee: Decimal,
    reverse_logistics_fee: Decimal,
    returns_fee: Decimal,
) -> oz_calcdata.OzReturnsFboResponse:
    """Create an instance of the core dataclass
    based on payload from HTTP request and calculations results

    :param payload: An instance of pydantic model
    :param box_volume: Package box volume based on the box size
    :param logistics_fee: Calculated logistics fee value
    :param reverse_logistics_fee: Calculated reverse logistics fee value
    :param returns_fee: Calculated returns fee value
    :return: An instance of OzReturnsFboResponse dataclass
    """
    return oz_calcdata.OzReturnsFboResponse(
        # base
        box_size=payload.box_size,
        box_volume=box_volume,
        local_index=payload.local_index,
        # fbs logistics constants
        minimal_price_fbs=payload.minimal_price_fbs,
        base_price_fbs=payload.base_price_fbs,
        volume_factor_fbs=payload.volume_factor_fbs,
        fix_large_fbs=payload.fix_large_fbs,
        # fbo logistics constants
        base_price_fbo=payload.base_price_fbo,
        volume_factor_fbo=payload.volume_factor_fbo,
        fix_large_fbo=payload.fix_large_fbo,
        # returns constants
        redemption_percentage=payload.redemption_percentage,
        nonredemption_processing_cost=payload.nonredemption_processing_cost,
        # calculated response data
        logistics_fee=logistics_fee,
        reverse_logistics_fee=reverse_logistics_fee,
        returns_fee=returns_fee,
    )


#############################################################################
#                      Responses: Ozon interfaces utils                     #
#############################################################################
#############################################################################
#                                  Profit                                   #
#############################################################################


def response_fill_fbs_profit_fee(
    payload: schemas.OzonProfitFbsPayload,
    log_fees: oz_calcdata.OzLogFees,
    results: oz_calcdata.OzProfitResult,
) -> oz_calcdata.OzProfitFbsResponse:
    """Create an instance of the core dataclass
    based on payload from HTTP request and calculations results

    :param payload: An instance of pydantic model
    :param log_fees: An instance of OzLogFees dataclass
    :param results: An instance of OzProfitResult dalaclass
    :return: An instance of OzProfitFbsResponse dataclass
    """
    return oz_calcdata.OzProfitFbsResponse(
        # tax system
        tax_system=payload.tax_system,
        # incomed main params
        local_index=payload.local_index,
        box_size=payload.box_size,
        # incomed logistics params
        minimal_price_fbs=payload.minimal_price_fbs,
        base_price_fbs=payload.base_price_fbs,
        volume_factor_fbs=payload.volume_factor_fbs,
        fix_large_fbs=payload.fix_large_fbs,
        # incomed profit params
        count=payload.count,
        cost_per_one=payload.cost_per_one,
        last_mile_percent=payload.last_mile_percent,
        comissions_percent=payload.comission_percent,
        aquiring_percent=payload.acquiring_percent,
        tax_percent=payload.tax_percent,
        risk_percent=payload.risk_percent,
        box_cost=payload.box_cost,
        wage_cost=payload.wage_cost,
        shipment_processing=payload.shipment_processing,
        total_price=payload.total_price,
        # calculated main param
        box_volume=log_fees.box_volume,
        # calculated logistics
        logistics_fee=log_fees.logistics_fee,
        # calculated returns
        reverse_logistics_fee=log_fees.reverse_logistics_fee,
        returns_fee=log_fees.returns_fee,
        # calculated marketplce fees
        comission_fee=results.base_fees.comission_fee,
        aquiring_fee=results.base_fees.aquiring_fee,
        last_mile_fee=results.base_fees.last_mile_fee,
        # calculated tax and risk fees
        tax_fee=results.tax_fee,
        risk_fee=results.risk_fee,
        # calculated cost row and profit
        cost_row=results.base_fees.cost_row,
        total_profit=results.total_profit,
    )


def response_fill_fbo_profit_fee(
    payload: schemas.OzonProfitFboPayload,
    log_fees: oz_calcdata.OzLogFees,
    results: oz_calcdata.OzProfitResult,
) -> oz_calcdata.OzProfitFboResponse:
    """Create an instance of the core dataclass
    based on payload from HTTP request and calculations results

    :param payload: An instance of pydantic model
    :param log_fees: An instance of OzLogFees dataclass
    :param results: An instance of OzProfitResult dalaclass
    :return: An instance of OzProfitFboResponse dataclass
    """
    return oz_calcdata.OzProfitFboResponse(
        # tax system
        tax_system=payload.tax_system,
        # incomed main params
        local_index=payload.local_index,
        box_size=payload.box_size,
        # incomed logistics fbs params
        minimal_price_fbs=payload.minimal_price_fbs,
        base_price_fbs=payload.base_price_fbs,
        volume_factor_fbs=payload.volume_factor_fbs,
        fix_large_fbs=payload.fix_large_fbs,
        # incomed logistics fbo params
        base_price_fbo=payload.base_price_fbo,
        volume_factor_fbo=payload.volume_factor_fbo,
        fix_large_fbo=payload.fix_large_fbo,
        # incomed profit params
        count=payload.count,
        cost_per_one=payload.cost_per_one,
        last_mile_percent=payload.last_mile_percent,
        comissions_percent=payload.comission_percent,
        aquiring_percent=payload.acquiring_percent,
        tax_percent=payload.tax_percent,
        risk_percent=payload.risk_percent,
        box_cost=payload.box_cost,
        wage_cost=payload.wage_cost,
        shipment_processing=payload.shipment_processing,
        total_price=payload.total_price,
        # calculated main param
        box_volume=log_fees.box_volume,
        # calculated logistics
        logistics_fee=log_fees.logistics_fee,
        # calculated returns
        reverse_logistics_fee=log_fees.reverse_logistics_fee,
        returns_fee=log_fees.returns_fee,
        # calculated marketplce fees
        comission_fee=results.base_fees.comission_fee,
        aquiring_fee=results.base_fees.aquiring_fee,
        last_mile_fee=results.base_fees.last_mile_fee,
        # calculated tax and risk fees
        tax_fee=results.tax_fee,
        risk_fee=results.risk_fee,
        # calculated cost row and profit
        cost_row=results.base_fees.cost_row,
        total_profit=results.total_profit,
    )
