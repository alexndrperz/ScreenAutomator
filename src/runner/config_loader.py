import json
from typing import List

from ..models import AutomationConfig
from .image_config_parser import ImageConfigParser
from .trigger_config_parser import TriggerConfigParser
from .constant_keyword_parser import ConstantKeywordParser
from .periodic_capture_parser import PeriodicCaptureParser


class ConfigLoader:
    """Lee el archivo JSON y produce la lista de automatizaciones a ejecutar."""

    def __init__(self) -> None:
        self._image_parser    = ImageConfigParser()
        self._trigger_parser  = TriggerConfigParser()
        self._keyword_parser  = ConstantKeywordParser()
        self._periodic_parser = PeriodicCaptureParser()

    def load(self, path: str) -> List[AutomationConfig]:
        """Carga el JSON y retorna todas las configuraciones de automatización."""
        data = self._read_json(path)
        return [self._assemble(item) for item in data]

    def _read_json(self, path: str) -> list:
        """Abre y deserializa el archivo JSON."""
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _assemble(self, data: dict) -> AutomationConfig:
        """Construye un AutomationConfig completo desde un objeto del JSON."""
        triggers = [self._trigger_parser.parse(t) for t in data["triggers"]]
        keyword_data = data.get("constant_keyword")
        center_panel_data   = data.get("center_panel")
        periodic_data       = data.get("periodic_capture")
        return AutomationConfig(
            image=self._image_parser.parse(data["image"]),
            triggers=triggers,
            debug=bool(data.get("debug", False)),
            constant_keyword=self._keyword_parser.parse(keyword_data) if keyword_data else None,
            center_panel=self._trigger_parser.parse(center_panel_data) if center_panel_data else None,
            periodic_capture=self._periodic_parser.parse(periodic_data) if periodic_data else None
        )
