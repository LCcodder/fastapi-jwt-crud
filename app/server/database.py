from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from app.server.config import config

print(config.DB_CONNECTION)
engine = create_async_engine(
    config.DB_CONNECTION,
    future=True,
    echo=True,
)


AsyncSessionFactory = async_sessionmaker(
    engine,
    autoflush=False,
    expire_on_commit=False,
)



async def get_db() -> AsyncGenerator:
    async with AsyncSessionFactory() as session:
        yield session