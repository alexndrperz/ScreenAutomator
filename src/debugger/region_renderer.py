from typing import Optional

from PIL import Image, ImageDraw

from ..models import SearchRegion, TriggerConfig


REGION_COLOR  = (0, 200, 0)    # verde  → search_region
TRIGGER_COLOR = (0, 100, 255)  # azul   → trigger
LINE_WIDTH    = 3
TRIGGER_HALF  = 15             # mitad del lado del cuadro del trigger


class RegionRenderer:
    """Dibuja los rectángulos de debug (search_region y trigger) sobre una imagen PIL."""

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
