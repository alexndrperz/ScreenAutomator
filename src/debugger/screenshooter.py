import pyautogui
from PIL import Image


class Screenshooter:
    """Captura la pantalla completa y devuelve una imagen PIL."""

    def capture(self) -> Image.Image:
        """Toma un screenshot de la pantalla en el momento actual.

        Returns:
            Imagen PIL con el contenido actual de la pantalla.
        """
        return pyautogui.screenshot()
