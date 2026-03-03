# PyAutoGUI Automation

Herramienta de automatización de mouse impulsada por JSON usando PyAutoGUI.
Detecta imágenes en pantalla, recorre waypoints y ejecuta eventos de click configurables.

---

## Estructura del proyecto

```
prueba/
├── main.py                   # Punto de entrada
├── config.json               # Lista de automatizaciones
├── README.md
└── src/
    ├── models.py             # Modelos de datos (dataclasses)
    ├── config_loader.py      # Parseo del JSON
    ├── image_locator.py      # Detección de imagen en pantalla
    ├── click_handler.py      # Resolución del tipo de click
    ├── mouse_controller.py   # Movimiento y clicks del mouse
    └── automation_runner.py  # Orquestador principal
```

---

## Instalación

```bash
pip install pyautogui opencv-python
```

> `opencv-python` es necesario para usar el parámetro `confidence` en la detección de imágenes.

---

## Uso

```bash
# Usa config.json por defecto
python main.py

# Usa un archivo JSON específico
python main.py ruta/mi_config.json
```

---

## Formato del JSON

El archivo de configuración es una **lista** de objetos de automatización.
Cada objeto representa una secuencia independiente que se ejecuta en orden.

```json
[
  {
    "image": {
      "path": "assets/target.png",
      "waypoints": [
        { "x": 200, "y": 300 },
        { "x": 400, "y": 300 },
        { "x": 400, "y": 500 }
      ]
    },
    "trigger": {
      "x": 960,
      "y": 540,
      "speed": 0.4,
      "click_type": "left"
    }
  }
]
```

### Propiedades

| Propiedad           | Tipo     | Descripción                                              |
|---------------------|----------|----------------------------------------------------------|
| `image.path`        | `string` | Ruta al archivo de imagen a detectar en pantalla         |
| `image.waypoints`   | `array`  | Lista de coordenadas `{x, y}` que recorrerá el mouse     |
| `trigger.x`         | `number` | Coordenada X donde se ejecuta el click final             |
| `trigger.y`         | `number` | Coordenada Y donde se ejecuta el click final             |
| `trigger.speed`     | `number` | Duración del movimiento entre puntos (segundos)          |
| `trigger.click_type`| `string` | Tipo de click: `left`, `right`, `middle`, `double`       |

### Tipos de click

| Valor    | Descripción           |
|----------|-----------------------|
| `left`   | Click izquierdo       |
| `right`  | Click derecho         |
| `middle` | Click con rueda       |
| `double` | Doble click izquierdo |

---

## Flujo de ejecución

Por cada objeto en el JSON:

1. **Detecta** la imagen en pantalla usando `image.path`
2. Si la encuentra, **mueve** el mouse a esa posición
3. **Recorre** los `waypoints` en orden con la velocidad `trigger.speed`
4. **Ejecuta** el click en `(trigger.x, trigger.y)` con `trigger.click_type`

---

## Arquitectura

```
AutomationRunner
├── ConfigLoader          ← lee JSON y construye los modelos
│   ├── ImageConfigParser
│   │   └── WaypointParser
│   └── TriggerConfigParser
├── ImageLocator          ← busca la imagen en pantalla
└── MouseController       ← mueve el mouse y dispara clicks
    └── ClickHandler      ← resuelve el tipo de click
```
