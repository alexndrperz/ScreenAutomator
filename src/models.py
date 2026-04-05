from dataclasses import dataclass, field
from typing import List, Optional


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
class ImageEntry:
    """Par identificador + ruta de una imagen a detectar."""
    id: str
    path: str


@dataclass
class ImageConfig:
    """Configuración de la/s imagen/es a detectar en pantalla."""
    images: List[ImageEntry]
    search_region: Optional[SearchRegion] = None


@dataclass
class TriggerConfig:
    """Define la posición, velocidad, tipo del evento click y delay previo a ejecutar."""
    x: float
    y: float
    speed: float
    click_type: str
    time: float = 0          # segundos de espera desde el trigger anterior
    just_when_see: Optional[str] = None  # id de imagen requerida; None = indiferente


@dataclass
class ConstantKeyword:
    """Combinación de teclas a presionar repetidamente en segundo plano."""
    keys: List[str]
    interval_seconds: float


@dataclass
class PeriodicCapture:
    """Captura limpia de pantalla cada N segundos en segundo plano."""
    interval_seconds: float


@dataclass
class AutomationConfig:
    """Configuración completa de una automatización: imagen, triggers y modo debug."""
    image: ImageConfig
    triggers: List[TriggerConfig]
    debug: bool = False
    constant_keyword: Optional[ConstantKeyword] = None
    center_panel: Optional[TriggerConfig] = None
    periodic_capture: Optional[PeriodicCapture] = None
    max_runs: Optional[int] = None  # ciclos máximos; None = sin límite
