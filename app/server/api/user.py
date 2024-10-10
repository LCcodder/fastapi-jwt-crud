from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.server.database import get_db
from app.server.schemas.user import CreateUser
from app.server.CRUD.user import create_new_user, get_user_by_username

router = APIRouter(prefix="/v1/users")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(payload: CreateUser, db_session: AsyncSession = Depends(get_db)):
    user = await create_new_user(db_session, payload)
    if not user:
        raise HTTPException(status_code=400, detail="User with that email already exists")

    return user


@router.get("/{username}", status_code=status.HTTP_200_OK)
async def get_user(username: str, db_session: AsyncSession = Depends(get_db)):
    user = await get_user_by_username(db_session, username)
    del user.password

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user
