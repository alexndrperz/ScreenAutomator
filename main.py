import sys

from src.runner.automation_runner import AutomationRunner


def main() -> None:
    """Punto de entrada. Usa config.json por defecto o el path pasado por argumento."""
    json_path = sys.argv[1] if len(sys.argv) > 1 else "config.json"
    runner = AutomationRunner()
    try:
        runner.run(json_path)
    except KeyboardInterrupt:
        print("\n[ScreenAutomator] Detenido por el usuario (Ctrl+C).")


if __name__ == "__main__":
    main()



# Pendiente
# - Falta añadir coordenadas draws a imagen de match + 
# - Hacer precision de imagen target 
# - Primera prueba real con tecnica real 
# - Trigger con captura de pantalla cada x tiempo + 
# - Errores de loops de capturas, control de stop y adicionales + 
