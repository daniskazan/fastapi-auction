from dataclasses import dataclass

from stories import Story
from stories import I
from stories import State

from core.auction.model import AuctionORM, AuctionItemORM
from core.auction.domain import Auction, AuctionItem
from core.auction.repositories import AuctionRepository


@dataclass
class AuctionService:
    repository: AuctionRepository

    def start_auction(self, *, auction: Auction, auction_item: AuctionItem) -> Auction:
        return self.repository.save(auction=auction, auction_item=auction_item)