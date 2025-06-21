import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["💬 Caută un partener"],
        ["❤️ Povestea ta"],
        ["ℹ️ Ajutor"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "👋 Bun venit pe LoveSync România!\n"
        "Alege o opțiune din meniu:",
        reply_markup=reply_markup
    )

if __name__ == "__main__":
    token = os.environ.get("BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
