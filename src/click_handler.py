from typing import Callable

import pyautogui


class ClickHandler:
    _ACTIONS: dict = {
        "left":   lambda x, y: pyautogui.click(x, y, button="left"),
        "right":  lambda x, y: pyautogui.click(x, y, button="right"),
        "middle": lambda x, y: pyautogui.click(x, y, button="middle"),
        "double": lambda x, y: pyautogui.doubleClick(x, y),
    }

    def perform(self, x: float, y: float, click_type: str) -> None:
        action = self._resolve_action(click_type)
        action(x, y)

    def _resolve_action(self, click_type: str) -> Callable:
        action = self._ACTIONS.get(click_type.lower())
        if not action:
            raise ValueError(f"Tipo de click desconocido: '{click_type}'")
        return action
