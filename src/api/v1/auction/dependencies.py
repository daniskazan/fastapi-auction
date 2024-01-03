from core.auction.services import AuctionService
from core.auction.repositories import AuctionRepository
from core.common.session import Session


def get_auction_service() -> AuctionService:
    return AuctionService(repository=AuctionRepository(session=Session))
