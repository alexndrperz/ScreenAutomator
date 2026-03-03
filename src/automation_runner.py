from .config_loader import ConfigLoader
from .image_locator import ImageLocator
from .click_handler import ClickHandler
from .mouse_controller import MouseController
from .models import AutomationConfig, ImageConfig, TriggerConfig


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
        self._go_to_image(config.image)
        self._trace_waypoints(config.image, config.trigger.speed)
        self._fire(config.trigger)

    def _go_to_image(self, image_cfg: ImageConfig) -> None:
        location = self._locator.find_center(image_cfg.path)
        if location:
            self._mouse.move_to(location)

    def _trace_waypoints(self, image_cfg: ImageConfig, speed: float) -> None:
        self._mouse.trace_path(image_cfg.waypoints, speed)

    def _fire(self, trigger: TriggerConfig) -> None:
        self._mouse.click_at(trigger.x, trigger.y, trigger.click_type)
