from fastapi import APIRouter

from api.v1.auction.controllers import router as auction_router

router = APIRouter(prefix="/api/v1")

router.include_router(auction_router)
