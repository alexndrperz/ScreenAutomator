import os
import time
from typing import List, Optional

import pyautogui

from ..models import ImageEntry, SearchRegion


class ImageLocator:
    """Busca una imagen en pantalla, opcionalmente dentro de una región."""

    CONFIDENCE = 0.50
    INTERVALO_REINTENTO = 0   #segundos

    def esperar_hasta_encontrar(self, images: List[ImageEntry], region: Optional[SearchRegion]) -> str:
        """Busca repetidamente hasta encontrar cualquiera de las imágenes; retorna el id encontrado."""
        search_region = self._to_region(region) if region else None
        while True:
            for entry in images:
                if self._locate(entry.path, search_region) is not None:
                    print(f"Imagen '{entry.id}' ({entry.path}) encontrada en pantalla.")
                    return entry.id
            time.sleep(self.INTERVALO_REINTENTO)

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
