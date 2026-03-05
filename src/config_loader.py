import json
from typing import List, Optional

from .models import SearchRegion, ImageConfig, TriggerConfig, AutomationConfig


class SearchRegionParser:
    def parse(self, data: dict) -> SearchRegion:
        return SearchRegion(
            x1=float(data["x1"]),
            y1=float(data["y1"]),
            x2=float(data["x2"]),
            y2=float(data["y2"])
        )


class ImageConfigParser:
    def __init__(self) -> None:
        self._region_parser = SearchRegionParser()

    def parse(self, data: dict) -> ImageConfig:
        region_data = data.get("search_region")
        return ImageConfig(
            path=data["path"],
            search_region=self._region_parser.parse(region_data) if region_data else None
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
            trigger=self._trigger_parser.parse(data["trigger"]),
            debug=bool(data.get("debug", False))
        )
