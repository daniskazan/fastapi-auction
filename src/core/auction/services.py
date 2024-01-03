import uuid

from core.auction.domain import Auction, AuctionItem
from core.auction.repositories import AuctionRepository


class AuctionService:
    def __init__(
            self,
            *,
            repository: AuctionRepository
    ):
        self.repository = repository

    def start_auction(self, *, auction: Auction, auction_item: AuctionItem) -> None:
        self.repository.save(auction=auction, auction_item=auction_item)

    def find_auction(self, auction_id: uuid.UUID):
        return self.repository.get_by_id(auction_id=auction_id)