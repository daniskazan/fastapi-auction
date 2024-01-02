import uuid
import datetime as dt

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.types import DateTime
from sqlalchemy.dialects.postgresql import UUID


class BaseORMModel(DeclarativeBase):
    __abstract__ = True

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)

    created_at: Mapped[dt.datetime] = mapped_column(
        DateTime, default=dt.datetime.now(tz=dt.UTC)
    )
    updated_at: Mapped[dt.datetime] = mapped_column(
        DateTime,
        default=dt.datetime.now(tz=dt.UTC),
        onupdate=dt.datetime.now(tz=dt.UTC),
    )