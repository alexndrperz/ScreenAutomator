from ..models import AutomationConfig
from .screenshooter import Screenshooter
from .region_renderer import RegionRenderer
from .debug_saver import DebugSaver


class DebugVisualizer:
    """Orquesta la captura, renderizado y guardado del screenshot de debug."""

    def __init__(self) -> None:
        self._shooter  = Screenshooter()
        self._renderer = RegionRenderer()
        self._saver    = DebugSaver()

    def visualize(self, config: AutomationConfig, index: int = 0) -> None:
        """Captura la pantalla, marca search_region y trigger, y guarda la imagen."""
        img = self._shooter.capture()
        self._renderer.draw_search_region(img, config.image.search_region)
        self._renderer.draw_trigger(img, config.trigger)
        path = self._saver.save(img, index)
        print(f"[Debug #{index}] Screenshot guardado en: {path}")
