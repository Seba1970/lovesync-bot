import os
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = os.environ.get("BOT_TOKEN")
bot = Bot(token=TOKEN)

app = Flask(__name__)

dispatcher = Dispatcher(bot=bot, update_queue=None, workers=0, use_context=True)

# === Comenzi ===
def start(update: Update, context: CallbackContext):
    update.message.reply_text("👋 Bine ai venit pe LoveSync România!")

def mesaj(update: Update, context: CallbackContext):
    update.message.reply_text("✅ Mesaj primit. Revenim în curând cu funcții active.")

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mesaj))

# === Ruta webhook ===
@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "OK", 200

# === Pornire pentru Render ===
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)



