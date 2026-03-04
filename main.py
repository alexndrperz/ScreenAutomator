import sys

from src.automation_runner import AutomationRunner


def main() -> None:
    """Punto de entrada de la aplicación.

    Lee la ruta del JSON desde el primer argumento de línea de comandos.
    Si no se pasa ninguno, usa 'config.json' por defecto.

    Returns:
        None
    """
    json_path = sys.argv[1] if len(sys.argv) > 1 else "config.json"
    runner = AutomationRunner()
    runner.run(json_path)


if __name__ == "__main__":
    main()
