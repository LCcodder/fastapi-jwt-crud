import datetime
from datetime import timezone

import bcrypt
import jwt
from fastapi import APIRouter, HTTPException, status

from src.config import config
from src.db.crud.users import get_user_by_email
from src.schemas.auth import UserCredentials

router = APIRouter(prefix="/auth")


@router.post("/", status_code=status.HTTP_200_OK)
async def authorize_and_generate_token(payload: UserCredentials):
    user = await get_user_by_email(payload.email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not bcrypt.checkpw(str.encode(payload.password), str.encode(user.password)):
        raise HTTPException(status_code=400, detail="Wrong user credentials")

    token = jwt.encode({
        "email": payload.email,
        "username": user.username,
        "exp": datetime.datetime.now(tz=timezone.utc) + config.JWT_EXPIRATION_DAYS
    }, config.JWT_SECRET, algorithm="HS256")

    return {
        "token": token
    }
