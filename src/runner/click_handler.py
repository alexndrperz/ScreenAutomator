from typing import Callable

import pyautogui


class ClickHandler:
    """Resuelve y ejecuta el tipo de click indicado sobre una posición de pantalla."""

    _ACTIONS: dict = {
        "left":   lambda x, y: pyautogui.click(x, y, button="left"),
        "right":  lambda x, y: pyautogui.click(x, y, button="right"),
        "middle": lambda x, y: pyautogui.click(x, y, button="middle"),
        "double": lambda x, y: pyautogui.doubleClick(x, y),
        "none":   lambda x, y: None,
    }

    def perform(self, x: float, y: float, click_type: str) -> None:
        """Ejecuta el click del tipo indicado en la posición dada."""
        action = self._resolve_action(click_type)
        action(x, y)

    def _resolve_action(self, click_type: str) -> Callable:
        """Obtiene la función de pyautogui correspondiente al tipo de click."""
        action = self._ACTIONS.get(click_type.lower())
        if not action:
            raise ValueError(f"Tipo de click desconocido: '{click_type}'")
        return action
