from dataclasses import dataclass
from decimal import Decimal


@dataclass
class LogFbsData:
    local_index: Decimal
    box_volume: Decimal
    minimal_price_fbs: Decimal
    base_price_fbs: Decimal
    volume_factor_fbs: Decimal
    fix_large_fbs: Decimal


@dataclass
class LogFboData:
    local_index: Decimal
    box_volume: Decimal
    base_price_fbo: Decimal
    volume_factor_fbo: Decimal
    fix_large_fbo: Decimal


@dataclass
class ReturnsData:
    box_size: str
    redemption_percentage: Decimal
    nonredemption_processing_cost: Decimal
    local_index: Decimal
    # logistics costs
    minimal_price_fbs: Decimal
    base_price_fbs: Decimal
    volume_factor_fbs: Decimal
    fix_large_fbs: Decimal
    base_price_fbo: Decimal | None = None
    volume_factor_fbo: Decimal | None = None
    fix_large_fbo: Decimal | None = None
    # flowing
    box_volume: Decimal | None = None
    logistics_fee: Decimal | None = None
    reverse_logistics_fee: Decimal | None = None
