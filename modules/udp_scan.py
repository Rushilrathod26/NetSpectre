import socket
import time


def scan_udp(target, ports):
    """
    Basic UDP scanner.
    ports: list of UDP port numbers
    """

    results = []

    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        return results

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1)

        start = time.perf_counter()

        try:
            sock.sendto(b"\x00", (ip, port))

            try:
                data, address = sock.recvfrom(1024)

                elapsed = round(
                    (time.perf_counter() - start) * 1000,
                    2
                )

                results.append({
                    "port": port,
                    "state": "open",
                    "response_time": elapsed
                })

            except socket.timeout:
                # UDP timeout means open|filtered.
                results.append({
                    "port": port,
                    "state": "open|filtered",
                    "response_time": None
                })

        except OSError:
            pass

        finally:
            sock.close()

    return results
