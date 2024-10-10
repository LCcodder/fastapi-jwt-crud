import os
import datetime


class Config:
    DB_CONNECTION = os.getenv(
        "DB_CONFIG",
        "postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}".format(
            DB_USER=os.getenv("DB_USER", "postgres"),
            DB_PASSWORD=os.getenv("DB_PASSWORD", "password"),
            DB_HOST=os.getenv("DB_HOST", "localhost"),
            DB_PORT=os.getenv("DB_PORT", "5432"),
            DB_NAME=os.getenv("DB_NAME", "fastapiCrud"),
        ),
    )

    JWT_SECRET = os.getenv("JWT_SECRET", "secret1234")
    JWT_EXPIRATION_DAYS = datetime.timedelta(days=int(os.getenv("JWT_EXPIRATION_DAYS", "93")))


config = Config
