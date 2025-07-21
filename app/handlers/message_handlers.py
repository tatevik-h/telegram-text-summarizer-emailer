from telegram import Update 
from telegram.ext import ContextTypes
from app.storage.user_data import get_user_email
from app.services.summarizer import summarize_text
from app.services.email_service import send_email


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text

    email = get_user_email(user_id)
    if not email:
        await update.message_reply_text("Please register your email first using /email your_email@example.com.")
        return 

    await update.message.reply_text("Summarizing your message ...")
    try:
        summary = summarize_text(text)
        await update.message.reply_text(f"Summary: \n (summary)")
        send_email(email, "Your Text Summary", summary)
        await update.message.reply_text(f"Summary sent to {email}")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

