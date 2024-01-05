from sqlalchemy import orm
from sqlalchemy import types

from core.auction.model import AuctionORM
from core.common.models.base import BaseORMModel

from core.users.domain import User
from core.common.utils.security import pwd_context


class UserORM(BaseORMModel):
    __tablename__ = "user"

    username: orm.Mapped[str] = orm.mapped_column(types.String, unique=True)
    password: orm.Mapped[str]
    email: orm.Mapped[str] = orm.mapped_column(unique=True)

    auctions: orm.Mapped[list[AuctionORM]] = orm.relationship()

    @classmethod
    def build_from_domain(cls, *, user: User) -> "UserORM":
        user_orm = cls(
            id=user.user_id,
            username=user.username,
            password=pwd_context.hash(user.password),
            email=user.email
        )
        return user_orm

    def convert_to_domain(self) -> User:
        return User(user_id=self.id, username=self.username, password=self.password, email=self.email)

    def __str__(self):
        return f"<UserORM> ID - {self.id}, USERNAME - {self.username}"
