from pydantic.dataclasses import dataclass
from decimal import Decimal


@dataclass
class LogWbData:
    box_size: str
    local_index: Decimal
    base_price: Decimal
    volume_factor: Decimal
    # flowing
    box_volume: Decimal | None = None
    logistics_fee: Decimal | None = None


@dataclass
class ReturnsWbData:
    box_size: str
    redemption_percentage: Decimal
    nonredemption_processing_cost: Decimal
    local_index: Decimal
    # logistics costs
    base_price: Decimal
    volume_factor: Decimal
    # flowing
    box_volume: Decimal | None = None
    logistics_fee: Decimal | None = None
    returns_fee: Decimal | None = None


#
#
# @dataclass
# class ReturnsFboData:
#     box_size: str
#     redemption_percentage: Decimal
#     nonredemption_processing_cost: Decimal
#     local_index: Decimal
#     # logistics costs
#     minimal_price_fbs: Decimal
#     base_price_fbs: Decimal
#     volume_factor_fbs: Decimal
#     fix_large_fbs: Decimal
#     base_price_fbo: Decimal
#     volume_factor_fbo: Decimal
#     fix_large_fbo: Decimal
#     # flowing
#     box_volume: Decimal | None = None
#     logistics_fee: Decimal | None = None
#     reverse_logistics_fee: Decimal | None = None
#     returns_fee: Decimal | None = None
