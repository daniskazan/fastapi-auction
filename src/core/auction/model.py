import decimal
import uuid
import datetime as dt

from core.auction.domain import Auction, AuctionItem
from core.auction.enums import AuctionStatusEnum, CurrencyEnum
from core.common.models.base import BaseORMModel
from sqlalchemy import orm
from sqlalchemy import schema


class AuctionItemORM(BaseORMModel):
    __tablename__ = "auction_item"
    auction_id: orm.Mapped[uuid.UUID] = orm.mapped_column(schema.ForeignKey(column="auction.id"), unique=True)
    image_url: orm.Mapped[str | None] = orm.mapped_column(default=None)
    starting_price: orm.Mapped[decimal.Decimal]
    current_price: orm.Mapped[decimal.Decimal]
    currency: orm.Mapped[CurrencyEnum]

    auction: orm.Mapped["AuctionORM"] = orm.relationship(back_populates="auction_item")

    @classmethod
    def build_from_domain(cls, *, auction_item: AuctionItem):
        return cls(
            id=auction_item.item_id,
            auction_id=auction_item.auction_id,
            image_url=auction_item.image_url,
            starting_price=auction_item.starting_price,
            current_price=auction_item.starting_price,
            currency=auction_item.currency
        )


class AuctionORM(BaseORMModel):
    __tablename__ = "auction"

    user_id: orm.Mapped[uuid.UUID]
    finish_at: orm.Mapped[dt.datetime]
    title: orm.Mapped[str]
    description: orm.Mapped[str]
    auction_status: orm.Mapped[AuctionStatusEnum]

    auction_item: orm.Mapped["AuctionItemORM"] = orm.relationship(back_populates="auction")

    def convert_to_domain(self,):
        return Auction(
            auction_id=self.id,
            user_id=self.user_id,
            finish_at=self.finish_at,
            title=self.title,
            description=self.description,
            auction_status=self.auction_status
        )

    @classmethod
    def build_from_domain(cls, auction: Auction):
        return cls(
            id=auction.auction_id,
            user_id=auction.user_id,
            finish_at=auction.finish_at,
            title=auction.title,
            description=auction.description,
            auction_status=auction.auction_status
        )

    def __str__(self):
        return f"<AuctionORM> {self.id}, {self.title}, {self.description}"
