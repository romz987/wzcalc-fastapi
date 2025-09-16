import math
from decimal import Decimal


def box_volume_clc(box_size: str) -> Decimal:
    """Calculate the box volume in liters from its dimensions.

    :param box_size: Dimensions of the box in cm, e.g. 15*10*10
    :return: The volume of the box in liters
    """
    factors = map(int, box_size.split("*"))
    result = math.prod(list(factors)) / 1000
    return Decimal(result)


def comissions_fee_clc(comission_percent: Decimal, value: Decimal) -> Decimal:
    """Comission fee calculator
    based on:
      - comission percentage
      - total value

    :param comission_percent: The percenatge of comission
    :param value: The total value on which the comission is calculated
    :return: The calculated comission fee as a Decimal
    """
    return value * (comission_percent / 100)
