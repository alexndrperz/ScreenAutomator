from dataclasses import dataclass
from typing import Optional


@dataclass
class Waypoint:
    """Punto de coordenadas en pantalla."""
    x: float
    y: float


@dataclass
class SearchRegion:
    """Rectángulo que delimita el área de búsqueda de imagen en pantalla."""
    x1: float  # esquina superior-izquierda
    y1: float  # esquina superior-izquierda
    x2: float  # esquina inferior-derecha
    y2: float  # esquina inferior-derecha


@dataclass
class ImageConfig:
    """Configuración de la imagen a detectar en pantalla."""
    path: str
    search_region: Optional[SearchRegion] = None


@dataclass
class TriggerConfig:
    """Define la posición, velocidad y tipo del evento click a ejecutar."""
    x: float
    y: float
    speed: float
    click_type: str


@dataclass
class AutomationConfig:
    """Configuración completa de una automatización: imagen, trigger y modo debug."""
    image: ImageConfig
    trigger: TriggerConfig
    debug: bool = False
