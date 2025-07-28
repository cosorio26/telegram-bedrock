# Importamos las librerías necesarias
import pytest
from unittest.mock import patch
from app.bedrock_service import preguntar_a_bedrock

# Test para la función preguntar_a_bedrock
@patch("app.bedrock_service.bedrock")
def test_preguntar_a_bedrock(mock_bedrock):
    # Configuramos el mock para que devuelva una respuesta simulada
    mock_bedrock.converse.return_value = {
        "output": {
            "message": {
                "content": [{"text": "La mejor fue Terminator"}]
            }
        }
    }
    # Llamamos a la función con un texto de prueba
    respuesta = preguntar_a_bedrock("¿Qué películas salieron en 1980?")
    assert respuesta == "La mejor fue Terminator"
