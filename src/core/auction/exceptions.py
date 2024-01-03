from fastapi.exceptions import HTTPException
from fastapi import status


class AuctionNotFoundError(Exception):
    """
    Raises when auction was not found.
    """


class AuctionNotFoundHTTPException(HTTPException):
    def __init__(
            self,
            status_code: int = status.HTTP_400_BAD_REQUEST,
            detail: str = "Not found.",
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers={"WWW-Authenticate": "Bearer"})