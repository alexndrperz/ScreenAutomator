import sys

from src.automation_runner import AutomationRunner


def main() -> None:
    json_path = sys.argv[1] if len(sys.argv) > 1 else "config.json"
    runner = AutomationRunner()
    runner.run(json_path)


if __name__ == "__main__":
    main()
