from ..models import PeriodicCapture


class PeriodicCaptureParser:
    """Convierte el bloque 'periodic_capture' del JSON en un PeriodicCapture."""

    def parse(self, data: dict) -> PeriodicCapture:
        return PeriodicCapture(
            interval_seconds=float(data["interval_seconds"])
        )
