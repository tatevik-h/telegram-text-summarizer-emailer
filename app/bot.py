from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from app.config import config
from app.handlers.command_handlers import start, set_email
from app.handlers.message_handlers import handle_message


def run_bot():
    app = ApplicationBuilder().token(config.TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("email": set_email))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("Bot is runnong ...")
    app.run_polling()


if __name__ == "__main__":
    run_bot()

