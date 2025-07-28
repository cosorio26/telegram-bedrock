# Importamos las librerías necesarias
from unittest.mock import patch
from app.controller import procesar_mensaje

# Test para la función procesar_mensaje
@patch("app.controller.preguntar_a_bedrock")
@patch("app.controller.enviar_mensaje")
def test_procesar_mensaje(mock_enviar, mock_preguntar):
    mock_preguntar.return_value = "Películas recomendadas"
    procesar_mensaje(chat_id=1234, texto_usuario="Recomiéndame pelis")
    mock_enviar.assert_called_with(1234, "Películas recomendadas")