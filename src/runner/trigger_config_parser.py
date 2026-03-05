from ..models import TriggerConfig


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
