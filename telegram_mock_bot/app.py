from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

app = Flask(__name__)

@app.route("/")
def index():
    return "Bot Flask corriendo en Docker 🐳"

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = update.message.text
    print(f"📩 Telegram dice: {mensaje}")
    
    # Aquí simulás Bedrock
    respuesta = f"🧪 Respuesta simulada a: '{mensaje}'"
    await update.message.reply_text(respuesta)

def correr_bot():
    app_telegram = ApplicationBuilder().token(TOKEN).build()
    app_telegram.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))
    app_telegram.run_polling()

if __name__ == "__main__":
    correr_bot()
