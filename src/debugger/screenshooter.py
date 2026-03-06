import time
from typing import Optional

import pyautogui
from PIL import Image


class Screenshooter:
    """Captura la pantalla completa y devuelve una imagen PIL."""

    def capture(self, delay: Optional[float] = None) -> Image.Image:
        """Toma un screenshot. Si delay es un número, espera ese tiempo en segundos antes de capturar."""
        print(f"Capturando pantalla... (delay={delay}s)")
        if delay is not None:
            time.sleep(delay)
        img =  pyautogui.screenshot()
        print("Pantalla capturada.")
        return img