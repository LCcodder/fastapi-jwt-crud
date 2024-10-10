from fastapi import FastAPI
from app.server.api.ping import router as ping_router
from app.server.api.user import router as user_router
from app.server.api.auth import router as auth_router

app = FastAPI()

app.include_router(ping_router)
app.include_router(user_router)
app.include_router(auth_router)
