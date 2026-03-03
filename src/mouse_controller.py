import pyautogui

from .models import Waypoint
from .click_handler import ClickHandler


class MouseController:
    def __init__(self, click_handler: ClickHandler) -> None:
        self._clicker = click_handler

    def move_to(self, point: Waypoint, duration: float = 0.3) -> None:
        pyautogui.moveTo(point.x, point.y, duration=duration)

    def click_at(self, x: float, y: float, click_type: str) -> None:
        self._clicker.perform(x, y, click_type)
