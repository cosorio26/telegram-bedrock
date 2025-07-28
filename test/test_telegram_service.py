# Importamos las liberías necesarias
import pytest
from unittest.mock import patch
from app.telegram_service import enviar_mensaje

# Test para la función enviar_mensaje
@patch("app.telegram_service.requests.post")
def test_enviar_mensaje(mock_post):
    # Configuramos el mock para que devuelva una respuesta simulada
    mock_post.return_value.status_code = 200
    # Llamamos a la función con un chat_id y un texto de prueba
    enviar_mensaje(chat_id=1234, texto="Hola")
    mock_post.assert_called_once()