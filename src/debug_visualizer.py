import os
from datetime import datetime
from typing import Optional

import pyautogui
from PIL import Image, ImageDraw

from .models import AutomationConfig, SearchRegion, TriggerConfig


# ── Constantes de estilo ──────────────────────────────────────
OUTPUT_DIR = "debug"
REGION_COLOR  = (0, 200, 0)    # verde  → search_region
TRIGGER_COLOR = (0, 100, 255)  # azul   → trigger
LINE_WIDTH    = 3
TRIGGER_HALF  = 15             # mitad del lado del cuadro del trigger


# ══════════════════════════════════════════════════════════════
#  Screenshooter
# ══════════════════════════════════════════════════════════════

class Screenshooter:
    """Captura la pantalla completa y devuelve una imagen PIL."""

    def capture(self) -> Image.Image:
        """Toma un screenshot de la pantalla en el momento actual.

        Returns:
            Imagen PIL con el contenido actual de la pantalla.
        """
        return pyautogui.screenshot()


# ══════════════════════════════════════════════════════════════
#  RegionRenderer
# ══════════════════════════════════════════════════════════════

class RegionRenderer:
    """Dibuja los rectángulos de debug sobre una imagen PIL."""

    def draw_search_region(self, img: Image.Image, region: Optional[SearchRegion]) -> None:
        """Dibuja un rectángulo verde sobre el área de búsqueda de imagen.

        Args:
            img:    Imagen PIL sobre la que se dibuja.
            region: Región de búsqueda. Si es None, no dibuja nada.
        """
        if not region:
            return
        draw = ImageDraw.Draw(img)
        draw.rectangle(
            [region.x1, region.y1, region.x2, region.y2],
            outline=REGION_COLOR,
            width=LINE_WIDTH
        )

    def draw_trigger(self, img: Image.Image, trigger: TriggerConfig) -> None:
        """Dibuja un rectángulo azul centrado en las coordenadas del trigger.

        Args:
            img:     Imagen PIL sobre la que se dibuja.
            trigger: Configuración del trigger con coordenadas x/y.
        """
        draw = ImageDraw.Draw(img)
        x, y = trigger.x, trigger.y
        draw.rectangle(
            [x - TRIGGER_HALF, y - TRIGGER_HALF,
             x + TRIGGER_HALF, y + TRIGGER_HALF],
            outline=TRIGGER_COLOR,
            width=LINE_WIDTH
        )


# ══════════════════════════════════════════════════════════════
#  DebugSaver
# ══════════════════════════════════════════════════════════════

class DebugSaver:
    """Guarda imágenes de debug en el directorio de salida del proyecto."""

    def __init__(self, output_dir: str = OUTPUT_DIR) -> None:
        self._output_dir = output_dir

    def save(self, img: Image.Image, index: int) -> str:
        """Guarda la imagen en el directorio de debug con un nombre único.

        Args:
            img:   Imagen PIL a guardar.
            index: Índice de la automatización dentro de la lista del JSON.

        Returns:
            Ruta completa del archivo PNG guardado.
        """
        os.makedirs(self._output_dir, exist_ok=True)
        path = os.path.join(self._output_dir, self._build_filename(index))
        img.save(path)
        return path

    def _build_filename(self, index: int) -> str:
        """Genera el nombre del archivo con timestamp e índice.

        Args:
            index: Índice de la automatización.

        Returns:
            Nombre de archivo con formato 'debug_YYYYMMDD_HHMMSS_<index>.png'.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"debug_{timestamp}_{index}.png"


# ══════════════════════════════════════════════════════════════
#  DebugVisualizer
# ══════════════════════════════════════════════════════════════

class DebugVisualizer:
    """Orquesta la captura, el renderizado y el guardado del screenshot de debug."""

    def __init__(self) -> None:
        self._shooter  = Screenshooter()
        self._renderer = RegionRenderer()
        self._saver    = DebugSaver()

    def visualize(self, config: AutomationConfig, index: int = 0) -> None:
        """Captura la pantalla, marca search_region y trigger, y guarda la imagen.

        Args:
            config: Configuración completa con imagen y trigger a marcar.
            index:  Índice de la automatización, usado en el nombre del archivo.
        """
        img = self._shooter.capture()
        self._renderer.draw_search_region(img, config.image.search_region)
        self._renderer.draw_trigger(img, config.trigger)
        path = self._saver.save(img, index)
        print(f"[Debug #{index}] Screenshot guardado en: {path}")
