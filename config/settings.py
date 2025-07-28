# Importamos las librerias necesarias
import os
from dotenv import load_dotenv

# Cargamos las varibales de entorno desde el archivo .env
load_dotenv()

# Definimos las variables de entorno
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
BEDROCK_MODEL_ID = os.getenv("BEDROCK_MODEL_ID")
REGION = os.getenv("BEDROCK_REGION", "us-east-1")
