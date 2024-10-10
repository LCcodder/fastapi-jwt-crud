import bcrypt
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.server.database import get_db
from app.server.schemas.auth import UserCredentials
from app.server.CRUD.user import get_user_by_email
import jwt
from app.server.config import config
import datetime
from datetime import timezone

router = APIRouter(prefix="/v1/auth")


@router.post("/", status_code=status.HTTP_200_OK)
async def authorize_and_generate_token(payload: UserCredentials, db_session: AsyncSession = Depends(get_db)):
    user = await get_user_by_email(db_session, payload.email)
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
