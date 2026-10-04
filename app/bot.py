from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from app.config import settings


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "👋 Loan Tracker Bot is running.\n\n"
        "Phase 1 is ready. Payment tracking will be added next."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Commands:\n"
        "/start - Start the bot\n"
        "/help - Show help\n\n"
        "Later you will be able to send messages like: "
        "Paid Rs.1500 - SBI"
    )


def build_application() -> Application:
    application = Application.builder().token(settings.telegram_bot_token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    return application


def main() -> None:
    build_application().run_polling()


if __name__ == "__main__":
    main()
