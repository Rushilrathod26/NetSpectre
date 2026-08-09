import socket
import ssl


def get_ssl_info(target):
    try:
        target = target.replace("https://", "").replace("http://", "")
        target = target.split("/")[0]

        context = ssl.create_default_context()

        with socket.create_connection((target, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=target) as ssock:

                cert = ssock.getpeercert()

                subject = dict(x[0] for x in cert.get("subject", []))
                issuer = dict(x[0] for x in cert.get("issuer", []))

                return {
                    "hostname": target,
                    "tls_version": ssock.version(),
                    "cipher": ssock.cipher()[0],
                    "subject": subject,
                    "issuer": issuer,
                    "valid_from": cert.get("notBefore"),
                    "valid_until": cert.get("notAfter")
                }

    except Exception as e:
        return {
            "error": str(e)
        }
