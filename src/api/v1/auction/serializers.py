from uuid import UUID
import datetime as dt
import decimal
from pydantic import BaseModel, Field

from core.auction.enums import CurrencyEnum


class AuctionItemContext(BaseModel):
    image_url: str
    starting_price: decimal.Decimal = Field(default=decimal.Decimal(0.0))
    currency: CurrencyEnum = CurrencyEnum.USD


class AuctionStartContext(BaseModel):
    user_id: UUID
    finish_at: dt.datetime
    title: str
    description: str
    auction_item: AuctionItemContext
