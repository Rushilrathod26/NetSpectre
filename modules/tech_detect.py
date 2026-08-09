import requests


def detect_technologies(target):
    try:
        if not target.startswith(("http://", "https://")):
            target = "http://" + target

        response = requests.get(target, timeout=5)

        technologies = []

        headers = response.headers

        server = headers.get("Server")
        powered = headers.get("X-Powered-By")

        if server:
            technologies.append(f"Server: {server}")

        if powered:
            technologies.append(f"Powered-By: {powered}")

        cookies = response.headers.get("Set-Cookie", "")

        if "wordpress" in cookies.lower():
            technologies.append("WordPress")

        if "php" in cookies.lower():
            technologies.append("PHP")

        if "asp.net" in cookies.lower():
            technologies.append("ASP.NET")

        if "cloudflare" in str(headers).lower():
            technologies.append("Cloudflare")

        return {
            "url": target,
            "status_code": response.status_code,
            "technologies": technologies
        }

    except Exception as e:
        return {
            "error": str(e)
        }
