from asyncio import current_task
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (AsyncSession, async_scoped_session,
                                    async_sessionmaker, create_async_engine)

from src.config import config

engine = create_async_engine(config.DB_CONNECTION)
session_maker = async_sessionmaker(engine, expire_on_commit=False)


@asynccontextmanager
async def Session(*args, **kwargs) -> AsyncGenerator[AsyncSession, None]:
    session_scoped = async_scoped_session(session_maker, current_task)
    async with session_scoped() as session:
        yield session
