from fastapi import APIRouter

from api.v1.auction.serializers import AuctionStartContext


router = APIRouter(prefix="/auction", tags=["auction"])



@router.post("/", name="auction:start")
def start_auction(
        ctx: AuctionStartContext
):
    return ctx