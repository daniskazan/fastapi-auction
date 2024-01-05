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
    initial_price: orm.Mapped[decimal.Decimal]
    current_price: orm.Mapped[decimal.Decimal]
    currency: orm.Mapped[CurrencyEnum]

    auction: orm.Mapped["AuctionORM"] = orm.relationship(back_populates="auction_item")

    @classmethod
    def build_from_domain(cls, *, auction_item: AuctionItem):
        return cls(
            id=auction_item.item_id,
            auction_id=auction_item.auction_id,
            image_url=auction_item.image_url,
            initial_price=auction_item.initial_price,
            current_price=auction_item.initial_price,
            currency=auction_item.currency
        )

    def convert_to_domain(self):
        return AuctionItem(
            item_id=self.id,
            auction_id=self.auction_id,
            image_url=self.image_url,
            initial_price=self.initial_price,
            current_price=self.current_price,
            currency=self.currency
        )


class AuctionORM(BaseORMModel):
    __tablename__ = "auction"

    user_id: orm.Mapped[uuid.UUID] = orm.mapped_column(schema.ForeignKey("user.id"))
    finish_at: orm.Mapped[dt.datetime]
    title: orm.Mapped[str]
    description: orm.Mapped[str]
    auction_status: orm.Mapped[AuctionStatusEnum]

    auction_item: orm.Mapped["AuctionItemORM"] = orm.relationship(back_populates="auction")

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

    def convert_to_domain(self):
        return Auction(
            auction_id=self.id,
            user_id=self.user_id,
            finish_at=self.finish_at,
            title=self.title,
            description=self.description,
            auction_status=self.auction_status,
            auction_item=self.auction_item.convert_to_domain()
        )

    def __str__(self):
        return f"<AuctionORM> {self.id}, {self.title}, {self.description}"
