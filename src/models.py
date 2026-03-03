from dataclasses import dataclass, field
from typing import List


@dataclass
class Waypoint:
    x: float
    y: float


@dataclass
class ImageConfig:
    path: str
    waypoints: List[Waypoint] = field(default_factory=list)


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
