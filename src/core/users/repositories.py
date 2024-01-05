from uuid import UUID

from sqlalchemy import exc
from sqlalchemy import sql

from core.common.repositories.base import Repository
from core.users.model import UserORM
from core.users.domain import User
from core.users.exceptions import UserNotFoundError, UserAlreadyExistsError


class UserRepository(Repository):
    def get_by_username(self, *, username: str) -> User:
        sql_query = sql.select(UserORM).where(
            sql.or_(UserORM.username == username, UserORM.email == username)
        )
        try:
            user_orm = self._session.execute(sql_query)
            user_orm = user_orm.scalar_one()
        except exc.NoResultFound:
            raise UserNotFoundError
        return user_orm.convert_to_domain()

    def get_by_id(self, *, user_id: UUID) -> User:
        try:
            user_orm: UserORM = self._session.get_one(UserORM, {"id": user_id})  # noqa
        except exc.NoResultFound:
            raise UserNotFoundError
        return user_orm.convert_to_domain()

    def save(self, *, user: User) -> User:
        user_orm = UserORM.build_from_domain(user=user)
        self._session.add(user_orm)
        try:
            self._session.commit()
        except exc.IntegrityError:
            self._session.rollback()
            raise UserAlreadyExistsError
        return user_orm.convert_to_domain()
