from typing import Optional

import pyautogui

from ..models import SearchRegion


class ImageLocator:
    """Busca una imagen en pantalla usando pyautogui, opcionalmente dentro de una región."""

    CONFIDENCE = 0.85

    def exists_on_screen(self, image_path: str, region: Optional[SearchRegion]) -> bool:
        """Indica si la imagen es visible en el área de pantalla especificada.

        Args:
            image_path: Ruta al archivo de imagen a buscar.
            region:     Región de pantalla donde buscar. Si es None, busca en toda la pantalla.

        Returns:
            True si la imagen fue encontrada, False en caso contrario.
        """
        search_region = self._to_region(region) if region else None
        return self._locate(image_path, search_region) is not None

    def _to_region(self, region: SearchRegion) -> tuple:
        """Convierte un SearchRegion al formato (x, y, width, height) que requiere pyautogui.

        Args:
            region: Región definida por dos esquinas (x1/y1 y x2/y2).

        Returns:
            Tupla (left, top, width, height) en píxeles enteros.
        """
        return (
            int(region.x1),
            int(region.y1),
            int(region.x2 - region.x1),
            int(region.y2 - region.y1)
        )

    def _locate(self, path: str, region: Optional[tuple]) -> Optional[object]:
        """Ejecuta la búsqueda de imagen en pantalla con pyautogui.

        Args:
            path:   Ruta al archivo de imagen.
            region: Tupla (left, top, width, height) o None para pantalla completa.

        Returns:
            Objeto con las coordenadas del centro si se encontró, None si no.
        """
        try:
            return pyautogui.locateCenterOnScreen(path, confidence=self.CONFIDENCE, region=region)
        except Exception:
            return None
