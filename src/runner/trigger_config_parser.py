from ..models import TriggerConfig


class TriggerConfigParser:
    """Convierte el bloque 'trigger' del JSON en un TriggerConfig."""

    def parse(self, data: dict) -> TriggerConfig:
        """Construye un TriggerConfig desde el dict del trigger."""
        return TriggerConfig(
            x=float(data["x"]),
            y=float(data["y"]),
            speed=float(data["speed"]),
            click_type=data["click_type"]
        )
