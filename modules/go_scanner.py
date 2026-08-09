import json
import subprocess
from core.services import get_service_name


def run_go_scanner(target, ports):
    command = [
        "./engine/scanner",
        "--target", target,
        "--ports", ports
    ]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )

        scan = json.loads(result.stdout)

        if scan["open_ports"] is None:
            scan["open_ports"] = []

        for item in scan["open_ports"]:
            if item["service"] == "unknown":
                item["service"] = get_service_name(item["port"])

        return scan

    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Go Scanner Failed:\n{e.stderr}")
        return None

    except json.JSONDecodeError:
        print("[ERROR] Invalid JSON received from Go scanner.")
        return None
