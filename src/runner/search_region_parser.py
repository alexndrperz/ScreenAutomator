from ..models import SearchRegion


class SearchRegionParser:
    """Convierte un dict del JSON en un SearchRegion."""

    def parse(self, data: dict) -> SearchRegion:
        """Construye un SearchRegion desde las claves x1/y1/x2/y2 del dict."""
        return SearchRegion(
            x1=float(data["x1"]),
            y1=float(data["y1"]),
            x2=float(data["x2"]),
            y2=float(data["y2"])
        )
