from core.auction.model import AuctionORM
from core.common.repositories.base import Repository
from core.auction.domain import Auction


class AuctionRepository(Repository):

    def save_auction(self, auction: Auction):
        auction_orm = AuctionORM.build_from_domain(auction=auction)
        self.session.add(auction_orm)
        self.session.commit()
