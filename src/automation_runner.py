from .config_loader import ConfigLoader
from .image_locator import ImageLocator
from .click_handler import ClickHandler
from .mouse_controller import MouseController
from .models import AutomationConfig, ImageConfig, TriggerConfig, Waypoint


class AutomationRunner:
    def __init__(self) -> None:
        self._loader = ConfigLoader()
        self._locator = ImageLocator()
        self._mouse = MouseController(ClickHandler())

    def run(self, json_path: str) -> None:
        configs = self._loader.load(json_path)
        for config in configs:
            self._execute(config)

    def _execute(self, config: AutomationConfig) -> None:
        if self._image_found(config.image):
            self._fire(config.trigger)

    def _image_found(self, image_cfg: ImageConfig) -> bool:
        return self._locator.exists_on_screen(image_cfg.path, image_cfg.search_region)

    def _fire(self, trigger: TriggerConfig) -> None:
        target = Waypoint(trigger.x, trigger.y)
        self._mouse.move_to(target, trigger.speed)
        self._mouse.click_at(trigger.x, trigger.y, trigger.click_type)
