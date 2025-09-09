from enum import Enum
from typing import Annotated
from pydantic import Field

BoxSize = Annotated[str, Field(pattern=r"^\d{1,3}\*\d{1,3}\*\d{1,3}$")]


class LogOptionEnum(Enum):
    FBS = "fbs"
    FBO = "fbo"


class TaxSystemEnum(Enum):
    SIMPLE = "simple"
    DIFFERENCE = "difference"
