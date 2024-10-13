import bcrypt
from sqlalchemy import insert, select

from src.db.models.users import User
from src.schemas.users import UserIn

from .session import Session


async def get_user_by_email(email: str) -> User | None:
    async with Session() as session:
        stmt = select(User).filter(User.email == email)
        result = await session.execute(stmt)
        return result.scalar()


async def get_user_by_username(username: str) -> User | None:
    async with Session() as session:
        stmt = select(User).filter(User.username == username)
        result = await session.execute(stmt)
        return result.scalar()


async def create_new_user(user: UserIn) -> User | None:
    async with Session() as session:
        found_user_by_email = await get_user_by_email(user.email)
        if found_user_by_email:
            return None

        found_user_by_username = await get_user_by_username(user.username)
        if found_user_by_username:
            return None

        query = (
            insert(User)
            .values(
                password=(bcrypt.hashpw(str.encode(user.password), bcrypt.gensalt(5))).decode(),
                **user.model_dump(exclude={"password"})
            )
            .returning(User)
        )

        result = await session.execute(query)
        created_user = result.scalar()
        await session.commit()
        return created_user
