import pyautogui
from PIL import Image


class Screenshooter:
    """Captura la pantalla completa y devuelve una imagen PIL."""

    def capture(self) -> Image.Image:
        """Toma un screenshot de la pantalla en el momento actual."""
        return pyautogui.screenshot()
