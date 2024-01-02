import decimal
import uuid
import datetime as dt

from core.auction.domain import Auction, AuctionItem
from core.auction.enums import AuctionStatusEnum, CurrencyEnum
from core.common.models.base import BaseORMModel

from sqlalchemy import orm


class AuctionORM(BaseORMModel):
    __tablename__ = "auction"

    user_id: orm.Mapped[uuid.UUID]
    finish_at: orm.Mapped[dt.datetime]
    title: orm.Mapped[str]
    description: orm.Mapped[str]
    auction_status: orm.Mapped[AuctionStatusEnum]

    @classmethod
    def build_from_domain(cls, auction: Auction):
        return cls(
            id=auction.id,
            user_id=auction.user_id,
            finish_at=auction.finish_at,
            title=auction.title,
            description=auction.description,
            auction_status=auction.auction_status
        )


class AuctionItemORM(BaseORMModel):
    auction_id: orm.Mapped[uuid.UUID]
    image_url: orm.Mapped[str | None] = orm.mapped_column(default=None)
    starting_price: orm.Mapped[decimal.Decimal]
    current_price: orm.Mapped[decimal.Decimal]
    currency: orm.Mapped[CurrencyEnum]

    @classmethod
    def build_from_domain(cls, *, auction_item: AuctionItem):
        return cls(
            id=auction_item.item_id,
            auction_id=auction_item.auction_id,
            image_url=auction_item.image_url,
            starting_price=auction_item.starting_price,
            current_price=auction_item.current_price,
            currency=auction_item.currency

        )