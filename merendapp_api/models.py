from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_as_dataclass, mapped_column, registry

table_registry = registry()


@mapped_as_dataclass(table_registry)
class Message:
    __tablename__ = 'messages'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    phone: Mapped[str]
    company: Mapped[str]
    company_type: Mapped[str]
    message: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )

@mapped_as_dataclass(table_registry)
class Review:
    __tablename__ = 'reviews'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str]
    role: Mapped[str]
    message: Mapped[str]
    rating: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
