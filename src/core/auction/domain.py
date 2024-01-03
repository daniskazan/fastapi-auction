from dataclasses import dataclass
import uuid
import decimal
import datetime as dt

from core.auction.enums import AuctionStatusEnum
from core.auction.enums import CurrencyEnum


@dataclass(kw_only=True)
class AuctionItem:
    item_id: uuid.UUID
    auction_id: uuid.UUID
    image_url: str | None = None
    starting_price: decimal.Decimal = decimal.Decimal(0.0)
    currency: CurrencyEnum = CurrencyEnum.USD


@dataclass(kw_only=True)
class Auction:
    auction_id: uuid.UUID
    user_id: uuid.UUID
    finish_at: dt.datetime
    title: str
    description: str
    auction_status: AuctionStatusEnum = AuctionStatusEnum.ACTIVE
