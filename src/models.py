from dataclasses import dataclass
from typing import Optional


@dataclass
class Waypoint:
    x: float
    y: float


@dataclass
class SearchRegion:
    x1: float  # esquina superior-izquierda
    y1: float  # esquina superior-izquierda
    x2: float  # esquina inferior-derecha
    y2: float  # esquina inferior-derecha


@dataclass
class ImageConfig:
    path: str
    search_region: Optional[SearchRegion] = None


@dataclass
class TriggerConfig:
    x: float
    y: float
    speed: float
    click_type: str


@dataclass
class AutomationConfig:
    image: ImageConfig
    trigger: TriggerConfig
