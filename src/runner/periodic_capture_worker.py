import threading
import time

from ..models import PeriodicCapture
from ..debugger.screenshooter import Screenshooter
from ..debugger.debug_saver import DebugSaver


class PeriodicCaptureWorker:
    """Captura la pantalla limpia (sin overlays) cada N segundos en un hilo separado."""

    def __init__(self, config: PeriodicCapture, index: int) -> None:
        self._config  = config
        self._index   = index
        self._shooter = Screenshooter()
        self._saver   = DebugSaver()
        self._thread  = threading.Thread(target=self._run, daemon=True)

    def start(self) -> None:
        print(f"[PeriodicCapture #{self._index}] Activo — captura cada {self._config.interval_seconds}s.")
        self._thread.start()

    def _run(self) -> None:
        while True:
            time.sleep(self._config.interval_seconds)
            img  = self._shooter.capture()
            path = self._saver.save(img, self._index, prefix="periodic")
            print(f"[PeriodicCapture #{self._index}] Captura guardada en: {path}")
