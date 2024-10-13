from typing import Literal
from fastapi import APIRouter, status

router = APIRouter(prefix="/ping")


@router.get("/", status_code=status.HTTP_200_OK)
async def get_ping() -> Literal['pong']:
    return "pong"
