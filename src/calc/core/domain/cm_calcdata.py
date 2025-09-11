from decimal import Decimal
from pydantic.dataclasses import dataclass

#############################################################################
#                       Request dataclasses Common                          #
#############################################################################

########################## Logistics and Returns ############################


@dataclass(frozen=True)
class LogMainParams:
    local_index: Decimal
    box_volume: Decimal


@dataclass(frozen=True)
class ReturnsParams:
    redemption_percentage: Decimal
    nonredemption_processing_cost: Decimal
