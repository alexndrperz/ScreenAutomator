from .config_loader import ConfigLoader
from .image_locator import ImageLocator
from .click_handler import ClickHandler
from .mouse_controller import MouseController
from .models import AutomationConfig, ImageConfig, TriggerConfig, Waypoint


class AutomationRunner:
    """Orquesta la carga del JSON y la ejecución de cada automatización."""

    def __init__(self) -> None:
        self._loader = ConfigLoader()
        self._locator = ImageLocator()
        self._mouse = MouseController(ClickHandler())

    def run(self, json_path: str) -> None:
        """Carga el JSON y ejecuta cada automatización en orden.

        Args:
            json_path: Ruta al archivo JSON con la lista de automatizaciones.

        Returns:
            None
        """
        configs = self._loader.load(json_path)
        for config in configs:
            self._execute(config)

    def _execute(self, config: AutomationConfig) -> None:
        """Ejecuta una automatización: dispara el trigger solo si la imagen es encontrada.

        Args:
            config: Configuración completa con imagen y trigger.

        Returns:
            None
        """
        if self._image_found(config.image):
            self._fire(config.trigger)

    def _image_found(self, image_cfg: ImageConfig) -> bool:
        """Verifica si la imagen está visible en la región de pantalla configurada.

        Args:
            image_cfg: Configuración de la imagen con ruta y región de búsqueda.

        Returns:
            True si la imagen fue encontrada en pantalla, False en caso contrario.
        """
        return self._locator.exists_on_screen(image_cfg.path, image_cfg.search_region)

    def _fire(self, trigger: TriggerConfig) -> None:
        """Mueve el mouse a la posición del trigger y ejecuta el click configurado.

        Args:
            trigger: Configuración con coordenadas, velocidad y tipo de click.

        Returns:
            None
        """
        target = Waypoint(trigger.x, trigger.y)
        self._mouse.move_to(target, trigger.speed)
        self._mouse.click_at(trigger.x, trigger.y, trigger.click_type)
