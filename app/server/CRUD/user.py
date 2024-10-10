from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import bcrypt
from app.server.models.user import User
from app.server.schemas.user import CreateUser


async def get_user_by_email(db: AsyncSession, email: str):

    query = select(User).filter(User.email == email)
    result = await db.execute(query)
    return result.scalar()


async def get_user_by_username(db: AsyncSession, username: str):

    query = select(User).filter(User.username == username)
    result = await db.execute(query)
    return result.scalar()


async def create_new_user(db: AsyncSession, user: CreateUser):
    found_user_by_email = await get_user_by_email(db, user.email)
    if found_user_by_email:
        return None

    found_user_by_username = await get_user_by_username(db, user.username)
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

    result = await db.execute(query)
    created_user = result.scalar()
    await db.commit()
    return created_user

