# PyAutoGUI Automation

Herramienta de automatización de mouse impulsada por JSON usando PyAutoGUI.
Detecta imágenes en una región de pantalla y ejecuta eventos de click configurables.

---

## Estructura del proyecto

```
prueba/
├── main.py                              # Punto de entrada
├── config.json                          # Lista de automatizaciones
├── .gitignore
├── README.md
├── debug/                               # Screenshots generados en modo debug (ignorado por git)
└── src/
    ├── models.py                        # Modelos de datos compartidos (dataclasses)
    ├── runner/                          # Lógica de ejecución de automatizaciones
    │   ├── search_region_parser.py      # Parsea el bloque search_region del JSON
    │   ├── image_config_parser.py       # Parsea el bloque image del JSON
    │   ├── trigger_config_parser.py     # Parsea el bloque trigger del JSON
    │   ├── config_loader.py             # Carga el archivo JSON completo
    │   ├── image_locator.py             # Detecta imagen en pantalla
    │   ├── click_handler.py             # Resuelve y ejecuta el tipo de click
    │   ├── mouse_controller.py          # Controla movimiento y clicks del mouse
    │   └── automation_runner.py         # Orquestador principal
    └── debugger/                        # Lógica del modo debug
        ├── screenshooter.py             # Captura la pantalla
        ├── region_renderer.py           # Dibuja rectángulos sobre la imagen
        ├── debug_saver.py               # Guarda el screenshot en debug/
        └── debug_visualizer.py          # Orquesta el flujo de debug
```

---

## Instalación

```bash
pip install pyautogui opencv-python Pillow
```

> - `opencv-python` es necesario para el parámetro `confidence` en la detección de imágenes.
> - `Pillow` es necesario para el modo debug (captura y dibujo de regiones).

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
    "debug": false,
    "image": {
      "path": "assets/target.png",
      "search_region": {
        "x1": 100,
        "y1": 100,
        "x2": 800,
        "y2": 600
      }
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

| Propiedad                    | Tipo      | Descripción                                                        |
|------------------------------|-----------|--------------------------------------------------------------------|
| `debug`                      | `boolean` | Si es `true`, activa el modo debug (ver sección Debug)             |
| `image.path`                 | `string`  | Ruta al archivo de imagen a detectar en pantalla                   |
| `image.search_region.x1`     | `number`  | Coordenada X de la esquina superior-izquierda de la región         |
| `image.search_region.y1`     | `number`  | Coordenada Y de la esquina superior-izquierda de la región         |
| `image.search_region.x2`     | `number`  | Coordenada X de la esquina inferior-derecha de la región           |
| `image.search_region.y2`     | `number`  | Coordenada Y de la esquina inferior-derecha de la región           |
| `trigger.x`                  | `number`  | Coordenada X donde se mueve el mouse y se ejecuta el click         |
| `trigger.y`                  | `number`  | Coordenada Y donde se mueve el mouse y se ejecuta el click         |
| `trigger.speed`              | `number`  | Duración del movimiento del mouse hacia el trigger (segundos)      |
| `trigger.click_type`         | `string`  | Tipo de click: `left`, `right`, `middle`, `double`                 |

> `search_region` es opcional. Si se omite, la búsqueda se realiza en toda la pantalla.

### Tipos de click

| Valor    | Descripción           |
|----------|-----------------------|
| `left`   | Click izquierdo       |
| `right`  | Click derecho         |
| `middle` | Click con rueda       |
| `double` | Doble click izquierdo |

---

## Modo Debug

Cuando `"debug": true`, la automatización **no ejecuta** el click. En su lugar:

1. Toma un screenshot de la pantalla en ese momento
2. Dibuja un **rectángulo verde** sobre el área de `search_region` (zona de búsqueda)
3. Dibuja un **rectángulo azul** centrado en `(trigger.x, trigger.y)` (destino del click)
4. Guarda la imagen en la carpeta `debug/` con el formato `debug_YYYYMMDD_HHMMSS_<index>.png`

```
debug/
└── debug_20260305_142301_0.png
```

> Los archivos de `debug/` están excluidos del repositorio por `.gitignore`.

---

## Flujo de ejecución

```
Para cada automatización en el JSON:
│
├── debug: true
│     └── Screenshot + marcado visual → guarda en debug/ → fin
│
└── debug: false
      ├── Busca imagen en search_region
      ├── Si NO la encuentra → fin
      └── Si la encuentra → mueve mouse a trigger → ejecuta click
```

---

## Arquitectura

```
src/
├── models.py                    (compartido por runner y debugger)
│
├── runner/
│   ├── AutomationRunner         ← orquestador principal
│   ├── ConfigLoader             ← ensambla la config desde el JSON
│   │   ├── ImageConfigParser
│   │   │   └── SearchRegionParser
│   │   └── TriggerConfigParser
│   ├── ImageLocator             ← busca la imagen en pantalla
│   └── MouseController          ← mueve el mouse y dispara clicks
│       └── ClickHandler         ← resuelve el tipo de click
│
└── debugger/
    ├── DebugVisualizer          ← orquesta el flujo de debug
    ├── Screenshooter            ← captura la pantalla
    ├── RegionRenderer           ← dibuja rectángulos verde y azul
    └── DebugSaver               ← guarda el PNG en debug/
```
