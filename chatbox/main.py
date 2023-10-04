from fastapi import FastAPI
from .src.autobot.main import router
app = FastAPI()

app.include_router(router)