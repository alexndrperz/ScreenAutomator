from typing import Optional, List

import pyautogui

from .models import Waypoint


class ImageLocator:
    CONFIDENCE = 0.85

    def find_center(self, image_path: str, waypoints: List[Waypoint]) -> Optional[Waypoint]:
        region = self._to_region(waypoints) if waypoints else None
        result = self._locate(image_path, region)
        return Waypoint(result.x, result.y) if result else None

    def _to_region(self, waypoints: List[Waypoint]) -> tuple:
        x1 = int(min(wp.x for wp in waypoints))
        y1 = int(min(wp.y for wp in waypoints))
        x2 = int(max(wp.x for wp in waypoints))
        y2 = int(max(wp.y for wp in waypoints))
        return (x1, y1, x2 - x1, y2 - y1)

    def _locate(self, path: str, region: Optional[tuple]) -> Optional[object]:
        try:
            return pyautogui.locateCenterOnScreen(path, confidence=self.CONFIDENCE, region=region)
        except Exception:
            return None
