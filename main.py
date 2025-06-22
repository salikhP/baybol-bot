from dotenv import load_dotenv
load_dotenv()

from contextlib import asynccontextmanager
import os
from fastapi import FastAPI, Request
from app.bot import application as telegram_app
from app.bot import bot
from app.db import init_db
from telegram import Update

WEBHOOK_URL = os.getenv("WEBHOOK_URL")

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    init_db()

    await telegram_app.initialize()

    if WEBHOOK_URL:
        await bot.set_webhook(url=WEBHOOK_URL)
        print(f"Webhook set to {WEBHOOK_URL}")

    yield

    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

@app.post("/webhook")
async def telegram_webhook(req: Request):
    data = await req.json()
    update = Update.de_json(data, telegram_app.bot)
    await telegram_app.process_update(update)
    return {"ok": True}
