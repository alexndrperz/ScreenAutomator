import time
from typing import List, Optional, Set

from ..models import AutomationConfig, ImageConfig, TriggerConfig, Waypoint
from ..debugger.debug_visualizer import DebugVisualizer
from .config_loader import ConfigLoader
from .image_locator import ImageLocator
from .click_handler import ClickHandler
from .mouse_controller import MouseController
from .constant_keyword_worker import ConstantKeywordWorker
from .periodic_capture_worker import PeriodicCaptureWorker


ESPERA_ENTRE_CICLOS    = 0     # segundos entre repeticiones del ciclo completo
CAPTURE_ON_MATCH       = True  # captura pantalla cada vez que se detecta la imagen
CENTER_PANEL_THRESHOLD = 5     # segundos; si el próximo trigger está a más de esto, ir a center_panel


class AutomationRunner:
    """Orquesta la carga del JSON y la ejecución de cada automatización."""

    def __init__(self) -> None:
        self._loader        = ConfigLoader()
        self._locator       = ImageLocator()
        self._mouse         = MouseController(ClickHandler())
        self._visualizer    = DebugVisualizer()
        self._debug_done: Set[int] = set()  # índices de configs debug ya ejecutados

    def run(self, json_path: str) -> None:
        """Carga el JSON, arranca los workers y repite el ciclo indefinidamente."""
        configs = self._loader.load(json_path)
        self._start_workers(configs)
        while True:
            for index, config in enumerate(configs):
                self._execute(config, index)
            self._esperar_ciclo()

    def _start_workers(self, configs: List[AutomationConfig]) -> None:
        """Arranca los workers de teclado y captura periódica por cada automatización que los defina."""
        for index, config in enumerate(configs):
            if config.constant_keyword:
                ConstantKeywordWorker(config.constant_keyword).start()
            if config.periodic_capture:
                PeriodicCaptureWorker(config.periodic_capture, index).start()

    def _esperar_ciclo(self) -> None:
        """Espera antes de reiniciar el ciclo completo."""
        time.sleep(ESPERA_ENTRE_CICLOS)

    def _execute(self, config: AutomationConfig, index: int) -> None:
        """Despacha la automatización: modo debug (una vez) o ejecución normal."""
        if config.debug:
            if index not in self._debug_done:
                self._visualizer.visualize(config, index)
                self._debug_done.add(index)
            return
        if self._esperar_imagen(config.image):
            if CAPTURE_ON_MATCH:
                self._capture_match(config, index)
            self._fire_all(config.triggers, config.center_panel)

    def _esperar_imagen(self, image_cfg: ImageConfig) -> bool:
        """Espera hasta que la imagen sea visible en pantalla, reintentando cada segundo."""
        return self._locator.esperar_hasta_encontrar(image_cfg.path, image_cfg.search_region)

    def _capture_match(self, config: AutomationConfig, index: int) -> None:
        """Captura la pantalla al detectar imagen, con los mismos overlays que el modo debug."""
        self._visualizer.capture_match(config, index)

    def _fire_all(self, triggers: List[TriggerConfig], center_panel: Optional[TriggerConfig] = None) -> None:
        """Ejecuta todos los triggers en secuencia, respetando el delay de cada uno.

        Si el delay de un trigger supera CENTER_PANEL_THRESHOLD segundos y hay center_panel
        configurado, mueve el mouse a esa posición de espera antes de dormir.
        """
        for trigger in triggers:
            if trigger.time > 0:
                if center_panel and trigger.time > CENTER_PANEL_THRESHOLD:
                    self._mouse.move_to(Waypoint(center_panel.x, center_panel.y), center_panel.speed)
                time.sleep(trigger.time)
            self._fire(trigger)

    def _fire(self, trigger: TriggerConfig) -> None:
        """Mueve el mouse al trigger y ejecuta el click configurado."""
        target = Waypoint(trigger.x, trigger.y)
        self._mouse.move_to(target, trigger.speed)
        self._mouse.click_at(trigger.x, trigger.y, trigger.click_type)
