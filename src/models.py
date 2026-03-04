from dataclasses import dataclass
from typing import Optional


@dataclass
class Waypoint:
    """Punto de coordenadas usado para posicionar el mouse."""
    x: float
    y: float


@dataclass
class SearchRegion:
    """Rectángulo de pantalla donde se buscará la imagen."""
    x1: float  # esquina superior-izquierda
    y1: float  # esquina superior-izquierda
    x2: float  # esquina inferior-derecha
    y2: float  # esquina inferior-derecha


@dataclass
class ImageConfig:
    """Configuración de la imagen a detectar y la región donde buscarla."""
    path: str
    search_region: Optional[SearchRegion] = None


@dataclass
class TriggerConfig:
    """Define dónde, cómo y a qué velocidad se ejecuta el click."""
    x: float
    y: float
    speed: float
    click_type: str


@dataclass
class AutomationConfig:
    """Agrupa la configuración de imagen y trigger para una automatización."""
    image: ImageConfig
    trigger: TriggerConfig
