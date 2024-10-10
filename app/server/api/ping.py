from fastapi import APIRouter, status, Depends, Request

router = APIRouter(prefix="/v1/ping")

@router.get("/", status_code=status.HTTP_200_OK)
async def get_ping():
    return "pong"
