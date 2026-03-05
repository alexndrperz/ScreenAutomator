import json
from typing import List

from ..models import AutomationConfig
from .image_config_parser import ImageConfigParser
from .trigger_config_parser import TriggerConfigParser


class ConfigLoader:
    """Lee el archivo JSON y produce la lista de automatizaciones a ejecutar."""

    def __init__(self) -> None:
        self._image_parser   = ImageConfigParser()
        self._trigger_parser = TriggerConfigParser()

    def load(self, path: str) -> List[AutomationConfig]:
        """Lee el archivo JSON y retorna todas las configuraciones de automatización.

        Args:
            path: Ruta al archivo JSON con la lista de automatizaciones.

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
            data: Dict con las claves 'image', 'trigger' y opcionalmente 'debug'.

        Returns:
            Instancia de AutomationConfig lista para ejecutar.
        """
        return AutomationConfig(
            image=self._image_parser.parse(data["image"]),
            trigger=self._trigger_parser.parse(data["trigger"]),
            debug=bool(data.get("debug", False))
        )
