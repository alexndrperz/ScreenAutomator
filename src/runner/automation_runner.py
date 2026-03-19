import time
from typing import List

from ..models import AutomationConfig, ImageConfig, TriggerConfig, Waypoint
from ..debugger.debug_visualizer import DebugVisualizer
from .config_loader import ConfigLoader
from .image_locator import ImageLocator
from .click_handler import ClickHandler
from .mouse_controller import MouseController
from .constant_keyword_worker import ConstantKeywordWorker


ESPERA_ENTRE_CICLOS = 60  # segundos entre repeticiones del ciclo completo


class AutomationRunner:
    """Orquesta la carga del JSON y la ejecución de cada automatización."""

    def __init__(self) -> None:
        self._loader     = ConfigLoader()
        self._locator    = ImageLocator()
        self._mouse      = MouseController(ClickHandler())
        self._visualizer = DebugVisualizer()

    def run(self, json_path: str) -> None:
        """Carga el JSON, arranca los workers de teclado y repite el ciclo indefinidamente."""
        configs = self._loader.load(json_path)
        self._start_keyword_workers(configs)
        while True:
            for index, config in enumerate(configs):
                self._execute(config, index)
            self._esperar_ciclo()

    def _start_keyword_workers(self, configs: List[AutomationConfig]) -> None:
        """Arranca un ConstantKeywordWorker por cada automatización que lo defina."""
        for config in configs:
            if config.constant_keyword:
                ConstantKeywordWorker(config.constant_keyword).start()

    def _esperar_ciclo(self) -> None:
        """Espera 1 minuto antes de reiniciar el ciclo completo."""
        time.sleep(ESPERA_ENTRE_CICLOS)

    def _execute(self, config: AutomationConfig, index: int) -> None:
        """Despacha la automatización: modo debug o ejecución normal."""
        if config.debug:
            self._visualizer.visualize(config, index)
            return
        if self._esperar_imagen(config.image):
            self._fire_all(config.triggers)

    def _esperar_imagen(self, image_cfg: ImageConfig) -> bool:
        """Espera hasta que la imagen sea visible en pantalla, reintentando cada segundo."""
        return self._locator.esperar_hasta_encontrar(image_cfg.path, image_cfg.search_region)

    def _fire_all(self, triggers: List[TriggerConfig]) -> None:
        """Ejecuta todos los triggers en secuencia, respetando el delay de cada uno."""
        for trigger in triggers:
            if trigger.time > 0:
                time.sleep(trigger.time)
            self._fire(trigger)

    def _fire(self, trigger: TriggerConfig) -> None:
        """Mueve el mouse al trigger y ejecuta el click configurado."""
        target = Waypoint(trigger.x, trigger.y)
        self._mouse.move_to(target, trigger.speed)
        self._mouse.click_at(trigger.x, trigger.y, trigger.click_type)
