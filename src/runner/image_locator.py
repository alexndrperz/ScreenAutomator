import os
import time
from typing import Optional

import pyautogui

from ..models import SearchRegion


class ImageLocator:
    """Busca una imagen en pantalla, opcionalmente dentro de una región."""

    CONFIDENCE = 0.50       
    INTERVALO_REINTENTO = 0   #segundos

    def esperar_hasta_encontrar(self, image_path: str, region: Optional[SearchRegion]) -> bool:
        """Busca la imagen cada segundo hasta encontrarla en pantalla."""
        search_region = self._to_region(region) if region else None
        while True:
            if self._locate(image_path, search_region) is not None:
                print(f"Imagen '{image_path}' encontrada en pantalla.")
                return True
            time.sleep(self.INTERVALO_REINTENTO)

    def exists_on_screen(self, image_path: str, region: Optional[SearchRegion]) -> bool:
        """Indica si la imagen es visible en el área de pantalla especificada."""
        search_region = self._to_region(region) if region else None
        return self._locate(image_path, search_region) is not None

    def _to_region(self, region: SearchRegion) -> tuple:
        """Convierte un SearchRegion al formato (x, y, width, height) de pyautogui."""
        return (
            int(region.x1),
            int(region.y1),
            int(region.x2 - region.x1),
            int(region.y2 - region.y1)
        )

    def _locate(self, image_path: str, region: Optional[tuple]) -> Optional[object]:
        """Ejecuta la búsqueda de imagen en pantalla con pyautogui."""
        try:
            full_path = os.path.join(os.getcwd(),"src", image_path)
            return pyautogui.locateCenterOnScreen(full_path, confidence=self.CONFIDENCE, region=region)
        except Exception as e:
            # print(f"Error al buscar la imagen '{image_path}': {e}")
            return None
