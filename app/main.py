from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from app.bot import bot, dispatcher
from app.db import init_db
import telegram
import os

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    init_db()
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)
