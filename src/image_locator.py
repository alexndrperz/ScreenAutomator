from typing import Optional

import pyautogui

from .models import SearchRegion


class ImageLocator:
    CONFIDENCE = 0.85

    def exists_on_screen(self, image_path: str, region: Optional[SearchRegion]) -> bool:
        """Retorna True si la imagen es encontrada dentro de la región dada."""
        search_region = self._to_region(region) if region else None
        return self._locate(image_path, search_region) is not None

    def _to_region(self, region: SearchRegion) -> tuple:
        """Convierte SearchRegion al formato (x, y, width, height) que usa pyautogui."""
        return (
            int(region.x1),
            int(region.y1),
            int(region.x2 - region.x1),
            int(region.y2 - region.y1)
        )

    def _locate(self, path: str, region: Optional[tuple]) -> Optional[object]:
        """Ejecuta la búsqueda de imagen en pantalla; retorna None si no la encuentra."""
        try:
            return pyautogui.locateCenterOnScreen(path, confidence=self.CONFIDENCE, region=region)
        except Exception:
            return None
