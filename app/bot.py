import os
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from sqlalchemy.orm import Session
from app.crud import user as crud_user
from app.db import get_db

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TELEGRAM_TOKEN:
    raise ValueError("TELEGRAM_TOKEN is not set in .env")

bot = Bot(token=TELEGRAM_TOKEN)

# main event processor: updates handler, listens for webhook
application = Application.builder().token(TELEGRAM_TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("👋 Welcome to Baybol — your personal finance tracker bot!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    db_gen = get_db()
    db: Session = next(db_gen)

    try:
        user_id = update.effective_user.id
        existing_user = crud_user.get_user(db, user_id)

        if not existing_user:
            crud_user.create_user_if_not_exists(db, user_id)
            print(f"New user created: {user_id}")
        else:
            print(f"User {user_id} already exists")

        await update.message.reply_text(f"You said: {update.message.text}")
    finally:
        db_gen.close()

# register handlers
application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
