# Importamos las librerías necesarias
from app.bedrock_service import preguntar_a_bedrock
from app.telegram_service import enviar_mensaje

# Función principal que maneja el flujo de la conversación
def procesar_mensaje(chat_id, texto_usuario):
    # Enviamos el mensaje del usuario a Bedrock y obtenemos la respuesta
    respuesta_ia = preguntar_a_bedrock(texto_usuario)
    
    # Enviamos la respuesta de Bedrock al chat de Telegram
    enviar_mensaje(chat_id, respuesta_ia)