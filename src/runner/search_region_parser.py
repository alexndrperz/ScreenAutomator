from ..models import SearchRegion


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
