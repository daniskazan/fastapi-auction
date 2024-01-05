import uuid

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status


from core.auction.domain import Auction, AuctionItem
from core.auction.services import AuctionService
from api.v1.auction.serializers import AuctionStartRequestBody, AuctionResponseSerializer
from api.v1.auction.dependencies import get_auction_service
from core.common.utils.generic_response import OkResponse


router = APIRouter(prefix="/auction", tags=["auction"])


@router.post("/", name="auction:start", response_model=OkResponse[AuctionResponseSerializer])
def start_auction(
        body: AuctionStartRequestBody,
        auction_service: AuctionService = Depends(get_auction_service)
):
    auction = Auction(
        auction_id=uuid.uuid4(),
        user_id=body.user_id,
        finish_at=body.finish_at,
        title=body.title,
        description=body.description,
    )
    auction_item = AuctionItem(
        item_id=uuid.uuid4(),
        auction_id=auction.auction_id,
        image_url=body.auction_item.image_url,
        initial_price=body.auction_item.initial_price,
        currency=body.auction_item.currency,
    )
    started_auction = auction_service.start_auction(auction=auction, auction_item=auction_item)

    return OkResponse.new(
        status_code=status.HTTP_201_CREATED,
        data=AuctionResponseSerializer.model_validate(started_auction)
    )
