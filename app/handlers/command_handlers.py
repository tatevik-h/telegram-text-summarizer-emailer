from telegram import Update
from telegram.ext import ContextTypes
from app.storage.user_data import set_user_email


async def start(user: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome! Use /emai your_email@example.com to register your email."        
    )


async def set_email(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1:
        await update.message.reply_text("Usage: /email your_email@example.com")
        return

    user_id = update.message.from_user.id
    email = context.args[0]
    set_user_email(user_id, email)
    await update.message.reply_text(f"Email saved: {email}")

