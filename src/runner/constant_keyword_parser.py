from ..models import ConstantKeyword


class ConstantKeywordParser:
    """Convierte el bloque 'constant_keyword' del JSON en un ConstantKeyword."""

    def parse(self, data: dict) -> ConstantKeyword:
        """Construye un ConstantKeyword desde el dict correspondiente."""
        return ConstantKeyword(
            keys=list(data["keys"]),
            interval_seconds=float(data["interval_seconds"])
        )
