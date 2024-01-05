from fastapi import APIRouter

from api.v1.auction.controllers import router as auction_router
from api.v1.users.controllers import router as user_router
from api.v1.auth.controllers import router as auth_router

router = APIRouter(prefix="/api/v1")

router.include_router(auction_router)
router.include_router(user_router)
router.include_router(auth_router)
