from fastapi import HTTPException
from fastapi import status


class InvalidCredentialsError(Exception):
    pass


class InvalidCredentialsHTTPException(HTTPException):
        def __init__(
                self,
                status_code: int = status.HTTP_400_BAD_REQUEST,
                detail: str = "Bad credentials.",
        ) -> None:
            super().__init__(status_code=status_code, detail=detail, headers={"WWW-Authenticate": "Bearer"})


class TokenExpiredHTTPException(HTTPException):
    def __init__(
            self,
            status_code: int = status.HTTP_400_BAD_REQUEST,
            detail: str = "Token expired",
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers={"WWW-Authenticate": "Bearer"})


class BadTokenHTTPException(HTTPException):
    def __init__(
            self,
            status_code: int = status.HTTP_400_BAD_REQUEST,
            detail: str = "Bad token send.",
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers={"WWW-Authenticate": "Bearer"})