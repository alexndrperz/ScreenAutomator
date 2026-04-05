from ..models import ImageConfig, ImageEntry
from .search_region_parser import SearchRegionParser


class ImageConfigParser:
    """Convierte el bloque 'image' del JSON en un ImageConfig."""

    def __init__(self) -> None:
        self._region_parser = SearchRegionParser()

    def parse(self, data: dict) -> ImageConfig:
        """Extrae las entradas de imagen y la región de búsqueda opcional."""
        region_data = data.get("search_region")
        images = [ImageEntry(id=entry["id"], path=entry["path"]) for entry in data["path"]]
        return ImageConfig(
            images=images,
            search_region=self._region_parser.parse(region_data) if region_data else None
        )
