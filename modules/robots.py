import requests


def get_robots(target):
    try:
        if not target.startswith(("http://", "https://")):
            target = "http://" + target

        url = target.rstrip("/") + "/robots.txt"

        response = requests.get(url, timeout=5)

        lines = []

        if response.status_code == 200:
            for line in response.text.splitlines():
                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                if line.lower().startswith(
                    ("user-agent:", "disallow:", "allow:", "sitemap:")
                ):
                    lines.append(line)

        return {
            "url": url,
            "status_code": response.status_code,
            "entries": lines
        }

    except Exception:
        return None
