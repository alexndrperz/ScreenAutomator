# Changelog

## [Iteración 2] - 2026-03-25

### Captura al detectar imagen (`CAPTURE_ON_MATCH`)
- Al encontrar la imagen objetivo se toma un screenshot automático con los mismos overlays del modo debug (región de búsqueda + marcadores de triggers con ID).
- Guardado en `debug/` con prefijo `match_` y timestamp completo (`YYYYMMDD_HHMMSS`).
- Controlado por la constante `CAPTURE_ON_MATCH` en `automation_runner.py`.

### Posición de reposo (`center_panel`)
- Nueva opción en el JSON por automatización, mismo formato que un trigger (`x`, `y`, `speed`, `click_type`, `time`).
- Si el delay del próximo trigger supera `CENTER_PANEL_THRESHOLD` (5 s), el mouse se mueve a `center_panel` antes de esperar.
- Nuevo `click_type: "none"` en `ClickHandler` para mover sin hacer click.

### Capturas periódicas limpias (`periodic_capture`)
- Nueva opción en el JSON por automatización: `{ "interval_seconds": N }`.
- Lanza un thread daemon (`PeriodicCaptureWorker`) que captura pantalla sin overlays cada N segundos.
- Guardado en `debug/` con prefijo `periodic_`. Si la propiedad no está en el JSON no se ejecuta nada.

### Debug sin loop infinito
- Las configs con `debug: true` ahora corren la visualización exactamente una vez.
- Se usa un `Set[int]` interno (`_debug_done`) para trackear los índices ya ejecutados.

### Control de salida con Ctrl+C
- `main.py` captura `KeyboardInterrupt` y termina limpiamente con un mensaje en consola.

### Otros
- `DebugSaver.save()` acepta parámetro `prefix` (default `"debug"`) para reutilización en distintos contextos.
- `_start_keyword_workers` renombrado a `_start_workers`, ahora también arranca los `PeriodicCaptureWorker`.
- `AutomationRunner` ya no instancia `Screenshooter` ni `DebugSaver` directamente; delega en `DebugVisualizer`.
