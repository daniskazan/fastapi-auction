from uuid import UUID
import datetime as dt
import decimal
from pydantic import Field

from core.common.serializers.base import PydanticBaseResponseModel
from core.auction.enums import CurrencyEnum


class AuctionItemContext(PydanticBaseResponseModel):
    image_url: str
    initial_price: decimal.Decimal = Field(default=decimal.Decimal(0.0))
    currency: CurrencyEnum = CurrencyEnum.USD


class AuctionStartContext(PydanticBaseResponseModel):
    user_id: UUID
    finish_at: dt.datetime
    title: str
    description: str
    auction_item: AuctionItemContext


class AuctionItemResponse(PydanticBaseResponseModel):
    item_id: UUID
    auction_id: UUID
    initial_price: decimal.Decimal
    current_price: decimal.Decimal
    currency: CurrencyEnum


class AuctionResponseSerializer(PydanticBaseResponseModel):
    auction_id: UUID
    user_id: UUID
    finish_at: dt.datetime
    title: str
    description: str
    auction_item: AuctionItemResponse
