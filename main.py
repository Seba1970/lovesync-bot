import os
import asyncio
import nest_asyncio
nest_asyncio.apply()

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ContextTypes, filters
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["💬 Caută un partener"],
                ["❤️ Povestea ta"],
                ["ℹ️ Ajutor"]]
    await update.message.reply_text(
        "👋 Bun venit pe LoveSync România!\nAlege o opțiune:",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "💬 Caută un partener":
        await update.message.reply_text("Match-making în curând.")
    elif text == "❤️ Povestea ta":
        await update.message.reply_text("Trimite-ne povestea ta și o publicăm anonim.")
    elif text == "ℹ️ Ajutor":
        await update.message.reply_text("Suport: @LoveSyncSupport")
    else:
        await update.message.reply_text("Alege o opțiune din meniu.")

async def main():
    token = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    await app.run_polling()

if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.get_event_loop().run_until_complete(main())





