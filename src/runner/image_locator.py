import os
import time
from typing import List, Optional

import pyautogui
from PIL import Image

from ..models import ImageEntry, SearchRegion


class ImageLocator:
    """Busca una imagen en pantalla, opcionalmente dentro de una región."""

    CONFIDENCE = 0.50
    INTERVALO_REINTENTO = 0   #segundos

    def esperar_hasta_encontrar(self, images: List[ImageEntry], region: Optional[SearchRegion]) -> str:
        """Valida los archivos, luego busca repetidamente hasta encontrar alguna imagen; retorna el id."""
        self._validar_imagenes(images)
        search_region = self._to_region(region) if region else None
        while True:
            for entry in images:
                if self._locate(entry.path, search_region) is not None:
                    print(f"Imagen '{entry.id}' ({entry.path}) encontrada en pantalla.")
                    return entry.id
            time.sleep(self.INTERVALO_REINTENTO)

    def _validar_imagenes(self, images: List[ImageEntry]) -> None:
        """Verifica que cada archivo de imagen exista y pueda abrirse; cierra el programa si no."""
        for entry in images:
            full_path = os.path.join(os.getcwd(), "src", entry.path)
            if not os.path.isfile(full_path):
                print(f"[Error] Imagen '{entry.id}': archivo no encontrado → {full_path}")
                raise SystemExit(1)
            try:
                with Image.open(full_path) as img:
                    img.verify()
            except Exception as e:
                print(f"[Error] Imagen '{entry.id}': no se puede abrir → {full_path} ({e})")
                raise SystemExit(1)

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
            full_path = os.path.join(os.getcwd(), "src", image_path)
            return pyautogui.locateCenterOnScreen(full_path, confidence=self.CONFIDENCE, region=region)
        except Exception:
            return None
