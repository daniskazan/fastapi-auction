import uuid
import decimal
import datetime as dt

from core.auction.enums import AuctionStatusEnum
from core.auction.enums import CurrencyEnum


class AuctionItem:
    def __init__(
            self,
            *,
            item_id: uuid.UUID,
            auction_id: uuid.UUID,
            image_url: str | None = None,
            starting_price: decimal.Decimal = decimal.Decimal(0.0),
            currency: CurrencyEnum = CurrencyEnum.USD,
    ):
        self.item_id = item_id
        self.auction_id = auction_id
        self.starting_price = starting_price
        self.current_price = starting_price
        self.currency = currency
        self.image_url = image_url


class Auction:
    def __init__(
            self,
            *,
            auction_id: uuid.UUID,
            user_id: uuid.UUID,
            finish_at: dt.datetime,
            title: str,
            description: str,
            auction_status: AuctionStatusEnum = AuctionStatusEnum.ACTIVE,
    ):
        self.id = auction_id
        self.user_id = user_id
        self.finish_at = finish_at
        self.title = title,
        self.description = description
        self.auction_status = auction_status

    def add_item(self, *, item: AuctionItem) -> None:
        item.auction_id = self.id
