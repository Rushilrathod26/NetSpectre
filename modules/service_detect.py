import socket


def detect_service(ip, port):

    try:

        sock = socket.create_connection(
            (ip, port),
            timeout=2
        )

        # Send basic HTTP request
        if port == 80:
            request = (
                "HEAD / HTTP/1.1\r\n"
                f"Host: {ip}\r\n"
                "Connection: close\r\n\r\n"
            )

            sock.send(request.encode())

        # Receive banner
        banner = sock.recv(1024)

        sock.close()

        if banner:
            return banner.decode(
                errors="ignore"
            ).strip().replace("\n", " ")

        return "Unknown"

    except Exception:
        return "Unknown"
