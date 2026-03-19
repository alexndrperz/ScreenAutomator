import threading
import time

import pyautogui

from ..models import ConstantKeyword


class ConstantKeywordWorker:
    """Presiona una combinación de teclas repetidamente en un hilo separado.

    El usuario puede activar/desactivar el worker presionando Enter en la terminal.
    """

    def __init__(self, config: ConstantKeyword) -> None:
        self._config = config
        self._active = threading.Event()
        self._active.set()  # arranca activo
        self._press_thread  = threading.Thread(target=self._run_press,  daemon=True)
        self._toggle_thread = threading.Thread(target=self._run_toggle, daemon=True)

    def start(self) -> None:
        """Lanza los hilos de pulsación y de toggle."""
        keys_str = "+".join(self._config.keys)
        print(f"[KeyboardWorker] Activo — teclas: {keys_str} cada {self._config.interval_seconds}s. Presiona Enter para pausar/reanudar.")
        self._press_thread.start()
        self._toggle_thread.start()

    def _run_press(self) -> None:
        """Presiona las teclas configuradas cada interval_seconds mientras está activo."""
        while True:
            if self._active.is_set():
                pyautogui.hotkey(*self._config.keys)
            time.sleep(self._config.interval_seconds)

    def _run_toggle(self) -> None:
        """Espera un Enter en la terminal y alterna el estado activo/pausado."""
        while True:
            input()
            if self._active.is_set():
                self._active.clear()
                print("[KeyboardWorker] Pausado. Presiona Enter para reanudar.")
            else:
                self._active.set()
                print("[KeyboardWorker] Reanudado. Presiona Enter para pausar.")
