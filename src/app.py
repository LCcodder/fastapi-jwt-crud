from fastapi import FastAPI

from src.api import auth, ping, user

app = FastAPI()

routers = [
    user.router,
    ping.router,
    auth.router
]


for i in routers:
    app.include_router(i, prefix="/api/v1")
