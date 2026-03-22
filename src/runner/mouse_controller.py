import pyautogui

from ..models import Waypoint
from .click_handler import ClickHandler


class MouseController:
    """Controla el movimiento y los clicks del mouse."""

    def __init__(self, click_handler: ClickHandler) -> None:
        # pyautogui.FAILSAFE = False
        self._clicker = click_handler

    def move_to(self, point: Waypoint, duration: float = 0.3) -> None:
        """Mueve el cursor a la posición indicada con animación."""
        pyautogui.moveTo(point.x, point.y, duration=duration)

    def click_at(self, x: float, y: float, click_type: str) -> None:
        """Ejecuta un click en la posición indicada."""
        self._clicker.perform(x, y, click_type)
