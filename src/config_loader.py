import json
from typing import List

from .models import Waypoint, ImageConfig, TriggerConfig, AutomationConfig


class WaypointParser:
    def from_dict(self, data: dict) -> Waypoint:
        return Waypoint(x=data["x"], y=data["y"])

    def from_list(self, items: list) -> List[Waypoint]:
        return [self.from_dict(item) for item in items]


class ImageConfigParser:
    def __init__(self) -> None:
        self._wp = WaypointParser()

    def parse(self, data: dict) -> ImageConfig:
        return ImageConfig(
            path=data["path"],
            waypoints=self._wp.from_list(data.get("waypoints", []))
        )


class TriggerConfigParser:
    def parse(self, data: dict) -> TriggerConfig:
        return TriggerConfig(
            x=float(data["x"]),
            y=float(data["y"]),
            speed=float(data["speed"]),
            click_type=data["click_type"]
        )


class ConfigLoader:
    def __init__(self) -> None:
        self._image_parser = ImageConfigParser()
        self._trigger_parser = TriggerConfigParser()

    def load(self, path: str) -> List[AutomationConfig]:
        data = self._read_json(path)
        return [self._assemble(item) for item in data]

    def _read_json(self, path: str) -> list:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _assemble(self, data: dict) -> AutomationConfig:
        return AutomationConfig(
            image=self._image_parser.parse(data["image"]),
            trigger=self._trigger_parser.parse(data["trigger"])
        )
