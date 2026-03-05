import os
from datetime import datetime

from PIL import Image


OUTPUT_DIR = "debug"


class DebugSaver:
    """Guarda imágenes de debug en el directorio de salida del proyecto."""

    def __init__(self, output_dir: str = OUTPUT_DIR) -> None:
        """
        Args:
            output_dir: Carpeta donde se guardan los screenshots. Por defecto 'debug/'.
        """
        self._output_dir = output_dir

    def save(self, img: Image.Image, index: int) -> str:
        """Guarda la imagen en el directorio de debug con un nombre único.

        Args:
            img:   Imagen PIL a guardar.
            index: Índice de la automatización dentro de la lista del JSON.

        Returns:
            Ruta completa del archivo PNG guardado.
        """
        os.makedirs(self._output_dir, exist_ok=True)
        path = os.path.join(self._output_dir, self._build_filename(index))
        img.save(path)
        return path

    def _build_filename(self, index: int) -> str:
        """Genera el nombre del archivo con timestamp e índice.

        Args:
            index: Índice de la automatización.

        Returns:
            Nombre de archivo con formato 'debug_YYYYMMDD_HHMMSS_<index>.png'.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"debug_{timestamp}_{index}.png"
