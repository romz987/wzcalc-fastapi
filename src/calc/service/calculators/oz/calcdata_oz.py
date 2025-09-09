from pydantic.dataclasses import dataclass
from decimal import Decimal


# TODO: RENAME ALL! ADD OZ!
@dataclass
class LogFbsData:
    local_index: Decimal
    box_size: str
    minimal_price_fbs: Decimal
    base_price_fbs: Decimal
    volume_factor_fbs: Decimal
    fix_large_fbs: Decimal
    # flowing
    box_volume: Decimal | None = None
    logistics_fee: Decimal | None = None


@dataclass
class LogFboData:
    local_index: Decimal
    box_size: str
    base_price_fbo: Decimal
    volume_factor_fbo: Decimal
    fix_large_fbo: Decimal
    # flowing
    box_volume: Decimal | None = None
    logistics_fee: Decimal | None = None


@dataclass
class ReturnsFbsData:
    box_size: str
    redemption_percentage: Decimal
    nonredemption_processing_cost: Decimal
    local_index: Decimal
    # logistics costs
    minimal_price_fbs: Decimal
    base_price_fbs: Decimal
    volume_factor_fbs: Decimal
    fix_large_fbs: Decimal
    # flowing
    box_volume: Decimal | None = None
    logistics_fee: Decimal | None = None
    reverse_logistics_fee: Decimal | None = None
    returns_fee: Decimal | None = None


@dataclass
class ReturnsFboData:
    box_size: str
    redemption_percentage: Decimal
    nonredemption_processing_cost: Decimal
    local_index: Decimal
    # logistics costs
    minimal_price_fbs: Decimal
    base_price_fbs: Decimal
    volume_factor_fbs: Decimal
    fix_large_fbs: Decimal
    base_price_fbo: Decimal
    volume_factor_fbo: Decimal
    fix_large_fbo: Decimal
    # flowing
    box_volume: Decimal | None = None
    logistics_fee: Decimal | None = None
    reverse_logistics_fee: Decimal | None = None
    returns_fee: Decimal | None = None


@dataclass
class ProfitOzFbsData:
    # base
    comission_percent: Decimal
    acquiring_percent: Decimal
    local_index: Decimal
    tax_percent: Decimal
    risk_percent: Decimal
    redemption_percentage: Decimal
    cost_per_one: Decimal
    count: int
    wage_cost: Decimal
    box_cost: Decimal
    box_size: str
    # specific
    total_price: Decimal
    shipment_processing: Decimal
    nonredemption_processing_cost: Decimal
    last_mile_percent: Decimal
    # fbs fbo specific
    minimal_price_fbs: Decimal
    base_price_fbs: Decimal
    volume_factor_fbs: Decimal
    fix_large_fbs: Decimal
    # flowing
    cost_row: Decimal | None = None
    box_volume: Decimal | None = None
    logistics_fee: Decimal | None = None
    reverse_logistics_fee: Decimal | None = None
    nonredemptions_fee: Decimal | None = None
    last_mile_fee: Decimal | None = None
    marketplace_comission_fee: Decimal | None = None
    aquiring_fee: Decimal | None = None
    tax_fee: Decimal | None = None
    risk_fee: Decimal | None = None
    profit: Decimal | None = None


@dataclass
class ProfitOzFboData:
    # base
    comission_percent: Decimal
    acquiring_percent: Decimal
    local_index: Decimal
    tax_percent: Decimal
    risk_percent: Decimal
    redemption_percentage: Decimal
    cost_per_one: Decimal
    count: int
    wage_cost: Decimal
    box_cost: Decimal
    box_size: str
    # specific
    total_price: Decimal
    shipment_processing: Decimal
    nonredemption_processing_cost: Decimal
    last_mile_percent: Decimal
    # fbs fbo specific
    minimal_price_fbs: Decimal
    base_price_fbs: Decimal
    volume_factor_fbs: Decimal
    fix_large_fbs: Decimal
    base_price_fbo: Decimal
    volume_factor_fbo: Decimal
    fix_large_fbo: Decimal
    # flowing
    cost_row: Decimal | None = None
    box_volume: Decimal | None = None
    logistics_fee: Decimal | None = None
    reverse_logistics_fee: Decimal | None = None
    nonredemptions_fee: Decimal | None = None
    last_mile_fee: Decimal | None = None
    marketplace_comission_fee: Decimal | None = None
    aquiring_fee: Decimal | None = None
    tax_fee: Decimal | None = None
    risk_fee: Decimal | None = None
    profit: Decimal | None = None
