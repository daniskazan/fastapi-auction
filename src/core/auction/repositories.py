import uuid

from sqlalchemy import exc
from core.auction.domain import Auction, AuctionItem
from core.auction.model import AuctionORM, AuctionItemORM
from core.common.repositories.base import Repository
from core.auction.exceptions import AuctionNotFoundError


class AuctionRepository(Repository):

    def get_by_id(self, *, auction_id: uuid.UUID) -> Auction:
        try:
            auction_orm: AuctionORM = self._session.get_one(AuctionORM, {"id": auction_id})  # noqa
        except exc.NoResultFound:
            raise AuctionNotFoundError
        return auction_orm.convert_to_domain()

    def save(self, *, auction: Auction, auction_item: AuctionItem) -> Auction:
        auction_orm = AuctionORM.build_from_domain(auction=auction)
        auction_item_orm = AuctionItemORM.build_from_domain(auction_item=auction_item)
        self._session.add_all([auction_orm, auction_item_orm])
        self._session.commit()
        return auction_orm.convert_to_domain()
