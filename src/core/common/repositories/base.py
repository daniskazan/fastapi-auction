import abc

from sqlalchemy import orm


class Repository(abc.ABC):
    def __init__(self, session: orm.Session) -> None:
        self._session = session
