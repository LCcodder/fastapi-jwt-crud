from fastapi import APIRouter, HTTPException, status

from src.db.crud.users import create_new_user, get_user_by_username
from src.schemas.users import UserIn

router = APIRouter(prefix="/users")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(payload: UserIn):
    user = await create_new_user(payload)
    if not user:
        raise HTTPException(status_code=400,
                            detail="User with that email already exists")

    return user


@router.get("/{username}", status_code=status.HTTP_200_OK)
async def get_user(username: str):
    user = await get_user_by_username(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    del user.password

    return user
