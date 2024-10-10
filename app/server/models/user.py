from sqlalchemy import Column, String, DateTime, VARCHAR
from app.server.models.base_class import Base
import datetime



class User(Base):
    __tablename__ = "users"

    email = Column("email", VARCHAR(64), primary_key=True, unique=True)

    username = Column("username", VARCHAR(32), unique=True)
    birthday = Column("birthday", VARCHAR(10), default=str(datetime.date.today()))

    # male/female
    sex = Column("sex", VARCHAR(6), default="male")
    profile_color = Column("profile_color", VARCHAR(13), default="#ffffff")
    bio = Column("bio", VARCHAR(100), default=None)
    password = Column("password", String)

    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())
