import requests


def get_http_headers(target):
    try:
        if not target.startswith(("http://", "https://")):
            target = "http://" + target

        response = requests.get(
            target,
            timeout=5,
            allow_redirects=True
        )

        return {
            "url": response.url,
            "status_code": response.status_code,
            "headers": dict(response.headers)
        }

    except Exception:
        return None
