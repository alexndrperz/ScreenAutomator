from ..models import AutomationConfig, ImageConfig, TriggerConfig, Waypoint
from ..debugger.debug_visualizer import DebugVisualizer
from .config_loader import ConfigLoader
from .image_locator import ImageLocator
from .click_handler import ClickHandler
from .mouse_controller import MouseController


class AutomationRunner:
    """Orquesta la carga del JSON y la ejecución de cada automatización."""

    def __init__(self) -> None:
        self._loader     = ConfigLoader()
        self._locator    = ImageLocator()
        self._mouse      = MouseController(ClickHandler())
        self._visualizer = DebugVisualizer()

    def run(self, json_path: str) -> None:
        """Carga el JSON y ejecuta cada automatización en orden."""
        configs = self._loader.load(json_path)
        for index, config in enumerate(configs):
            self._execute(config, index)

    def _execute(self, config: AutomationConfig, index: int) -> None:
        """Despacha la automatización: modo debug o ejecución normal."""
        if config.debug:
            self._visualizer.visualize(config, index)
            return
        if self._image_found(config.image):
            self._fire(config.trigger)

    def _image_found(self, image_cfg: ImageConfig) -> bool:
        """Verifica si la imagen está visible en la región de pantalla configurada."""
        return self._locator.exists_on_screen(image_cfg.path, image_cfg.search_region)

    def _fire(self, trigger: TriggerConfig) -> None:
        """Mueve el mouse al trigger y ejecuta el click configurado."""
        target = Waypoint(trigger.x, trigger.y)
        self._mouse.move_to(target, trigger.speed)
        self._mouse.click_at(trigger.x, trigger.y, trigger.click_type)
