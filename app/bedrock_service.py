# Importamos las librerías necesarias
import boto3
from config import settings

bedrock = boto3.client("bedrock-runtime", region_name=settings.REGION)


# Función fallback en caso que el modelo no responda
def fallback():
    return "Lo siento, no pude procesar tu solicitud en este momento. Por favor, inténtalo más tarde."

# Función para enviar una solicitud a Bedrock
def preguntar_a_bedrock(texto_usuario):
    # Codigo temporal mockeando la respuesta de Bedrock
    return f"Recibi tu respuesta: {texto_usuario}"

    #respuesta = bedrock.converse(
    #    modelId=settings.BEDROCK_MODEL_ID,
    #    messages=[{"role": "user", "content": [{"text": texto_usuario}]}],
    #    inferenceConfig={
    #        "maxTokens": 300
    #    },
    #    accept="application/json",
    #)

    # Respondemos con fallback si no hay respuesta
    #if not respuesta or len(respuesta.strip()) < 5:
    #    return fallback()
    

    #return respuesta["output"]["message"]["content"][0]["text"]