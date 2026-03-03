from typing import Optional

import pyautogui

from .models import Waypoint


class ImageLocator:
    CONFIDENCE = 0.85

    def find_center(self, image_path: str) -> Optional[Waypoint]:
        result = self._locate(image_path)
        return Waypoint(result.x, result.y) if result else None

    def _locate(self, path: str) -> Optional[object]:
        try:
            return pyautogui.locateCenterOnScreen(path, confidence=self.CONFIDENCE)
        except Exception:
            return None
