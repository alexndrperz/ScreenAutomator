# PyAutoGUI Automation

Herramienta de automatización de mouse impulsada por JSON usando PyAutoGUI.
Detecta imágenes en una región de pantalla y ejecuta eventos de click configurables.

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

| Propiedad                    | Tipo     | Descripción                                                        |
|------------------------------|----------|--------------------------------------------------------------------|
| `image.path`                 | `string` | Ruta al archivo de imagen a detectar en pantalla                   |
| `image.search_region.x1`     | `number` | Coordenada X de la esquina superior-izquierda de la región         |
| `image.search_region.y1`     | `number` | Coordenada Y de la esquina superior-izquierda de la región         |
| `image.search_region.x2`     | `number` | Coordenada X de la esquina inferior-derecha de la región           |
| `image.search_region.y2`     | `number` | Coordenada Y de la esquina inferior-derecha de la región           |
| `trigger.x`                  | `number` | Coordenada X donde se mueve el mouse y se ejecuta el click         |
| `trigger.y`                  | `number` | Coordenada Y donde se mueve el mouse y se ejecuta el click         |
| `trigger.speed`              | `number` | Duración del movimiento del mouse hacia el trigger (segundos)      |
| `trigger.click_type`         | `string` | Tipo de click: `left`, `right`, `middle`, `double`                 |

> `search_region` es opcional. Si se omite, la búsqueda se realiza en toda la pantalla.

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

1. **Busca** la imagen (`image.path`) dentro de la región definida por `search_region`
2. Si la encuentra, **mueve** el mouse a `(trigger.x, trigger.y)` con `trigger.speed`
3. **Ejecuta** el click en esa posición con `trigger.click_type`

---

## Arquitectura

```
AutomationRunner
├── ConfigLoader           ← lee JSON y construye los modelos
│   ├── ImageConfigParser
│   │   └── SearchRegionParser
│   └── TriggerConfigParser
├── ImageLocator           ← busca la imagen en la región de pantalla
└── MouseController        ← mueve el mouse y dispara clicks
    └── ClickHandler       ← resuelve el tipo de click
```
