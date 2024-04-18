from enum import Enum
from datetime import datetime

from pydantic import BaseModel, PrivateAttr, Field


class ScratchTicketState(str, Enum):
    OPEN = 'open'
    PLAYED = 'played'

    def __str__(self):
        return self.value


class ScratchTicketPrize(str, Enum):
    GIFT = 'gift'
    LOYALTY_POINTS = 'loyaltyPoints'

    def __str__(self):
        return self.value


class ScratchTicketDisclaimer(BaseModel):
    title: str
    text: str


class ScratchTicketDetails(BaseModel):
    image: str
    title: str
    text: str
    disclaimer: ScratchTicketDisclaimer


class ScratchTicket(BaseModel):
    id: str
    imageUrl: str
    title: str
    validFrom: datetime
    validTo: datetime
    state: ScratchTicketState
    prize: ScratchTicketPrize = Field(..., alias="prize", exclude=True)
    details: ScratchTicketDetails = Field(..., alias="details", exclude=True)


class PostPlayScratchTicket(BaseModel):
    id: str


class GetPlayScratchTicket(BaseModel):
    image: str
    prize: ScratchTicketPrize
