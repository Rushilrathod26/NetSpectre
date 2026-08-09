import socket


def dns_lookup(target):
    try:
        hostname = target

        # Reverse lookup if target is an IP
        try:
            ip = socket.gethostbyname(target)
        except socket.gaierror:
            return None

        try:
            reverse_name = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            reverse_name = "Unknown"

        return {
            "hostname": hostname,
            "ip": ip,
            "reverse_dns": reverse_name
        }

    except Exception:
        return None
