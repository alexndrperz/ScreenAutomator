import os
from datetime import datetime

from PIL import Image


OUTPUT_DIR = "debug"


class DebugSaver:
    """Guarda imágenes de debug en el directorio de salida del proyecto."""

    def __init__(self, output_dir: str = OUTPUT_DIR) -> None:
        self._output_dir = output_dir

    def save(self, img: Image.Image, index: int, prefix: str = "debug") -> str:
        """Guarda la imagen en debug/ con nombre único basado en timestamp e índice."""
        os.makedirs(self._output_dir, exist_ok=True)
        path = os.path.join(self._output_dir, self._build_filename(index, prefix))
        img.save(path)
        return path

    def _build_filename(self, index: int, prefix: str = "debug") -> str:
        """Genera el nombre del archivo con formato <prefix>_YYYYMMDD_HHMMSS_<index>.png."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{prefix}_{timestamp}_{index}.png"
