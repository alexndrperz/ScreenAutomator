import sys

from src.runner.automation_runner import AutomationRunner


def main() -> None:
    """Punto de entrada. Usa config.json por defecto o el path pasado por argumento."""
    json_path = sys.argv[1] if len(sys.argv) > 1 else "config.json"
    runner = AutomationRunner()
    runner.run(json_path)


if __name__ == "__main__":
    main()



# Observaciones:
# - Se debe añadir un trigger que haga cambio a temp 5m 
# - Al momento del click debe tirar un cap 
# - Debe haber otros tiggers que mueven el mouse de los botones