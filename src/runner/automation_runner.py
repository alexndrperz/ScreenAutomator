import time

from ..models import AutomationConfig, ImageConfig, TriggerConfig, Waypoint
from ..debugger.debug_visualizer import DebugVisualizer
from .config_loader import ConfigLoader
from .image_locator import ImageLocator
from .click_handler import ClickHandler
from .mouse_controller import MouseController


ESPERA_ENTRE_CICLOS = 60  # segundos entre repeticiones del ciclo completo


class AutomationRunner:
    """Orquesta la carga del JSON y la ejecución de cada automatización."""

    def __init__(self) -> None:
        self._loader     = ConfigLoader()
        self._locator    = ImageLocator()
        self._mouse      = MouseController(ClickHandler())
        self._visualizer = DebugVisualizer()

    def run(self, json_path: str) -> None:
        """Carga el JSON y repite el ciclo indefinidamente, esperando 1 minuto entre cada pasada."""
        configs = self._loader.load(json_path)
        while True:
            for index, config in enumerate(configs):
                self._execute(config, index)
            self._esperar_ciclo()

    def _esperar_ciclo(self) -> None:
        """Espera 1 minuto antes de reiniciar el ciclo completo."""
        time.sleep(ESPERA_ENTRE_CICLOS)

    def _execute(self, config: AutomationConfig, index: int) -> None:
        """Despacha la automatización: modo debug o ejecución normal."""
        if config.debug:
            self._visualizer.visualize(config, index)
            return
        if self._esperar_imagen(config.image):
            self._fire(config.trigger)

    def _esperar_imagen(self, image_cfg: ImageConfig) -> bool:
        """Espera hasta que la imagen sea visible en pantalla, reintentando cada segundo."""
        return self._locator.esperar_hasta_encontrar(image_cfg.path, image_cfg.search_region)

    def _fire(self, trigger: TriggerConfig) -> None:
        """Mueve el mouse al trigger y ejecuta el click configurado."""
        target = Waypoint(trigger.x, trigger.y)
        self._mouse.move_to(target, trigger.speed)
        self._mouse.click_at(trigger.x, trigger.y, trigger.click_type)
