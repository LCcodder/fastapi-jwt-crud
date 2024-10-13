from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    email: Mapped[str] = mapped_column(primary_key=True, unique=True)
    username: Mapped[str] = mapped_column(unique=True)
    birthday: Mapped[str] = mapped_column(insert_default=func.now())
    sex: Mapped[str] = mapped_column(default="male")
    profile_color: Mapped[str] = mapped_column(default="#ffffff")
    bio: Mapped[str | None] = mapped_column(default=None)
    password: Mapped[str] = mapped_column()

    created_at: Mapped[datetime] = mapped_column(insert_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        onupdate=func.now(),
        insert_default=func.now()
    )
