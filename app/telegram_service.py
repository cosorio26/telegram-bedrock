# Importamos las librerías necesarias
import requests
from config import settings

# Funcion para enviar un mensaje a un chat de Telegram
def enviar_mensaje(chat_id, texto):
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": texto,
    }
    requests.post(url, json=payload)