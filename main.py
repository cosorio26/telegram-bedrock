# Importamos las librerias necesarias
from flask import Flask, request
from app.controller import procesar_mensaje

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Obtenemos los datos del mensaje enviado desde Telegram
    data = request.get_json()
    chat_id = data['message']['chat']['id']
    texto_usuario = data['message']['text']
    
    # Procesamos el mensaje del usuario
    procesar_mensaje(chat_id, texto_usuario)
    
    return 'OK', 200

if __name__ == '__main__':
    app.run(debug=True)