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
# - Problema de que ante errores graves el programa se quede iterando
# - Primera prueba real con tecnica real  
# - Numero maximo tabs es 9
