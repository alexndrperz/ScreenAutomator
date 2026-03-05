from ..models import ImageConfig
from .search_region_parser import SearchRegionParser


class ImageConfigParser:
    """Convierte el bloque 'image' del JSON en un ImageConfig."""

    def __init__(self) -> None:
        self._region_parser = SearchRegionParser()

    def parse(self, data: dict) -> ImageConfig:
        """Extrae la ruta de imagen y la región de búsqueda opcional."""
        region_data = data.get("search_region")
        return ImageConfig(
            path=data["path"],
            search_region=self._region_parser.parse(region_data) if region_data else None
        )
