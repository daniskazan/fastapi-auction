from fastapi import status
from fastapi import HTTPException


class UserNotFoundError(Exception):
    pass


class UserAlreadyExistsError(Exception):
    pass



class UserAlreadyExistsHTTPException(HTTPException):
    def __init__(
            self,
            status_code: int = status.HTTP_400_BAD_REQUEST,
            detail: str = "User already exists.",
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers={"WWW-Authenticate": "Bearer"})


class UserNotFoundHTTPException(HTTPException):
    def __init__(
            self,
            status_code: int = status.HTTP_400_BAD_REQUEST,
            detail: str = "Not found.",
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers={"WWW-Authenticate": "Bearer"})