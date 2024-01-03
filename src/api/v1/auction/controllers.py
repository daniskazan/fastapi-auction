import uuid

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi.encoders import jsonable_encoder
from core.auction.domain import Auction, AuctionItem
from core.auction.services import AuctionService
from api.v1.auction.serializers import AuctionStartContext
from api.v1.auction.dependencies import get_auction_service
from core.common.utils.generic_response import OkResponse
from core.auction.exceptions import AuctionNotFoundError, AuctionNotFoundHTTPException



router = APIRouter(prefix="/auction", tags=["auction"])


@router.post("/", name="auction:start")
def start_auction(
        ctx: AuctionStartContext,
        auction_service: AuctionService = Depends(get_auction_service)
):
    auction = Auction(
        auction_id=uuid.uuid4(),
        user_id=ctx.user_id,
        finish_at=ctx.finish_at,
        title=ctx.title,
        description=ctx.description,
    )
    auction_item = AuctionItem(
        item_id=uuid.uuid4(),
        auction_id=auction.auction_id,
        image_url=ctx.auction_item.image_url,
        starting_price=ctx.auction_item.starting_price,
        currency=ctx.auction_item.currency,
    )
    auction_service.start_auction(auction=auction, auction_item=auction_item)
    return OkResponse.new(status_code=status.HTTP_201_CREATED, data=jsonable_encoder(auction))



@router.get(
    "/{auction_id}",
    name="auction:get_by_id",
    response_model=OkResponse[Auction],
)
def get_auction(
        auction_id: uuid.UUID,
        auction_service: AuctionService = Depends(get_auction_service)
):
    try:
        auction: Auction = auction_service.find_auction(auction_id=auction_id)
    except AuctionNotFoundError:
        raise AuctionNotFoundHTTPException
    return OkResponse.new(status_code=status.HTTP_200_OK, data=jsonable_encoder(auction))