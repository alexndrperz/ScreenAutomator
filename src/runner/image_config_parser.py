from ..models import ImageConfig
from .search_region_parser import SearchRegionParser


class ImageConfigParser:
    """Convierte el bloque 'image' del JSON en un modelo ImageConfig."""

    def __init__(self) -> None:
        self._region_parser = SearchRegionParser()

    def parse(self, data: dict) -> ImageConfig:
        """Extrae la ruta de imagen y la región de búsqueda opcional.

        Args:
            data: Dict con la clave 'path' y opcionalmente 'search_region'.

        Returns:
            Instancia de ImageConfig. search_region será None si no está en el JSON.
        """
        region_data = data.get("search_region")
        return ImageConfig(
            path=data["path"],
            search_region=self._region_parser.parse(region_data) if region_data else None
        )
