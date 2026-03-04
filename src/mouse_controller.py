import pyautogui

from .models import Waypoint
from .click_handler import ClickHandler


class MouseController:
    """Controla el movimiento y los clicks del mouse usando pyautogui y ClickHandler."""

    def __init__(self, click_handler: ClickHandler) -> None:
        """
        Args:
            click_handler: Instancia de ClickHandler que resuelve los tipos de click.
        """
        self._clicker = click_handler

    def move_to(self, point: Waypoint, duration: float = 0.3) -> None:
        """Mueve el cursor a la posición indicada con una animación de duración configurable.

        Args:
            point:    Coordenadas destino del cursor.
            duration: Tiempo en segundos que tarda el movimiento. Por defecto 0.3s.

        Returns:
            None
        """
        pyautogui.moveTo(point.x, point.y, duration=duration)

    def click_at(self, x: float, y: float, click_type: str) -> None:
        """Ejecuta un click en la posición indicada delegando al ClickHandler.

        Args:
            x:          Coordenada X del click en píxeles.
            y:          Coordenada Y del click en píxeles.
            click_type: Tipo de click ('left', 'right', 'middle', 'double').

        Returns:
            None
        """
        self._clicker.perform(x, y, click_type)
