from dataclasses import dataclass
from typing import Optional


@dataclass
class Waypoint:
    """Punto de coordenadas en pantalla usado para posicionar el mouse.

    Attributes:
        x: Coordenada horizontal en píxeles.
        y: Coordenada vertical en píxeles.
    """
    x: float
    y: float


@dataclass
class SearchRegion:
    """Rectángulo de pantalla que delimita el área de búsqueda de una imagen.

    Attributes:
        x1: Coordenada X de la esquina superior-izquierda.
        y1: Coordenada Y de la esquina superior-izquierda.
        x2: Coordenada X de la esquina inferior-derecha.
        y2: Coordenada Y de la esquina inferior-derecha.
    """
    x1: float
    y1: float
    x2: float
    y2: float


@dataclass
class ImageConfig:
    """Configuración de la imagen a detectar en pantalla.

    Attributes:
        path:          Ruta al archivo de imagen que se buscará.
        search_region: Región de pantalla donde buscar. Si es None, busca en toda la pantalla.
    """
    path: str
    search_region: Optional[SearchRegion] = None


@dataclass
class TriggerConfig:
    """Define la posición, velocidad y tipo del evento click a ejecutar.

    Attributes:
        x:          Coordenada X del destino del click.
        y:          Coordenada Y del destino del click.
        speed:      Duración en segundos del movimiento del mouse hacia el destino.
        click_type: Tipo de click: 'left', 'right', 'middle' o 'double'.
    """
    x: float
    y: float
    speed: float
    click_type: str


@dataclass
class AutomationConfig:
    """Agrupa la configuración completa de una automatización (imagen + trigger).

    Attributes:
        image:   Configuración de la imagen a detectar.
        trigger: Configuración del evento click a ejecutar si la imagen es encontrada.
    """
    image: ImageConfig
    trigger: TriggerConfig
