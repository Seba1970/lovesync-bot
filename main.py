import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["💬 Caută un partener"],
        ["❤️ Povestea ta"],
        ["ℹ️ Ajutor"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "👋 Bun venit pe LoveSync România!\nAlege o opțiune din meniu:",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "💬 Caută un partener":
        await update.message.reply_text("Funcția de potrivire este momentan în dezvoltare. Revenim curând!")
    elif text == "❤️ Povestea ta":
        await update.message.reply_text("Trimite-ne povestea ta de dragoste! Echipa noastră o va publica anonim, dacă dorești.")
    elif text == "ℹ️ Ajutor":
        await update.message.reply_text("Pentru suport, contactează echipa: @LoveSyncSupport")
    else:
        await update.message.reply_text("Alege o opțiune din meniu.")

if __name__ == "__main__":
    token = os.environ.get("BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
