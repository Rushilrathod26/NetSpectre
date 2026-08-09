from scapy.all import IP, TCP, sr1
import socket


def collect_fingerprint(target):
    try:
        ip = socket.gethostbyname(target)

        # Try common TCP ports.
        probe_ports = [80, 443, 445, 135, 22]

        for port in probe_ports:
            pkt = IP(dst=ip) / TCP(dport=port, flags="S")

            reply = sr1(
                pkt,
                timeout=2,
                verbose=0
            )

            if reply is None:
                continue

            ttl = reply.ttl
            window = None
            df = False

            if IP in reply:
                df = bool(reply[IP].flags.DF)

            if TCP in reply:
                window = reply[TCP].window

            # We got a TCP response, so fingerprint is usable.
            return {
                "ip": ip,
                "ttl": ttl,
                "window": window,
                "df": df,
                "probe_port": port
            }

        return None

    except Exception as e:
        print(f"[DEBUG] Fingerprint error: {e}")
        return None
