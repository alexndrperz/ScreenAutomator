import json
from typing import List, Optional

from .models import SearchRegion, ImageConfig, TriggerConfig, AutomationConfig


class SearchRegionParser:
    """Convierte un dict del JSON en un modelo SearchRegion."""

    def parse(self, data: dict) -> SearchRegion:
        """Construye un SearchRegion a partir de un dict con claves x1/y1/x2/y2.

        Args:
            data: Dict con las claves 'x1', 'y1', 'x2', 'y2'.

        Returns:
            Instancia de SearchRegion con las coordenadas convertidas a float.
        """
        return SearchRegion(
            x1=float(data["x1"]),
            y1=float(data["y1"]),
            x2=float(data["x2"]),
            y2=float(data["y2"])
        )


class ImageConfigParser:
    """Convierte el bloque 'image' del JSON en un modelo ImageConfig."""

    def __init__(self) -> None:
        self._region_parser = SearchRegionParser()

    def parse(self, data: dict) -> ImageConfig:
        """Extrae la ruta de imagen y la región de búsqueda opcional.

        Args:
            data: Dict con la clave 'path' y opcionalmente 'search_region'.

        Returns:
            Instancia de ImageConfig. search_region será None si no está definido en el JSON.
        """
        region_data = data.get("search_region")
        return ImageConfig(
            path=data["path"],
            search_region=self._region_parser.parse(region_data) if region_data else None
        )


class TriggerConfigParser:
    """Convierte el bloque 'trigger' del JSON en un modelo TriggerConfig."""

    def parse(self, data: dict) -> TriggerConfig:
        """Construye un TriggerConfig desde un dict con las propiedades del trigger.

        Args:
            data: Dict con las claves 'x', 'y', 'speed' y 'click_type'.

        Returns:
            Instancia de TriggerConfig con los valores tipados.
        """
        return TriggerConfig(
            x=float(data["x"]),
            y=float(data["y"]),
            speed=float(data["speed"]),
            click_type=data["click_type"]
        )


class ConfigLoader:
    """Lee el archivo JSON y produce la lista de automatizaciones a ejecutar."""

    def __init__(self) -> None:
        self._image_parser = ImageConfigParser()
        self._trigger_parser = TriggerConfigParser()

    def load(self, path: str) -> List[AutomationConfig]:
        """Lee el archivo JSON y retorna todas las configuraciones de automatización.

        Args:
            path: Ruta al archivo JSON que contiene la lista de automatizaciones.

        Returns:
            Lista de AutomationConfig, una por cada objeto del JSON.
        """
        data = self._read_json(path)
        return [self._assemble(item) for item in data]

    def _read_json(self, path: str) -> list:
        """Abre y deserializa el archivo JSON.

        Args:
            path: Ruta al archivo JSON.

        Returns:
            Lista de dicts crudos tal como están en el archivo.
        """
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _assemble(self, data: dict) -> AutomationConfig:
        """Construye un AutomationConfig completo a partir de un objeto del JSON.

        Args:
            data: Dict con las claves 'image' y 'trigger'.

        Returns:
            Instancia de AutomationConfig lista para ejecutar.
        """
        return AutomationConfig(
            image=self._image_parser.parse(data["image"]),
            trigger=self._trigger_parser.parse(data["trigger"])
        )
